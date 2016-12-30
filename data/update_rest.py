import sys
sys.path.append('/srv/www/idehe.com/store2/code')
from data_handle import data_mhandle
from html_handle import index_write
ifile = 'rest.csv'
ofile = 'rest_data.csv'

ifile2 = 'rest2.csv'
ofile2 = 'rest2_data.csv'

file_path = "/srv/www/idehe.com/store2/data/"

data_mhandle(ifile, ofile, file_path) # grab online data, update into csv
data_mhandle(ifile2, ofile2, file_path) # grab online data, update into csv

index_write()