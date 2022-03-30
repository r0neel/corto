from flask import Flask, render_template, request, redirect


app = Flask(__name__)  # noqa: E402

urls = {"abc", "cde"}  # noqa: E402

from random import choice  # noqa: E402
import string  # noqa: E402


def generate_short_id(num_of_chars: int):
    # """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/corto', methods=['GET', 'POST'])
def create_corto():
    if request.method == 'POST':
        corto_id = generate_short_id(8)
        fname = request.form.get("full-url")
        to_print = "corto/" + corto_id
        print(f"hello I have been posted {corto_id}")
        # print(request.form)
        # piece_count = request.form['piece_count']
        # result = pricer.predict(piece_count)
        return render_template('home.html', new_corto_url=to_print)
    else:
        pass
        # return render_template('predict.html', default=0, result=0, title='Predict')


@app.route('/corto/<string_id>', methods=['GET', 'POST'])
def corto_url(string_id):
    if request.method == 'GET':
        if string_id in urls:
            return redirect("http://www.example.com", code=302)
        else:
            return redirect("/", code=302)


@app.errorhandler(404)
def page_not_found(err):
    return render_template('errors/404.html'), 404


# @app.errorhandler(405)
# def metod_not_allowed(err):
#     return render_template('errors/405.html'), 405


# @app.errorhandler(500)
# def internal_server_error(err):
#     return render_template('errors/500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
