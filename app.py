from flask import Flask, render_template, redirect, request
from forms import HonorariosForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '98123JKasj123'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HonorariosForm()

    if form.validate_on_submit():
        return render_template('resultado.html')

    return render_template('index.html', title='Calcular honorarios', form=form)
