# Import built-in library datetime.
import datetime

# For this example, the datetime object used will be today's date.
date_obj = datetime.date.today()

# Obtaining string representation of date_obj in DDMMYYYY format.
# Argument "%d%m%Y" should be in the order required by the output.
# Reorder to obtain order string representation formats e.g. "%m%d%Y" for MMDDYYYY format.
date_string = date_obj.strftime("%d%m%Y")

# Sample output.
print(date_string)
