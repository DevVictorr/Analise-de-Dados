from pandas import DataFrame as pd
from pandas.core.frame import DataFrame
import numpy as np



data = {
        "Jogador":["Victor","Bruno","Cimel","GoldB"],
        "Skill":[8,4,10,9],
        "HS":[3.2,1.0,5.0,4.0]
}

frame = DataFrame(data, columns=['Jogador','Skill','HS','Wins'])

#print(type(frame))

frame['Wins'] = np.arange(4.)

print(frame)
print('////////////////////')

print(frame.describe())