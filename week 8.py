import datetime as dt

# How many seconds have you alive?
birthday = dt.datetime(year=2003, month=9, day=17)
dt_now = dt.datetime.now()
alive = dt_now - birthday
secs = (alive.days *24* 60 *60) + alive.seconds
res = f"I have been alive for {secs} seconds"
print(res)

# Calculate age in years after 1340 days
days = 1340
future = dt.datetime . now() + dt.timedelta(days=days)
alive = future - birthday
age = alive.days//365
res = f"I will be {age} years old in {days} days"
print(res)