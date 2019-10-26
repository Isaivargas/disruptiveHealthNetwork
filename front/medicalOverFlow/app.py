from flask import Flask,render_template
# import flask
app1 = Flask(__name__)             # create an app instance



@app1.route("/")                   # at the end point /
def hello():
    return render_template("index.html")  # which returns "hello world"




if __name__ == "__main__":        # on running python app.py
    app1.run(host='127.0.0.1', port=8080, debug=True)                  # run the flask app
