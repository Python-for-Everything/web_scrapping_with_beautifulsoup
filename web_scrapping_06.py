import requests
from bs4 import BeautifulSoup
import pandas

website = 'https://books.toscrape.com/'
html = requests.get(website)
text_html = (html.text)

# membuat soup
soup = BeautifulSoup(text_html, 'lxml')

# ambil judul buku
box_article = soup.find_all('article', class_ = 'product_pod')

judul_buku = []
for item in box_article:
    tag_h3 = item.find('h3')
    tag_a = tag_h3.find('a')
    judul_buku.append(tag_a['title'])

print(judul_buku)

# harga buku
tag_p = soup.find_all('p', class_ = 'price_color')
harga_buku = []
for item in tag_p:
    harga_buku.append(item.getText()[1:])

buku = {
    'JUDUL_BUKU' : judul_buku,
    'HARGA' : harga_buku
}
df_buku = pandas.DataFrame(buku)
print(df_buku)
