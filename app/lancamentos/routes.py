from os import path
from flask import render_template, redirect, url_for, request, flash, jsonify
from sqlalchemy import extract

from app.lancamentos import lancamento

from ..model import db, lancamentos as Lacamento

from ..lancamentos.serialize import lancamento_schema, lancamentos_schema



@lancamento.route('/index')
def index():
	
	return render_template('lancamentos/index.html', title='Lançamentos')


@lancamento.route('/search', methods=['GET', 'POST'])
def search():
	data = request.get_json()
	mes = str(data[0])
	ano = str(data[1])
	if request.method == 'POST':
		lc = Lacamento.query.filter(extract('month', Lacamento.data_lancamento)== mes).filter(extract('year', Lacamento.data_lancamento) == ano).all()
		retorno = lancamentos_schema.dump(lc)		
		return jsonify(retorno)
	return redirect(url_for('lancamento.index'))