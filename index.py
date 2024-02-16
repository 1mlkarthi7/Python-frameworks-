from flask import Flask
helloworld=Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\":\"This is python flask app\"}"
if __name__=="__main__":
    helloworld.run(host="0.0.0.0",port=int("3000"),debug=True)