from bs4 import BeautifulSoup
import requests
import shutil

html_page = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(html_page.content, 'html.parser')
warning = soup.find('div', class_="alert alert-warning")
book_container = warning.nextSibling.nextSibling

print(book_container)

images = book_container.findAll('img')
example = images[0]
example
print(example)
example.attrs['src']

url_base = "http://books.toscrape.com/"
url_ext = example.attrs['src']
full_url = url_base + url_ext
r = requests.get(full_url, stream=True)
if r.status_code == 200:
   with open("images/book1.jpg", 'wb') as f: 
      r.raw.decode_content = True
      shutil.copyfileobj(r.raw, f)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import pandas as pd
from IPython.display import Image, HTML
row_1 = [example.attrs['alt'], '<img src="images/book1.jpg"/>']
df = pd.DataFrame(row_1).transpose()
df.columns = ['Title', 'Cover']
HTML(df.to_html(escape=False))
df

img = mpimg.imread('images/book1.jpg')
imgplot = plt.imshow(img)
plt.show()

