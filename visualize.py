import csv
import matplotlib.pyplot as plt
import os
import shutil

def create_dir(path, delete=False):
    try:
        os.makedirs(path)
    except FileExistsError:
        if delete:
            shutil.rmtree(path)
            os.makedirs(path)
        else:
            pass

# Constants
start_time = 0.0
G_CONSTANT = 9.81

# Edit the following constants
ZERO_DATA = -8486.84
ROCKET_MASS = 0.235
ROCKET_DATA = -8990.62
ROCKET_END_DATA = -8787.86
LOOK_START = 2200
LOOK_END = 2600
DATA_TITLE = '2024-06-08 Nozzle Test'
FILE_PATH = 'data/20240608_노즐 분사data.csv'
calibrationFactor = (ROCKET_DATA-ZERO_DATA)/(ROCKET_MASS*G_CONSTANT)
print(f"calibration factor:{calibrationFactor}")

# Data Loading
with open(FILE_PATH, 'r', newline='') as f:
    reader = csv.reader(f)
    row_datas = [row for row in reader]
row_datas = [[float(data[0]), float(data[1])] for data in row_datas[1:]]

# Data Preprocessing
start_time = float(row_datas[0][0])
timeforce_datas = [[data[0]-start_time, (data[1]-ROCKET_DATA)/calibrationFactor] for data in row_datas]
rocket_start_mass = ROCKET_MASS
rocket_end_mass = ROCKET_MASS + (ROCKET_END_DATA-ROCKET_DATA)/(calibrationFactor*G_CONSTANT)
print(f"rocket start mass:{rocket_start_mass:.3f} kg")
print(f"rocket end mass:{rocket_end_mass:.3f} kg")
rocket_mass_delta = (rocket_start_mass-rocket_end_mass) / (timeforce_datas[LOOK_END][0]-timeforce_datas[LOOK_START][0])

acceleration = 0.0
velocity = 0.0
position = 0.0

acceleration_datas = []
velocity_datas = []
position_datas = []
gravity_forces = []

for i in range(LOOK_START, LOOK_END):
    mass = rocket_start_mass - rocket_mass_delta * (timeforce_datas[i][0]-timeforce_datas[LOOK_START][0])
    force = timeforce_datas[i][1]-G_CONSTANT*mass
    gravity_forces.append([timeforce_datas[i][0], G_CONSTANT*mass])
    acceleration = force/mass
    velocity += acceleration*(timeforce_datas[i][0]-timeforce_datas[i-1][0])
    position += velocity*(timeforce_datas[i][0]-timeforce_datas[i-1][0])
    if position < 0:
        acceleration = 0.0
        velocity = 0.0
        position = 0.0
    acceleration_datas.append([timeforce_datas[i][0], acceleration])
    velocity_datas.append([timeforce_datas[i][0], velocity])
    position_datas.append([timeforce_datas[i][0], position])

print(f"rocket Max-acceleration:{max([data[1] for data in acceleration_datas]):.3f} m/s^2, Mean-acceleration:{sum([data[1] for data in acceleration_datas])/len(acceleration_datas):.3f} m/s^2")
print(f"rocket Max-velocity:{max([data[1] for data in velocity_datas]):.3f} m/s, Mean-velocity:{sum([data[1] for data in velocity_datas])/len(velocity_datas):.3f} m/s")
print(f"rocket Max-height:{max([data[1] for data in position_datas]):.3f} m")

# Visualization
# 1. full force-time graph
# 2. force-time graph for a specific time range
fig, ax = plt.subplots(2,2, figsize=(20,10))
fig.suptitle(DATA_TITLE, fontsize=16)
ax1 = ax[0,0]
ax2 = ax[0,1]
ax3 = ax[1,0]
ax4 = ax[1,1]

fig1_time = [data[0] for data in timeforce_datas]
fig1_force = [data[1] for data in timeforce_datas]
ax1.plot(fig1_time, fig1_force)
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Force (N)')
ax1.set_title('Force-Time Graph(Full time range)')
ax1.grid()

fig2_time = [data[0] for data in timeforce_datas[LOOK_START:LOOK_END]]
fig2_force = [data[1] for data in timeforce_datas[LOOK_START:LOOK_END]]
ax2.plot(fig2_time, fig2_force, label='Force')
ax2.plot([data[0] for data in gravity_forces], [data[1] for data in gravity_forces], 'r', label='Gravity')
ax2.legend()
ax2.set_xlabel('time (s)')
ax2.set_ylabel('Force (N)')
ax2.set_title(f'Force-Time Graph({fig2_time[0]:.2f} ~ {fig2_time[-1]:.2f} s)')
ax2.grid()

fig3_time = [data[0] for data in velocity_datas]
fig3_velocity = [data[1] for data in velocity_datas]
ax3.plot(fig3_time, fig3_velocity)
ax3.set_xlabel('time (s)')
ax3.set_ylabel('Velocity (m/s)')
ax3.set_title(f'Velocity-Time Graph({fig3_time[0]:.2f} ~ {fig3_time[-1]:.2f} s)')
ax3.grid()

fig4_time = [data[0] for data in position_datas]
fig4_position = [data[1] for data in position_datas]
ax4.plot(fig4_time, fig4_position)
ax4.set_xlabel('time (s)')
ax4.set_ylabel('Position (m)')
ax4.set_title(f'Position-Time Graph({fig4_time[0]:.2f} ~ {fig4_time[-1]:.2f} s)')
ax4.grid()

# Save the Data
create_dir('result')
create_dir(f'result/{DATA_TITLE}', delete=True)
plt.savefig(f'result/{DATA_TITLE}/result.png')

# Save Each subplots
fig1 = plt.figure(figsize=(10,5))
plt.plot(fig1_time, fig1_force)
plt.xlabel('time (s)')
plt.ylabel('Force (N)')
plt.title('Force-Time Graph(Full time range)')
plt.grid()
plt.savefig(f'result/{DATA_TITLE}/force-time(full).png', dpi=300)

fig2 = plt.figure(figsize=(10,5))
plt.plot(fig2_time, fig2_force, label='Force')
plt.plot([data[0] for data in gravity_forces], [data[1] for data in gravity_forces], 'r', label='Gravity')
plt.legend()
plt.xlabel('time (s)')
plt.ylabel('Force (N)')
plt.title(f'Force-Time Graph({fig2_time[0]:.2f} ~ {fig2_time[-1]:.2f} s)')
plt.grid()
plt.savefig(f'result/{DATA_TITLE}/force-time(Part).png', dpi=300)

fig3 = plt.figure(figsize=(10,5))
plt.plot(fig3_time, fig3_velocity)
plt.xlabel('time (s)')
plt.ylabel('Velocity (m/s)')
plt.title(f'Velocity-Time Graph({fig3_time[0]:.2f} ~ {fig3_time[-1]:.2f} s)')
plt.grid()
plt.savefig(f'result/{DATA_TITLE}/velocity-time.png', dpi=300)

fig4 = plt.figure(figsize=(10,5))
plt.plot(fig4_time, fig4_position)
plt.xlabel('time (s)')
plt.ylabel('Position (m)')
plt.title(f'Position-Time Graph({fig4_time[0]:.2f} ~ {fig4_time[-1]:.2f} s)')
plt.grid()
plt.savefig(f'result/{DATA_TITLE}/position-time.png', dpi=300)