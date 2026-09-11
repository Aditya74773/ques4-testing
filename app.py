from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            message = "Login successful"
        else:
            message = "Invalid username or password"

    return render_template("login.html", message=message)


@app.route("/form", methods=["GET", "POST"])
def form():
    message = ""

    if request.method == "POST":
        name = request.form.get("name")

        if not name:
            message = "Name is required"
        else:
            message = "Form submitted successfully"

    return render_template("form.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)