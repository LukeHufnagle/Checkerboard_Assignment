from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", num = 4)

@app.route('/<int:num>')
def change_size(num):
    return render_template("index.html", num=num)

if __name__=="__main__":
    app.run(debug=True)