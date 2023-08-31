import sqlite3

con = sqlite3.connect('database.db')
pm = con.cursor()
pm.execute('create table if not exists mobiles(id integer ,company varcher(100),model varcher(100),madein varcher(100),memory varcher(100) ,color varcher(100), price integer)')
# =============================================================================================================
# pm.execute('insert into  mobiles(id,company,model,madein,memory,color,price) values (46,IPHONE,14PROMAX,USA,1T,BLUE,90000000')
con.commit()
















