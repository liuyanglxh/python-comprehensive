import requests
from util import file_util
import json


def get_hist_price(stock_code, days):
    url = """
    https://push2his.eastmoney.com/api/qt/stock/kline/get?fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57
    """.strip()
    params = {
        'secid': '0.' + stock_code,
        'fields1': 'f1%2Cf2%2Cf3%2Cf4%2Cf5',
        'fields2': 'f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57',
        'lmt': days,
        'klt': '101',
        'fqt': '1',
        'end': '30000101'
    }
    resp = requests.get(url, params)
    return resp.json()['data']['klines']


def parse(price_info):
    lst = []
    for x in price_info:
        splits = x.split(',')
        day, start, end, max_price, min_price, unkown1, unkown2 = splits
        lst.append({
            'day': day,
            'start': start,
            'end': end,
            'max_price': max_price,
            'min_price': min_price
        })
    return lst


def analysis(stock_price_lst):
    pass


# stock_code, days = '002127', 58
# print(parse(get_hist_price(stock_code, days)))

data = [{'day': '2021-03-24', 'start': '9.30', 'end': '9.04', 'max_price': '9.33', 'min_price': '8.98'}, {'day': '2021-03-25', 'start': '9.13', 'end': '9.33', 'max_price': '9.53', 'min_price': '9.07'}, {'day': '2021-03-26', 'start': '9.31', 'end': '9.51', 'max_price': '9.62', 'min_price': '9.25'}, {'day': '2021-03-29', 'start': '9.53', 'end': '9.28', 'max_price': '9.55', 'min_price': '9.23'}, {'day': '2021-03-30', 'start': '9.23', 'end': '9.12', 'max_price': '9.27', 'min_price': '9.03'}, {'day': '2021-03-31', 'start': '9.13', 'end': '9.01', 'max_price': '9.15', 'min_price': '8.98'}, {'day': '2021-04-01', 'start': '9.02', 'end': '9.11', 'max_price': '9.17', 'min_price': '9.00'}, {'day': '2021-04-02', 'start': '9.21', 'end': '9.09', 'max_price': '9.25', 'min_price': '9.05'}, {'day': '2021-04-06', 'start': '9.09', 'end': '9.13', 'max_price': '9.16', 'min_price': '8.97'}, {'day': '2021-04-07', 'start': '9.12', 'end': '9.41', 'max_price': '9.50', 'min_price': '9.05'}, {'day': '2021-04-08', 'start': '9.40', 'end': '9.26', 'max_price': '9.41', 'min_price': '9.24'}, {'day': '2021-04-09', 'start': '9.22', 'end': '9.09', 'max_price': '9.22', 'min_price': '9.05'}, {'day': '2021-04-12', 'start': '9.16', 'end': '9.00', 'max_price': '9.29', 'min_price': '8.99'}, {'day': '2021-04-13', 'start': '9.01', 'end': '8.76', 'max_price': '9.02', 'min_price': '8.68'}, {'day': '2021-04-14', 'start': '8.68', 'end': '8.89', 'max_price': '8.92', 'min_price': '8.56'}, {'day': '2021-04-15', 'start': '8.80', 'end': '8.99', 'max_price': '9.06', 'min_price': '8.75'}, {'day': '2021-04-16', 'start': '8.78', 'end': '8.78', 'max_price': '8.92', 'min_price': '8.67'}, {'day': '2021-04-19', 'start': '8.76', 'end': '8.76', 'max_price': '8.95', 'min_price': '8.61'}, {'day': '2021-04-20', 'start': '8.69', 'end': '8.76', 'max_price': '8.87', 'min_price': '8.68'}, {'day': '2021-04-21', 'start': '8.70', 'end': '8.59', 'max_price': '8.74', 'min_price': '8.58'}, {'day': '2021-04-22', 'start': '8.58', 'end': '8.52', 'max_price': '8.62', 'min_price': '8.51'}, {'day': '2021-04-23', 'start': '8.49', 'end': '8.08', 'max_price': '8.50', 'min_price': '8.05'}, {'day': '2021-04-26', 'start': '7.98', 'end': '7.91', 'max_price': '8.16', 'min_price': '7.85'}, {'day': '2021-04-27', 'start': '7.87', 'end': '8.15', 'max_price': '8.26', 'min_price': '7.69'}, {'day': '2021-04-28', 'start': '8.11', 'end': '8.19', 'max_price': '8.45', 'min_price': '7.99'}, {'day': '2021-04-29', 'start': '8.08', 'end': '7.91', 'max_price': '8.12', 'min_price': '7.89'}, {'day': '2021-04-30', 'start': '7.89', 'end': '7.91', 'max_price': '8.01', 'min_price': '7.80'}, {'day': '2021-05-06', 'start': '7.95', 'end': '7.76', 'max_price': '7.97', 'min_price': '7.74'}, {'day': '2021-05-07', 'start': '7.74', 'end': '7.76', 'max_price': '7.92', 'min_price': '7.61'}, {'day': '2021-05-10', 'start': '7.85', 'end': '8.04', 'max_price': '8.11', 'min_price': '7.83'}, {'day': '2021-05-11', 'start': '7.95', 'end': '8.03', 'max_price': '8.09', 'min_price': '7.93'}, {'day': '2021-05-12', 'start': '8.03', 'end': '8.29', 'max_price': '8.30', 'min_price': '8.01'}, {'day': '2021-05-13', 'start': '8.21', 'end': '8.83', 'max_price': '8.99', 'min_price': '8.17'}, {'day': '2021-05-14', 'start': '8.92', 'end': '8.82', 'max_price': '9.05', 'min_price': '8.66'}, {'day': '2021-05-17', 'start': '8.81', 'end': '8.76', 'max_price': '8.95', 'min_price': '8.69'}, {'day': '2021-05-18', 'start': '8.76', 'end': '9.23', 'max_price': '9.47', 'min_price': '8.76'}, {'day': '2021-05-19', 'start': '9.27', 'end': '9.32', 'max_price': '9.68', 'min_price': '9.11'}, {'day': '2021-05-20', 'start': '9.30', 'end': '9.07', 'max_price': '9.37', 'min_price': '8.99'}, {'day': '2021-05-21', 'start': '9.12', 'end': '9.07', 'max_price': '9.39', 'min_price': '8.95'}, {'day': '2021-05-24', 'start': '9.12', 'end': '9.03', 'max_price': '9.20', 'min_price': '8.95'}, {'day': '2021-05-25', 'start': '9.07', 'end': '9.08', 'max_price': '9.16', 'min_price': '8.90'}, {'day': '2021-05-26', 'start': '9.11', 'end': '10.01', 'max_price': '10.01', 'min_price': '9.08'}, {'day': '2021-05-27', 'start': '10.17', 'end': '9.99', 'max_price': '10.46', 'min_price': '9.90'}, {'day': '2021-05-28', 'start': '9.93', 'end': '9.59', 'max_price': '10.01', 'min_price': '9.58'}, {'day': '2021-05-31', 'start': '9.59', 'end': '10.03', 'max_price': '10.20', 'min_price': '9.53'}, {'day': '2021-06-01', 'start': '10.05', 'end': '9.89', 'max_price': '10.11', 'min_price': '9.77'}, {'day': '2021-06-02', 'start': '9.96', 'end': '10.01', 'max_price': '10.17', 'min_price': '9.79'}, {'day': '2021-06-03', 'start': '10.03', 'end': '10.12', 'max_price': '10.52', 'min_price': '9.94'}, {'day': '2021-06-04', 'start': '9.98', 'end': '9.84', 'max_price': '9.99', 'min_price': '9.73'}, {'day': '2021-06-07', 'start': '9.94', 'end': '9.78', 'max_price': '10.09', 'min_price': '9.55'}, {'day': '2021-06-08', 'start': '9.79', 'end': '9.76', 'max_price': '9.94', 'min_price': '9.62'}, {'day': '2021-06-09', 'start': '9.70', 'end': '9.43', 'max_price': '9.77', 'min_price': '9.43'}, {'day': '2021-06-10', 'start': '9.38', 'end': '9.42', 'max_price': '9.77', 'min_price': '9.35'}, {'day': '2021-06-11', 'start': '9.37', 'end': '9.32', 'max_price': '9.59', 'min_price': '9.23'}, {'day': '2021-06-15', 'start': '9.34', 'end': '9.07', 'max_price': '9.38', 'min_price': '8.90'}, {'day': '2021-06-16', 'start': '9.12', 'end': '9.10', 'max_price': '9.33', 'min_price': '9.00'}, {'day': '2021-06-17', 'start': '9.08', 'end': '8.91', 'max_price': '9.12', 'min_price': '8.91'}, {'day': '2021-06-18', 'start': '8.96', 'end': '9.09', 'max_price': '9.19', 'min_price': '8.81'}]

file_util.append_lines('/Users/liuyang/stock/002127.txt', [json.dumps(x) for x in data])
