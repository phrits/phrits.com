from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re
import urllib.request

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)

url = 'https://phrits.com/content/parts/part_fat_tom.php'
browser.visit(url)
html = browser.html
soup_contents = soup(html, 'html.parser')
elem=soup_contents.select_one('h1')
title=elem.text

# def place_paragraph(page,
#     heading_counter = 0,
#     # content_counter = 0,
#     text = "",
#     heading = ""):
#     if (heading == "h1"):
# #        page["title"] = text
#         print("h1")
#     elif (heading == "h2"):
#         print("h2")
#         # page["content"][heading_counter] = text
#         # heading_counter += 1
#     else:
#         print(f'other: {heading}')
# #        page["content"][heading_counter]["paragraphs"].append(text)
#     return page

page = {
    "title": "",
    "content": [
        {"heading": "",
        "paragraphs": []}
    ]
}
counter_h1 = 0;
counter_h2 = 0;
counter_h3 = 0;
counter_h4 = 0;
counter_h5 = 0;
counter_h6 = 0;
counter = 0
for i in soup_contents.find_all():
    counter += 1
    print(f'{counter}: {i.name}')
    if (i.name=="p"):
        print(f'p: ')
    elif (i.name =="h2"):
        print(f'h2: {i.text}')
    elif (i.name =="h1"):
        print(f'h1: {i.text}')
    elif (i.name == "div"): # and ((i.class_ == "insetRight") or (i.class_ == "insetLeft"))):
        print(f'div: {i.class_}')


# counter=0;
# for i in soup_contents.find_all():
#     if (i.name == "h1"):
#         page['title'] = i.text
# #    elif (i.name == "h2"):
#     elif (i.text in ("Food", "Acidity", "Time", "Temperature", "Oxygen", "Moisture")):
#         page["content"][counter]["heading"] = i.text
#         counter+=1
#     #     print(page["content"][counter]["heading"])
#     #     counter+=1
#     # elif (i.name == "p"):
#     #      print(f'..{counter}..')

# print(page)
# stuff=pd.read_json('foo.json')
# print(stuff)

