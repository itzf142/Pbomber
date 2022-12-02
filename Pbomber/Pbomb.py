import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


print('Enter target number:')
nu = input()
print('Enter amount:')
am = int(input())
# print('Hello, ' + nu)
sl = 1

while sl < am:
    driver = webdriver.Chrome(executable_path='E:\PRITOM\Apps\chromedriver_win32/chromedriver.exe')
    driver.get('https://ultranetrn.com.br/fonts/api.php?number=' + nu)
    print(sl)
    if sl == 10000:
        break
    sl += 1






