import requests
from bs4 import BeautifulSoup
import csv

def extract_product_info(product):
    name = product.find('h3').find('a')['title']
    price = product.find('p', class_='price_color').text
    rating = product.find('p', class_='star-rating')['class'][1]
    return name, price, rating

def scrape_books_to_scrape():
    url = 'http://books.toscrape.com/catalogue/page-1.html'
    products = []
    
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        book_list = soup.find_all('article', class_='product_pod')

        for book in book_list:
            name, price, rating = extract_product_info(book)
            products.append((name, price, rating))

        next_button = soup.find('li', class_='next')
        if next_button:
            next_url = next_button.find('a')['href']
            url = 'http://books.toscrape.com/catalogue/' + next_url
        else:
            break

    return products

def save_to_csv(products, filename='products.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Rating'])
        writer.writerows(products)

def main():
    products = scrape_books_to_scrape()
    save_to_csv(products)
    print(f"Scraped data has been saved to 'products.csv'")

if __name__ == "__main__":
    main()
