from datetime import date

user_input = input().split(' ')
dayofweek = int(user_input[0])
monthofyear = int(user_input[1])
d = date(2009, monthofyear, dayofweek) 
print(d.strftime('%A'))