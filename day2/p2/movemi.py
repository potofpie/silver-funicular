pos = {"v": 0,  "h": 0, "aim": 0 }

def move(cmd, units):
    if(cmd == 'up'):
        pos["aim"] = pos["aim"] - (units)
    elif(cmd == 'down'):
        pos["aim"] = pos["aim"] + (units)
    elif(cmd == 'forward'):
        pos["h"] = pos["h"] + (units)
        pos["v"] = pos["v"] + (pos["aim"]*units) 
    
with open('../input.txt') as f:
    lines = f.readlines()
    for lindex, l in enumerate(lines):
        cmd, units = l.split(' ') 
        move(cmd, int(units))
    
print(pos["v"]*pos["h"])