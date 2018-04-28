l = ['ankur','soni','ankur',1,1,2,2,'ankur']

dict = {}

for i in l:
      count = dict.get(i,0)
      dict[i] = count +1

for j in dict:
      print(j,' ',dict[j])