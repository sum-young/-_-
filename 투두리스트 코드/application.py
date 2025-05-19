# from flask import url_for, session, Flask, render_template, request, redirect
# application = Flask(__name__)
# application.secret_key = "Qwer!123!"

# ID = "test"
# PW = "1234"

# @application.route("/")
# def home():
#     if "userID" in session:
#         return render_template("home.html", username = session.get("userID"), login=True)
#     else:
#         return render_template("home.html", login=False)


# @application.route("/login", methods=["get"])
# def login():
#     global ID, PW
#     user_id = request.args.get("loginID")
#     user_pw = request.args.get("loginPW")

#     if ID == user_id and PW == user_pw:
#         session["userID"] = user_id
#         return redirect(url_for("home"))
#     else:
#         return redirect(url_for("home"))


# @application.route("/logout")
# def logout():
#     session.pop("userID")
#     return redirect(url_for("home"))
# application.run(host="0.0.0.0",port=5400)