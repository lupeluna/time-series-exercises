import pandas as pd
import numpy as np
import os


def get_items():
    items_list = []

    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()
    n = data['payload']['max_page']

    for i in range(1,n+1):
        url = 'https://python.zach.lol/api/v1/items?page='+str(i)
        response = requests.get(url)
        data = response.json()
        page_items = data['payload']['items']
        items_list += page_items
    return pd.DataFrame(items_list)
    
    
def get_stores():   
    stores_list = []

    response = requests.get('https://python.zach.lol/api/v1/stores')
    data = response.json()
    n = data['payload']['max_page']

    for i in range(1,n+1):
        url = 'https://python.zach.lol/api/v1/stores?page='+str(i)
        response = requests.get(url)
        data = response.json()
        page_stores = data['payload']['stores']
        stores_list += page_stores
    return pd.DataFrame(stores_list)
    
    
def get_sales():    
    sales_list = []

    response = requests.get('https://python.zach.lol/api/v1/sales')
    data = response.json()
    n = data['payload']['max_page']

    for i in range(1,n+1):
        url = 'https://python.zach.lol/api/v1/sales?page='+str(i)
        response = requests.get(url)
        data = response.json()
        page_sales = data['payload']['sales']
        sales_list += page_sales
    return pd.DataFrame(sales_list)
    
    
def get_all_sales_data():
    if os.path.isfile('combined.csv'):
        df = pd.read_csv('combined.csv', index_col=0)
        return df
    else:
        items = get_items()
        stores = get_stores()
        sales = get_sales()
        sales['store_id'] = sales['store']
        sales = sales.drop(columns='store')
        sales_plus_stores = pd.merge(sales, stores, on='store_id', how='inner')
        sales_plus_stores['item_id'] = sales_plus_stores['item']
        sales_plus_stores = sales_plus_stores.drop(columns='item')
        df = pd.merge(sales_plus_stores, items, on='item_id', how='inner')
        return df
    
    
    
