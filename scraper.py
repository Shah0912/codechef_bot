from selenium import webdriver
import requests
import bs4
import os


contest_url = "https://www.codechef.com/LRNDSA01"
# System.setProperty("webdriver.chrome.driver","C:\\Users\\Aditya\\Downloads\\chromdriver")
browser = webdriver.Chrome("C:\\Users\\Aditya\\Downloads\\chromedriver")
# WebDriver driver = new ChromeDriver()
browser.get(contest_url)
# driver.get("https://www.google.com")
request = requests.get(contest_url)
soup = bs4.BeautifulSoup(request.text, "lxml")
anchors = soup.select('a[href*="LRNDSA01/problems"]');


for anchor in anchors:
    print(anchor)
    
