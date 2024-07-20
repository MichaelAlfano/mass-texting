#
# September 18, 2023
# Michael Alfano (michaelalfano2004@gmail.com, 802-491-9240)
# send-texts.py
#
# Usage: python3 send-texts.py
#

import os
import time

numbers = list(
    set(
        [
            #  Insert numbers here
            #  VSCode hack: Do option + shift + left click to edit multiple lines at once.
            #               This makes it easy to format numbers and add commas
            #  VERY IMPORTANT: numbers need to be formatted without dashes and parenthesis
            #  Examples:
            #  1234567890,
            #  9876543210,
            #  ...
        ]
    )
)

message = "ADD YOUR MESSAGE HERE"

messageDelay = 0.15


def sendMessage(receiver, message):
    os.system(
        'osascript scripts/sendiMessage.scpt "' + receiver + '" "' + message + '"'
    )


for i, number in enumerate(numbers):
    to = str(number)
    msg = message

    sendMessage(to, str(msg))

    print("Message " + str(i + 1) + " of " + str(len(numbers)) + " sent")

    time.sleep(messageDelay)

print("Send completed")
