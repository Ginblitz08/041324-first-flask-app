# from flask import Flask                  from here

# app=Flask(__name__)                       basic format:    
# if __name__== "__main__":
#     app.run()                             to here




#@app.route("/", methods=["GET"])                    #-decorator      http://127.0.0.1:5000 in browser
#def hello_world():
#   return "Hello, World!"


# @app.route("/about", methods=["GET"])               #     http://127.0.0.1:5000/about in browser
# def about():
#     return "this app is created by Gino"


# @app.route("/contact",methods=["GET"])              #     http://127.0.0.1:5000/contact in browser
# def contact():
#     return "this is the contact page"







from flask import Flask, render_template

app=Flask(__name__)

@app.route("/", methods=["GET"])                    #-decorator      http://127.0.0.1:5000 in browser
def hello_world():
    html="""
    <html>
        <head>
            <title>Hello, World!</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This app is written using Flask</p>
        </body>
    </html>
    """
    return html

@app.route("/about", methods=["GET"])             
def about():
    return render_template("about.html")

@app.route("/contact",methods=["GET"])              
def contact():
    return render_template("contacts.html")

@app.route("/market-home", methods=["GET"])
def market_home():
    return render_template("market-home.html")

@app.route("/market-about", methods=["GET"])
def market_about():
    return render_template("market-about.html")

@app.route("/market-contact", methods=["GET"])
def market_contact():
    return render_template("market-contact.html")


if __name__== "__main__":
    app.run()




