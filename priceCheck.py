import urllib.request
import re
from decimal import *
import os
import datetime

nonSaleSeasonPrice = Decimal(2071.50)
page = urllib.request.urlopen('http://www.farfetch.com/ca/shopping/women/mulberry-gold-tone-hardware-medium-tote-item-11535822.aspx?storeid=10167&from=1&ffref=lp_pic_6_2_')
content = str(page.read())
tag = '<span class="listing-price" data-tstid="itemprice" itemprop="price">'
index = content.index(tag) + len(tag) + 1
formattedPrice = content[index: index+8]

priceGroups = re.match(r'(\d{1,3}),(\d{3}).?(\d{0,2})', formattedPrice)
price = priceGroups.group(1) + priceGroups.group(2)
if priceGroups.group(3):
    price += '.' + priceGroups.group(3)

price = Decimal(price)
priceDiff = Decimal(price - nonSaleSeasonPrice)


log = open('./priceLog.txt', 'a')
log.write(str(datetime.date.today()) + ': ' + str(price) + ' | ' + str(priceDiff) + '\n')
log.close()
os.system('afplay ./priceCheckAlert.m4a')
