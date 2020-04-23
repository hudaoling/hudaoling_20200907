
import xlrd
#打开一个workbook
workbook = xlrd.open_workbook('filters.xlsx')
#抓取所有sheet页的名称
worksheets = workbook.sheet_names()
print('worksheets is %s' %worksheets)

#定位到sheet-filters
worksheet1 = workbook.sheet_by_name(u'filters')

#或者 遍历所有sheet对象
# for worksheet_name in worksheets:
#     worksheet = workbook.sheet_by_name(worksheet_name)
#     print(worksheet,worksheet_name)

#遍历sheet-filters中所有行row
num_rows = worksheet1.nrows
for curr_row in range(num_rows):
    row = worksheet1.row_values(curr_row)
    print('row%s is %s' %(curr_row,row))
#遍历sheet-filters中所有列col
num_cols = worksheet1.ncols
for curr_col in range(num_cols):
    col = worksheet1.col_values(curr_col)
    print('col%s is %s' %(curr_col,col))
#遍历sheet-filters中所有单元格cell
for rown in range(num_rows):
    for coln in range(num_cols):
        cell = worksheet1.cell_value(rown,coln)
        print(cell)