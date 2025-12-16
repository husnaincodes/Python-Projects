
from flask import Flask, request,redirect,url_for,session,Response,flash,get_flashed_messages
app = Flask(__name__)
app.secret_key = "supersecret"
# home login page
@app.route("/",methods =["GET" ,"POST"] )
def login():
    if request.method =="POST":
        username = request.form.get("username")

        password = request.form.get("password")

        if username == "admin" and password == "1234":

            session["user"] = username
            flash("Login successful!", "success")
            return redirect(url_for("welcome"))
   
        else:
    
            return Response("In valid . Try again!", mimetype="text/plain")
    messages = get_flashed_messages(with_categories=True)
    msg_html = "".join([f"<p style='color:red;'>{m[1]}</p>" if m[0] == "error" 
                        else f"<p style='color:green;'>{m[1]}</p>" for m in messages])

    return    """
            <h2>Login page</h2>
            <form method = "POST">
            Username :<input type= "text" name = "username"><br>
            Password :<input type = "password" name = "password"><br>
            <input  type ="submit" value = "Login" >
            </form>

"""

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
        <h2>Welcome,{session["user"]}!</h2>
        
        <a href="{url_for('logout')}">Logout</a>
        """
    return redirect(url_for("login"))


#logout
@app.route("/logout")
def logout():
    session.pop("user",None)
    flash("You have been logged out successfully.", "success")
    return redirect(url_for("login"))
if __name__ == "__main__":

    app.run(debug=True)














