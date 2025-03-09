import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    isCorrectFormat = re.search(r"^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$", s, re.IGNORECASE)
    if isCorrectFormat:
        groups = isCorrectFormat.groups()
        if int(groups[0]) > 12 or int(groups[3]) > 12:
            raise ValueError
        if groups[1] and int(groups[1]) > 59 or groups[4] and int(groups[4]) > 59:
            raise ValueError
        first_time = new_format(groups[0], groups[1], groups[2])
        second_time = new_format(groups[3], groups[4], groups[5])
        return first_time + " to " + second_time
    else:
        raise ValueError

def new_format(hour, minute, am_pm):
    hour = int(hour)
    if am_pm.upper() == "PM" and hour != 12:
        hour += 12
    elif am_pm.upper() == "AM" and hour == 12:
        hour = 0

    if minute is None:
        minute = '00'

    return f"{hour:02d}:{minute}"

if __name__ == "__main__":
    main()
