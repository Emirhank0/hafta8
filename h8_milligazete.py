import requests
from bs4 import BeautifulSoup

def icerik_cek(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    tarih = soup.find('span', class_='tarih').get_text(strip=True).split('-')[0].strip()

    baslik = soup.h1.get_text(strip=True)

    ilk_paragraf = ""
    tum_paragraflar = soup.find_all('p')

    for p in tum_paragraflar:
        text = p.get_text(' ', strip=True)
        if "AKP sıralarına kolonya şişesi" in text:
            ilk_paragraf = text
            break

    diger_icerik = ' '.join(
        [p.get_text(' ', strip=True) for p in tum_paragraflar if p.get_text(strip=True) != ilk_paragraf])

    return f"{tarih};{baslik};{ilk_paragraf} {diger_icerik}"


if __name__ == "__main__":
    veri = icerik_cek("https://www.milligazete.com.tr/haber/24248095/ali-mahir-basarir-kimdir")
    with open('content.txt', 'w', encoding='utf-8') as f:
        f.write(veri)
