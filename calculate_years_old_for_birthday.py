from datetime import datetime

birthday = datetime.strptime('2002-12-18', '%Y-%m-%d').date()
print(birthday)
today = datetime.now().date()
print(today)
years = (today.year-birthday.year)
if birthday.month >= today.month and birthday.day > today.day:
  years -= 1
print(years)