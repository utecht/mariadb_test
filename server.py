import pymysql
from flask import Flask
import json

app = Flask(__name__)

@app.route('/class/<path:class_id>', methods=['GET'])
def get_students(class_id):
    connection = pymysql.connect(host='localhost',user='root',db='benchmark',cursorclass=pymysql.cursors.DictCursor)
    c = connection.cursor()
    c.execute('select * from students join classes on student = sid where id = %s', class_id)
    a = c.fetchall()
    c.close()
    return json.dumps(a)

@app.route('/student/<path:student_id>', methods=['GET'])
def get_student(student_id):
    connection = pymysql.connect(host='localhost',user='root',db='benchmark',cursorclass=pymysql.cursors.DictCursor)
    c = connection.cursor()
    c.execute('select * from students where sid = %s', student_id)
    a = c.fetchall()
    c.close()
    return json.dumps(a)

@app.route('/classes/')
def get_classes():
    c = connection.cursor()
    c.execute('select id from class')
    a = c.fetchall()
    c.close()
    return json.dumps(a)


if __name__ == '__main__':
    app.run(debug=True)
