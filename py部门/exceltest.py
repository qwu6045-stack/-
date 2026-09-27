import pandas as pd

data = [i**2 for i in range(10,2,-1)]
datasa = pd.Series(data)

print(datasa)

sondata = {
    'age':[i+1 for i in range(5)],
    'fuck':['work','java','test','hook','mean'],
    'li':['shan','zhe','song','bie','gun']

    }

sondatami = pd.DataFrame(sondata)

print(sondatami)