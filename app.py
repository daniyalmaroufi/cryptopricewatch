import csv
from pycoingecko import CoinGeckoAPI
from terminaltables import AsciiTable

watch_list = []

with open('watch_list.txt') as csvfile:
    list = csv.reader(csvfile)
    for row in list:
        watch_list.append(row[0])

cg = CoinGeckoAPI()

data = cg.get_price(ids=','.join(watch_list), vs_currencies='usd')

table_data = [['Crypto', 'Price']]
for key, value in data.items():
    table_data.append([key, value['usd']])

table = AsciiTable(table_data)
print(table.table)
