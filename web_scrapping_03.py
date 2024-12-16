from bs4 import BeautifulSoup
import pandas

file_web = open('contoh2_web.html', mode='r')
hal_web = file_web.read()
file_web.close()

# Membuat soup
soup = BeautifulSoup(hal_web, 'lxml')

# mengambil table
box_table = soup.find('table')
#print(box_table.prettify())

# Mengambil judul kolom
tag_judul_kolom = box_table.find_all('th')
judul_kolom = []
for item in tag_judul_kolom:
    judul_kolom.append(item.getText())

# Mengambil isi kolom
tag_isi_kolom = box_table.find_all('td')
isi_kolom = []
for item in tag_isi_kolom:
    isi_kolom.append(item.getText())

# Slicing isi kolom
#print(isi_kolom)
bahasa_pemrograman = (isi_kolom[0::3])
lama_pembelajaran = (isi_kolom[1::3])
harga = isi_kolom[2::3]

# print(bahasa_pemrograman)
# print(lama_pembelajaran)
# print(harga)

informasi_kursus = {
    judul_kolom[0] : bahasa_pemrograman,
    judul_kolom[1] : lama_pembelajaran,
    judul_kolom[2] : harga
}

df_informasi_kursus = pandas.DataFrame(informasi_kursus)
df_informasi_kursus.to_csv('hasil_scrapping_03.csv')




