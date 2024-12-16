import requests
from bs4 import BeautifulSoup

# URL utama untuk hasil pencarian Superman
base_url = "https://subslikescript.com"
search_url = "https://subslikescript.com/search?q=superman"


# Fungsi untuk mendapatkan daftar link film dari halaman pencarian
def get_movie_links(search_url):
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "lxml")

    # Mencari semua link film dari halaman pencarian
    movie_links = []
    for link in soup.select("div[class='search-results'] a"):
        url = base_url + link["href"]  # Menggabungkan base_url dengan href
        movie_links.append(url)

    return movie_links


# Fungsi untuk mengambil naskah film dari link film tertentu
def get_movie_script(movie_url):
    response = requests.get(movie_url)
    soup = BeautifulSoup(response.text, "lxml")

    # Mencari judul film dan naskah
    title = soup.find("h1").get_text(strip=True)
    script = soup.find("div", class_="full-script").get_text(separator="\n", strip=True)

    return {"title": title, "script": script}


# Main program
if __name__ == "__main__":
    print("Fetching Superman movie scripts...\n")

    # Ambil semua link film dari halaman hasil pencarian
    movie_links = get_movie_links(search_url)
    print(f"Total movies found: {len(movie_links)}\n")

    # Loop untuk mengambil naskah dari setiap film
    for i, movie_url in enumerate(movie_links[:10]):  # Batasi hanya 10 film pertama
        try:
            movie_data = get_movie_script(movie_url)
            print(f"Movie {i + 1}: {movie_data['title']}")

            # Simpan naskah ke file
            file_name = movie_data['title'].replace(" ", "_").replace("/", "_") + ".txt"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(movie_data['script'])

            print(f"Script saved to: {file_name}\n")
        except Exception as e:
            print(f"Failed to fetch script for {movie_url}: {e}\n")

    print("All scripts have been fetched!")
