from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

app = Flask(__name__)
app.secret_key = "RRA_CYBER_SECRET_2026"

# ================= SPLASH =================
@app.route("/")
def splash():
    return render_template("splash.html")

# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin":
            session["user"] = "admin"
            return redirect("/dashboard")
        return render_template("login.html", error="Login incorrect")

    return render_template("login.html")

# ================= DASHBOARD =================
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    stats = {
        "tax_systems": 45,
        "customs_operations": 120,
        "employees": 350,
        "cyber_incidents": 7
    }
    return render_template("dashboard.html", stats=stats)

# ================= PAGES =================
@app.route("/presentation")
def presentation(): return render_template("presentation.html")

@app.route("/cartographie")
def cartographie(): return render_template("cartographie.html")

@app.route("/inventaire")
def inventaire(): return render_template("inventaire.html")

@app.route("/risques")
def risques():
    data = {
        "Threat": ["Ransomware", "Phishing", "Insider Abuse"],
        "Impact": [5, 4, 3],
        "Probability": [4, 3, 2]
    }
    df = pd.DataFrame(data)
    df["Risk Score"] = df["Impact"] * df["Probability"]
    return render_template("risques.html", tables=df.to_html(classes="table table-dark table-striped"))

@app.route("/simulation")
def simulation(): return render_template("simulation.html")

@app.route("/gouvernance")
def gouvernance(): return render_template("gouvernance.html")

# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)