import pandas as pd
import numpy as np


def prep_all_sales(df):
    df.sale_date = df.sale_date.apply(lambda x: x[:-13])
    df.sale_date = pd.to_datetime(df.sale_date)
    df = df.reset_index()
    df = df.set_index('sale_date').sort_index()
    df['month'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df['sale_amount'] * df['item_price']
    return df

    
    
#     df.sale_date = pd.to_datetime(df.sale_date)
#     df = df.set_index('sale_date').sort_index()
#     df['month'] = df.index.month
#     df['day_of_week'] = df.index.day_name()
#     df['sales_total'] = df.sale_amount * df.item_price
#     return df


def prep_germany(df):

    # convert 'Date' column to datetime format
    germany_df['Date'] = pd.to_datetime(germany_df.Date)
    
    # set the index to 'Date'
    germany_df = germany_df.set_index('Date').sort_index()
    
    # add 'month' column to df
    germany_df['month'] = germany_df.index.month_name()
    
    # add 'year' column to df
    germany_df['year'] = germany_df.index.year
    
    # fill any missing values
    germany_df = germany_df.fillna(0)
    
    return germany_df