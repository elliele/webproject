from bs4 import BeautifulSoup
import requests

#61. Beautiful Soup
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

search = input("Enter search term: ")
params = {"q": search}
r = requests.get("http://www.bing.com/search", headers=headers, params=params)

soup = BeautifulSoup(r.text, "html.parser")

#print(soup.prettify())

#62. Parsing our soup

#get a list w/ an ID of the results
#soup.find("element we're looking for", {dictionary object of any attrbiute})
results = soup.find("ol", {"id": "b_results"})  # finding the 'ol's from the html which has a 'id': b_results
links = results.findAll("li", {"class": "b_algo"})

item_text = None
item_href = None

for item in links:
    item_text = item.find("a").text  # extracting text from all the links in the list
    item_href = item.find("a").attrs["href"]  # extracting links, .attrs specifies special attributes
    item_summary = item.find("a").parent.parent.find("p").text  # parent content in the html of the selected item

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print(item_summary)

        children = item.find("h2")
        print("Next Sibling of the h2", children.next_sibling)