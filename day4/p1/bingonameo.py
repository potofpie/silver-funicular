from termcolor import colored


class Point:
    def __init__(self, number) -> None:
        self.marked = False
        self.number = int(number)

    def __str__(self):
        if( self.number > 9):
            return  colored(f'{str(self.number)} ', 'red') if self.marked else f'{str(self.number)} '
        else:
            return  colored(f' {str(self.number)} ', 'red') if self.marked else f' {str(self.number)} '

class Row:
    def __init__(self, rowString) -> None:
        
        self.points =  [Point(i) for i in rowString.replace('        ','').replace('  ',' ').split(' ')]
    def __str__(self):
        return ''.join([f'{p}' for p in self.points])

class Board:
    def __init__(self, boardString) -> None:
        self.rows = [Row(i) for i in boardString.split('\n') ]
        self.win = False
    

    def _row_check_win(self):
        if  any([all([p.marked for p in r.points]) for r in self.rows]):
            self.win = True

        
    def _col_check_win(self):
        if any([ all([self.rows[j].points[i].marked for j in range(0, len(self.rows))]) for i in range(0, len(self.rows))]):
            self.win = True
                            

    def check_win(self):
        return self._col_check_win() or self._row_check_win()

    def calc_board(self):
        score = 0
        for r in self.rows:
            for p in r.points:
                if(not p.marked):
                    score+=p.number
        return score



        

    def markNumber(self, number):
        for r in self.rows:
            for p in r.points:
                if(p.number == number):
                    p.marked = True
        self.check_win()
        return self.win 

    def __str__(self):
        status_text = (colored('winner!','green') if  self.win else colored('nope','red')) + '\n'
        return  f'Board Status: {status_text}' + ''.join([f'{r}\n' for r in self.rows])
        

def read_file_to_array(filepath):
    with open(filepath) as f:
        return [l.strip() for l in f.readlines()]

text = read_file_to_array('../input.txt')
calls = [int(i) for i in text[0].split(',')]
justbored =text[2:]
jbs = []
for jb in justbored:
    if(jb != ''):
        jbs.append(jb)
b_count = int(len(jbs)/5)




boards = []
for bc in range(0,b_count):
    b = Board(
        boardString=f'''{jbs[ (bc*5) ]}
        {jbs[ (bc*5)+1 ]}
        {jbs[ (bc*5)+2 ]}
        {jbs[ (bc*5)+3 ]}
        {jbs[ (bc*5)+4 ]}'''
    )
    boards.append(b)




for c in calls:
    for b in boards:
        if(b.markNumber(c)):
            print(b.calc_board() * c)
            exit()

