#Image scraper

from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import requests
import os

#make it loopable

def StartSearch():

    search = input("Search for: ")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name
                    )
    r = requests.get("http://www.bing.com/search",  params=params)

    #turn request into Beautiful Soup
    soup = BeautifulSoup(r.text, "html.parser")

    #extracting image from "a" element and class = thumb
    links = soup.findAll("a", {"class": "thumb"})

    for item in links: #create new request for each item url
        try:
            img_obj = requests.get(item.attrs["href"]) # extracting links, .attrs specifies special attributes
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save = ("./scraped_images/" + title, img.format)
            except:
                print("Could not save image.")
        except:
            print("Could not request Image")



    StartSearch()

StartSearch()
