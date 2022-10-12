from flask import Flask

app = Flask(__name__)

serverName = "PyQuickApache"
errors = ['The server\'s homepage (index.html) was not found. If you are the developer of this site, make sure index.html is in the "static" folder.', 'The requested page couldn\'t be found.']

@app.route('/')
def index():
    try:
        f = open("static/index.html", 'r')
        return str(f.read())
    except Exception as e:
        return f"<h1> {serverName} </h1> {errors[0]} <br> ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ <br> <i>Error Code 0</i> <br> <i>Returned by server: {e}"

@app.route('/<requestedPage>')
def returnPage(requestedPage):
    try:
        f = open(f"static/{requestedPage}", 'r')
        return str(f.read())
    except Exception as e:
        return f"<h1> {serverName} </h1> {errors[1]} <br> ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ <br> <i>Error Code 1</i> <br> <i>Returned by server: {e}"

if __name__ == "__main__":
    app.run(
        debug=True,
        port=80
    )