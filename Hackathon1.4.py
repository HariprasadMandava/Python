print("HARIPRASAD MANDAVA")
import os
import psutil
print("..................................Memory utilization........................")
pid = os.getpid ()
py = psutil.Process (pid)
memoryUse = py.memory_info () [0]/2.**30
print ('memory use:', memoryUse)