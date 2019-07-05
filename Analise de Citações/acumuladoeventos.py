import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#definindo o eixo x (anos)
X_AXIS = (
'2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014',
'2015','2016','2017','2018'
)

#definindo o index(x,label)
index = pd.Index(X_AXIS, name='Anos Analisados')

#definindo o dataset dos eventos
data = {
        'WRE': (0,0,0,0,0,0,0,0,0,8,0,38,7,21,25,8,0,0),
        'SBIE': (12,12,0,0,0,45,40,22,15,6,15,0,0,35,21,25,24,2),
        'WEI': (0,0,0,0,0,0,0,0,0,0,16,107,5,35,5,9,2,3),
        'WIE': (0,0,0,0,42,0,15,19,53,33,10,13,28,2,31,2,1,0)
}

#montando o grafico acumulado
df = pd.DataFrame(data, index=index)
ax = df.plot(kind='bar', stacked=True, figsize=(18.5, 10.5), hatch=('*'))
ax.set_ylabel('Citações')



#print
#plt.savefig('stacked.pdf')
plt.show()