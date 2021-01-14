from databases import mysql

test = mysql.mysql()
# print(test.getAll())
fu = test.getFBKey()

for row in fu:

    print(row)