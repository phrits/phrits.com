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
from bs4.element import PageElement
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
from bs4 import BeautifulSoup as bs
import sys
from pre_models import HPage, Section, Heading, Paragraph

MAX_OUTLINE_LEVEL = 99  # Arbitrarily large number for things that aren't headings
DIV_LEVEL = 50  # Arbitrary


# *****************************************************************************
# def error_out
# *****************************
def error_out(e, msg_exit = ''):
    msg = 'Program Fail\n' \
        + '------------\n' \
        + msg_exit
    print(f'\n\n{e.__class__.__name__}')
    sys.exit(msg)


# *****************************
# *****************************
def session_launch():
# *****************************
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
        return(soup)
    except Exception as e:
        error_out(e,
            f'Neither rich, nor green.\n' +
            'Couldn\'t make soup from URL {opt_url}'
            )

# *****************************************************************************

# *****************************
# *****************************
def gather_links(tag_links):
    return(tag_links)

# *****************************
# *****************************
def is_heading(tag = None):
    if tag.name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        return True
    else:
        return False


# *****************************************************************************
# Assorted options. Might as well gather them early.
# *****************************
opt_browser = 'chrome' # splinter defaults to firefox
opt_headless = True
# opt_url = 'https://phrits.com/content/fat_tom.php'
# opt_url = 'https://phrits.com/writing/'
opt_url = 'https://phrits.com/recipes/'
opt_parser = 'html.parser'



# *****************************
# *****************************
# *****************************
# *****************************
try:
    soup = session_launch()
except:
    error_out(Exception, "Failed init.")

page = HPage()


tag_outers = soup.find_all("div", class_="outerband")
for tag_outer in tag_outers:
    tag_inners = tag_outer.find_all("div", class_="innerband")
    for tag_inner in tag_inners:
        gather_links(tag_inner.find_all('a'))
        tag_content = tag_inner.findChildren(recursive=False);
        int_sequence = -1
        for tag in tag_content:
            if is_heading(tag):
                int_sequence += 1
                heading = Heading(),
                heading.s_heading = tag.text
                heading.fk_parent = page
                heading.int_sequence = int_sequence
                print(heading)
                page.arr_sections.append(heading)
            elif tag.name in ("p"):
                int_sequence += 1
                paragraph = Paragraph()
                paragraph.fk_parent = page.pk_id
                paragraph.txt_content = tag.content
                page.arr_sections.append(paragraph)
#                print(paragraph)
    

            elif tag.name in ("div"):
                next
            else:
                next




# print(f'\n\n{page}')
