pos = {"v": 0,  "h": 0 }

def move(cmd, units):
    if(cmd == 'up'):
        pos["v"] = pos["v"] - (1*units)
    elif(cmd == 'down'):
        pos["v"] = pos["v"] + (1*units)
    elif(cmd == 'forward'):
        pos["h"] = pos["h"] + (1*units)
    
with open('../input.txt') as f:
    lines = f.readlines()
    for lindex, l in enumerate(lines):
        cmd, units = l.split(' ') 
        move(cmd, int(units))
    
print(pos["v"]*pos["h"])