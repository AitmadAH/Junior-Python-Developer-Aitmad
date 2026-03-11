import datetime

def get_next_birthday(birthdate):
    today = datetime.date.today()
    current_year_birthday = datetime.date(today.year, birthdate.month, birthdate.day)
    if current_year_birthday < today:
        return datetime.date(today.year + 1, birthdate.month, birthdate.day)
    return current_year_birthday

def calculate_time_until(birthday):
    now = datetime.datetime.now()
    birthday_datetime = datetime.datetime.combine(birthday, datetime.time())
    delta = birthday_datetime - now
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    return days, hours, minutes

def get_birthdate_from_user():
    while True:
        birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
        try:
            birthdate = datetime.datetime.strptime(birth_input, "%Y-%m-%d").date()
            return birthdate
        except ValueError:
            print("Invalid format! Please enter the date as YYYY-MM-DD.")

def main():
    print("🎉 Welcome to the Birthday Calculator! 🎉")
    birthdate = get_birthdate_from_user()
    next_birthday = get_next_birthday(birthdate)
    days, hours, minutes = calculate_time_until(next_birthday)
    
    if days == 0 and hours == 0 and minutes == 0:
        print("🎂 Happy Birthday! Today is your special day!")
    else:
        print(f"Your next birthday is on {next_birthday.strftime('%A, %B %d, %Y')}")
        print(f"Time left: {days} days, {hours} hours, and {minutes} minutes 🎁")

if __name__ == "__main__":
    main()