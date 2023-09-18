# Import built-in library datetime.
import datetime

# Assign string representing date in DDMMYYYY format e.g. 04072023.
# Order of day, month and year can be changed e.g. MMDDYYYY.
date_string = "04072023"

# Obtaining datetime object from date_string.
# Argument "%d%m%Y" should match the order of day, month and year in date_string; reorder where appropriate.
# .date() method used at the end of the line to extract only the date component of datetime object, omitting the time component.
formatted_date = datetime.datetime.strptime(date_string, "%d%m%Y").date()

# Output is in YYYY-MM-DD by default.
print(formatted_date)
