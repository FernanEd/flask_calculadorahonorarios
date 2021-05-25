from flask import Flask, render_template, redirect, request
from forms import HonorariosForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '98123JKasj123'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HonorariosForm()

    if form.validate_on_submit():
        iva = 0.16
        r_iva = 0.106666
        r_isr = 0.10
        honorarios = form.honorarios.data
        subtotal = honorarios + honorarios * iva
        neto = subtotal - honorarios * r_iva - honorarios * r_isr
        calculos = {
            'iva' : iva,
            'r_iva' : r_iva,
            'r_isr' : r_isr,
            'honorarios' : honorarios,
            'subtotal' : subtotal,
            'neto' : neto
        }
        return render_template('resultado.html', calculos=calculos)

    return render_template('index.html', title='Calcular honorarios', form=form)
