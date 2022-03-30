from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/create_corto_url', methods=['GET', 'POST'])
def create_corto_url():
    if request.method == 'POST':
        pass
        # print(request.form)
        # piece_count = request.form['piece_count']
        # result = pricer.predict(piece_count)
        # return render_template('predict.html', default=piece_count, title='Result', result=result)
    else:
        pass
        # return render_template('predict.html', default=0, result=0, title='Predict')


if __name__ == "__main__":
    app.run(debug=True)
