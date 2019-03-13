# Live counter to show how much someone has made during a semester
# based on how much they will make total.  In other words, the
# ammount per second in this program is not the same as the 
# hourly wage divided by 3600.  

import time
import datetime
import pytz

# number of days in the UMBC Spring 2019 academic calendar
defaultDays = 114
# standard CMSC 201 UTA pay (hourly)
defaultPay = 10.10
# how many hours worked a week
hoursPerWeek = 10
# how many full weeks worked
fullWeeks = defaultDays // 7
# how much you will make total
totalPay = defaultPay * fullWeeks * hoursPerWeek
# start date for the semester 
startDateRaw = datetime.datetime(2019,1,28,8)
timezone = pytz.timezone('America/New_York')
startDate = timezone.localize(startDateRaw)

# create a timedelta object with the ammount of days in it
totalTime = datetime.timedelta(days=defaultDays)
totalSecondsWorked = totalTime.total_seconds()

# how much you get paid per second
secondPay = totalPay / totalSecondsWorked

# find the current time
currentTime = datetime.datetime.now(pytz.timezone('America/New_York'))

# loop until the semester is over
while (currentTime < (startDate + totalTime)):

	# figure out how long it's been since the start of the semester
	timeWorked = currentTime - startDate
	secondsWorked = int(timeWorked.total_seconds())
	
	# how much money has been made over that time 
	moneyMade = secondsWorked * secondPay

	# big gross print mess (cause colors)
	print('\033c')
	print("It has been", secondsWorked, "seconds since the semester started")
	print("you get paid", '\033[92m${:,.10f}'.format(secondPay), "\033[0;0mdollars every second!")
	print("you have made",'\033[92m${:,.10f}'.format(moneyMade), "\033[0;0mdollars so far")
	print("you will make", '\033[92m${:,.2f}'.format(totalPay), "\033[0;0min total this semester")
	
	# wait a second then loop again
	time.sleep(1)
	
	currentTime = datetime.datetime.now(pytz.timezone('America/New_York'))
