import sys
sys.path.append('/srv/www/idehe.com/store2/code')
from data_handle import data_mhandle
from html_handle import index_write
funda_ifile = 'uncategory.csv'
funda_ofile = 'uncategory_data.csv'

file_path = "/srv/www/idehe.com/store2/stock_data/"

data_mhandle(funda_ifile, funda_ofile, file_path)

index_write()