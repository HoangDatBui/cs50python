def main():
    month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        date = input("Date: ").strip()
        try:
            month, day, year = date.split("/")
            day = int(day)
            month = int(month)
            if day <= 31 and month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                continue

        except ValueError:
            try:
                month_day, year = date.split(", ")
                month, day = month_day.split(" ")
                if month.isdigit():
                    continue
                if month in month_list:
                    month = month_list.index(month) + 1
                day = int(day)
                month = int(month)
                if day <= 31 and month <= 12:
                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:
                    continue
            except:
                continue



main()
