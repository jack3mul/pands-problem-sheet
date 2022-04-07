This script is to determine if the current day is a weekday or weekend day
This is easily implemented in python using the datetime module
I used datetime.today().weekday to achieve this
It outputs a number which goes from 0 to 6 -> 5 & 6 being weekend days
This was the way I scripted the problem: find todays "number" and compare to 5&6
If not equivalent then declare it a weekday