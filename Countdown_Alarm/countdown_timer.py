#Countdown timer
import time
import winsound
#Imports we might need 
    #Something for timer
    #import for sound

#Asking user for timer input in hour and minutes
timer = input("Enter a time in the format HH:MM:SS\n")
h, m, s = map(int, timer.split(":"))
timer_seconds = (h * 3600) + (m * 60) + (s * 1)
print(timer_seconds)
#Logic to countdown
#for every second that is reduced
#do a time.sleep(1) 1 second representing the seconds between.
#when the length of the delimeter is == 0:
    #print("Countdown over")
while timer_seconds > 0:
    timer_seconds -= 1
    time.sleep(1)
    print(timer_seconds)
    if timer_seconds == 0:
        play_sound = winsound.PlaySound("piano_alarm", winsound.SND_ASYNC + winsound.SND_LOOP)
        input("Enter any input to stop sound")
        winsound.PlaySound(None, 0)
        print("Count Down Over")

    
