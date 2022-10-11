from datetime import datetime
from os import curdir

x= input("isminiz:")
now = datetime.now()

current_time = now.strftime ("%H:%M:%S")
current_date = now.strftime ("%d.%m.%Y")
print("Merhaba " , x , " Bugünün tarihi " , current_date , "Saat " , current_time)