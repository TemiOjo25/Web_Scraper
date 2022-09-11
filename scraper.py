import bs4
import requests
import time



def find_books():
    basic_url = 'https://books.toscrape.com/catalogue/page-{}.html'
    four_five_rating = []
    for p in range(1, 11):
        result = requests.get(basic_url.format(p))

        soup = bs4.BeautifulSoup(result.text, 'html.parser')
        books = soup.select('.product_pod')

        for book in books:

            if book.select('.star-rating.Four'):
                title = book.select('a')[1]['title']
                price = book.select('p')[1].getText()
                res = title + f'--------\tSTAR-RATING: ' + '* ' * 4 + f'------- PRICE: {price}'
                four_five_rating.append(res)

            if book.select('.star-rating.Five'):
                title = book.select('a')[1]['title']
                price = book.select('p')[1].getText()
                res = title + f'--------\tSTAR-RATING: ' + '* ' * 5 + f'------- PRICE: {price}'
                four_five_rating.append(res)

    for i in four_five_rating:
        print(i)


if __name__ == '__main__':
    while True:
        find_books()
        time_wait = 5
        time.sleep(time_wait * 1)


