import shutil
print(".............................Disk utilization..........................")
path = "/Users/Administrator.DEMO/Documents"
stat = shutil.disk_usage(path)
print("Disk usage statistics:")
print(stat)