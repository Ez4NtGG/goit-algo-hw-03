from datetime import datetime 

# ЗАВДАННЯ 1

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")

    current_date = datetime.today().date()

    difference = (current_date - given_date).days

    return difference

if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
