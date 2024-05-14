import requests
from bs4 import BeautifulSoup

#fetching data from a website -- coding temple website
#create response object

response = requests.get("https://www.codingtemple.com/")

#check the status of my response (status_code attribuite)
print(response.status_code)

# print(response.content) <-- printing the entire response to show all the content
#of the webpage we submitted a request for

#using beautiful soup to parse html

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify()) <--- Formats the html in a 'slightly' more readable form

#using soup to grab specific html elements

print(soup.title.text)

print(soup.a)

print(soup.h1.text)