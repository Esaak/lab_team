import jetFunctions as jet
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (12,7))

kolibrovka1 = jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/00_mm.txt')
kolibrovka2=jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/20_mm.txt')
kolibrovka3=jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/30_mm.txt')
kolibrovka4=jet.readJetData('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/50_mm.txt')

y1 = np.array(kolibrovka1[0])
y2 = np.array(kolibrovka2[0])
y3 = np.array(kolibrovka3[0])
y4 = np.array(kolibrovka4[0])
#coef=np.loadtxt('/home/gr105/Laba2/lab_team-master/jet-starter-kit/sripts/acp2pa')

p1 = 0.2756 * y1 -221.5866
u1=np.sqrt((2*p1)/1.2)
x1 = np.linspace(0, (4*(2.9/500)), 100)
x1max=np.argmax(u1)
delta1=x1[x1max]
x1=x1-delta1+0.001

q1=1.2*2*np.pi*0.000058*4*1000*u1*x1
q1=np.abs(q1)/2

y2 = np.array(kolibrovka2[0])
p2 = 0.2756 * y2 -221.5866
u2= np.sqrt((2*p2)/1.2)
x2 = np.linspace(0, (4*(2.9/500)), 100)
x2max=np.argmax(u2)
delta2=x2[x2max]
x2=x2-delta2+0.001

q2=1.2*2*np.pi*0.000058*4*1000*u2*x2
q2=np.abs(q2)/2

y3 = np.array(kolibrovka3[0])
p3 = 0.2756 * y3 -221.5866
u3= np.sqrt((2*p3)/1.2)
x3 = np.linspace(0, (4*(2.9/500)), 100)
x3max=np.argmax(u3)
delta3=x3[x3max]
x3=x3-delta3+0.001

q3=1.2*2*np.pi*0.000058*4*1000*u3*x3
q3=np.abs(q3)/2

y4 = np.array(kolibrovka4[0])
p4 = 0.2756 * y4 -221.5866
u4= np.sqrt((2*p4)/1.2)
x4 = np.linspace(0, (4*(2.9/500)), 100)
x4max=np.argmax(u4)
delta4=x4[x4max]
x4=x4-delta4+0.001

q4=1.2*2*np.pi*0.000058*4*1000*u4*x4
q4=np.abs(q4)/2 

plt.title('График зависимости расхода от расстояния до сопла')
plt.xlabel('Положение трубки Пито относительно центра струи [m]')
plt.ylabel('Расход топлива в сечении [г/с]')
plt.minorticks_on()


plt.plot(x1,q1, color = 'g', label = 'Q1 (00 mm) ')
plt.plot(x2,q2, color = 'r', label = 'Q2 (20 mm) ')
plt.plot(x3,q3, color = 'b', label = 'Q3 (30 mm)')
plt.plot(x4,q4, color = 'y', label = 'Q4 (50 mm)')
plt.grid(
   which='major'
)
plt.grid(
   which='minor',
   linestyle = '--'
)
plt.show()
