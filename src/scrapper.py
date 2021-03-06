from datetime import date
import requests
from bs4 import BeautifulSoup
import re

# define settings 
DATE = date.today().strftime("%Y/%m/%d")
NUMBER_CLASS = re.compile('Clue-label.*')
TEXT_CLASS = re.compile('Clue-text.*')
LAYOUT_CLASS = re.compile('Layout-clueLists.*')
LISTS_CLASS = re.compile('ClueList-wrapper.*')
JSON_LIST = {}

# read content from url
URL = "https://www.nytimes.com/crosswords/game/mini/" + DATE
page = requests.get(URL)

# parse content using BeautifulSoup html parser
soup = BeautifulSoup(page.content, "html.parser")

try:
    # get Across and Down layout section
    layout_section = soup.find("section", class_=LAYOUT_CLASS)

    try:
        # get each list from parsed section (first list is Across and second is Down)
        clue_lists = layout_section.find_all("div", class_=LISTS_CLASS)
        groups = []

        for clue_list in clue_lists:

            # get title of each list
            title_element = clue_list.find("h3")
            title_text = title_element.text.strip()

            # get all elements of each list
            clue_elements = clue_list.find_all("li")
            items = []
                
            for clue_element in clue_elements:
                # get number of clue
                number_element = clue_element.find("span", class_=NUMBER_CLASS)
                clue_number = number_element.text.strip()

                # get text of clue
                text_element = clue_element.find("span", class_=TEXT_CLASS)
                clue_text = text_element.text.strip()

                # create clue items
                items.append({"number": clue_number, "text": clue_text})
            
            # create groups with items and append to groups array
            groups.append({"group": title_text, "items": items})

        JSON_LIST['clues'] = groups

    except:
        print("clue_lists not found.")

except:
    print("layout_section not found.")

print(JSON_LIST)