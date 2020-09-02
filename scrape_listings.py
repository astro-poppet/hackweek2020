from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

path_to_chromedriver = '/home/louise/Codes/hackweek2020/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.implicitly_wait(10)
url = 'https://arxiv.org/list/astro-ph/new'
browser.get(url) #open browser


meta_class = "//div[contains(@class,'meta')]"
title_class  = "//div[contains(@class,'list-title mathjax')]"
author_class  = "//div[contains(@class,'list-authors')]"
field_class  = "//div[contains(@class,'list-subjects')]"
abstract_class  = "//div[contains(@class,'mathjax')]"
titles_element = browser.find_elements_by_xpath("{}{}".format(meta_class, title_class))
authors_element = browser.find_elements_by_xpath("{}{}".format(meta_class, author_class))
fields_element = browser.find_elements_by_xpath("{}{}".format(meta_class, field_class))
abstracts_element = browser.find_elements_by_xpath("{}{}".format(meta_class, abstract_class))
print(titles_element)
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
authors = [x.text for x in authors_element]
fields = [x.text for x in fields_element]
abstracts = [x.text for x in abstracts_element]

# print out all the titles.
print('titles:')
print(titles, '\n')

print('fields:')
print(fields, '\n')
