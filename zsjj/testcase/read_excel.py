# coding:utf-8
import xlrd

data = xlrd.open_workbook('testdata.xls')
table = data.sheet_by_name(u'Sheet1')

hangs=table.nrows #总行数
lies = table.ncols #总列数

print hangs
print lies
print  table.row_values(1)
print table.col_values(0)