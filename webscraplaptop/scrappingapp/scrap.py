from bs4 import BeautifulSoup
import requests

#amazon_url='https://pricee.com/?q=laptop'
amazon_url="https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&marketplace=FLIPKART&page="

#for i in range(1,20):

def scrappeddata():
    output=[]
    for i in range(1,20):
        amazon_page=requests.get(amazon_url+str(i))
        amazon_soup=BeautifulSoup(amazon_page.content,'html.parser')
        all_data=amazon_soup.find_all("div",class_="_1AtVbE col-12-12")
        
        amazon_dict={}
        for each in all_data:
            price=each.find("div",class_="_30jeq3 _1_WHN1")
            title=(each.find("div",class_="_4rR01T"))
            target_link=(each.find("a",class_="_1fQZEK"))
            if title is not None:
                amazon_dict['title']=title.text
                amazon_dict["target_link"]=target_link['href']
                amazon_dict["price"]=price.string
        output.append(amazon_dict)
    print(len(output)) 
    return output
