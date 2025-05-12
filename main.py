import os
from flask import Flask

app = Flask(__name__)

# @app.route("/") hangi path kullanılacaksa o eklenir.
@app.route("/file")
def hello():
    return "Hello World from alperenokur.com/file"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use Cloud Run's expected port
    app.run(host="0.0.0.0", port=port)
