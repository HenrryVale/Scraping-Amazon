
from bs4 import BeautifulSoup
import requests


def main(URL):
    #print("Ejecutando primera validación de productos")
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    })

    webpage = requests.get(URL, headers=HEADERS)

    soup = BeautifulSoup(webpage.content, "lxml")

    products = soup.find_all('div', {"class": "a-section a-spacing-base"})

    save_products = []
    for product in products:
        img_tag = product.find('img', {"class": "s-image"})
        img_url = img_tag['src'] if img_tag else 'URL no encontrada'

        desc_tag = product.find(
            'span', {"class": 'a-size-base-plus a-color-base a-text-normal'})
        description = desc_tag.get_text(
            strip=True) if desc_tag else 'Descripción no encontrada'

        price_symbol_tag = product.find('span', {"class": 'a-price-symbol'})
        price_symbol = price_symbol_tag.get_text(
            strip=True) if price_symbol_tag else ''

        price_tag = product.find('span', {"class": 'a-price-whole'})
        price = price_tag.get_text(strip=True) if price_tag else '0'

        price_fraction_tag = product.find(
            'span', {"class": 'a-price-fraction'})
        price_fraction = price_fraction_tag.get_text(
            strip=True) if price_fraction_tag else '0'

        starts_tag = product.find('span', {"class": "a-icon-alt"})
        starts = starts_tag.get_text(strip=True) if starts_tag else ''

        valoration_tag = product.find(
            'span', {"class": "a-size-base s-underline-text"})
        valoration = valoration_tag.get_text(
            strip=True) if valoration_tag else ''

        product_ok_tag = product.find('span', {"class": 'a-price-symbol'})
        product_ok = True if product_ok_tag else False

        full_price = f"{price}{price_fraction}" if price and price_fraction else "0"

        save_products.append({
            "img_url": img_url,
            "description": description,
            "price_symbol": price_symbol,
            "price": price,
            "price_fraction": price_fraction,
            "full_price": full_price,
            "starts": starts,
            "valoration": valoration,
            "product_ok": product_ok
        })
    save_products = [p for p in products if p.get("product_ok") ]
    return save_products

def mainV2(URL):
    #print("Ejecutando segunda validación de productos")
    HEADERS = ({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    })

    webpage = requests.get(URL, headers=HEADERS)

    soup = BeautifulSoup(webpage.content, "lxml")

    products = soup.find_all('div', {"class": "sg-col-inner"})

    save_products = []
    for product in products:
        img_tag = product.find('img', {"class": "s-image"})
        img_url = img_tag['src'] if img_tag else 'URL no encontrada'

        desc_tag = product.find(
            'span', {"class": 'a-size-medium a-color-base a-text-normal'})
        description = desc_tag.get_text(
            strip=True) if desc_tag else 'Descripción no encontrada'

        price_symbol_tag = product.find('span', {"class": 'a-price-symbol'})
        price_symbol = price_symbol_tag.get_text(
            strip=True) if price_symbol_tag else ''

        price_tag = product.find('span', {"class": 'a-price-whole'})
        price = price_tag.get_text(strip=True) if price_tag else '0'

        price_fraction_tag = product.find(
            'span', {"class": 'a-price-fraction'})
        price_fraction = price_fraction_tag.get_text(
            strip=True) if price_fraction_tag else '0'

        starts_tag = product.find('span', {"class": "a-icon-alt"})
        starts = starts_tag.get_text(strip=True) if starts_tag else ''

        valoration_tag = product.find(
            'span', {"class": "a-size-base s-underline-text"})
        valoration = valoration_tag.get_text(
            strip=True) if valoration_tag else ''

        product_ok_tag = product.find('img', {"class": "s-image"})
        product_ok = True if product_ok_tag else False

        product_avaliable_tag = product.select_one('div[data-cy="secondary-offer-recipe"] > div.a-row.a-size-base.a-color-secondary > span.a-size-base.a-color-secondary')
        product_avaliable = product_avaliable_tag.get_text(strip=True) if product_avaliable_tag else ''

        product_avaliable_ok = False if product_avaliable =="No featured offers available" or price=="0"  else product_ok


        full_price = f"{price}{price_fraction}" if price and price_fraction else "0"

        save_products.append({
            "img_url": img_url,
            "description": description,
            "price_symbol": price_symbol,
            "price": price,
            "price_fraction": price_fraction,
            "full_price": full_price,
            "starts": starts,
            "valoration": valoration,
            "product_ok": product_avaliable_ok
        })
    save_products = [p for p in save_products if p.get("product_ok") == True]
    return save_products
