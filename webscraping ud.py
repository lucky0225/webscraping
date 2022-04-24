import pandas as pd 

url = "https://en.wikipedia.org/wiki/Wars_and_battles_involving_Prussia"
tables = pd.read_html(url)
#no of tables
print(len(tables))
#tabel content
print(tables[2].head)
spanish_war = tables[4].head
print(type(spanish_war))


url_2 = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"
tables_2 = pd.read_html(url_2)
print(len(tables_2))
richest_people_2021 = tables_2[3].head
print(richest_people_2021)
print(type(richest_people_2021))
#print(richest_people_2021.dtypes)
