# Scrap.py
# Main program logic; Scraps scheduling data from peoplestuffuk.com, checks to see if it has been updated, and if it has
# updates a shared calender. Scrapes calender from peoplestuff and puts it into an appropriate format.
# Published under the Apache License 2.0, maintained by James Bolton (james@neojames.me)

import argparse
from datetime import datetime, timedelta

from mechanicalsoup import *

parser = argparse.ArgumentParser()
parser.add_argument("username")
parser.add_argument("password")
args = parser.parse_args()

browser = StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='NCSA_Mosaic/2.7b4: X11/AIX 1 000180663000',
)

# Uncomment for a more verbose output:
# browser.set_verbose(1)
# browser.set_debug(1)

# Login to PeopleStuff
browser.open("https://www.peoplestuffuk.com/WFMMCDPRD/Login.jsp")
browser.select_form('form')
browser["txtUserID"] = args.username
browser["txtPassword"] = args.password
browser.submit_selected()

# # Uncomment to launch a web browser on the current page:
# browser.launch_browser()

# Get current weeks calender
page = browser.get_current_page()
tables = page.findAll("table")
goodTables = tables[28].get_text().splitlines()
# with open('../cache/table.txt', 'w') as f:
#     print(goodTables, file=f)
# lines = open('../cache/table.txt').read().splitlines()

# Write calender to list
schedule = [goodTables[22].replace(u'\xa0', u'').replace('-', ', '),
            goodTables[45].replace(u'\xa0', u'').replace('-', ', '),
            goodTables[68].replace(u'\xa0', u'').replace('-', ', '),
            goodTables[91].replace(u'\xa0', u'').replace('-', ', '),
            goodTables[114].replace(u'\xa0', u'').replace('-', ', '),
            goodTables[137].replace(u'\xa0', u'').replace('-', ', '),
            goodTables[160].replace(u'\xa0', u'').replace('-', ', ')]

# Prepare list of subjects for gCal
subjects = ["Subject", "Start date", "Start time", "End time"]

# Prepare current date
today = datetime.now().date()
start = today - timedelta(days=today.weekday())

# Create list for each day in gCal format

# Monday
if not schedule[0]:
    print("Monday off!")
else:
    monday = ["Work", str(start), schedule[0]]
    print(monday)

# Tuesday
if not schedule[1]:
    print("Tuesday off!")
else:
    tuesday = ["Work", str(start), schedule[1]]
    print(tuesday)

# Wednesday
if not schedule[2]:
    print("wednesday")
else:
    wednesday = ["Work", str(start), schedule[2]]
    print(wednesday)

# Thursday
if not schedule[3]:
    print("Thursday off!")
else:
    thursday = ["Work", str(start), schedule[3]]
    print(thursday)

# Friday
if not schedule[4]:
    print("Friday off!")
else:
    friday = ["Work", str(start), schedule[4]]
    print(friday)

# Saturday
if not schedule[5]:
    print("Saturday off!")
else:
    saturday = ["Work", str(start), schedule[5]]
    print(saturday)

# Sunday
if not schedule[6]:
    print("Sunday off!")
else:
    sunday = ["Work", str(start), schedule[6]]
    print(sunday)

# TODO: Convert into consistantly ordered CSV to make comparisson easier.

browser.close()
