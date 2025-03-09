def main():
    time = input("What time is it? ")
    if 8 => convert(time) >= 7:
        print("breakfast time")
    elif 13 => convert(time) >= 12:
        print("lunch time")
    elif 19 => convert(time) >= 18:
        print("dinner time")
    else:
        pass

def convert(time):
    hour, minute = time.split(':')
    hour, minute = int(hour), int(minute)
    min = minute / 60
    return hour + min

if __name__ == "__main__":
    main()

