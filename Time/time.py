import time

# pip install time

current_day = time.asctime()

print(current_day)

print(time.strftime('%A'))
print(time.strftime('%a'))

print(time.strftime('%B'))
print(time.strftime('%b'))

print(time.strftime('%H'))
print(time.strftime('%M'))

print(time.strftime('%H:%M'))