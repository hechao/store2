import sys
sys.path.append('/srv/www/idehe.com/store2/code')
from data_handle import data_mhandle
from html_handle import index_write
ifile = 'ETF.csv'
ofile = 'ETF_data.csv'

file_path = "/srv/www/idehe.com/store2/stock_data/"

data_mhandle(ifile, ofile, file_path) # grab online data, update into csv

index_write()