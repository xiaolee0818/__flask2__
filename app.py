from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    
    data = {"key1": '''Download ready-to-use compiled code for Bootstrap v5.3.0-alpha3 to easily drop into your project, which includes:

            Compiled and minified CSS bundles(see CSS files comparison)
            Compiled and minified JavaScript plugins(see JS files comparison''', "key2": '''Expressions
            Jinja allows basic expressions everywhere. These work very similarly to regular Python
            even if you’re not working with Python you should feel comfortable with it.''', "key3": ''' On this page
            如何運作
            範例
            僅有幻燈片
            包含控制項
            包含指示器
            包含字幕
            淡入淡出
            個別設置 .carousel-item 的時間間隔
            禁用觸控滑動
            Dark variant
            Custom transition
            Sass
            Variables
            Usage
            透過資料屬性
            透過 JavaScript
            選項
            方法
            事件'''}
    # for item in data.items():
    # print(item)

    return render_template("index.jinja.html", content_data=data)


@app.route("/features/")
def features():
    
    return render_template("features.jinja.html")


@app.route("/priceing/")
def learining():
    
    return render_template("priceing.jinja.html")


@app.route("/about/")
def about():
    
    return render_template("about.jinja.html")
