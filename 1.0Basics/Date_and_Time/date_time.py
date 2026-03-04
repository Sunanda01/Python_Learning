from datetime import datetime, date, time, timedelta
import time
now = datetime.now()
print(now)         
print(now.date())  
print(now.time()) 

today = date.today()
print(today)     

dt = datetime(2025, 8, 8, 14, 30, 45)
print(dt)          


print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2025-08-08 18:50:00
print(now.strftime("%A, %d %B %Y"))       # Friday, 08 August 2025

date_str = "08-08-2025 18:45"
dt = datetime.strptime(date_str, "%d-%m-%Y %H:%M")
print(dt)  # 2025-08-08 18:45:00

tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
after_2_hours = now + timedelta(hours=2)

print(tomorrow)
print(yesterday)
print(after_2_hours)

print(now.year)    # 2025
print(now.month)   # 8
print(now.day)     # 8
print(now.hour)    # 18

print("Start")
time.sleep(2)  # pause 2 sec
print("End")

# %Y → Year (2025)
# %m → Month (01–12)
# %d → Day (01–31)
# %H → Hour (00–23)
# %M → Minute
# %S → Second
# %A → Weekday name
# %B → Month name