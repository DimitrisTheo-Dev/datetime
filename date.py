import datetime
import pytz
today = datetime.date.today()
birthday = datetime.date(2002, 2, 5)
alive = (today - birthday).days

#years = (10000 - alive)/365
#years2 = (10000 - alive)%365
#months = years2/30
#months2 = years2%30
#days =  months2/12

#print(years, months, days)
#while alive < 10000:
#   alive += 1
#    print(alive)

#tdelta = datetime.timedelta(days=3386)
#print(today + tdelta)
print(today.weekday()) #monday, tuesday etc
print(datetime.time(7, 2, 20, 15))
#datetime.date( Y M D)
#datetime.time(H M S MS)
#datetime.datetime( Y M D H M S MS)

hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)
datetime = datetime.datetime.now(tz=pytz.UTC)
#date_pacific = datetime.today.astimezone(pytz.timezone('US/Pacific'))
print(datetime)
for tz in pytz.all_timezones:
    print(tz)

print(datetime.strftime('%B %d, %Y')) #f = formatting

#strp p = parsing
#thing = datetime.datetime.strptime('february 05,2002', '%B %d, %Y')
#print(repr(thing))