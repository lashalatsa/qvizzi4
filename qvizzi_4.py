# import requests
# from bs4 import BeautifulSoup
# from time import sleep
# import csv
#
# file = open('hotels.csv','w', newline='\n')
# file_obj = csv.writer(file)
# file_obj.writerow(['name','price'])
#
# url_params = {'Attrs':'hotel_category','hotel_cat':9,'page':1}
# url = 'https://turebi.ge/ka/hotels?Attrs=&hotel_category=&hotel_cat=9&Keyword=&Page=1'
# while url_params['page'] <=10:
#     r = requests.get(url)
#     content = r.text
#     soup = BeautifulSoup(content, 'html.parser')
#     hotels_block = soup.find('div',{'class':'row search-result hotels-search'})
#     all_hotels = hotels_block.find_all('div',{'class':'col-lg-12 col-md-12 col-sm-12 col-xs-12 mg-tp-20 padding-0'})
#     # print(hotels_block)
#     # print(all_hotels)
#     for each in all_hotels:
#         price1 = each.find('div',{'class':'price'})
#         price = price1.span.text
#         # print(price)
#         name_bar = each.find('div', {'class': 'hotel-title-1 pos-rel'})
#         name = name_bar.a.text
#         # print(name)
#         about = each.p
#         file_obj.writerow([price,name,about])
#     url_params['page']+=1
#     sleep(15)
