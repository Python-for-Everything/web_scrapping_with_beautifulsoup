from bs4 import BeautifulSoup

file_web = open('contoh_tabel.html', mode='r')
hal_web = file_web.read()
file_web.close()

# Membuat soup
soup = BeautifulSoup(hal_web, 'lxml')

# Find the table
box_tabel = soup.find('table', id= 'sample-table')

# Judul kolom
tag_judul = box_tabel.find_all('th')
judul_kolom = []
for item in tag_judul:
    judul_kolom.append(item.text)

# isi kolom
isi_tabel = []
box_tr = box_tabel.find_all('tr')

isi_kolom = []
for item in box_tr:
    box_td = item.find_all('td')
    for i in box_td:
        isi_kolom.append(i.getText())

kolom_name = isi_kolom[0::3]
kolom_age = isi_kolom[1::3]
kolom_city = isi_kolom[2::3]

tabel = {
    judul_kolom[0]: kolom_name,
    judul_kolom[1]: kolom_age,
    judul_kolom[2]: kolom_city
}

import pandas

pandas.DataFrame(tabel).to_csv('hasil_tabel.csv')