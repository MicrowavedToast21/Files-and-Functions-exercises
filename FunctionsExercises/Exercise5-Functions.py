from datetime import datetime

def is_valid_date(date_str):
    try:
      date_object = datetime.strptime(date_str, "%d/%m/%Y")
      return True
    except ValueError:
        return False
def is_valid_day_month(day, month):
    if 1 <= day <= 31 and 1 <= month <= 12:
        return True
    else:
        return False

while True:
    date_string = input("Enter a date in the format dd/mm/yyyy: ")

    if is_valid_date(date_string):
        date_object = datetime.strptime(date_string, "%d/%m/%Y")
        day = date_object.day
        month = date_object.month

        if is_valid_day_month(day, month):
            print(f"Valid date!. The day is: {day}, month is {month}, year is: {date_object.year}")
            break
        else:
            print("Invalid date or month. Please enter a valid date.")
    else:
        print("Invalid date. Please enter a valid date.")