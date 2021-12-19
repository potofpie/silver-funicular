from enum import Enum


class Direction(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    DIAGONAL = 3


class PointPair:
    def __init__(self, pointPairString, id):
        headString, tailString = pointPairString.split(' -> ')
        # print(headString, tailString)
        self.id = id
        self.head = Point(headString)
        self.tail = Point(tailString)
        self.line = Line(self.head, self.tail)
    def __str__(self):
        return f'''
        ID:    {self.id}
        Head:    {self.head}
        Tail:    {self.tail}
        Line Direction: {self.line.direction}
        Line Points:    {[ str(p) for p in self.line.points]}

        '''

class Line:
    def __init__(self, head, tail):
        # f, s = lineString.split(' -> ')
        self.points = []
        self.direction = None
        if(head.x == tail.x):
            self.direction = Direction.HORIZONTAL
            if(head.y < tail.y):
                for i in range(head.y, tail.y+1):
                    self.points.append(Point(f'{head.x},{i}'))
            elif(head.y > tail.y):
                for i in range(head.y, tail.y-1,-1):
                    self.points.append(Point(f'{head.x},{i}'))
                
        elif(head.y == tail.y):
            self.direction = Direction.VERTICAL
            if(head.x < tail.x):
                for i in range(head.x, tail.x+1):
                    self.points.append(Point(f'{i},{tail.y}'))
            elif(head.x > tail.x):
                for i in range(head.x, tail.x-1,-1):
                    self.points.append(Point(f'{i},{tail.y}'))
        else:
            self.direction = Direction.DIAGONAL
        
class Point:
    def __init__(self, pointString):
        x, y = pointString.split(',')
        self.x = int(x)
        self.y = int(y)
    def __str__(self):
        return f'[{self.x}, {self.y}]'

def read_file_to_array(filepath):
    with open(filepath) as f:
        return [l.strip() for l in f.readlines()]

text = read_file_to_array('../input.txt')
point_pairs  = [PointPair(i,id) for id, i   in enumerate(text)]


for i in point_pairs:
    print(str(i))

def _util_to_determine_board_size():
    BOARD_POINTS_X = set()
    BOARD_POINTS_Y = set()
    for i in point_pairs:
        BOARD_POINTS_X.add(i.head.x)
        BOARD_POINTS_X.add(i.tail.x)
        BOARD_POINTS_Y.add(i.head.y)
        BOARD_POINTS_Y.add(i.tail.y)
    print(BOARD_POINTS_Y)
    print(BOARD_POINTS_X)

def faster_maybe(map):
    for pp in point_pairs:
        if(pp.line.points != Direction.DIAGONAL):
            for p in pp.line.points:
                map[p.x][p.y] = map[p.x][p.y] + 1
    return map

map = [ [ 0 for j in range(0,1000)] for i in range(0,1000)]
BOARD_SIZE = 1000
marked = faster_maybe(map)

c = 0 
for i in marked:
    for j in i:
        if j > 1:
            c+=1

print(c)







