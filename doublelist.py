tmap = [[1,2,3,4,5,6],
        [2,4,7,9,3,2],
        [4,3,5,6,7,1]
]

def map(tmap,waterlevel):
      for i in range(0,len(tmap)):
            for j in tmap[i]:
                  if j <= waterlevel:
                        print("W",end=' ')
                  else:
                        print(".",end=' ')
            print("\n")
map(tmap, 3)