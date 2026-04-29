dc={'shrimp':700,'cheese':850,'snack':750}
dc['ball']=900

print(dc)

for i in dc:
    dc[i]+=100

print(dc)

dc['corn']=dc['cheese']
del dc['cheese']

print(dc)