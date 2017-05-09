import sys
sys.path.append('/srv/www/idehe.com/store2/code')
from data_handle import data_sort
from html_handle import index_write

ifile = 'rest.csv'
ofile = 'rest_data.csv'

ifile2 = 'rest2.csv'
ofile2 = 'rest2_data.csv'

ifile_path = "/srv/www/idehe.com/store2/data/"
ofile_path = "/srv/www/idehe.com/store2/data_output/"

data_sort(ifile, ofile, ifile_path, ofile_path) # grab online data, update into csv
data_sort(ifile2, ofile2, ifile_path, ofile_path) # grab online data, update into csv

index_write()