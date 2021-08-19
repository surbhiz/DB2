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
sql = "SELECT PNAME,PNUMBER,DNAME,concat('[',group_concat('" + '{"EMP_LNAME":"' + "',EMP_LNAME,'" + '","EMP_FNAME":"' + "',EMP_FNAME,'" + '","HOURS":' + "',HOURS,'}'),']') as project_data FROM company.project_data group by PNAME;"
cursor.execute(sql)

project_results = cursor.fetchall()

project_dict = {}
emp_arr = []

project_json = open("C:/Users/surbh/Downloads/DB2/db2_project2/project_doc.json",'w')


project_json.write("[")
for each_project in project_results:

    out_string = '{"PNAME":"' + str(each_project[0]) + '","PNUMBER":' + str(each_project[1]) + ',"DNAME":"' + str(each_project[2]) + '","PROJECT":' + str(each_project[3]) + '},'
    project_json.write(out_string)
    project_json.write("\n")
project_json.write("]")