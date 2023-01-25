import requests
from bs4 import BeautifulSoup
import pandas as pd


gst_mapping = pd.read_csv("gst_mapping.csv")
def extract_product_info(url):
   
    response = requests.get(url)
   
    soup = BeautifulSoup(response.content, "html.parser")
   
    product_info = {
        "name": soup.find("span", {"class": "product-name"}).text,
        "category": soup.find("span", {"class": "product-category"}).text,
        "details": soup.find("span", {"class": "product-details"}).text,
        "price": soup.find("span", {"class": "product-price"}).text,
    }
   
    product_info["gst_rate"] = gst_mapping.loc[gst_mapping["category"] == product_info["category"], "gst_rate"].values[0]
    return product_info


product1 = extract_product_info("http://www.website1.com/product1")
print(product1)

product2 = extract_product_info("http://www.website2.com/product2")
print(product2)


products = pd.DataFrame([product1, product2])

products["price"] = products["price"].str.extract(r"(\d+)").astype(
average_gst_rate_by_category = products.groupby("category")["gst_rate"].mean()
print(average_gst_rate_by_category)
