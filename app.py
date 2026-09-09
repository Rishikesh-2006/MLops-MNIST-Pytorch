from flask import Flask,render_template,url_for

app = Flask(__name__)


@app.route('/')
def home():
    css = url_for('static',filename = 'front.css')
    return render_template('front.html',css_path = css)


if __name__ == '__main__':
    app.run()

    