from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = 'user cr'

@app.route('/')
def index():
    return "I work for now!"

if __name__ == "__main__":
    app.run(debug=True)