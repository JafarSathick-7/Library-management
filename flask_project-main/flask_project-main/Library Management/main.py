from flask import *
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="flask"
app.config['MYSQL_CURSORCLASS']="DictCursor"
mysql=MySQL(app)
@app.route('/')
def home():
    return render_template('login.html')
#LOGIN PROCESS
@app.route('/ulogin',methods=['GET','POST'])
def ulogin():
    if request.method=="POST":
        uname=request.form['uname']
        pas=request.form['upass']
        con = mysql.connection.cursor()
        con.execute("select * from user where uname=%s and password=%s;",[uname,pas])
        r = len(con.fetchall())
        con.close()
        if r==1:
            return redirect(url_for('dash'))
        else:
            flash("Invalid usname or password")
            return redirect(url_for('home'))
#Register process
@app.route('/uregister',methods=['GET','POST'])
def uregister():
    if request.method=="POST":
        name = request.form['uname']
        email=request.form['email']
        pas=request.form['password']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO user(uname,email,password) values (%s,%s,%s);",(name,email,pas))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('login'))
@app.route('/login')
def logout():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/dash')
def dash():
    con = mysql.connection.cursor()
    con.execute("select * from books;")
    r = len(con.fetchall())
    con.execute("select * from user;")
    d=len(con.fetchall())
    con.execute("select * from issue;")
    a = len(con.fetchall())
    con.execute("select * from transaction;")
    b = len(con.fetchall())
    con.close()
    return render_template('dash.html',us=d,bo=r,i=a,t=b)
@app.route('/user')
def user():
    con = mysql.connection.cursor()
    con.execute("select * from user;")
    r=con.fetchall()
    con.close()
    return render_template('user.html',data=r)
@app.route('/book')
def book():
    con = mysql.connection.cursor()
    con.execute("select * from books;")
    r = con.fetchall()
    con.close()
    return render_template('book.html',data=r)
@app.route('/transaction')
def trans():
    con = mysql.connection.cursor()
    con.execute("select * from transaction;")
    r = con.fetchall()
    con.close()
    return render_template('transaction.html',data=r)
@app.route('/issuebook')
def issue():
    con = mysql.connection.cursor()
    con.execute("select * from issue;")
    r = con.fetchall()
    con.close()
    return render_template('issuebook.html',data=r)
#edit user
@app.route('/edituser/<string:id>',methods=['GET','POST'])
def edituser(id):
    con = mysql.connection.cursor()
    con.execute("select * from user where u_id=%s;",id)
    r=con.fetchone()
    con.close()
    return render_template('edituser.html',id=r)
#editbook
@app.route('/editbook/<string:id>',methods=['GET','POST'])
def editbook(id):
    con = mysql.connection.cursor()
    con.execute("select * from books where b_id=%s;",id)
    r=con.fetchone()
    con.close()
    return render_template('editbook.html',id=r)
#edittrans
@app.route('/edittrans/<string:id>',methods=['GET','POST'])
def edittrans(id):
    con = mysql.connection.cursor()
    con.execute("select * from transaction where t_id=%s;",id)
    r=con.fetchone()
    con.close()
    return render_template('edittrans.html',id=r)
#editissue
@app.route('/editissue/<string:id>',methods=['GET','POST'])
def editissue(id):
    con = mysql.connection.cursor()
    con.execute("select * from issue where is_id=%s;",id)
    r=con.fetchone()
    con.close()
    return render_template('editissue.html',id=r)
#delete user
@app.route('/deleteuser/<string:u_id>',methods=['GET','POST'])
def deleteuser(u_id):
    con = mysql.connection.cursor()
    con.execute("delete from user where u_id=%s;",u_id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for('user'))
#delete book
@app.route('/deletebook/<string:id>',methods=['GET','POST'])
def deletebook(id):
    con = mysql.connection.cursor()
    con.execute("delete from books where b_id=%s;",id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for('book'))
#delete issue
@app.route('/deleteissue/<string:id>',methods=['GET','POST'])
def deleteissue(id):
    con = mysql.connection.cursor()
    con.execute("delete from issue where is_id=%s;",id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for('issue'))
#delete transaction
@app.route('/deletetrans/<string:id>',methods=['GET','POST'])
def deletetrans(id):
    con = mysql.connection.cursor()
    con.execute("delete from transaction where t_id=%s;",id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for('trans'))

#Add user
@app.route('/adduser',methods=['GET','POST'])
def adduser():
    if request.method=="POST":
        id = request.form['uid']
        name = request.form['uname']
        email=request.form['uemail']
        pas=request.form['password']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO user(u_id,uname,email,password) values (%s,%s,%s,%s);",(id,name,email,pas))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('user'))
#Add book
@app.route('/addbook',methods=['GET','POST'])
def addbook():
    if request.method == "POST":
        id = request.form['bid']
        name = request.form['bname']
        author = request.form['author']
        qnt = request.form['quantity']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO books(b_id,bname,author,quantity) values (%s,%s,%s,%s);", (id,name,author,qnt))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('book'))
#Add issue
@app.route('/addissue',methods=['GET','POST'])
def addissue():
    if request.method == "POST":
        id = request.form['iid']
        uname = request.form['uname']
        bname = request.form['bname']
        idate = request.form['idate']
        edate = request.form['edate']
        rdate = request.form['rdate']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO issue(is_id,uname,bname,is_date,ex_date,re_date) values (%s,%s,%s,%s,%s,%s);", (id,uname,bname,idate,edate,rdate))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('issue'))
#Add transaction
@app.route('/addtrans',methods=['GET','POST'])
def addtrans():
    if request.method == "POST":
        id = request.form['tid']
        uname = request.form['uname']
        bname = request.form['bname']
        due = request.form['due']
        sts = request.form['status']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO transaction(t_id,uname,bname,due,status) values (%s,%s,%s,%s,%s);", (id,uname,bname,due,sts))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('trans'))
#update user
@app.route('/updateuser',methods=['GET','POST'])
def updateuser():
    if request.method=="POST":
        id = request.form['uid']
        name = request.form['uname']
        email=request.form['uemail']
        pas=request.form['password']
        con = mysql.connection.cursor()
        con.execute("update user set u_id=%s,uname=%s,email=%s,password=%s where u_id=%s;",(id,name,email,pas,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('user'))
#update book
@app.route('/updatebook',methods=['GET','POST'])
def updatebook():
    if request.method == "POST":
        id = request.form['bid']
        name = request.form['bname']
        author = request.form['author']
        qnt = request.form['quantity']
        con = mysql.connection.cursor()
        con.execute("update books set b_id=%s,bname=%s,author=%s,quantity=%s where b_id=%s;",(id,name,author,qnt,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('book'))
#update issue
@app.route('/updateissue',methods=['GET','POST'])
def updateissue():
    if request.method == "POST":
        id = request.form['iid']
        uname = request.form['uname']
        bname = request.form['bname']
        idate = request.form['idate']
        edate = request.form['edate']
        rdate = request.form['rdate']
        con = mysql.connection.cursor()
        con.execute("update issue set is_id=%s,uname=%s,bname=%s,is_date=%s,ex_date=%s,re_date=%s where is_id=%s;", (id,uname,bname,idate,edate,rdate,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('issue'))
#Update transaction
@app.route('/updatetrans',methods=['GET','POST'])
def updatetrans():
    if request.method == "POST":
        id = request.form['tid']
        uname = request.form['uname']
        bname = request.form['bname']
        due = request.form['due']
        sts = request.form['status']
        con = mysql.connection.cursor()
        con.execute("update transaction set t_id=%s,uname=%s,bname=%s,due=%s,status=%s where t_id=%s;",(id,uname,bname,due,sts,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('trans'))
if __name__=="__main__":
    app.secret_key='hari123'
    app.run(debug=True)