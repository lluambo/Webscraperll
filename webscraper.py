import datetime # datetime for the pretty date
import random # random for the response header
import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4


url = "https://pixelford.com/blog/" # url you want to scrape
random_number = random.randint(1, 9999999999)# random for the response header
response = requests.get(url, headers={"User-Agent": f"Random number: {random_number}"}) # TO make sure the response is not blocked
html = response.content
soup = BeautifulSoup(html, "html.parser") # html.parser as the soup has diffrent formats
a_tags =soup.find_all('a', class_="entry-title-link")
blogs = soup.find_all("article", class_="type-post")

blog_data = []

for blog in blogs:# looping through the articles and getting the title and time
    title = blog.find('a', class_="entry-title-link").get_text()# getting the title
    time = blog.find('time', class_="entry-time").get("datetime")# getting the time
    blog_datetime = datetime.datetime.fromisoformat(time)# converting the time to datetime
    pretty_date = blog_datetime.strftime("%I:%M %p, %a %b %d, %Y")# converting the time to pretty format
    html_link = blog.find('a', class_="entry-title-link").get("href")# getting the link
    blog_data.append({# appending the data into a dictionary incase you want to manipulate it later
        "title": title,
        "pretty_date": pretty_date,
        "html_link": html_link
    })
    print(f"{title} - {pretty_date} - {html_link}")# printing the data in a clean format
