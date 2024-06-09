import csv
import matplotlib.pyplot as plt

# Constants
start_time = 0.0
g = 9.81

# Data Calibration Factor
zero = -8486.84
mass = 0.235
rocket = -8990.62
cali = (rocket-zero)/(mass*g)
print(cali)

# Data Loading
with open('20240608_노즐 분사data.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    datas = [row for row in reader]

# Data Preprocessing
datas = datas[2200:2600]
start_time = float(datas[0][0])
datas = [[float(data[0]), float(data[1])] for data in datas]
for i, data in enumerate(datas):
    datas[i][0] = data[0]-start_time
    datas[i][1] = (data[1]-rocket)/cali

times = [data[0] for data in datas]
values = [data[1] for data in datas]

plt.plot(times, values)
plt.xlabel('time (s)')
plt.grid()
plt.ylabel('Force (N)')
plt.title('Force-Time Graph')

# Adding annotation
note = "2024/06/08 Nozzle Test - I.F"
plt.annotate(note, xy=(1, 0), xycoords='axes fraction', fontsize=6,
             xytext=(0, -30), textcoords='offset points',
             ha='right', va='bottom')

plt.show()