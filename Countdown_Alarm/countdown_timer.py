import time
import winsound

# Function to convert time format to seconds
def get_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s

# Countdown function
def countdown(t_second, message):
    while t_second:
        mins, secs = divmod(t_second, 60) 
        hours, mins = divmod(mins, 60)
        timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs) 
        print(timeformat, end='\r')
        time.sleep(1)   
        t_second -= 1
    print(message)
    winsound.PlaySound("piano_alarm", winsound.SND_ASYNC + winsound.SND_LOOP)

#Function to stop Alarm
def stop_alarm():
    input("Press Enter to stop the alarm.")
    winsound.PlaySound(None, winsound.SND_ASYNC)


def cycle(work_seconds, rest_seconds, cycles):
    for _ in range(cycles):
        # Running the work timer
        countdown(work_seconds, "Work Session Over. Time to rest!")
        stop_alarm()

        # Running the rest timer
        countdown(rest_seconds, "Rest Session Over. Time to get back to work!")
        stop_alarm()


# Asking user for timer input in hour, minutes, and seconds
wk_timer = input("Set Work Timer: Enter a time to work in the format HH:MM:SS\n")
rest_timer = input("Set Rest Timer: Enter a time to rest in the format HH:MM:SS\n")

#Asking for number of cycle
cycle_input = int(input("Enter number of cycle: "))

# Converting time format to seconds
work_seconds = get_seconds(wk_timer)
rest_seconds = get_seconds(rest_timer)

# Starting the Pomodoro cycles
cycle(work_seconds, rest_seconds, cycle_input)
