from datetime import datetime
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = int(now.strftime("%H"))
print("date and time =", type(dt_string))