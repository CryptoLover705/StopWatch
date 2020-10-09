"""
Code: CryptoLover705
Updated: oct 9, 2020 2:02 pm
"""

import time
import sys

prompt = "type 's' start stopwatch / or 'exit': "
print(exit)

def stopwatch():
    s = 0
    while True:
        try:
            # print one line only
            sys.stdout.write("\r")
            sys.stdout.write(str(format(s, ".2f")) + " Seconds...")
            sys.stdout.flush()
            s += 0.01
            time.sleep(0.01)    
        except KeyboardInterrupt:
            print("\nPaused: "+ format(s, ".2f")+ " Seconds")
            prompt2 = "Press 'r' to resume / 'R' to reset /any key to break: "
            reply = input(prompt2)
            if reply == 'r':
                continue
            elif reply == 'R':
                s = 0
            else:
                s = 0
                break
            
while True:
    press = input(prompt)
    if press == 'exit()' or press == 'exit':
       exit(0)
    elif press == 's':
        print("Press volume down + c to pause / ctrl+c")
        stopwatch()
    else:
        print("Try again")

# run @ pyroid3 or cmd terminal
