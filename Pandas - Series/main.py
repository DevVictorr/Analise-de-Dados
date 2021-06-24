import pandas as pd



#print(pd.__version__)


obj = pd.Series([5,4,7])

print(obj)


obj2 = pd.Series([5,7,3,5,1,0,2], pd.Index(['a','b','c','d','e','f','g']))

print("//////////////////////////////")

print(obj2)

print("//////////////////////////////")

print(obj2[obj2 > 3])

print("//////////////////////////////")

print('d' in obj2)