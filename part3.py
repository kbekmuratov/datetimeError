class DateTimeError(Exception):
    def __init__(self, component, value, requirement):
        self.component = component
        self.value = value
        self.requirement = requirement

    def __str__(self):
        return (
            f"Error: {self.value} for {self.component} "
            f"should be {self.requirement}. Don't be mad write currect date."
        )


def leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


class Date:
    def __init__(self, year, month, day):
        self.validate_date(year, month, day)
        self.year = year
        self.month = month
        self.day = day

    def validate_date(self, year, month, day):
        if type(year) != int:
            raise DateTimeError("year", year, "an integer between 0 and 9999")
        if not (0 <= year <= 9999):
            raise DateTimeError("year", year, "between 0 and 9999")
        if type(month) != int:
            raise DateTimeError("month", month, "an integer between 1 and 12")
        if not (1 <= month <= 12):
            raise DateTimeError("month", month, "between 1 and 12")
        if type(day) != int:
            raise DateTimeError("day", day, "an integer between 0 and 31")
        if not (1 <= day <= 31):
            raise DateTimeError("day", day, "between 1 and 31")

        if month == 2:
            max_days = 29 if leap(year) else 28
        elif month in [4, 6, 9, 11]:
            max_days = 30
        else:
            max_days = 31

        if not (1 <= day <= max_days):
            raise DateTimeError("day", day, f"between 1 and {max_days}")

    def __str__(self):
        return f"{self.year:04d}/{self.month:02d}/{self.day:02d}"


class DateTime(Date):
    def __init__(self, year, month, day, hour, minute, second):
        super().__init__(year, month, day)
        self.validate_time(hour, minute, second)
        self.hour = hour
        self.minute = minute
        self.second = second

    def validate_time(self, hour, minute, second):

        if type(hour) != int:
            raise DateTimeError("hour", hour, "an integer between 0 and 23")
        if type(minute) != int:
            raise DateTimeError("minute", minute, "an integer between 0 and 59")
        if type(second) != int:
            raise DateTimeError("second", second, "an integer between 0 and 59")

        if not (0 <= hour <= 23):
            raise DateTimeError("hour", hour, "between 0 and 23")
        if not (0 <= minute <= 59):
            raise DateTimeError("minute", minute, "between 0 and 59")
        if not (0 <= second <= 59):
            raise DateTimeError("second", second, "between 0 and 59")

    def __str__(self):
        date_str = super().__str__()
        time_str = f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        return f"{date_str} {time_str}"


try:
    datetime = DateTime(2024, 4, 30, "23", 59, 59)
    print(datetime)
except DateTimeError as error:
    print(error)


try:
    datetime = DateTime(2024, 11, 25, 12, 30, 45)
    print(datetime)
except DateTimeError as error:
    print(error)


try:
    date = Date(2024, "February", 28)
    print(date)
except DateTimeError as error:
    print(error)

try:
    print(datetime)
except DateTimeError as error:
    print(error)

try:
    date = Date(2024, 2, 28)
    print(date)
except DateTimeError as error:
    print(error)

try:
    datetime = DateTime(2021, 2, 29, 15, 0, 0)
    print(datetime)
except DateTimeError as error:
    print(error)

try:
    datetime = DateTime(2024, 11, "f", 12, 30, 45)
    print(datetime)
except DateTimeError as error:
    print(error)
