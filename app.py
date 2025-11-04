from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError

from models import local_secao, Ingredientes, Receita
from sqlalchemy import select

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def home():
    return redirect('/index')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/receita')
def get_receitas():
    db_session = local_secao()
    try:
        receitas = select(Receita)
        result = db_session.execute(receitas).scalars()
        return render_template('site_receita.html', receitas=result)
    except SQLAlchemyError as e:
        print(f'Erro: {e}')
    except Exception as e:
        print(f'Erro ao consultar Receitas: {e}')
    finally:
        db_session.close()


@app.route('/ingredientes')
def get_ingredientes():
    db_session = local_secao()
    try:
        ingrediente = select(Ingredientes)
        result = db_session.execute(ingrediente).scalars()
        return render_template('site_receita4.html', ingredientes=result)
    except SQLAlchemyError as e:
        print(f'Erro: {e}')
    except Exception as e:
        print(f'Erro ao consultar Ingredientes: {e}')
    finally:
        db_session.close()


if __name__ == '__main__':
    app.run(debug=True)
