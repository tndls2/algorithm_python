hour, minute = map(int, input().split())
duration = int(input())

new_minute = minute + duration
if new_minute//60 >= 1:
    hour += new_minute//60
    new_minute %= 60

hour %= 24

print(hour, new_minute)