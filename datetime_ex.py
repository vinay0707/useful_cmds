import datetime
import pytz # third party library

# create a simple date
d = datetime.date(2017, 5, 15)

print(d)

#today's date
tday = datetime.date.today()

print(tday)
#ISO Monday 1 and Sunday is 7
print(tday.isoweekday())
# Monday 0 and Sunday is 6
print(tday.weekday())



#time delta

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)

print(tday - tdelta)

# date difference
bday = datetime.date(2017,7,7)
till_day = bday - tday

print(till_day.days)
print(till_day.total_seconds())


# time

t = datetime.time(11,05,44,100000)
print(t)


#date and time

dt = datetime.datetime(2017,5,14,11,05,44,0)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.today()
# dt_utcnow = datetime.datetime.today()
#
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)



dt = datetime.datetime(2017,5,14,12,30,45,tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# convert to Arizona timezone
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Arizona'))
print(dt_mtn)


# get the all timezones
# for tz in pytz.all_timezones:
#     print(tz)

dt_az  = datetime.datetime.now() # this is naive datetime means without timezone information
az_tz = pytz.timezone('US/Arizona')
print(dt_az)

# Adding timezone to datetime
dt_az = az_tz.localize(dt_az)
print(dt_az)

#convert to MST to EST
dt_est = dt_az.astimezone(pytz.timezone('US/Eastern'))
print(dt_est)

#
dt_az = datetime.datetime.now(tz=pytz.timezone('US/Arizona'))
print(dt_az)

#print ISO format... Ex. 2017-05-14T23:42:00.513759-07:00
print(dt_az.isoformat())

#Specific format... refer documentation
print(dt_az.strftime('%B %d, %Y'))

# String to date
dt_str = 'May 14, 2017'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

#strftime - datetime to string
#strptime - string to datetime

