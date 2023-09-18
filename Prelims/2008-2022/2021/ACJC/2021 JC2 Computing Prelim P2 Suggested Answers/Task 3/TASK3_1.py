# TASK 3.1
def second_dose_date(date):
    # This represents the maximum number of days in [Jan, Feb, Mar, ..., Dec]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Extract month and day
    month = int(date[4:6])
    day = int(date[6:])

    # Calculate the result month and day
    new_month = month + ((day + 21) // days[month-1])
    new_day = (day + 21) % days[month-1]
    
    # Format the result month
    if new_month < 10:
        new_month = "0" + str(new_month)
    else:
        new_month = str(new_month)

    # Format the result day
    if new_day < 10:
        new_day = "0" + str(new_day)
    else:
        new_day = str(new_day)

    # Concatenate the strings and return the result date
    result = "2021" + new_month + new_day
    
    return result

# Test cases
print(second_dose_date("20210105"))
print(second_dose_date("20210212"))	
print(second_dose_date("20210919"))
