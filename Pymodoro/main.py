import time, os, sys

version = "v0.3"

# TODO
# - remove cursor from countdown
# - add total pomodoro cycles
# - improve alarms

def clear():
    if os.name == "nt": os.system('cls')
    if os.name == "posix": os.system('clear')

clear()

def main():
    while True:
        pomodoro()
        choice = input("Start again? [y/n]: ")
        if choice.lower() == "y" or choice.lower() == "yes": continue
        else: 
            clear()
            break
        
def pomodoro():
    breaks = 0

    while breaks < 4:
        # work
        clear()
        t = 25 * 60 # 25 minutes
        print("Pymodoro " + version + "\n\nTotal breaks: " + str(breaks) + "\n\nWork time")
        while t:
            mins = t // 60
            secs = t % 60
            timer = f"{mins}:{secs}"
            print(timer, end="\r") # \r replaces last line
            time.sleep(1)
            t -= 1
        print('\a') # terminal bell

        if breaks == 3: choice = input("Long rest? [y/n] ")
        else: choice = input("Short rest? [y/n] ")

        if choice.lower() == "y" or choice.lower() == "yes":
            # break
            clear()
            if breaks == 3: t = 10 * 60 # 10 minutes on the 4th break
            else: t = 5 * 60 # 5 minutes
            print("Pymodoro " + version + "\n\nTotal breaks: " + str(breaks) + "\n\nBreak time")
            while t: 
                mins = t // 60 
                secs = t % 60
                timer = f"{mins}:{secs}"
                print(timer, end="\r")
                time.sleep(1)
                t -= 1 
            breaks += 1
            print('\a') # terminal bell
            choice = input("Back to work? [y/n] ")
            if choice.lower() == "y" or choice.lower() == "yes": continue
            else: break
        else: break

if __name__ == "__main__":
    main()
