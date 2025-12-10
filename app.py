from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    
    # Example using SMTP (Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "yourgmail@gmail.com"
    smtp_pass = "your-app-password"

    email_message = f"From: {name} <{email}>\n\n{message}"

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(email, smtp_user, email_message)
    server.quit()
    
    return redirect("/?sent=true")

if __name__ == "__main__":
    app.run(debug=True)
