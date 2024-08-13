from flask import Flask,render_template,url_for,redirect,request,flash,session
from flask_mysqldb import MySQL


app=Flask(__name__)
app.secret_key="123"

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="venkat"
app.config["MYSQL_DB"]="registeration"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

@app.route("/")
@app.route("/home",methods=["POST","GET"])
def home():
    if 'signin' in request.form:
        if request.method=="POST":
            name=request.form["uname"]
            email=request.form["uemail"]
            age=request.form["uage"]
            contact=request.form["ucontact"]
            password=request.form["upass"]
            cur=mysql.connection.cursor()
            cur.execute("insert into sigin (name,email,age,contact_number,password) values (%s,%s,%s,%s,%s)",[name,email,age,contact,password])
            mysql.connection.commit()
            cur.close()
            flash("Successfully Registeration")
        return render_template("base.html")
    elif "userlogin" in request.form:
        if request.method=="POST":
            email=request.form["uemail"]
            password=request.form["upass"]
            try:
                cur=mysql.connection.cursor()
                cur.execute("select * from sigin where email=%s and password=%s",[email,password])
                res=cur.fetchone()
                if res:
                    session["email"]=res["email"]
                    session["password"]=res["password"]
                    return redirect(url_for("doctorvisit")) #login move in html page change 
                else:
                    flash("Invalid email and password ")
                    return render_template("base.html")
            except Exception as e:
                print(e)
            finally:
                mysql.connection.commit()
                cur.close()
    return render_template("base.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():                 
    session.clear()
    return render_template("base.html")

@app.route("/doctorvisit")
def doctorvisit():
    return render_template("doctorvisit.html")

@app.route("/gc")
def gc():
    return render_template("gc.html")

@app.route("/skin")
def skin():
    return render_template("skin.html")

@app.route("/eye")
def eye():
    return render_template("eye.html")

@app.route("/cardio")
def cardio():
    return render_template("cardio.html")

@app.route("/dashbord")
def dashbord():
    return render_template("dashbord.html")

@app.route("/meeting")
def meeting():
    return render_template("meeting.html",username=session["email"])

@app.route("/join",methods=["POST","GET"])
def join():
    if request.method=="POST":
        room_id=request.form.get("roomID")
        return redirect(f"/meeting?roomID=(room_id)")
    return render_template("join.html")

if __name__=="__main__":
    app.run(debug=True)




