import time     # time library
from plyer import notification      #plyer library

title = 'Do calisthenics everyday for 30mins only.'     

message = 'At least Push-ups, Chin-ups, Abs training, Cobra strech, Downdog Strech' 

# new thing. for exception to check bug, use try and except   
try:
    notification.notify(title = title,      #notify function call
                    message = message,
                    app_icon = "daily-health-app.ico",      #must ".ico" format
                    timeout = 60,
                    toast = False)
except Exception as e:
    print(f"Oops! {e}")

time.sleep(60*60)       #time duration to pause the program