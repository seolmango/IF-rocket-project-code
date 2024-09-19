import serial
import time
import csv

py_serial = serial.Serial(
    # Change this to your own port
    port='COM3',
    baudrate=115200,
)

datas = []

while True:
    try:
        data = py_serial.readline().decode('utf-8').strip()
        if data == '':
            continue
        print(data)
        temp = [time.time(), data]
        datas.append(temp)
    except KeyboardInterrupt:
        py_serial.close()
        print("값을 저장합니다.")
        with open('data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['time', 'raw_data'])
            for data in datas:
                writer.writerow(data)
        print("값 저장 완료")
        break
    except Exception as e:
        print(e)
        py_serial.close()
        print("오류 발생 전까지 값을 저장합니다.")
        with open('data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['time', 'raw_data'])
            for data in datas:
                writer.writerow(data)
            writer.writerow([time.time(), e])
        break