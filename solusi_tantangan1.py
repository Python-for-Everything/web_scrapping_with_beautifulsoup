from bs4 import BeautifulSoup

file_web = open('contoh2_web.html', mode='r')
hal_web = file_web.read()
file_web.close()

# Membuat soup
soup = BeautifulSoup(hal_web, 'lxml')

# Scrapping paragraf terakhir
tag_paragraf = soup.find_all('p')
tag_p_target = tag_paragraf[-1]
print(tag_p_target.getText())