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
            '\tCouldn\'t make soup from URL {opt_url}'
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

# from django.db import models
# MAX_INDEX_LEVEL = 99
# NEGATIVE_ONE = -1
# ZERO = 0
# SEQUENCE_DEFAULT = ZERO

# class Page(models.Model):
#     title = models.CharField(max_length=255, default="Page Title")
#     dt_create = models.DateTimeField(auto_now_add=True)
#     def get_content():
#         # query the child table
#         return None
#     def get_heading():
#         # query the child table
#         return None
#     def get_paragraph():
#         # query the child table
#         return None

# class Paragraph(models.Model):
#     page = models.ForeignKey(Page, on_delete=models.CASCADE)
#     int_index = models.IntegerField(default=MAX_INDEX_LEVEL)
#     int_sequence = models.IntegerField(default=SEQUENCE_DEFAULT)
#     content = models.TextField()




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

page = Page()
int_sequence = 0;

tag_outers = soup.find_all("div", class_="outerband")
for tag_outer in tag_outers:
    tag_inners = tag_outer.find_all("div", class_="innerband")
    for tag_inner in tag_inners:
        gather_links(tag_inner.find_all('a'))
        tag_content = tag_inner.findChildren(recursive=False);
        try:
            paragraph = Paragraph()
            paragraph.int_sequence = int_sequence
            paragraph.content = tag_content.contents
        except:
            print(Exception)
print(tag_content)



# print(f'\n\n{page}')
