from datetime import datetime
from zoneinfo import ZoneInfo

# UTC Time
utc_time = datetime.now(ZoneInfo("UTC"))

# Different Region Times
dhaka_time = datetime.now(ZoneInfo("Asia/Dhaka"))
london_time = datetime.now(ZoneInfo("Europe/London"))
new_york_time = datetime.now(ZoneInfo("America/New_York"))
tokyo_time = datetime.now(ZoneInfo("Asia/Tokyo"))

print("UTC Time      :", utc_time.strftime("%Y-%m-%d %H:%M:%S %Z"))
print("Dhaka Time    :", dhaka_time.strftime("%Y-%m-%d %H:%M:%S %Z"))
print("London Time   :", london_time.strftime("%Y-%m-%d %H:%M:%S %Z"))
print("New York Time :", new_york_time.strftime("%Y-%m-%d %H:%M:%S %Z"))
print("Tokyo Time    :", tokyo_time.strftime("%Y-%m-%d %H:%M:%S %Z"))