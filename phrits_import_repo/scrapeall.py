# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
#   scrapeall.py
#
#   Author: Fritz Knack
#
#   Scrape every page at phrits.com as it exists on 2021-12-24.
#
#   General Comments
# *****************************
# See DESIGN_scrapeall.md for full worklog.
#
# 2021-12-24
# Meta and Initialization.
#
# 2021-12-26
# part_FATTOM.php scraped.
#
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************

# *****************************
"""
Imports
*******************************

from webdriver_manager.chrome import ChromeDriverManager
Runs the Chrome engine

from splinter import Browser
Browser automation. Execute scripts, move the mouse, modify cookies,
fill forms, search and navigate by element, back, forward, etc.

from bs4 import BeautifulSoup as soup
HTML content parser.

import sys
System calls (e.g., sys.exit())

"""
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
from bs4 import BeautifulSoup as bs
import sys
# *****************************************************************************


# *****************************************************************************
# def error_out
# *****************************
def error_out(e, msg_exit = ''):
    msg = 'Program Fail\n' \
        + '------------\n' \
        + msg_exit
    print(f'\n\n{e.__class__.__name__}')
    sys.exit(msg)


# *****************************************************************************
# Assorted options. Might as well gather them early.
# *****************************
opt_browser = 'chrome' # splinter defaults to firefox
opt_headless = True
opt_url = 'https://phrits.com/content/fat_tom.php'
opt_url = 'https://phrits.com/writing/'
opt_url = 'https://phrits.com/recipes/'
opt_parser = 'html.parser'

"""
Init
*******************************
path_exe:           ChromeDriverManager requirement
browser:            application
session_reponse:    application sesssion (e.g., chrome browser
soup:               base soup object, the (sub)page in HTML


"""

# get the browser engine
try:
    path_exe = {'executable_path': ChromeDriverManager().install()}
except Exception as e:
    error_out(e,
        'Unable to launch find path for ChromeDriverManager.install().'
        )

# get the browser session
try:
    browser = Browser(opt_browser, **path_exe, headless=opt_headless)
except Exception as e:
    error_out(e,
        f'Unable to create a session for URL {opt_url}'
        )

# go to the page
try:
    browser.visit(opt_url)
    session_reponse = browser.html
except Exception as e:
    error_out(e,
        f'Unable to retrieve page for URL {opt_url}'
        )

# Waiting in a hot tureen!
try: 
    soup = bs(session_reponse, opt_parser)
except Exception as e:
    error_out(e,
        f'Neither rich, nor green.\n' +
        'Couldn\'t make soup from URL {opt_url}'
        )

page = {
    "title": '',
    "h1_para": [],
    "h2s": [{
        "title": '',
        "h2_para": []
    }]
}
outer_bands = soup.find_all("div", class_="outerband")
for outer_band in outer_bands:
    inner_bands = outer_band.find_all("div", class_="innerband")
    h1_counter = -1
    h2_counter = -1
    for inner_band in inner_bands:
        h1s = inner_band.find_all("h1")
        for h1 in h1s:
            h1_counter += 1
            h2 = ''
            if not page['title']:
                page['title'] = h1.text
            try:
                elem = h1.find_next()
            except:
                elem = None
            while(elem):
                if elem.name == "h1":
                    elem = None
                elif elem.name == 'p' and not h2:
                    page["h1_para"].append(elem.contents)
                elif elem.name == 'h2':
                    h2_counter += 1
                    p_counter = 0
                    h2 = elem.text
                    h2_record = {
                        "title": h2,
                        "h2_paras": []
                    }
                    if h2_counter == 0:
                        page['h2s'][h2_counter] = h2_record
                    else:
                        page['h2s'].append(h2_record)
                elif elem.name == 'p':
                    if p_counter == 0:
                        page['h2s'][h2_counter]['h2_paras'] = elem.contents
                        p_counter += 1
                    else:
                        page['h2s'][h2_counter]['h2_paras'].append(elem.contents)
                try:
                    elem = elem.find_next()
                except:
                    elem = None

print(page)