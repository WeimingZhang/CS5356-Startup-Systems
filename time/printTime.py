from flask import Flask
import time
app = Flask(__name__)

@app.route("/")
def printTime():
    ts = time.time()
    return str(int(ts))

if __name__ == "__main__":
    app.run()
