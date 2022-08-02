class robotStatus:
    ALIVE = 0
    DEAD  = 1
    CRASH = 2
    WATER = 3

BATTERY_VAL = 10
class robot:
    # mapa, x, y, bateria
    def __init__(self, T, x, y, b):
        self.__map = T
        self.__x = x
        self.__y = y
        self.__battery = b
        self.__status = self.spawn(T, x, y)

    def spawn(self, T, x, y):
        if self.get_battery() <= 0:
            return robotStatus.DEAD
        place = T[x][y]
        match place:
            case 'T':
                return robotStatus.ALIVE
            case 'B':
                self.take_battery(T, x, y)
                return robotStatus.ALIVE
            case 'G':
                return robotStatus.CRASH
            case 'W':
                return robotStatus.WATER
            case _:
                return None
                
    def move(self, new_x, new_y):
        if new_x>=len(self.__map) or new_x<0 or new_y>=len(self.__map[0]) or new_y<0:
            self.__battery -= 1
            self.__status = robotStatus.CRASH
            return
        place = self.__map[new_x][new_y]
        if place == 'T' or place =='W' or place =='B':
            self.__x = new_x
            self.__y = new_y
            self.__battery -= 1
        if place == 'B':
            self.take_battery(self.__map,self.__x,self.__y)
        if place == 'G':
            self.__battery -= 1
            self.__status = robotStatus.CRASH
        if place == 'W':
            self.__status = robotStatus.WATER
        if self.__battery <=0:
            self.__status = robotStatus.DEAD

    def take_battery(self, T, x, y):
        T[x][y] = 'T'
        self.__battery += BATTERY_VAL

    def left(self, val = 1):
        for _ in range(val):
            status = self.get_status()
            if status == robotStatus.CRASH or status == robotStatus.WATER or status == robotStatus.DEAD:
                continue
            elif self.__battery <=0:
                self.__status = robotStatus.DEAD
                continue
            elif self.get_status() == 0:
                self.move(self.__x, self.__y - 1)            
        return self
                
            
    
    def right(self, val = 1):        
        for _ in range(val):
            status = self.get_status()
            if status == robotStatus.CRASH or status == robotStatus.WATER or status == robotStatus.DEAD:
                continue
            elif self.__battery <= 0:
                self.__status = 1
                continue
            elif self.get_status() == 0:
                self.move(self.__x, self.__y+1)
        return self

    def up(self, val = 1):       
        for _ in range(val):
            status = self.get_status()
            if status == robotStatus.CRASH or status == robotStatus.WATER or status == robotStatus.DEAD:
                continue
            elif self.__battery <=0:
                self.__status = 1
                continue
            elif self.get_status() == 0:
                self.move(self.__x-1, self.__y)
        return self

    def down(self, val = 1):
        for _ in range(val):
            status = self.get_status()
            if status == robotStatus.CRASH or status == robotStatus.WATER or status == robotStatus.DEAD:
                continue
            elif self.__battery <=0:
                self.__status = 1
                continue
            elif self.get_status() == robotStatus.ALIVE:
                self.move(self.__x+1, self.__y)
        return self

    def get_status(self):
        return self.__status

    def get_battery(self):
        return self.__battery

    def get_map(self):
        map = self.__map
        if self.get_status() == robotStatus.ALIVE:
            map[self.__x][self.__y] = 'R'
        else:
            map[self.__x][self.__y] = 'X'

        return map

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
