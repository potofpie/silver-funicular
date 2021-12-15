c=0
with open('input.txt') as f:
    lines = f.readlines()
    print(len(lines))
    for lindex, l in enumerate(lines):
        if(lindex != 0):
            if int(lines[lindex-1]) < int(l.strip()):
                c+=1
