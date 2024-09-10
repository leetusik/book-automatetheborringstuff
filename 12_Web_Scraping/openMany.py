#! python3
# searchpypi.py  - Opens several search results.

import sys
import webbrowser

import bs4
import requests

print("Searching...")  # display text while downloading the search result page
res = requests.get("https://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
# Open a browser tab for each result.
linkElems = soup.find_all("a", class_="package-snippet")

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = "https://pypi.org" + linkElems[i].get("href")
    print("Opening", urlToOpen)
    webbrowser.open(urlToOpen)
