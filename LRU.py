def LRU(x,i):
    y = x%block
    min = 100 
    hit = 0
    for j in range(0,n):
        if cache[y][j] == x:
            print("\nHIT")
            hit = 1
            place = j
            break
        
    if hit == 1:
        track[y][place] = i
        show()
    else:
        print("\nMISS")
        for j in range(0,n):
            if track[y][j] < min:
                min = track[y][j]
                place = j
        cache[y][place] = x
        track[y][place] = i
        show()



def show():
    for rows in cache:
        print("\t\t",rows)
    # for rows in track:
    #     print(rows)

cache = []
temp = []
track = []

n,m = map( int, input().split() )
block = m//n

for i in range(0,n):
    temp.append(-1)
for i in range(block):
    cache.append(temp.copy())
    track.append(temp.copy())

show()
i=0
while True:
    x = int(input())
    if x==-1:
        break
    LRU(x,i)
    i+=1

# 4 8
# 2 4 6 112 4 6 2 10 37 13 30 67 11 5 30 -1