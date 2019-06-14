import math

def fix(d):
    if d == "north":
        result[1]+=1
        actual[1]-=1
    if d == "south":
        result[1]-=1
        actual[1]+=1
    if d == "east":
        result[0]+=1
        actual[0]-=1
    if d == "west":
        result[0]-=1
        actual[0]+=1
    if d == "northwest":
        fix("north")
        fix("west")
    if d == "northeast":
        fix("north")
        fix("east")
    if d == "southwest":
        fix("south")
        fix("west")
    if d == "southeast":
        fix("south")
        fix("east")
        
for i in range(1,13):
    result = [0,0]
    actual = [0,0]
    f = open("input/"+str(i)+".txt")
    for j in range(int(f.readline())):
        fix(f.readline()[:-1])
    dist = (math.sqrt(((result[0]-actual[0])**2)+((result[1]-actual[1])**2)))
    print(chr(ord("a")+(round(dist)%26)), end='')
    f.close()
