import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/movie/Batman_Returns-103776'
html = requests.get(website)
text_html = (html.text)

# membuat soup
soup = BeautifulSoup(text_html, 'lxml')

# Judul film
box_article = soup.find('article', class_ = 'main-article')
tag_h1 = box_article.find('h1')
judul = tag_h1.getText()

# Naskah film
tag_div = box_article.find('div', class_ = 'full-script')
full_transcript = tag_div.getText(strip=True, separator='\n')

# Menyimpan ke dalam text
file = open('batman-1992.txt', mode='w')
file.write(judul + '\n\n')
file.write(full_transcript)
file.close()



