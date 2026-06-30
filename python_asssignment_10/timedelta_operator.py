from datetime import datetime, timedelta

# দুটি date
date1 = datetime(2024, 1, 10)
date2 = datetime(2024, 1, 25)

# Date difference
difference = date2 - date1

print("Date 1:", date1.date())
print("Date 2:", date2.date())
print("Difference:", difference.days, "days")

# timedelta দিয়ে days যোগ করা
new_date = date1 + timedelta(days=15)

print("New Date after adding 15 days:", new_date.date())