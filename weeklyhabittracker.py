habit=("snowboarding",True,7,30.45)
print(habit)
weeklyhabit=(1,1,1,0,0,1,0)
print(weeklyhabit)
print("total days tracked",len(weeklyhabit))
print("Day1 status",weeklyhabit[0])
print("Day4 status",weeklyhabit[3])
first3days=weeklyhabit[0:3]
print("FIRST 3 DAYS",first3days)
weekendays=weeklyhabit[5:7]
print("weekend daays",weekendays)
weeklyhabit=weeklyhabit+(1,)
print("after adding one more day",weeklyhabit)
completed = weeklyhabit.count(1)
missed = weeklyhabit.count(0)
print("Completed days:", completed)
print("Missed days:", missed)
done = 0
not_done = 0

for i in range(0, len(weeklyhabit)):
if weeklyhabit[i] == 1:
done += 1
else:
not_done += 1

if done > not_done:
    print("Great habit progress")
else:
    print("try being more consistent")
    print("")
print("weekly habit tracker sumary")
print("Habit Name:", habit_info[0])
print("Weekly Record:", weekly_habits)
print("Completed:", done)
print("Missed:", not_done)
