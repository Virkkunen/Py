import time, os

version = "v0.1"
choice = "y"

def clear():
    os.system('cls')

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
        t = 25 * 60
        print("Pymodoro " + version + "\n\nTotal breaks: " + str(breaks) + "\n\nWork time")
        while t:
            mins = t // 60
            secs = t % 60
            timer = f"{mins}:{secs}"
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

        # break
        clear()
        if breaks == 3: t = 10 * 60
        else: t = 5 * 60
        print("Pymodoro " + version + "\n\nTotal breaks: " + str(breaks) + "\n\nBreak time")
        while t: 
            mins = t // 60 
            secs = t % 60
            timer = f"{mins}:{secs}"
            print(timer, end="\r")
            time.sleep(1)
            t -= 1 
        breaks += 1

if __name__ == "__main__":
    main()