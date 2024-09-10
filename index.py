import psutil
import platform
from datetime import datetime
import wmi
import socket




print("                        Сведения о компьютере                        ")
print()
c = wmi.WMI()
bios = c.Win32_BIOS()[0]
print(f"Версия BIOS :                   {bios.Version}")
motherboard = c.Win32_BaseBoard()[0]
print(f"Информация о материнской плате: {motherboard.Manufacturer} {motherboard.Product}")
videocard = c.Win32_VideoController()[0]
print(f"Информация о видеокарте:        {videocard.Description}")
inf = platform.uname()
print(f"Машина:                         {inf.machine}")
proc = c.Win32_Processor()[0]
print(f"Процессор:                      {inf.processor} {proc.Name}")
memor=psutil.virtual_memory()
print(f"Объем памяти:                   {(((memor.total)/1024)/1024)/1024} GB")
print(f"Операционная система:           {inf.system}", f"{inf.release}")
namehost = socket.gethostname()
ipadres = socket.gethostbyname(namehost)
print("Локальный IP-адрес:            ", ipadres)
m = input()

