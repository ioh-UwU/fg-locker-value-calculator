# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

# Used For file management
import os
# Used to ensure Discord is the active window before performing any action.
import win32gui
# Used to download spreadsheets
from requests import get
# Used for data analysis and organization
import pandas as pd
from pynput import mouse
import pyautogui as pgui
from pyperclip import paste

def wait_for_continue():
    '''Waits for the user to type and enter "continue."
    '''
    game_setup_confirmation = ''
    while game_setup_confirmation.lower().strip() not in ('continue', 'exit'):
        game_setup_confirmation = input('Enter "Continue" to continue or "Exit" to stop the program: ')
    if game_setup_confirmation.lower().strip() == 'exit':
        quit()

def dc_is_active_win():
    '''Checks if Fall Guys is the active window.
    '''
    try:
        if 'Discord' in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
            return True
    except:
        return False

def wait_for_dc_active_win():
    '''Waits until Discord is the active window, if it isn't already.
    '''
    first_check = True
    while not dc_is_active_win():
        if first_check:
            print('Please ensure Discord is open and set as the active window!')
            first_check = False
    while clicking:
        pass

# Temporary credit so I know where to find this link
# ASCII headers generated from https://patorjk.com/software/taag/#p=display&f=Modular&t=Script

#  _______  _______  ______    _______  _______  ______   _______  __   __  _______  _______  _______  _______
# |       ||       ||    _ |  |       ||   _   ||      | |       ||  | |  ||       ||       ||       ||       |
# |  _____||    _  ||   | ||  |    ___||  |_|  ||  _    ||  _____||  |_|  ||    ___||    ___||_     _||  _____|
# | |_____ |   |_| ||   |_||_ |   |___ |       || | |   || |_____ |       ||   |___ |   |___   |   |  | |_____
# |_____  ||    ___||    __  ||    ___||       || |_|   ||_____  ||       ||    ___||    ___|  |   |  |_____  |
#  _____| ||   |    |   |  | ||   |___ |   _   ||       | _____| ||   _   ||   |___ |   |___   |   |   _____| |
# |_______||___|    |___|  |_||_______||__| |__||______| |_______||__| |__||_______||_______|  |___|  |_______|

# Google Sheets spreadsheet Group IDs (Don't touch these! They're how the program knows which sheets are which!)
GIDS = {
    'changelog': '349407293',
    'non_seasonal_costumes': '2085473202',
    'single_costume_pieces': '1770087200',
    'ffa_costumes': '0',
    'legacy_costumes': '154614782',
    'colors': '892700064',
    'patterns': '252685768',
    'faces': '1756798647',
    'emotes': '1554596774',
    'celebrations': '1465053061',
    'banners': '465238921',
    'nicknames': '375606285',
}
FILE_NAMES = GIDS.keys()


def get_spreadsheet_url(gid):
    """Gets the URL of a spreadsheet form its GID (so I only need to store the GIDs in the dictionary above instead of the whole URL)
    """
    return f'https://docs.google.com/spreadsheets/d/1eaa8MfYVrtkA1apyfKGWITRLAUqzPoBo10dsbXGMbDM/export?gid={gid}&format=csv'


def update_csv_files():
    """Downloads up-to-date versions of all of the spreadsheets.
    """
    for file_name in FILE_NAMES:
        print(f'Updating {file_name}.csv')
        f = get(get_spreadsheet_url(GIDS[file_name]), allow_redirects=True, timeout=20)
        open(f'spreadsheets/{file_name}.csv', 'wb').write(f.content)


def determine_prices(dataframe, sb_ceiling, price_col, currency_col):
    """Determines what currency, if any, each item in a spreadsheet should be if it is blank.
    data_pair:      The key/value pair from the dataframes dictionary.
    sb_ceiling:     The maximum value of a showbucks item in this spreadsheet (this method will need to update if this ever overlaps with the cheapest kudos item in each section)
    price_col:      The Price/Method/etc. column.
    currency_col:   The Currency column.
    """
    for i, row in dataframe.iterrows():
        # Is the item from the crown ranks?
        if 'crown rank' in str(row[dataframe.columns[price_col]]).lower() or 'crown rank' in str(row[dataframe.columns[currency_col + 1]]).lower():
            dataframe.iat[i, currency_col] = 'Crowns'

        # Is the item purchased for Kudos or Showbucks?
        elif str(row[dataframe.columns[price_col]]).isdigit():
            currency = 'Showbucks'
            if int(row[dataframe.columns[price_col]]) > sb_ceiling:
                currency = 'Kudos'
            dataframe.iat[i, currency_col] = currency

        # Is the item from a DLC pack? (unused)
        elif 'pack' in str(row[dataframe.columns[price_col]]).lower():
            price = str(row[dataframe.columns[price_col]]).split('-', maxsplit=1)[0]
            if 'pack' not in price.lower() or '$' in str(row[dataframe.columns[price_col - 1]]):
                dataframe.iat[i, price_col] = price.strip()
                dataframe.iat[i, currency_col] = 'Dollars'

        # Is the item from a fame pass?
        elif str(row[dataframe.columns[currency_col]]) == 'nan' and str(row[dataframe.columns[price_col]]) != 'nan':
            dataframe.iat[i, currency_col] = 'Fame'

        # Is the item currently unobtainable?
        elif str(row[dataframe.columns[currency_col]]) == 'nan' and str(row[dataframe.columns[price_col]]) == 'nan':
            dataframe.iat[i, currency_col] = 'No Price'

        # Otherwise, leave it as-is!

#  _______  _______  ______    ___   _______  _______
# |       ||       ||    _ |  |   | |       ||       |
# |  _____||       ||   | ||  |   | |    _  ||_     _|
# | |_____ |    ___||   |_||_ |   | |   |_| |  |   |
# |_____  ||   |    |    __  ||   | |    ___|  |   |
#  _____| ||   |___ |   |  | ||   | |   |      |   |
# |_______||_______||___|  |_||___| |___|      |___|
# Initial confirmation to start.
print('Be sure to read the readme before continuing!')
print('This script creates and manages its files and it is HIGHLY reccomended that you run it inside its own folder.')
wait_for_continue()
print('\n')

# Creates a folder for the spreadsheet CSVs wherever this script is located.
if not os.path.exists('spreadsheets'):
    os.mkdir('spreadsheets')

# Downloads the current changelog and creates a dataframe from it.
print('Downloading latest changelog...')
cl = get(get_spreadsheet_url(GIDS['changelog']), allow_redirects=True, timeout=20)
open('spreadsheets/changelog_new.csv', 'wb').write(cl.content)
changelog_new = pd.DataFrame(pd.read_csv('spreadsheets/changelog_new.csv'))


# If there is already a changelog, see if the new one has an update. If so, update everything.
if os.path.exists('spreadsheets/changelog.csv'):
    changelog = pd.DataFrame(pd.read_csv('spreadsheets/changelog.csv'))
    if changelog.iat[0, 0] != changelog_new.iat[0, 0]:
        print('There is a new update! Downloading it now...')
        update_csv_files()
    else:
        print ('Spreadsheets are up to date!')

# Otherwise, download everything.
else:
    print('No spreadsheets found. Downloading them now...')
    update_csv_files()
os.remove('spreadsheets/changelog_new.csv')


# Creates updated dataframes from the spreadsheets and their key/value pairs!
dataframes = dict(zip(FILE_NAMES, [None]*len(FILE_NAMES)))
for key in dataframes.keys():
    dataframes[key] = pd.DataFrame(pd.read_csv(f'spreadsheets/{key}.csv'))
    data_pairs = zip(dataframes.keys(), dataframes.values())


# Fixes all of the price types for the dataframes.
for data_pair in data_pairs:
    headers = [h.lower() for h in data_pair[1].columns.str.strip()]
    if 'currency' in headers:
        match data_pair[0]:
            case 'non_seasonal_costumes':
                determine_prices(data_pair[1], 1200, 5, 6)
            case 'single_costume_pieces':
                determine_prices(data_pair[1], 400, 4, 5)
            case 'ffa_costumes':
                determine_prices(data_pair[1], 1200, 5, 6)
            case 'legacy_costumes':
                determine_prices(data_pair[1], 1200, 5, 6)
            case 'colors':
                determine_prices(data_pair[1], 300, 3, 4)
            case 'patterns':
                determine_prices(data_pair[1], 300, 3, 4)
            case 'faces':
                determine_prices(data_pair[1], 400, 3, 4)
            case 'emotes':
                determine_prices(data_pair[1], 600, 3, 4)
            case 'celebrations':
                determine_prices(data_pair[1], 700, 3, 4)
            case 'banners':
                determine_prices(data_pair[1], 100, 3, 4)
            case 'nicknames':
                determine_prices(data_pair[1], 50, 3, 4)

# Listener to detect mouse clicks.
mouse_pos = None
clicking = None
def on_click(x, y, pressed):
    global mouse_pos, clicking
    mouse_pos = (x, y)
    clicking = pressed
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

LOCKER_STRINGS = ('upper', 'lower', 'emote', 'face', 'colour', 'pattern', 'celebration', 'nameplate', 'nickname')
bbox = [0, 0, 0, 0]
next_button = [0, 0]
data = {}
total_items = 0

def copy_locker_text(locker_type):
    # Helps ensure no funny business occurs
    wait_for_dc_active_win()

    # Highlights the bot's text.
    pgui.moveTo(bbox[2], bbox[3])
    pgui.mouseDown(button='left')
    pgui.moveTo(bbox[0], bbox[1])
    pgui.mouseUp(button='left')
    pgui.hotkey('ctrl', 'c')
    pgui.leftClick(next_button[0], next_button[1])
    pgui.moveTo(next_button[0], next_button[1] + 30)
    # And stores it in a variable.
    copied_text = paste().split('\n')

    # Removes all the date strings, '\r' escapes, and the favorited item emojis.
    formatted_text = [l.replace(':fgheart:', '').replace('\r', '').strip() for l in copied_text if "Earned:" not in l]

    # Removes the filler from the start of the array.
    # (Not a static value to account for possible variance in the height of the copied text area.)
    for _ in formatted_text:
        cull = str(formatted_text.pop(0)).lower()    # vvv Prevents improper parsing caused by short text boxes.
        if 'locker' in cull and locker_type in cull:
            break

    # Gets the current and maximum page numbers. (Used for iteration.)
    temp_stats = formatted_text[-1].split('•')[0].split(' ')
    page, page_max = temp_stats[1], temp_stats[3]
    # Final cleaning up of the array of items.
    item_amount = formatted_text[0].split(' ')[-2]
    final_items = formatted_text
    for i in (0, -1, -1):
        final_items.pop(i)

    return [final_items, int(page), int(page_max), int(item_amount)]

wait_for_dc_active_win()
print('please open a channel that has the Bean Bot discord bot enabled \nand log in via the bot\'s /login command.')
wait_for_continue()
wait_for_dc_active_win()

for locker in LOCKER_STRINGS:
    pgui.press('Escape')
    pgui.typewrite(f'/locker {locker}')
    pgui.press('Tab')
    pgui.press('Enter')

    print('Please wait for the bot\'s message to process...')
    wait_for_continue()
    wait_for_dc_active_win()

    if bbox == [0, 0, 0, 0]:
        # Prevents the first point of the calibration from occuring when navigating back to Discord.
        while clicking:
            pass
        print('CALIBRATION: Click the bottom right of the bot\'s message box.')
        while not clicking:
            pass
        bbox[2], bbox[3] = mouse_pos
        while clicking:
            pass
        print('CALIBRATION: Click the top left of the bot\'s message box.')
        while not clicking:
            pass
        bbox[0], bbox[1] = mouse_pos
        while clicking:
            pass

    if next_button == [0, 0]:
        # Prevents the first point of the calibration from occuring when navigating back to Discord.
        while clicking:
            pass
        print('CALIBRATION: Click directly under the center of the "Next" button.')
        print('             Ensure your cursor is as close to the button as possible without actually highlighting it.')
        while not clicking:
            pass
        next_button[0] = mouse_pos[0]
        next_button[1] = mouse_pos[1] - 10
        while clicking:
            pass

    items = []
    locker_page_info = [0, 1, 2] # Temporary assignments.
    while locker_page_info[1] < locker_page_info[2]:
        # Sets the things to the things they are. (10/10 commenting, so descriptive!)
        locker_page_info = copy_locker_text(locker)
        items += locker_page_info[0]
        if locker_page_info[0] == 1:
            total_items += locker_page_info[3]
        # Waits for user input to account for delay when the bot loads a new page.
        print('Left click to continue.')
        while not clicking:
            pass
        while clicking:
            pass

    # Finally adds all the items to the data dictionary.
    data[locker] = items

mouse_listener.stop()

print('All data collected. Calculating locker value... (This may take a while.)')

# Format --> data_key: [dataframes, item_price_cols, item_currency_cols]
DATA_TO_DATAFRAME = {
    'upper': [['non_seasonal_costumes', 'single_costume_pieces', 'ffa_costumes', 'legacy_costumes'], [3, 4, 3, 3], [6, 4, 6, 6]],
    'lower': [['non_seasonal_costumes', 'single_costume_pieces', 'ffa_costumes', 'legacy_costumes'], [4, 4, 4, 4], [6, 4, 6, 6]],
    'emote': [['emotes'], [3], [4]],
    'face': [['faces'], [3], [4]],
    'colour': [['colors'], [3], [4]],
    'pattern': [['patterns'], [3], [4]],
    'celebration': [['celebrations'], [3], [4]], 
    'nameplate': [['banners'], [3], [4]],
    'nickname': [['nicknames'], [3], [4]] 
}

checked_items = []

kudos_price = 0
showbucks_price = 0
dollars_price = 0
no_currency = 0
unobtainable = 0

# Takes every item and searches it in its coresponding dataframes.
for key, item_set in data.items():
    for item in item_set:
        # Accounts for duplicate items.
        if [item, key] not in checked_items:
            dfs, price_cols, currency_cols = DATA_TO_DATAFRAME[key]
            for i, df in enumerate(dfs):
                price_index = price_cols[i]
                currency_index = currency_cols[i]
                for j, row in dataframes[df].iterrows():
                    # If the item is found, gets its price.
                    if row[1] == item:
                        try:
                            price = int(row[price_index])
                        except ValueError:
                            price = 0
                        if key == 'upper':
                            if item in data['lower']:
                                try:
                                    price = int(row[price_index + 1])
                                except ValueError:
                                    price = 0
                        elif key == 'lower':
                            if item in data['upper']:
                                price = 0
                        # Adds the price to the correct currency variable.
                        if row[currency_index] == 'Kudos':
                            kudos_price += price
                        elif row[currency_index] == 'Showbucks':
                            showbucks_price += price
                        elif row[currency_index] == 'No Price':
                            unobtainable += 1
                        else:
                            no_currency += 1
            checked_items.append([item, key])

# Displays all of the results!
print(f'\nTotal Items: {total_items}')
print(f'Unobtainable items: {unobtainable}')
print(f'Unpriced items: {no_currency}')
print(f'Showbucks Value: {showbucks_price}')
print(f'Kudos Value: {kudos_price}')