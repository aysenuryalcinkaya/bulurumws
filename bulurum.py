import requests
from bs4 import BeautifulSoup
import ssl
import certifi

# Specify the URL
url = "https://www.bulurum.com/dir/avukatlar"

# Create a session with SSL verification using certifi package
session = requests.Session()
session.verify = certifi.where()

# Send an HTTP GET request using the session
response = session.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.content

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find avukat-listesi div elements
    avukat_listesi = soup.find_all("div", class_="avukat-listesi")

    for avukat in avukat_listesi:
        avukat_ad = avukat.find("h2").text
        avukat_iletisim = avukat.find("p", class_="iletisim").text

        # Print avukat information
        print("Avukat Adı:", avukat_ad)
        print("İletişim Bilgileri:", avukat_iletisim)
        print("-" * 30)
else:
    print("Request was not successful. Status code:", response.status_code)
