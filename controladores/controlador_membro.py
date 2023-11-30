from flask import render_template, request, redirect
from flask import Blueprint
from classes.membro import Membro
import conectores.conector_membro as conector_membro
import conectores.conector_plano as conector_plano


membros_blueprint = Blueprint("membros", __name__)


@membros_blueprint.route("/membros")
def membros_index():
    membros = conector_membro.get_all_active()
    return render_template("membros/index.html", membros = membros, title = "Membros")

@membros_blueprint.route("/membros/inativo")
def membros_inativos():
    membros = conector_membro.get_all_inactive()
    return render_template("membros/index.html", membros = membros, title = "Membros")

@membros_blueprint.route("/membros/novo")
def novo_membro():
    tipos_planos = conector_plano.get_all()
    return render_template("membros/novo.html", tipos_planos = tipos_planos, title = "Novo Membro")

@membros_blueprint.route("/membros", methods = ["POST"])
def cadastra_membro():
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    data_nascimento = request.form["data_nascimento"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    endereco = request.form["endereco"]
    tipodoplano = request.form["tipodoplano"]
    data_inicio = request.form["data_inicio"]
    ativo = request.form["ativo"]
    plano = conector_plano.get_one(tipodoplano)
    novo_membro = Membro(nome, sobrenome, data_nascimento, endereco, telefone, email, plano, data_inicio, ativo)
    conector_membro.new(novo_membro)
    return redirect("/membros")

@membros_blueprint.route("/membros/<id>/edit")
def edita_membro(id):
    membro = conector_membro.get_one(id)
    tipos_planos = conector_plano.get_all()
    return render_template("/membros/editar.html", membro = membro, tipos_planos = tipos_planos, title = "Editar Detalhes do Membro")

@membros_blueprint.route("/membros/<id>", methods=["POST"])
def atualiza_membro(id):
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    data_nascimento = request.form["data_nascimento"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    endereco = request.form["endereco"]
    tipodoplano = request.form["tipodoplano"]
    data_inicio = request.form["data_inicio"]
    ativo = request.form["ativo"]
    plano = conector_plano.get_one(tipodoplano)
    membro_atualizado = Membro(nome, sobrenome, data_nascimento, endereco, telefone, email, plano, data_inicio, ativo, id)
    conector_membro.edit(membro_atualizado)
    return redirect("/membros")

@membros_blueprint.route("/membros/<id>")
def mostra_detalhes(id):
    membro = conector_membro.get_one(id)
    atividades_agendadas = conector_membro.get_activities(id)
    tipo_plano = conector_plano.get_one(membro.tipo_plano.id)
    return render_template("/membros/mostrar.html", membro = membro, tipo_plano = tipo_plano, atividades_agendadas = atividades_agendadas, title = "Mostrar Detalhes")

@membros_blueprint.route("/membros/<id>/delete")
def deleta_membro(id):
    conector_membro.delete_one(id)
    return redirect("/membros")