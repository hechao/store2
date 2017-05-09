#! /usr/bin/python
#-*- encoding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')


from csv_handle import csv_readlist, csv_writelist
from xq_handle import xq_data_A, xq_data_A_filter, xq_data_index_bond, xq_data_index_filter, xq_data_bond_filter

#from google_data import data_filter, gfile_check

def update_data_A(ifile, file_path):
    # read csv SID list, get data, filter, update list
    update_data = csv_readlist(ifile, file_path)
    for i in update_data:
        xdA = xq_data_A(i['SID'])
        data_filtered = xq_data_A_filter(xdA)
        i.update(data_filtered)
    #print stock_data
    return update_data

def update_data_bond(ifile, file_path):
    # read csv SID list, get data, filter, update list
    update_data = csv_readlist(ifile, file_path)
    for i in update_data:
        xdA = xq_data_index_bond(i['SID'])
        data_filtered = xq_data_bond_filter(xdA)
        i.update(data_filtered)
    #print stock_data
    return update_data
    
def data_add_range_A(updated_data):
    # find data high and low
    for i in updated_data:
        #print type(i['jk'])
        cur_price = float(i['current_price'][1:])
        KL = float(i['52KL'])
        KH = float(i['52KH'])
        cal_tmp = (cur_price-KL)/(KH-KL)
        #print cal_tmp
        i['range'] = round(cal_tmp*100,2)
    ## 手动替换显示一些不靠谱数据
    basedata = csv_readlist('basedata.csv', "/srv/www/idehe.com/store2/data/")
    for u in updated_data:
        for j in basedata:
            if u['SID'] == j['SID']:
                u.update(j)
    #print updated_data
    return updated_data


def data_sort_A(infile, outfile, ifile_path, ofile_path):
    #grab data
    udA = update_data_A(infile, ifile_path)
    # update range 
    data_ranged_A = data_add_range_A(udA)
    # write back
    csv_writelist(outfile, ofile_path, data_ranged_A)

def data_sort_bond(infile, outfile, ifile_path, ofile_path):
    #grab data
    udB = update_data_bond(infile, ifile_path)
    # write back
    csv_writelist(outfile, ofile_path, udB)    
    
if __name__ == "__main__":
    ifile = "ETF.csv"
    ofile = "ETF_data.csv"
    bond_ifile = "bond.csv"
    bond_ofile = "bond_data.csv"
    #g_path = '/srv/www/idehe.com/store2/stock/'
    
    #file_path = "/srv/www/idehe.com/store2/stock_data/"
    
    ifile_path = "/srv/www/idehe.com/store2/data/"
    ofile_path = "/srv/www/idehe.com/store2/data_output/"
    
    data_sort_bond(bond_ifile, bond_ofile, ifile_path, ofile_path)
    
    