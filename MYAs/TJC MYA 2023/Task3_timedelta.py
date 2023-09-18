# Import built-in library datetime.
import datetime

# For this example, the datetime object used will be today's date.
date_obj = datetime.date.today()

# Add 1 week to date_obj.
newdate = date_obj + datetime.timedelta(weeks = 1)

print(newdate)

# Besides the parameter weeks, other parameters include the following:
    # days
    # seconds
    # microseconds
    # milliseconds
    # minutes
    # hours
