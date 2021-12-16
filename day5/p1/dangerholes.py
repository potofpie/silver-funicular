
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
points  = [ [Point(i.split(" -> ")[0]) , Point(i.split(" -> ")[1])  ]  for i in text]
print(points)