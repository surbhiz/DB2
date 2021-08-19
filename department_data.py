import mysql.connector
import json
from pymongo import MongoClient

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user = 'root',
    password = '',
    database="company"
)

cursor = mydb.cursor()
sql = "SELECT DNAME,MANAGER_LNAME,MGR_START_DATE,concat('[',group_concat('" + '{"E_LNAME":"' + "',E_LNAME,'" + '","E_FNAME":"' + "',E_FNAME,'" + '","SALARY":' + "',SALARY,'}'),']') as department_data FROM company.department_data group by DNAME;"
cursor.execute(sql)

department_results = cursor.fetchall()

department_dict = {}
emp_arr = []

project_json = open("C:/Users/surbh/Downloads/DB2/db2_project2/department_doc.json",'w', encoding='utf-8')


project_json.write("[")
for each_project in department_results:
    
    out_string = '{"DNAME":"' + str(each_project[0]) + '","MANAGER_LNAME":"' + str(each_project[1]) + '","MGR_START_DATE":"' + str(each_project[2]) + '","DEPARTMENT":' + str(each_project[3]) + '},'
    #print(f"json: {json.dumps(out_string)}")
    project_json.write((out_string))
    project_json.write("\n")

project_json.write("]")