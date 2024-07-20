""" zid_project1.py

"""
import json
import os

import toolkit_config as cfg

ROOTDIR = os.path.join(cfg.PRJDIR, 'project1')
DATDIR = os.path.join(ROOTDIR, 'data')
TICPATH = os.path.join(ROOTDIR, 'TICKERS.txt')

COLUMNS = ['Volume', 'Date', 'Adj Close', 'Close', 'Open', 'High']

COLWIDTHS = {
    'Volume': 14,
    'Date': 11,
    'Adj Close': 19,
    'Close': 10,
    'Open': 6,
    'High': 20}

def get_tics(pth):

    tics = {}
    with open(pth, 'r') as file:
        for line in file:
            if line.strip():
                exchange, ticker = line.strip().replace('"','').split('=')
                tics[ticker.lower()] = exchange.lower()
    return tics

# def _test_get_tics():
#     """ Test function for the `get_tics` function. Will print the tickers as
#     returned by the `get_tics` function.
#     """
#     pth = TICPATH
#     tics = get_tics(pth)
#     print(tics)

def read_dat(tic):
    fdata_path = os.path.join(DATDIR, f"{tic}_prc.dat")
    with open(fdata_path) as fdata:
        dlines = [line.strip() for line in fdata]
    return dlines

# def _test_read_dat():
#     """ Test function for the `read_dat` function. Will read the lines of the
#     first ticker in `TICPATH` and print the first line in the list.
#     """
#     pth = TICPATH
#     tics = sorted(list(get_tics(pth).keys()))
#     tic = tics[0]
#     lines = read_dat(tic)
#     # Print the first line in the file
#     print(f'The first line in the dat file for {tic} is:')
#     print(lines[0])

def line_to_dict(line):
    datdata = {}
    start = 0
    for column in COLUMNS:
        col = COLWIDTHS[column]
        value = line[start:start + col]
        datdata[column] = value
        start += col

    return datdata

# def _test_line_to_dict():
#     """ Test function for the `read_dat` function. This function will perform
#     the following operations:
#     - Get the tickers using `get_tics`
#     - Read the lines of the ".dat" file for the first ticker
#     - Convert the first line of this file to a dictionary
#     - Print this dictionary
#     """
#     pth = TICPATH
#     tics = sorted(list(get_tics(pth).keys()))
#     lines = read_dat(tics[0])
#     dic = line_to_dict(lines[0])
#     print(dic)

def verify_tickers(tic_exchange_dic, tickers_lst=None):
    if tickers_lst is not None:
        if not tickers_lst:
            raise Exception("Ticker is an empty list.")
        for ticker in tickers_lst:
            if ticker not in tic_exchange_dic:
                raise KeyError(f"'{ticker}' is not a valid key in the tickers dictionary.")
def verify_cols(col_lst=None):
    if col_lst is not None:
        if not col_lst:
            raise Exception("Column name is empty.")
        for col in col_lst:
            if col not in COLUMNS:
                raise Exception(f"'{col}' is not found in COLUMNS.")
def create_data_dict(tic_exchange_dic, tickers_lst=None, col_lst=None):
    if tickers_lst is None:
        tickers_lst = list(tic_exchange_dic.keys())
    else:
        verify_tickers(tic_exchange_dic, tickers_lst)

    if col_lst is None:
        col_lst = COLUMNS
    else:
        verify_cols(col_lst)

    data_dict = {}
    for ticker in tickers_lst:
        data_dict[ticker] = {
            'exchange': tic_exchange_dic[ticker],
            'data': []
        }
        lines = read_dat(ticker)
        for line in lines:
            line_data = line_to_dict(line)
            specified_data = {col: line_data[col] for col in col_lst}
            data_dict[ticker]['data'].append(specified_data)

    return data_dict
def _test_create_data_dict():
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)

    for tic in tickers_lst:
        data_dict[tic]['data'] = data_dict[tic]['data'][:3]

    print(data_dict)

def create_json(data_dict, pth):
    with open(pth, 'w') as json_file:
        json.dump(data_dict, json_file)

def _test_create_json(json_pth):
    """ Test function for the `create_json_ function.
    This function will save the dictionary returned by `create_data_dict` to the path specified.

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)
    create_json(data_dict, json_pth)
    print(f'Data saved to {json_pth}')

if __name__ == "__main__":
    # Test functions
    # _test_get_tics()
    # _test_read_dat()
    # _test_line_to_dict()
    # _test_create_data_dict()
    # _test_create_json(os.path.join(DATDIR, 'data.json'))  # Save the file to data/data.json
    pass
