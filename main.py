import requests
from bs4 import BeautifulSoup


def link_olusturucu(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')

    if soup.find("h1"):
        baslik = soup.find("h1").get_text(strip=True)
    else:
        baslik = "Başlık bulunamadı"

    tarih = ""
    for tag in soup.find_all(["div", "span"]):
        text = tag.get_text(strip=True)
        if "Mar" in text and "-" in text:
            tarih = text
            break

    haber = ""
    haber_div = soup.find("div", {"class": "haber-detay"})
    if haber_div:
        haber = haber_div.get_text(" ", strip=True)

    formatted = f"{tarih};{baslik};{haber}"

    print(formatted)

    with open("icerik.txt", "w", encoding="utf-8") as file:
        file.write(formatted)


link = "https://www.milligazete.com.tr/haber/24248095/ali-mahir-basarir-kimdir"
link_olusturucu(link)
