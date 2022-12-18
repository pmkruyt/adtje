from flask import Flask, render_template
import pandas as pd

app = Flask(__name__,template_folder='')


df = pd.read_csv("data.csv")
df=df[['web_name','now_cost','first_name']]

@app.route('/')
def home():
   
   return render_template("index.html", data=df.to_html())

if __name__ == '__main__':
   app.run()
