from os import path

from app import images #para upload de images

from app.pages import pages

from flask import render_template, redirect, url_for, request, flash

from ..model import db, servidores as Servidor
from datetime import datetime as dt

from ..forms.form_servidor import FormServidor
from ..forms.form_photo import FormPhoto


# @pages.route('/')
# @pages.route('/index')
# def index():
# 	return redirect(url_for('pages.home'))

# Exibe uma tela de menu
@pages.route('/', methods=['GET'])
@pages.route('/home', methods=['GET'])
def home():
	return render_template('pages/home.html', title='Início')

# Exibe uma tabela com todos os registros
@pages.route('/servidores', methods=['GET'])
def servidores():
	servidores = Servidor.query.order_by(Servidor.create_at).all()
	return render_template('pages/servidores.html', title="Lista de Servidores", rows=servidores)

# Permite cadastrar novo registro
@pages.route('/novo_servidor', methods=['GET', 'POST'])
def novo_servidor():
	form = FormServidor()	
	if request.method == 'POST':
		if form.validate_on_submit:
			filename = images.save(request.files['photo'])
			url = images.url(filename)	
			# Verifica se o cpf já existe
			cpf = form.cpf.data	
			retorno = Servidor.query.filter_by(cpf=cpf).first()	
			if retorno is not None:
				flash( 'O CPF já está cadastrado.')
				return render_template('pages/novo_servidor.html', title="Cadastro de Servidor", form=form)
			else:	# caso contrário insere no banco de dados			
				servidor = Servidor()
				servidor.nome = form.nome.data
				servidor.cpf  = cpf
				servidor.banco = form.banco.data
				servidor.agencia = form.agencia.data
				servidor.conta = form.conta.data
				servidor.tipoconta = form.tipoconta.data
				servidor.photo = filename
				servidor.photo_url = url
				db.session.add(servidor)
				db.session.commit()
				flash('Novo registro, {}, cadastrado!'.format(servidor.nome), 'sucess')
				return redirect(url_for('pages.servidores'))
		else:
			flash('ERROR! O registro não foi adicionado', 'error')
		
	return render_template('pages/novo_servidor.html', title="Cadastro de Servidor", form=form)

# Exibe a página de edição
# Após a edição, faz a atualização no banco de dados
# Obs. A atualização da foto é feita em separado
@pages.route('/<int:id>/edit/', methods=['GET', 'POST'])
def edit(id):
	row = Servidor.query.filter_by(id=id).first()	
	if row:
		form = FormServidor(request.form, obj=row)
		if request.method == 'POST' and form.validate_on_submit:
			# Atualiza o registro
			updated = Servidor.query.filter_by(id=id).update({
				Servidor.nome : form.nome.data,
				Servidor.cpf  : form.cpf.data,
				Servidor.banco: form.banco.data,
				Servidor.agencia: form.agencia.data,
				Servidor.conta: form.conta.data,
				Servidor.tipoconta: form.tipoconta.data
			})
			
			db.session.commit()
			flash('Registro atualizado!', 'sucess')
			return redirect(url_for('pages.servidores'))
		# Exibe a página de edição
		return render_template('pages/edit.html', form=form, id=row.id)
	else:
		flash('O Registro com ID: #{}, não existe na base de dados.'.format(id), 'error')
		return redirect(url_for('pages.servidores'))


# Deleta o registro selecionado
# Exibe a página de confirmação
# E após confirmado, deleta o registro		
@pages.route('/<int:id>/delete/', methods=['GET', 'POST'])
def delete(id):
	if request.method == 'GET':
		row = Servidor.query.filter_by(id=id).all()
		return render_template('pages/delete.html', rows=row)
	if request.method == 'POST':
		if Servidor.query.filter_by(id=id).first() is not None:
			servidor = Servidor.query.get(id)
			# servidor = Servidor.query.filter_by(id=id).delete() # posso usar dessa forma seguida de um commit
			db.session.delete(servidor) # remover essa linha caso use o modo acima
			db.session.commit()
			flash('Registro {} removido com sucesso!'.format(servidor.nome), 'sucess')
			return redirect(url_for('pages.servidores'))
		else:
			flash('ERROR! O registro não foi removido', 'error')
			return redirect(url_for('pages.servidores'))


@pages.route('/<int:id>/update_photo/', methods=['GET', 'POST'])
def update_photo(id):
	row = Servidor.query.filter_by(id=id).first()
	if row:
		form = FormPhoto(request.form, obj=row)
		if request.method == 'POST' and form.validate_on_submit:
			filename = images.save(request.files['photo'])
			url = images.url(filename)
			updeted = Servidor.query.filter_by(id=id).update({
				Servidor.photo : filename,
				Servidor.photo_url: url
			})	
			db.session.commit()	
			flash('Foto atualizada com sucesso!', 'sucess')	
			return redirect(url_for('pages.servidores'))
		return render_template('pages/update_photo.html', form=form, row=row)
	else:
		flash('O Registro com ID: #{}, não existe na base de dados.'.format(id), 'error')
		return redirect(url_for('pages.servidores'))