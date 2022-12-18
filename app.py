from flask import Flask, render_template
import pandas as pd

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
   df = pd.read_csv("data.csv")
   return render_template("index.html", data=df.to_html())

if __name__ == '__main__':
   app.run()
