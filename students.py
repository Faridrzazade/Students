
from datetime import datetime

class Students:
    def __init__(self, name, surname, birthday_year, birthday_month, birthday_day, price, speciality):
        self.name = name
        self.surname = surname
        self.birthday_year = int(birthday_year)
        self.birthday_month = int(birthday_month)
        self.birthday_day = int(birthday_day)
        self.price = price
        self.speciality = speciality

    def display_information(self):
        print(f"Name: {self.name},\nSurname: {self.surname},\nBirthday Year: {self.birthday_year},\nBirthday Month: {self.birthday_month},\nBirthday Day: {self.birthday_day},\nPrice: {self.price},\nSpeciality: {self.speciality}")

user_name = input("Enter your name: ")
user_surname = input("Enter your surname: ")
user_birthday_year = input("Enter year birthday: ")
user_birthday_month = input("Enter birthday month: ")
user_birthday_day = input("Enter birthday day: ")
user_price = int(input("Enter your school price: "))
user_speciality = input("Enter your speciality: ")

school_account = Students(user_name, user_surname, user_birthday_year, user_birthday_month, user_birthday_day, user_price, user_speciality)

def change_major_input():
    user_major_change = input("Enter new speciality: ")
    school_account.speciality = user_major_change
    print("New speciality:", school_account.speciality)

def calculation_of_age():
    date_today = datetime.now()
    today_year = date_today.year
    today_month = date_today.month
    today_day = date_today.day

    age_year = today_year - school_account.birthday_year
    age_month = today_month - school_account.birthday_month
    age_day = today_day - school_account.birthday_day

    if age_day < 0:
        age_month -= 1
        age_day += 30

    if age_month < 0:
        age_year -= 1
        age_month += 12

    print("Age:", age_year, "years", age_month, "months", age_day, "days")

school_account.display_information()
change_major_input()
calculation_of_age()
