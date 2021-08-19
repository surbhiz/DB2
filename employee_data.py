import mysql.connector
import json

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user = 'root',
    password = '',
    database="company"
)

cursor = mydb.cursor()
sql = "SELECT EMP_LNAME,EMP_FNAME,DNAME,concat('[',group_concat('" + '{"PNAME":"' + "',PNAME,'" + '","PNUMBER":"' + "',PNUMBER,'" + '","HOURS":' + "',HOURS,'}'),']') as employee_data FROM company.employee_data group by EMP_LNAME;"
cursor.execute(sql)

employee_results = cursor.fetchall()

project_json = open("C:/Users/surbh/Downloads/DB2/db2_project2/employee_doc.json",'w', encoding='utf-8')


project_json.write("[")
for each_project in employee_results:
    
    out_string ='{"EMP_LNAME":"' + str(each_project[0]) + '","EMP_FNAME":"' + str(each_project[1]) + '","DNAME":"' + str(each_project[2]) + '","EMPLOYEE":' + str(each_project[3]) + '},'
    #print(f"json: {json.dumps(out_string)}")
    project_json.write(out_string)
    project_json.write("\n")
project_json.write("]")
