import os
from flask import Flask, render_template, url_for

template_dir = os.path.abspath('./web')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
