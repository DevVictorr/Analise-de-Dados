import pandas as pd

obj = pd.Series([1,2,3,2] , pd.Index(['Victor','Bru','Ci','Ma']))

print(obj.isnull())