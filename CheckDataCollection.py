import xlrd

dir = './testfile/现场记录-饮食工坊.xlsx'

book = xlrd.open_workbook(dir)
#print("The number of worksheets is {0}".format(book.nsheets))
#print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(2)
#print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("creatTs is {0}".format(sh.cell_value(rowx=1, colx=2)))
print(xlrd.xldate_as_tuple(sh.cell(1, 2).value, 0))

a = []
b = []
for rx in range(1,sh.nrows):
# for rx in range(1,3):
    #print(sh.row(rx))
    a.append(int(sh.row(rx)[6].value))
    a.append(xlrd.xldate_as_tuple(sh.row(rx)[2].value,0)[:3])
    for j in range(17,14,-1):
        a.append(sh.row(rx)[j].value)

    #print(a)
    b.append(a)
    a=[]

print(b)

year = 2019
month = 5
day = 16

