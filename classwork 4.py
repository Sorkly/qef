


# import requests
# import urllib.request
# urllib.request
#1
# opener = urllib.request.build_opener()
# response = opener.open("https://httpbin.org/get")
# print(response.read())
# response = requests.get("https://httpbin.org/get")
# print(response.content)
#2
# response = requests.get("https://httpbin.org/get")
# print(response.content)
# print(f"Datatype{type(response.content)}")
#3
# response = requests.get("https://httpbin.org/get")
# print(response.text)
# print(f"Datatype{type(response.content)}")
#4
# response = requests.post("https://httpbin.org/post",
#                          data=("Test data :" " number"),)

# print(response.text)

#5
# res_parse_list = []
# response = requests.get("https://coinmarketcap.com")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 res_parse_list.append(parse_elem_2)
                

# bitcoin_exchange = res_parse_list[0]
# print(bitcoin_exchange)

# import sqlite3

# connection = sqlite3.connect("itstep_DB.sl3", timeout=5)
# cur = connection.cursor()
# print(connection)
# print(cur)
# connection.close()

# import os
# print(os.path.abspath("itstep_DB_sp2211.sl3"))
# import sqlite3
# connection = sqlite3.connect("itstep_DB_sp2211.sl3", timeout=5)
# cur = connection.cursor()
# # cur.execute("DROP TABLE IF EXISTS first_table;")
# cur.execute("CREATE TABLE first_table (name TEXT);")
# connection.commit()
# connection.close()
 
# import sqlite3
# connection = sqlite3.connect("itstep_DB_sp2211.sl3", timeout=5)
# cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
# cur.execute("INSERT INTO first_table (name) VALUES ('John');")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table;")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()


import sqlite3
connection = sqlite3.connect("itstep_DB_sp2211.sl3", timeout=5)
cur = connection.cursor()
cur.execute("DROP TABLE first_table;")
connection.commit()
connection.close()
 