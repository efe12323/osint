import requests
from bs4 import BeautifulSoup

def arama_sonuclari(aranan_isim):
    # Google'da arama yapmak için URL oluşturma
    url = f"https://www.google.com/search?q={aranan_isim}"
    
    # Google'a istek gönderme
    response = requests.get(url)
    
    # Eğer istek başarılı ise, sayfanın içeriğini çekme
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Google arama sonuçlarını çekme
        linkler = soup.find_all('a')
        
        # Her bir link için işlem yapma
        for link in linkler:
            href = link.get('href')
            if href.startswith('/url?q='):
                # URL'yi çıkarma
                url = href.split('/url?q=')[1].split('&')[0]
                print(url)

# Kullanıcıdan isim ve soyad isteme
isim = input("Lütfen aranacak kişinin ismini ve soyadını girin: ")

# Arama sonuçlarını alma
arama_sonuclari(isim)
