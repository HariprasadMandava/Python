print("MANDAVA HARIPRASAD")
import wmi
c = wmi.WMI ()
import contextlib
file_path = 'process.txt'
for process in c.Win32_Process ():
  with open(file_path, "a") as o:
    with contextlib.redirect_stdout(o):
       print(f"{process.ProcessId}, {process.Name}")
import pandas as pd
read_file = pd.read_csv (r'C:\Users\Administrator.DEMO\PycharmProjects\pythonProject\process.txt')
read_file.to_csv (r'C:\Users\Administrator.DEMO\PycharmProjects\pythonProject\process1.csv', index=None)
import pandas as pd
a = pd.read_csv(r'C:\Users\Administrator.DEMO\PycharmProjects\pythonProject\process1.csv')
a.to_html("Table.htm")
html_file = a.to_html()
c = wmi.WMI ()
import contextlib
file_path = 'randomfile4.txt'
for process in c.Win32_Process ():
  with open(file_path, "a") as o:
    with contextlib.redirect_stdout(o):
       print(f"{process.ProcessId}, {process.Name}")
import pandas as pd
read_file = pd.read_csv (r'C:\Users\Administrator.DEMO\PycharmProjects\pythonProject\process.txt')
read_file.to_csv (r'C:\Users\Administrator.DEMO\PycharmProjects\pythonProject\process1.csv', index=None)
import pandas as pd
a = pd.read_csv(r'C:\Users\Administrator.DEMO\PycharmProjects\pythonProject\process1.csv')
a.to_html("Table.htm")
html_file = a.to_html()