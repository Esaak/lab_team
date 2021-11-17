import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(12,7))
x1 =  []
y1 = []
x1 = (0, 20, 30, 50)
y1 = (3.42, 3.5, 4.42, 4.97)
plt.scatter(x1,y1, color = 'g')
x1= np.array(x1)
y1=np.array(y1)
coef = np.polyfit(x1,y1,1)
y2 = np.polyval(coef, x1)
plt.plot(x1,y2, color = 'b')
plt.title('График зависимости расхода от расстояния до сопла')
plt.xlabel('Расстояние до сопла [mm]')
plt.ylabel('Расход [г/с]')
plt.minorticks_on()
plt.grid(
   which='major'
)
plt.grid(
   which='minor',
   linestyle = '--'
)
plt.show()
