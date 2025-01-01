#Web scraping is the process of extracting data from websites. It involves fetching a webpage and extracting specific information, which can be stored in a structured format, such as a spreadsheet or database.
#Think of web scraping like a digital scavenger hunt. It’s the process of going through websites to gather specific information that you’re interested in.
#For example, if you wanted to track the prices of a product across different e-commerce sites, you could use web scraping to automatically pull that data and put it into a spreadsheet.
#Following code that I've written takes data like title,price,availability of books,ratiings from a website and stores it in a txt file.
import requests
from bs4 import BeautifulSoup
books = ''
for i in range (50):
    res = requests.get(f'https://books.toscrape.com/catalogue/page-{i+1}.html')

    if res.status_code != 200:
        print('error occured')
        break
    else:
        htlm_content = res.content
        soup = BeautifulSoup(htlm_content,'html.parser')
        data = soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
        
        for item in data:
            title = item.find('h3').find('a').get('title')
            price = item.find('div',class_='product_price').find('p',class_='price_color').text
            in_stock = item.find('div',class_='product_price').find('p',class_='instock availability').text.strip()
            rating = item.find('p').get('class')[1]
            books = (f'{books}\nTitle : {title}\nPrice : {price}\nAvailable: {in_stock}\nRating : {rating}\n{'*'*25}')
with open('books.txt','w') as book_record:
    book_record.write(books)
                

