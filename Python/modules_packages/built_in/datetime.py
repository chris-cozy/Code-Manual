# This module allows you to utilize date-time objects
# Creation of a time object
    # initialization params are (hour, minute, second, microsecond)
    # The params you don't fill in are filled for you with 0
    # You can access these params like attributes
import datetime
mytime = datetime.time(3,40,5)

# Creation of a date object - similar to creation of time object
    # initialization params are (year, month, day)
# Using today() grabs the current date
# You can access these params like attributes
mydate = datetime.date.today()
print(mydate.year)

# ctime() formats the date in a date-timestamp format
mydate_ctime = mydate.ctime()


# To create a date-time object
    # initialization params are (year, month, day, hour, minute, second, microsecond)
from datetime import datetime
mydatetime = datetime(2021,10,3, 14, 20, 1)
print(mydatetime)

# You can replace elements using the replace() method
mydatetime = mydatetime.replace(year = 2022)


# Can perform operations with these objects as well (date or datetime object)
    # Returns a timedelta object, returns difference in number of days, as well as time difference
    # With this object there are also attributes such as total seconds between the objects
from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,12,4)
diff = date1 - date2
print(diff)

datetime1 = datetime(2021,11,3,12,30,56)
datetime2 = datetime(2020,12,4,7,23,21)
diff = datetime1 - datetime2
print(diff)