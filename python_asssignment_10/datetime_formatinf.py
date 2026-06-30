import datetime
current_time = datetime.datetime.now()
formated_date = current_time.strftime("%d-%m-%y %H:%M:%S")
print(formated_date)