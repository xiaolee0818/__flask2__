from flask import Flask,render_template
import pandas_datareader.data as pdr
import yfinance as yf
import datasource



app = Flask(__name__)
@app.route("/")
def index():
    stock_data=datasource.get_stock_data(stock_id=2330)
    return render_template("index.jinja.html",data=stock_data)


@app.route("/features/")
def features():
    
    return render_template("features.jinja.html")

@app.route("/priceing/")
def priceing():
    
    return render_template("priceing.jinja.html")

@app.route("/about/")
def about():
    return render_template("about.jinja.html")
