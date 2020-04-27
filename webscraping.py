'''Viejo, no entiendo una goma'''
import bs4
import requests

response = requests.get("https://www.dustloop.com/wiki/index.php?title=GBVS/Gran/Frame_Data")

if response is not None:
    html = bs4.BeautifulSoup(response.text, 'html.parser')

    title = html.select("#Health")[0].text
    paragraphs = html.select("tr")
    for para in paragraphs:
        print (para.text)

    # just grab the text up to contents as stated in question
    intro = '\n'.join([ para.text for para in paragraphs[0:5]])
    print (intro)

# class wikitable
