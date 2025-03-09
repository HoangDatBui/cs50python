from datetime import date
import inflect
import sys

def main():
    birth_date = input("Date of Birth: ")
    try:
        minutes = calculate_minutes(birth_date)
        words = convert_to_words(minutes)
        print(words + " minutes")
    except ValueError:
        sys.exit("Invalid date")

def calculate_minutes(birth_date):
    try:
        birth = date.fromisoformat(birth_date)
        today = date(2000, 1, 1)  # Assuming this is the current date for the demo
        days = (today - birth).days
        return days * 24 * 60
    except ValueError:
        raise ValueError("Invalid date format")

def convert_to_words(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize()

if __name__ == "__main__":
    main()
