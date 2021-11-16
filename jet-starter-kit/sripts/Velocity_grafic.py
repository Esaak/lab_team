import jetFunctions as jet
import matplotlib.pyplot as plt
import numpy as np

kolibrovka1 = jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/00_mm.txt')

kolibrovka2=jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/20_mm.txt')
kolibrovka3=jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/30_mm.txt')
kolibrovka4=jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/50_mm.txt')

y1 = np.array(kolibrovka1[0])

#coef=np.loadtxt('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/acp2pa')

p1 = 0.2756 * y1 -221.5866
u1=np.sqrt((2*p1)/1.2)
x1 = np.linspace(0, (4*(2.9/500)), 100)
x1max=np.argmax(u1)
delta1=x1[x1max]
x1=x1-delta1
y2 = np.array(kolibrovka2[0])
p2 = 0.2756 * y2 -221.5866
u2= np.sqrt((2*p2)/1.2)
x2 = np.linspace(0, (4*(2.9/500)), 100)
x2max=np.argmax(u2)
delta2=x2[x2max]
x2=x2-delta2
y3 = np.array(kolibrovka3[0])
p3 = 0.2756 * y3 -221.5866
u3= np.sqrt((2*p3)/1.2)
x3 = np.linspace(0, (4*(2.9/500)), 100)
x3max=np.argmax(u3)
delta3=x3[x3max]
x3=x3-delta3
y4 = np.array(kolibrovka4[0])
p4 = 0.2756 * y4 -221.5866
u4= np.sqrt((2*p4)/1.2)
x4 = np.linspace(0, (4*(2.9/500)), 100)
x4max=np.argmax(u4)
delta4=x4[x4max]
x4=x4-delta4
# y1.append(np.round(np.mean(kolibrovka[0])))
# kolibrovka1=jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/20_mm.txt')
# y1.append(np.round(np.mean(kolibrovka1[0])))
# acp2pa=[]
# acp2pa.append(0)
# acp2pa.append(148)
# plt.title('Колибровочный график зависимости показаний АЦП от давления')
# plt.ylabel('Отчеты АЦП')
# plt.xlabel('Давление')
# plt.minorticks_on()
# y1=np.array(y1)
# x1=np.array(acp2pa)
# coef = np.polyfit(x1,y1,1)
# line1, = plt.plot(x1,y1)
plt.plot(x1,u1, color = 'g')
plt.plot(x2,u2, color = 'r')
plt.plot(x3,u3, color = 'b')
plt.plot(x4,u4, color = 'y')
plt.grid(
   which='major'
)
plt.grid(
   which='minor',
   linestyle = '--'
)
plt.show()
