# from flask import Flask

# app=Flask(__name__)
# if __name__== "__main__":
#     app.run()


from flask import Flask

app=Flask(__name__)

@app.route("/", methods=["GET"])                    #-decorator
def hello_world():
    return "Hello, World!"

if __name__== "__main__":
    app.run()