
# coding: utf-8

# In[3]:


import urllib.robotparser as rp


# In[4]:


parser = rp.RobotFileParser()


# In[5]:


#url = "https://www.tripadvisor.com/"


# In[10]:


#base_url = "https://www.tripadvisor.com/"
#robot_url = base_url + "/robots.txt"
#agent = "*"


# In[16]:


import requests
import re
import pandas

# In[22]:


def robot_checker(url, base, agent="*"):
    parser.set_url(base+"/robots.txt")
    parser.read()
    if parser.can_fetch(url, agent)==True:
        return requests.get(url)
    else:
        print("sorry, but you are not allowed to scrape this page.")


# In[23]:

class ls:
    def __init__(self, ls):
        self.ls = ls
    def strip_spaces(self):
        return [str(i).strip() for i in ls]
    def to_string(self):
        return " ".join(self.ls)
    def unlist(self):
        return list(chain.from_iterable(self.ls))     
    def select_numbers(self):
        return [float(i) for i in self.ls if i.isdigit()==True]
    def select_letters(self):
        return [str(i) for i in self.ls if i.isalpha()==True]

class parsers:
    def __init__(self, page):
        self.page = page
    def get_links(page):
        links =  self.page.find_all("a")
        return [i.get("href") for i in links] 
    def get_heading(self):
        headings =  self.page.find_all(re.compile("h[1-6]{1}"))
        return [i.get_text() for i in headings]
    def get_tables(self):
        tables =  self.page.find_all("table") 
        return pd.read_html(self.page)

