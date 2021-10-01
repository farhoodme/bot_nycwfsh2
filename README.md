BOT_NYCWFSH2 project, a NY Times Crossword Puzzle scrapper.

## Project Description

This project contains just a scrapper.py file that scrape Across and Down clues from [NY Times Crossword Puzzle](https://www.nytimes.com/crosswords/game/mini), convert the clue items to json format and save as json.


## Prerequisites Python Packages

This project needs Python 3 to run. Before run the application install these packages:

- beautifulsoup4 (https://www.crummy.com/software/BeautifulSoup)
- selenium (https://selenium-python.readthedocs.io)
- re (https://docs.python.org/3/library/re.html)
- urllib (https://docs.python.org/3/library/urllib.html)

You can use this command for install requirements packages:

```bash
pip install -r requirements.txt
```


## Error Handling and Logging

For handling exceptions I use [`selenium.common.exceptions`](https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html), and for logging I use Python logging module, that write logs (with exceptions details) to the `app.log` file.



