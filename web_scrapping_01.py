import requests
from bs4 import BeautifulSoup
import textwrap

file_web = open('contoh2_web.html', mode='r')
hal_web = file_web.read()
file_web.close()

# Membuat soup
soup = BeautifulSoup(hal_web, 'lxml')

tag_judul = soup.find('h1', id='main_title')
judul_web = tag_judul.getText()

tag_paragraf = soup.find_all('p', class_ ='opening')

# Cara 1 --> Menampilkan Hasil Paragraf
#for paragraf in tag_paragraf:
#    print(textwrap.fill(paragraf.text, width=125))  # Bungkus teks, maksimal 125 karakter per baris
#    print()  # Tambahkan baris kosong untuk memisahkan paragraf

# Cara 2 --> Menampilkan Hasil
paragraf1 = tag_paragraf[0].getText()
paragraf2 = tag_paragraf[1].getText()

file = open('hasil_scrapping_01.txt', mode='w')
file.write('JUDUL: \n')
file.write(judul_web+'\n')
file.write('ISI PARAGRAF: \n')
file.write(paragraf1+'\n')
file.write(paragraf2)

