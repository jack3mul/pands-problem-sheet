from datetime import datetime

if datetime.today().weekday != 5 and datetime.today().weekday != 6:
    print("Unfortunately today is a weekday")
else:
    print("It is the weekend, Yay!")