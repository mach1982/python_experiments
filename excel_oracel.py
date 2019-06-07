import xlsxwriter
import cx_Oracle

con = cx_Oracle.connect('hr/password@127.0.0.1:1521/xe')
sql1="""select last_name , salary from EMPLOYEES"""
cursor.execute(sql1)

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('salary.xlsx')
worksheet = workbook.add_worksheet()



# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 1

# Iterate over the data and write it out row by row.
worksheet.write(0,0,"Name")
worksheet.write(0,1,"Salary")
for r in cursor:
    
    worksheet.write(row,col-1,r[0])
    worksheet.write(row, col,r[1])
   
    row += 1




workbook.close()