# FalL Guys Locker Value Calculator
## A script to find how many Showbucks and Kudos your Fall Guys locker is worth!

## Item Pricing data obtained from the [Fall Guys Cosmetics Spreadsheet](https://docs.google.com/spreadsheets/d/1eaa8MfYVrtkA1apyfKGWITRLAUqzPoBo10dsbXGMbDM/edit#gid=1017097573)

## _TO USE: Download the repository. The raw python file will be directly in the repository folder, but the executable is inside the `locker-value-calculator`  folder. I would have made it a single executable but GitHub has a commit file size limit of 25MB lol._
# Prerequisites
* The [Discord](https://discord.com/download) app
* A server with the [Bean Bot](https://discord.com/api/oauth2/authorize?client_id=757943040198443054&permissions=380104993856&scope=bot%20applications.commands) Discord bot
### AND, if using the script instead of the executable:
* [Python](https://www.python.org/downloads/) 3.10 or newer (made and tested on [3.10.8](https://www.python.org/downloads/release/python-3108/))
* [pip](https://pip.pypa.io/en/stable/installation/) (Should come with the python installation)
### libraries:
* **os** (for file management) (includeed in the base python installation)
* **win32gui** (for active window detection)
* **requests** (for downloading the spreadsheets)
* **pandas** (for data manipulation and analysis)
* **pynput** (for mouse click and position detection)
* **pyautogui** (for mouse and keyboard control)
* **pyperclip** (for obtaining clipboard contents)
# Usage
## Disclaimers
* The script creates and manages files (specifically, a folder which then houses all of the spreadsheets) within its directory, so it is _**strongly**_ reccomended that it is isolated in some folder when run!
* ALWAYS wait until the next page is shown before clicking again when cycling between locker pages! (This ONLY does not apply for the last page of each locker)
* The script works by cycling through Bean Bot's `/locker`  command and copying the text it outputs. If you have Discord's scaling settings set significantly different from the defaults, consider temporarily setting them to the default values\
\
![Discord scaling settings](https://github.com/ioh-UwU/fg-locker-value-calculator/assets/81399391/d1a60a62-7a2f-4934-8f4d-c9deb4e30501)
\
`Space Between Message Groups` can be set to its maximum value to improve the reliability of copied text, but this is not strictly necessary. 
* Don't wait _too_ long between inputs with the bot! The navigation buttons on the locker dissapear after a few minutes of no interaction!
## Instructions
1. Run the file. You will be prompted with a disclaimer similar to the first point above. type "continue" into the terminal and hit ender to keep going\
(this will be the case every time a similar message shows up)

The script will then download or update and organize all of the spreadsheets that it uses.

2. Open the Discord app or, if it is open already, navigate to it. THe script will continue after this.
3. You will be prompted to log in to use Bean Bot. It is **STRONGLY RECCOMENDED** that you use the bot in a private server or channel to avoid any interruptions from other server members typing!\
**DO NOT NAVIGATE AWAY FROM THE CHANNEL AFTER COMPLETING THIS STEP!**
4. You will be prompted to continue again in the terminal window. When you navigate back, the bot will automatically enter the first /locker command, and calibration will start.
5. Calibration\
You will be prompted to click the bottom right of the bot's message box, then the top left, and finally directly under the "Next" button.\
Ensure that your clicks are within the area that gets lightly highlighted when you hover over the message...

![Message highlight graphic](https://github.com/ioh-UwU/fg-locker-value-calculator/assets/81399391/350f944c-850b-4233-a6a6-94d04ee4e5c8)

That your bottom-right click is below the bottom of the message and far enough to the right...

![Message highlight graphic](https://github.com/ioh-UwU/fg-locker-value-calculator/assets/81399391/12921927-a364-429a-a0a6-1c69676ea43a)

That your top-left click is within the message box...
_(Going outside can cause some strange behavior by copying a lot more text from other parts of the app than what is expected.)_

![Message highlight graphic](https://github.com/ioh-UwU/fg-locker-value-calculator/assets/81399391/eb6aa75a-55d2-4db0-bbd9-a32bd994170c)

And that your click below the "Next" button is as close as possible without highlighting the button.

![Button highlight graphic](https://github.com/ioh-UwU/fg-locker-value-calculator/assets/81399391/6cd337aa-7911-447a-9f5b-42063bccc8ba)

6. Click whenever the next page loads (the blue highlighted text goes away), repeat for every page of the locker.\
For the last page, once the text is highlighted and copied, click again to enter the command for the next locker.
7. Type continue in the terminal again, similar to step 3.
8. Repeat step six and seven until all locker menus have been processed. A message will appear in the terminal at this point saying all data has been collected (and there will not be another `/locker`  command following the final click).
9. Wait for the data to be processed. This may take a while, depending on how many items you have and how fast your CPU is.
10. The value statistics for your locker will be outputed in the terminal window!

# Potential Problems
* ### Interaction Failed after "Next" is clicked!
First wait a few seconds to see if the error goes away on its own, but if this does not work, simply click the "Previous" button. This will remove the error message, copy some text again (duplicates are accounted for, so this does not matter), and then continue once caught back up.
* ### A number in the results is much higher than I think it should be!
As with anything like this, there will be edge cases that may not be accounted for properly. If a number is too high, something (or several) has most-likely gotten around the checks in place and been counted more than once, and this can be resolved by running the script again with better calibration positions.
* ### The command wasn't sent and is uncompleted in my message box!
This shouldn't happen, but if something strange occurs, the command can be completed manually and submitted prior to continuing with text input in the terminal.
