# Metro Police Speed System Task

average_speed = float(input("Enter the average speed:"))
speed_used = float(input("Enter the speed used: "))
points = (speed_used - average_speed)//5

if speed_used <= average_speed:
    print("OK")

else:
    speed_used - average_speed
    diff = (speed_used - average_speed) /5
    print(diff)

    if int(diff) >= 12:
        print( "Time to go to jail")