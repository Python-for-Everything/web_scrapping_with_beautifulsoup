from bs4 import BeautifulSoup

# Sample HTML Data (dapat diganti jika HTML disimpan dalam file)
html_data = """
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>City</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>John Doe</td><td>30</td><td>New York</td></tr>
        <tr><td>Jane Smith</td><td>25</td><td>Los Angeles</td></tr>
        <tr><td>Mike Johnson</td><td>40</td><td>Chicago</td></tr>
        <tr><td>Emily Davis</td><td>22</td><td>Houston</td></tr>
        <tr><td>David Wilson</td><td>35</td><td>Phoenix</td></tr>
        <tr><td>Laura Brown</td><td>28</td><td>Philadelphia</td></tr>
        <tr><td>Chris White</td><td>32</td><td>San Antonio</td></tr>
        <tr><td>Anna Martin</td><td>27</td><td>San Diego</td></tr>
        <tr><td>James Lee</td><td>45</td><td>Dallas</td></tr>
        <tr><td>Linda Taylor</td><td>38</td><td>San Jose</td></tr>
        <tr><td>Robert Clark</td><td>50</td><td>Austin</td></tr>
        <tr><td>Mary Harris</td><td>29</td><td>Jacksonville</td></tr>
        <tr><td>Michael Lewis</td><td>34</td><td>Fort Worth</td></tr>
        <tr><td>Sarah Robinson</td><td>31</td><td>Columbus</td></tr>
        <tr><td>William Walker</td><td>43</td><td>Charlotte</td></tr>
        <tr><td>Patricia Young</td><td>26</td><td>San Francisco</td></tr>
        <tr><td>Daniel Hall</td><td>37</td><td>Indianapolis</td></tr>
        <tr><td>Barbara Allen</td><td>41</td><td>Seattle</td></tr>
        <tr><td>Paul King</td><td>39</td><td>Denver</td></tr>
        <tr><td>Lisa Wright</td><td>33</td><td>Washington</td></tr>
    </tbody>
</table>
"""

# Parse HTML menggunakan BeautifulSoup dan metode lxml
soup = BeautifulSoup(html_data, "lxml")

# Temukan semua baris data dalam tabel
table = soup.find("table")
rows = table.find_all("tr")[1:]  # Lewati header

# List untuk menyimpan hasil scraping
data = []

# Loop untuk mengambil Nama, Age, dan City
for row in rows:
    cols = row.find_all("td")
    name = cols[0].text.strip()
    age = cols[1].text.strip()
    city = cols[2].text.strip()
    data.append({"Name": name, "Age": age, "City": city})

# Menampilkan hasil scraping
print(f"{'Name':<20} {'Age':<5} {'City'}")
print("-" * 40)
for item in data:
    print(f"{item['Name']:<20} {item['Age']:<5} {item['City']}")
