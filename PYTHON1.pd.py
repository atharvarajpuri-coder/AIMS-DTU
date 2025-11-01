import pandas as pd

data={'player name':['travis Head','Jos Buttler', 'Mitchel Marsh']}

DF=pd.DataFrame(data)

rank={'travis Head':'1','Jos Buttler':'2','Mitchel Marsh':'3'}

DF['encoded']=DF['player name'].map(rank)

print("orignal data:")
print(DF)