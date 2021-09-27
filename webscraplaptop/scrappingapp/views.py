from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def itemsearch(request):
    
    flipkart_url="https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&marketplace=FLIPKART&sort=price_asc&page="
    output=[]
    for i in range(1,33):
        flipkart_page=requests.get(flipkart_url+str(i))
        flipkart_soup=BeautifulSoup(flipkart_page.content,'html.parser')
        all_data=flipkart_soup.find_all("div",class_="_1AtVbE col-12-12")
        
        for each in all_data:
            flipkart_dict={}
            price=each.find("div",class_="_30jeq3 _1_WHN1")
            title=(each.find("div",class_="_4rR01T"))
            target_link=(each.find("a",class_="_1fQZEK"))
            if title is not None:
                flipkart_dict['title']=title.text
                flipkart_dict["target_link"]=target_link['href']
                flipkart_dict["price"]=price.string
                flipkart_dict["store"]="Flipkart"
                output.append(flipkart_dict)
            
    return render(request,'index.html',{"data":output})