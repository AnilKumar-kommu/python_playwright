#clock use in python
import time
# def clock():
#     while True:
#         # Get the current local time
#         local_time = time.localtime()
#         # Format the time as HH:MM:SS
#         current_time = time.strftime("%H:%M:%S", local_time)
#         print("Current Time:", current_time)
#         # Wait for 1 second before updating the time
#         time.sleep(1)
#         clock()
#         print("Right Shift c by 1:", current_time )
#
# clock()

def clock():
    while True:
        local_time=time.localtime()
        time.strftime("%H:%M:%S",local_time)
        print("Current Time:",local_time)





