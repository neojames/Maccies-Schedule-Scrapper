# Scrap.py
# Main program logic; Scraps scheduling data from peoplestuffuk.com, checks to see if it has been updated, and if it has
# updates a shared calender. Scrapes calender from peoplestuff and puts it into an appropriate format.
# Published under the Apache License 2.0, maintained by James Bolton (james@neojames.me)

import argparse
from getpass import getpass

import mechanicalsoup

parser = argparse.ArgumentParser(description="Login to GitHub.")
parser.add_argument("username")
args = parser.parse_args()

args.password = getpass("Please enter your GitHub password: ")

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_403=True,
    user_agent='MyBot/-1.1: mysite.example.com/bot_info',
)
# Uncomment for a more verbose output:
# browser.set_verbose(1)

browser.open("https://github.com")
browser.follow_link("login")
browser.select_form('#login form')
browser["login"] = args.username
browser["password"] = args.password
resp = browser.submit_selected()

# Uncomment to launch a web browser on the current page:
# browser.launch_browser()

# verify we are now logged in
page = browser.get_current_page()
messages = page.find("div", class_="flash-messages")
if messages:
    print(messages.text)
assert page.select(".logout-form")

print(page.title.text)

# verify we remain logged in (thanks to cookies) as we browse the rest of
# the site
page2 = browser.open("https://github.com/MechanicalSoup/MechanicalSoup")
assert page2.soup.select(".logout-form")
