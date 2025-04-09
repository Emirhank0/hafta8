import requests
from bs4 import BeautifulSoup


def icerik_cek(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    tarih = soup.find('span', class_='tarih').get_text(strip=True).split('-')[0].strip()

    baslik = soup.h1.get_text(strip=True)

    icerik = []
    main_text = soup.find('div', {'id': 'main-text'})

    if main_text:
        first_paragraph = main_text.find('p')
        if first_paragraph:
            icerik.append(first_paragraph.get_text(strip=True))

        paragraphs = main_text.find_all('p')[1:]
        for p in paragraphs:
            text = p.get_text(' ', strip=True)
            if text and text not in icerik:
                icerik.append(text)

    haber = ' '.join(icerik)

    return f"{tarih};{baslik};{haber}"


if __name__ == "__main__":
    veri = icerik_cek("https://www.milligazete.com.tr/haber/24248095/ali-mahir-basarir-kimdir")
    with open('content.txt', 'w', encoding='utf-8') as f:
        f.write(veri)
