from flask import Flask, render_template
import pandas as pd

app = Flask(__name__,template_folder='')


#df = pd.read_csv("data.csv")
#df=df[['web_name','now_cost','first_name']]

@app.route('/')
def home():
   dataframes = []
   for i in range(1, 3):
       df = pd.read_csv(f"data{i}.csv")
       df2=df.to_html()
       dataframes.append(df.to_html())
   return render_template("index.html", data=dataframes)


if __name__ == '__main__':
   app.run()
