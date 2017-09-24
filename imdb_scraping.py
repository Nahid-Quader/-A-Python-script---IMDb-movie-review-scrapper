

# This script is a imdb review scraper. It will scrap all reviews from imdb website for the given movie



import urllib2
from bs4 import BeautifulSoup
from imdb import IMDb
ia = IMDb()
movie = raw_input("Enter a movie name : ")
search = ia.search_movie(movie)
print search[0].summary()
movieID = search[0].movieID
root_address="http://www.imdb.com/title/tt"+str(movieID)+"/"
p = urllib2.urlopen(root_address+"reviews?")
soup1 = BeautifulSoup(p, 'html.parser')
pnumber = soup1.find_all('font', attrs={'face': 'Arial, Helvetica, sans-serif'})
string= pnumber[0].get_text()
string=string.split()
index= len(string)-1
string=string[index]
max_pagno=string.replace(":","")
max_pagno=int(max_pagno)
count =0
pageno=0
page=urllib2.urlopen(root_address)
soup = BeautifulSoup(page,'html.parser')
content= soup.find_all('div',attrs={'id' : 'tn15content'})
num = 1
flag = False
for i in range(max_pagno):
        count += 1
        print "\n\nPage NO :", count, "\n\n"
        pageextra = "reviews?start=" + str(pageno)
        pageno=int(pageno)+10
        address = root_address + pageextra
        page = urllib2.urlopen(address)
        soup = BeautifulSoup(page, 'html.parser')
        content = soup.find_all('div', attrs={'id': 'tn15content'})
        for i in range(len(content)):
                review = content[i].find_all('p',attrs={'class': ''})
                for i in range(len(review)):

                    for tag in review[i]:
                        if tag.name == "b" or tag.name == "a":
                            pass
                        else:
                            print "Review ", num, " :",
                            num += 1
                            print review[i].get_text(), "\n"
                            break
