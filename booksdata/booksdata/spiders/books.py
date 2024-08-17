from pymongo import MongoClient
from pathlib import Path
import scrapy
import datetime




client = MongoClient("mongodb+srv://awaz:9813510096%40Nj@awaz.8back.mongodb.net/")
db = client.scrappy
def insertIntoDB(page,title,image,rating,price,stock):
    collection=db[page]
    doc =  {
    "Title": title,
    "image": image,
    "Rating": rating,
    "price":price,
    "stock":stock,
    "date": datetime.datetime.now(tz=datetime.timezone.utc),}

    inserted=collection.insert_one(doc)
    return(inserted.inserted_id)



class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com"]

    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)






    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        #Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        bookdetail = {}

        cards=response.css(".product_pod")
        for card in cards:
            title=card.css(".image_container img")
            title=title.attrib["alt"]
            #print(title)
            
            image=card.css(".image_container img")
            image=image.attrib["src"].replace("../../../../media","https://books.toscrape.com/media")
            #print(image)

            rating=card.css(".star-rating").attrib["class"].split(" ")[1]
            #print(rating)

            price=card.css(".price_color::text").get()
            #print(price)


            if (card.css(".icon-ok").get())==None:
                stock=False
            else:
                stock=True
            #print(stock)

            insertIntoDB(page,title,image,rating,price,stock)