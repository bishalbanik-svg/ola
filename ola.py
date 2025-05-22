import requests
from bs4 import BeautifulSoup

url = "https://www.olx.in/items/q-car-cover"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    with open("car_cover_results.txt", "w", encoding="utf-8") as f:
        for listing in soup.find_all("a", href=True):
            title = listing.get_text(strip=True)
            link = listing["href"]
            if title and "/item/" in link:
                f.write(f"{title}\nhttps://www.olx.in{link}\n\n")
    print("Results saved to car_cover_results.txt")
else:
    print("Failed to fetch page:", response.status_code)
