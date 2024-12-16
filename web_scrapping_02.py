from bs4 import BeautifulSoup

file_web = open('contoh2_web.html', mode='r')
hal_web = file_web.read()
file_web.close()

# Membuat soup
soup = BeautifulSoup(hal_web, 'lxml')

# Melakukan scrapping daftar kursus
box_ul = soup.find('ul', class_ = 'daftar_kursus')
kursus = box_ul.find_all('li')
daftar_kursus = []
for item in kursus:
    x = item.getText()
    daftar_kursus.append(x)

# Melakukan scrapping langkah belajar
box_ol = soup.find('ol', class_ = 'langkah_belajar')
langkah = box_ol.find_all('li')
langkah_belajar = []
for item in langkah:
    langkah_belajar.append(item.getText())

file = open('hasil_scrapping_02.txt', mode='w')
file.write('DAFTAR KURSUS YANG DITAWARKAN: \n')
for item in daftar_kursus:
    file.write(item+'\n')
file.write('LANGKAH BELAJAR: \n')
for num, item in enumerate(langkah_belajar, start=1):
    file.write(str(num)+'. '+item+'\n')
file.close()


