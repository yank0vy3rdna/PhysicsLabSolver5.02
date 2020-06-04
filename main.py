import pandas
import matplotlib.pyplot as plt
import numpy as np


df1 = pandas.read_csv('1.csv', sep=',')
df2 = pandas.read_csv('2.csv', sep=',')
df3 = pandas.read_csv('3.csv', sep=',')


def MNK(x: pandas.Series, y: pandas.Series):
    meanx, meany = np.mean(x), np.mean(y)
    D = np.power(x-meanx, 2).sum()
    b = ((x-meanx)*(y-meany)).sum()
    b /= D
    a = meany - meanx * b
    di = y - (a+b*x)
    temp = np.power(di, 2).sum()/(len(x)-2)
    sb2 = temp/D
    db = 2*np.sqrt(sb2)
    return b, a, db


tg1, y1, dtg1 = MNK(df1['Frequency (Hz)'], df1['Voltage (V)'])
tg2, y2, dtg2 = MNK(df2['Frequency (Hz)'], df2['Voltage (V)'])
tg3, y3, dtg3 = MNK(df3['Frequency (Hz)'], df3['Voltage (V)'])

plank = np.mean([tg1, tg2, tg3])

dPlank = np.sqrt(dtg1**2+dtg2**2+dtg3**2)/3


data = {'Frequency (Hz)': 0, 'Voltage (V)': 0}
data = [data]

df1 = pandas.concat([pandas.DataFrame(data), df1], ignore_index=True)
df2 = pandas.concat([pandas.DataFrame(data), df2], ignore_index=True)
df3 = pandas.concat([pandas.DataFrame(data), df3], ignore_index=True)

data = np.array([y1, 0])
interpolation1 = pandas.DataFrame()
interpolation1['y'] = pandas.Series(data)
data = np.array([0, df1.loc[1]['Frequency (Hz)']])
interpolation1['x'] = pandas.Series(data)

data = np.array([y2, 0])
interpolation2 = pandas.DataFrame()
interpolation2['y'] = pandas.Series(data)
data = np.array([0, df2.loc[1]['Frequency (Hz)']])
interpolation2['x'] = pandas.Series(data)

data = np.array([y3, 0])
interpolation3 = pandas.DataFrame()
interpolation3['y'] = pandas.Series(data)
data = np.array([0, df3.loc[1]['Frequency (Hz)']])
interpolation3['x'] = pandas.Series(data)

ax = plt.subplot(111)

ax.plot(interpolation1['x'], interpolation1['y'],
        color='0', linestyle='--', linewidth=1)
ax.plot(interpolation2['x'], interpolation2['y'],
        color='0', linestyle='--', linewidth=1)
ax.plot(interpolation3['x'], interpolation3['y'],
        color='0', linestyle='--', linewidth=1)


ax.plot(df1['Frequency (Hz)'], df1['Voltage (V)'],
        'g-o', color='blue', label='Цезий')
ax.plot(df2['Frequency (Hz)'], df2['Voltage (V)'],
        'g-o', color='orange', label='Аллюминий')
ax.plot(df3['Frequency (Hz)'], df3['Voltage (V)'],
        'g-o', color='green', label='Ниобий')

ax.grid()
ax.legend()


print('Для 1 металла угловой коэффициент: ', tg1)
print('Для 2 металла угловой коэффициент: ', tg2)
print('Для 3 металла угловой коэффициент: ', tg3)

print('Погрешность углового коэффициента 1 металла:', dtg1)
print('Погрешность углового коэффициента 2 металла:', dtg2)
print('Погрешность углового коэффициента 3 металла:', dtg3)

print('Для 1 металла пересечение интерполяционной прямой с осью Y: ', y1)
print('Для 2 металла пересечение интерполяционной прямой с осью Y: ', y2)
print('Для 3 металла пересечение интерполяционной прямой с осью Y: ', y3)

print('Для 1 металла работа выхода:', -y1,'эВ')
print('Для 2 металла работа выхода:', -y2,'эВ')
print('Для 3 металла работа выхода:', -y3,'эВ')

print('Постоянная Планка: ', plank)

print('Погрешность постоянной Планка:', dPlank)

plt.show()
