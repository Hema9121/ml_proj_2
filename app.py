from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def index():
    return "hema is a good girl, this is her second proj !HURRAY"

if __name__=="__main__":
    app.run(debug=True)