import requests

url_price_rub = 'https://market.csgo.com/api/v2/prices/RUB.json'


list_price = requests.get(url_price_rub)

quality = {
    'Battle-Scarred': 1,
    'Well-Worn': 2, 
    'Field-Tested': 3,
    'Minimal Wear': 4, 
    'Factory New': 5

}


def min_max_price(name_skin, list_price):
    highest_price = 0
    lowest_price = None
    highest_price_1 = 0
    lowest_price_1 = None
    highest_price_2 = 0
    lowest_price_2 = None
    highest_price_3 = 0
    lowest_price_3 = None
    highest_price_4 = 0
    lowest_price_4 = None
    highest_price_5 = 0
    lowest_price_5 = None
    for item in list_price:
        if name_skin in item['market_hash_name']: 
            if '(Factory New)' in item['market_hash_name']:
                if float(item['price']) > highest_price: 
                    highest_price = float(item['price'])
                if not lowest_price or float(item['price']) < lowest_price: 
                    lowest_price = float(item['price'])
            if '(Minimal Wear)' in item['market_hash_name']:
                if float(item['price']) > highest_price_1: 
                    highest_price_1 = float(item['price'])
                if not lowest_price_1 or float(item['price']) < lowest_price_1: 
                    lowest_price_1 = float(item['price'])
            if '(Field-Tested)' in item['market_hash_name']:
                if float(item['price']) > highest_price_2: 
                    highest_price_2 = float(item['price'])
                if not lowest_price_2 or float(item['price']) < lowest_price_2: 
                    lowest_price_2 = float(item['price'])
            if '(Well-Worn)' in item['market_hash_name']:
                if float(item['price']) > highest_price_3: 
                    highest_price_3 = float(item['price'])
                if not lowest_price_3 or float(item['price']) < lowest_price_3: 
                    lowest_price_3 = float(item['price'])
            if '(Battle-Scarred)' in item['market_hash_name']:
                if float(item['price']) > highest_price:_4:
                    highest_price_4 = float(item['price'])
                if not lowest_price_4 or float(item['price']) < lowest_price_4: 
                    lowest_price_4 = float(item['price'])
            
    return highest_price, lowest_price, highest_price_1, lowest_price_1, highest_price_2, lowest_price_2, highest_price_3, lowest_price_3, highest_price_4, lowest_price_4

print( 'Factory new: ' highest_price, lowest_price,'. ''Minimal wear: ' highest_price_1, lowest_price_1,'. ''Field-Tested: ' highest_price_2, lowest_price_2,'. ''Well-Worn: ' highest_price_3, lowest_price_3,'. ''Battle-Scarred: ' highest_price_4)


def min_max_price(name_skin, list_price, quality_skin):
    if quality_skin= 'Battle-Scarred':
        quality_skin = 1
    if quality_skin = 'Well-Worn'
    quality_skin_3
    quality_skin_4
    quality_skin_5
    highest_price = 0
    lowest_price = None
    for item in list_price:
        if name_skin in item['market_hash_name']: 
            if '(Factory New)' in item['market_hash_name']:
                if float(item['price']) > highest_price: 
                    highest_price = float(item['price'])
                if not lowest_price or float(item['price']) < lowest_price: 
                    lowest_price = float(item['price'])