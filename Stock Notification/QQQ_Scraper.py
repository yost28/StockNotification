import requests
from bs4 import BeautifulSoup
import numpy as np
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

page = requests.get('https://finance.yahoo.com/quote/QQQ/holdings?p=QQQ')
soup = BeautifulSoup(page.text, 'html.parser')

last_links = soup.find(class_='Ta(end) BdT Bdc($screenerBorderGray) H(36px)')
# print (last_links)


# quote =soup.find("div", {"class":"Pos(r) Bgc($bg-content) Miw(1007px) Maw(1260px) tablet_Miw(600px)--noRightRail Bxz(bb) Bdstartc(t) Bdstartw(20px) Bdendc(t) Bdends(s) Bdendw(20px) Bdstarts(s) Mx(a)"},{"data-reactid":"27"})
quote = soup.find("div", {"class": "Mb(20px)"}, {"data-test": "top-holdings"})

quote2 = quote.find_all('td')
quote3 = quote.find_all('a')
symbols = []
percentage = []
i = 0

for stock in quote3:
    symbols.append(stock.contents[0])

for stock in quote2:
    percentage.append((str(stock.contents[0])[:-1]))

del symbols[0]
#print(symbols)

for i in range(0, 10, 1):
    del percentage[i]
    del percentage[i]
    percentage[i] = float(percentage[i])

total = sum(percentage)

for i in range(0, 10, 1):
    percentage[i] = percentage[i] / total

#print(percentage)
#print (total)
for i in range(0, 10, 1):
    sheet1.write(0, i, symbols[i])
    sheet1.write(1, i, percentage[i])

wb.save('example.xls')

