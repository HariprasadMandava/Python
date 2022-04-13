print("MANDAVA HARIPRASAD")
import psutil
print(".........................CPU utilization........................")
print(psutil.cpu_freq())
while True:
    cpu = psutil.cpu_percent(interval=1)
    print(cpu)
    if cpu > 10:
        print("Reached the limit")
        break