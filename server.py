"""Server for movie ratings app."""

from flask import Flask, render_template
import os


app = Flask(__name__)
app.secret_key = "dev"


@app.route("/")
def homepage():
    """View homepage."""
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run()