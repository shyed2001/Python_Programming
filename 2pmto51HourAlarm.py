print('''
Alarm Clock V 1.11
''')
print('''
ptesent_time=2pm=14=a
Hours_to_Alarm=51=b
hours_per_day=24=c
''')
a=ptesent_time_2pm=14
b=Hours_to_Alarm=51
c=hours_per_day=24
print('''
Days_to_alarm=d=b//c
hourts_to_alarm_after_2pm=e=b%c
''')
Days_to_alarm=d=b//c
hourts_to_alarm_after_2pm=e=b%c
print("Days_to_alarm=d=b//c =" ,d )
print("hourts_to_alarm_after_2pm=e=b%c =" ,e )

print('''
The alarm goes off at
''', a+e,"00hrs or", 2+e,"pm")

print('''
Alarm Clock V 1.22
''')
print('''
CT=float(input("Enter the current time in 00.00 hours / 24 hours format: "))
WT=float(input("Enter the alarm waiting time in 00.00 hours/24 hours format: "))

''')
CT=float(input("Enter the current time in 00.00 hours / 24 hours format: "))
WT=float(input("Enter the alarm waiting time in 00.00 hours/24 hours format: "))
print(CT,"CT= the current time in 00.00 hours / 24 hours format: ")
print(WT,"WT= the alarm waiting time in 00.00 hours/24 hours format:  ")
print('''
add_days=(WT//24)
add_hours=(WT%24)
''')
add_days=(WT//24)
add_hours=(WT%24)

print("The alarm goes off after", add_days, "days ", "at",
(CT+add_hours),"hrs")

print('''

''')