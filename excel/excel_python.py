import xlsxwriter
import cx_Oracle

con = cx_Oracle.connect('hr/password@127.0.0.1:1521/xe')
cursor = con.cursor()
sql1="""select last_name , salary from EMPLOYEES"""
cursor.execute(sql1)

workbook = xlsxwriter.Workbook('salary1.xlsx')
worksheet = workbook.add_worksheet()

row = 1
col = 1

worksheet.write(0,0,"Name")
worksheet.write(0,1,"Salary")

for r in cursor:
    
    worksheet.write(row,col-1,r[0])
    worksheet.write(row, col,r[1])
   
    row += 2

workbook.close()