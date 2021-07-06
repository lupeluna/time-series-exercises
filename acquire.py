import pandas as pd
import numpy as np
import os
import requests


def get_df(name):
    '''
    This function takes in the string ‘items’, ‘stores’, or ‘sales’ and
    returns a df containing all pages and creates a .csv file for future use.
    '''
    base_url = 'https://python.zach.lol'
    api_url = base_url + '/api/v1/'
    response = requests.get(api_url + name)
    data = response.json()
    file_name=(name+'.csv')
    if os.path.isfile(file_name):
        return pd.read_csv(name+'.csv')
    else:
        # create list from 1st page
        my_list = data['payload'][name]
        # loop through the pages and add to list
        while data['payload']['next_page'] != None:
            response = requests.get(base_url + data['payload']['next_page'])
            data = response.json()
            my_list.extend(data['payload'][name])
        # Create DataFrame from list
        df = pd.DataFrame(my_list)
        # Write DataFrame to csv file for future use
        df.to_csv(name + '.csv', index=False)
    return df



def get_items():
    if os.path.isfile('items.csv'):
        df = pd.read_csv('items.csv', index_col=0)
        return df
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
    df.to_csv('items.csv', index=False)

    return pd.DataFrame(items_list)
    
    
def get_stores():
    if os.path.isfile('stores.csv'):
        df = pd.read_csv('stores.csv', index_col=0)
        return df
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
    df.to_csv('stores.csv', index=False)

    return pd.DataFrame(stores_list)
    
    
def get_sales():
    if os.path.isfile('sales.csv'):
        df = pd.read_csv('sales.csv', index_col=0)
        return df
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
    df.to_csv('sales.csv', index=False)


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
        df.to_csv('combined.csv', index=False)

        return df
    
    
    
def get_germany_power():
    '''
    returns Germany power data into a csv, and creates it for you
    '''
    if os.path.isfile('germany_power.csv'):
        df = pd.read_csv('germany_power.csv', index_col=0)
        return df
    else:
        
        data = pd.read_csv("https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv")
        data.to_csv('germany_power.csv')
    return data
    
    
    
