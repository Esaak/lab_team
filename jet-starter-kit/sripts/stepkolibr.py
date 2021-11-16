import matplotlib.pyplot as plt
import numpy as np

y1 =[]
y1.append(0)
y1.append(0.029)
acp2pa=[]
acp2pa.append(0)
acp2pa.append()
plt.title('Колибровочный график зависимости перемещения трубки Пито от шага Двигателя')
plt.ylabel('Перемещение трубки Пито')
plt.xlabel('Количество шагов')
plt.minorticks_on()
x1=np.array(acp2pa)
y1=np.array(y1)
coef = np.polyfit(x1,y1,1)
line1, = plt.plot(x1,y1)
plt.grid(
    which='major'
)
plt.grid(
    which='minor',
    linestyle = '--'
)

print(coef)
plt.show()
