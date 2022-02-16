from flask import Flask,render_template,request
from flask_mysqldb import MySQL


app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] ='suganth2021!'
app.config['MYSQL_DB']='fl'

mysql=MySQL(app)
@app.route('/flask1/create',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email) VALUES(%s,%s)",(name,email))
        mysql.connection.commit()
        cur.close()
    return render_template('1st page.html')
@app.route("/flask1/list")
def users():
    cur= mysql.connection.cursor()
    result=cur.execute("SELECT * FROM users")
    userDetails= cur.fetchall()
    return render_template("example.html",userDetails=userDetails)

if __name__=="__main__":
    app.run(debug=True)
