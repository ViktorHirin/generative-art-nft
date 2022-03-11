#!/usr/bin/env python
# coding: utf-8


import json

filename = './output/upload.json'

with open(filename, "r") as file:
    data = json.load(file)

for count in range(10000):
    ITEM_JSON = {
        "nft_url": "https://opensea.io/assets/matic/0x4f6a59a078a024f02b4259dba4c4b552722093b5/" + str(count),
        "supply": 1,
        "blockchain": "Polygon",
        "sale_type": "",
        "price": 0.002,
        "method": "",
        "duration": [
          "08-03-2022 1:00", "31-08-2022 1:00"
        ],
        "specific_buyer": "",
        "quantity": 1
    }
    
    data.append(ITEM_JSON)

with open(filename, "w") as file:
    json.dump(data, file)
