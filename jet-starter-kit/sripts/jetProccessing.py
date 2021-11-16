import jetFunctions as jet
import matplotlib.pyplot as plt
import numpy as np
kolibrovka = jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/00_Pa.txt')
y1 =[]
y1.append(np.round(np.mean(kolibrovka[0])))
kolibrovka1=jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/70_Pa.txt')
y1.append(np.round(np.mean(kolibrovka1[0])))
acp2pa=[]
acp2pa.append(0)
acp2pa.append(148)
plt.title('Колибровочный график зависимости показаний АЦП от давления')
plt.ylabel('Отчеты АЦП')
plt.xlabel('Давление')
plt.minorticks_on()
y1=np.array(y1)
x1=np.array(acp2pa)
coef = np.polyfit(y1,x1,1)
line1, = plt.plot(x1,y1,label = 'P= 0,2756*N-221,5866 ')
plt.legend()
plt.grid(
    which='major'
)
plt.grid(
    which='minor',
    linestyle = '--'
)

print(coef)
plt.show()
