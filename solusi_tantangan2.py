from bs4 import BeautifulSoup

file_web = open('contoh2_web.html', mode='r')
hal_web = file_web.read()
file_web.close()

# Membuat soup
soup = BeautifulSoup(hal_web, 'lxml')

# Scraping judul utama (tag <h2> berwarna hijau tebal)
judul = soup.find('h2')  # Mencari tag <h2>
print("Judul Utama:", judul.get_text())  # Menampilkan teks dari tag <h2>

# Scraping langkah-langkah (list pada tag <ol> dan <li>)
tag_langkah = soup.find('ol')  # Mencari tag <ol> (ordered list)
langkah_list = tag_langkah.find_all('li')  # Mencari semua elemen <li> di dalam <ol>

# Menampilkan setiap langkah dalam list
print("\nLangkah-langkah:")
for idx, langkah in enumerate(langkah_list, start=1):  # Looping untuk menampilkan setiap <li>
    print(f"{idx}. {langkah.get_text()}")  # Menampilkan teks dari setiap elemen <li>