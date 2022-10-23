import mysql.connector

mydb=mysql.connector

from flask import Flask,request
app=Flask(__name__)


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dataentry",)


if mydb.is_connected():
    print("connected")


@app.route('/', methods=['GET', 'POST'])
def register(cnx=None):
        msg = 'Please Fill up the Form'
        if request.method == 'POST' in request.form:
            name = request.form['name']
            labour_hours = request.form['labour-hours']
            mrp = request.form['mrp']

            array = [name, mrp, labour_hours ]


            cursor.execute( "INSERT INTO `product info`  VALUES (NULL,'{}','{}','{}');".format(name,mrp,labour_hours))
            cnx.commit()
            msg = 'You have successfully registered'

cursor=mydb.cursor()
cursor.execute("INSERT * FROM `product info`")


