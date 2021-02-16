#!/usr/bin/env python
# coding: utf-8

# In[21]:


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)


# In[22]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# In[4]:


html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')
slide_elem.find("div", class_='content_title')


# In[5]:


news_title = slide_elem.find("div",class_='content_title').get_text()
news_title


# In[6]:


news_p = slide_elem.find("div",class_='article_teaser_body').get_text()
news_p


# In[7]:


url2 = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
browser.visit(url2)


# In[12]:


html2 = browser.html
jpl_soup = BeautifulSoup(html2, 'html.parser')
img_url = jpl_soup.find("img", class_='BaseImage').get("src")
img_url


# In[13]:


import pandas as pd


# In[14]:


url3 = 'https://space-facts.com/mars/'
tables = pd.read_html(url3)
tables


# In[15]:


df = tables[0]
df.head()


# In[17]:


html_df = df.to_html()
html_df


# In[31]:


url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url4)


# In[39]:




clicks = browser.find_by_css("a.product-item h3")
len(clicks)


# In[42]:


hemisphere_image_urls = []

for i in range(len(clicks)):
    link = {}
    browser.find_by_css("a.product-item h3")[i].click()
    link['title'] = browser.find_by_css('h2.title').text
    link['img'] = browser.find_by_text('Sample').first['href']
    hemisphere_image_urls.append(link)
    browser.back()
    
hemisphere_image_urls


# In[43]:


browser.quit()


# In[ ]:




