from flask import Flask,request,jsonify,redirect
import json
import sqlite3
app=Flask(__name__)
app.secret_key="slvnsvdkcdvdf"
conn = sqlite3.connect('course1.db')
command1 = """CREATE TABLE IF NOT EXISTS
course(id INTEGER ,name TEXT)"""
cursor = conn.cursor()
cursor.execute(command1)
@app.route('/app/courses/all',methods=['GET'])
def show():
    if request.method=='GET':
     conn = sqlite3.connect('course1.db')
     cursor = conn.cursor()
     cursor.execute("SELECT * from course")
     courses=cursor.fetchall()
     return jsonify(courses)
@app.route('/app/courses',methods=['GET'])
def id():
    if request.method=='GET':
        if 'id' in request.args:
            id=int(request.args['id'])
        else:
            return "unknown request"
        f=1
        conn = sqlite3.connect('course1.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * from course")
        courses=cursor.fetchall()
        res=[]
        for course in courses:
          if course[0]==id:
            res.append(course)
            f=0
            break
        if f==0:
            return jsonify(res)
        else:
            return "ID not in the json list!"
@app.route('/app/courses/add',methods=['GET','POST'])
def create():
    if request.method=='GET':
        if 'id' and 'name' in request.args:
            id=int(request.args['id'])
            name=str(request.args['name'])
        else:
            return "unknown request"
        conn = sqlite3.connect('course1.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO course VALUES(?,?)",(id,name))
        conn.commit()
        return redirect('/app/courses/all')
@app.route('/app/courses/remove',methods=['GET'])
def remove():
    if request.method=='GET':
        if 'id' in request.args:
            id=int(request.args['id'])
        else:
            return "unknown request"
        conn = sqlite3.connect('course1.db')
        cursor = conn.cursor()
        cursor.execute("DELETE from course WHERE id=?",(id,))
        conn.commit()
        return redirect('/app/courses/all')
if __name__ =='__main__':
    app.run(debug=True)