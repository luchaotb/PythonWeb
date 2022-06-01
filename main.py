from flask import Flask, render_template, url_for

main = Flask(__name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/xvii')
def xvii():
    return render_template("xvii.html")

@main.route('/xviii')
def xviii():
    return render_template("xviii.html")

@main.route('/xix')
def xix():
    return render_template("xix.html")

@main.route('/xx')
def xx():
    return render_template("xx.html")

@main.route('/xxi')
def xxi():
    return render_template("xxi.html")


@main.route('/mail')
def mail():
    return render_template("mail.html")


if __name__ == "__main__":
    main.run(debug=True)
