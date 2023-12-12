X = int(input())  
H = int(input())  
M = int(input())  

total_sleep = H * 60 + M + X

alarm_hours = total_sleep // 60
alarm_minutes = total_sleep % 60

print(alarm_hours)
print(alarm_minutes)