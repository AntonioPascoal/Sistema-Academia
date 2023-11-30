from flask import  render_template, request, redirect
from flask import Blueprint
from classes.atividade import Atividade
import conectores.conector_atividade as conector_atividade
import conectores.conector_instrutor as conector_instrutor
import conectores.conector_plano as conector_plano

atividades_blueprint = Blueprint("atividades", __name__)


@atividades_blueprint.route("/atividades")
def atividades_index():
    atividades = conector_atividade.get_all_active()
    return render_template("atividades/index.html", atividades = atividades, title = "atividades")

@atividades_blueprint.route("/atividades/inativo")
def inactive_atividades():
    atividades = conector_atividade.get_all_inactive()
    return render_template("atividades/index.html", atividades = atividades, title = "atividades")

@atividades_blueprint.route("/atividades/novo")
def nova_atividade():
    instrutores = conector_instrutor.get_all()
    tipos_planos = conector_plano.get_all()
    return render_template("atividades/novo.html", instrutores = instrutores, tipos_planos = tipos_planos, title = "Nova Atividade")

@atividades_blueprint.route("/atividades", methods = ["POST"])
def cadastra_atividade():
    nome = request.form["nome"]
    instrutor = request.form["instrutor"]
    data = request.form["data"]
    duracao = request.form["duracao"]
    capacidade = request.form["capacidade"]
    tipodoplano = request.form["tipo_plano"]
    ativo = request.form["ativo"]
    plano = conector_plano.get_one(tipodoplano)
    instrutor = conector_instrutor.get_one(instrutor)
    nova_atividade = Atividade(nome, instrutor, data, duracao, capacidade, plano, ativo)
    conector_atividade.new(nova_atividade)
    return redirect("/atividades")


@atividades_blueprint.route("/atividades/<id>/edit")
def edita_atividade(id):
    instrutores = conector_instrutor.get_all()
    tipos_planos = conector_plano.get_all()
    atividade = conector_atividade.get_one(id)
    instrutor = conector_instrutor.get_one(atividade.instrutor)
    plano = conector_plano.get_one(atividade.tipo_plano.id)
    return render_template("/atividades/editar.html", 
        atividade = atividade, 
        instrutor = instrutor, 
        plano = plano, 
        instrutores = instrutores, 
        tipos_planos = tipos_planos, 
        title = "Editar Detalhes da Atividade")


@atividades_blueprint.route("/atividades/<id>", methods = ["POST"])
def atualiza_atividade(id):
    nome = request.form["nome"]
    instrutor = request.form["instrutor"]
    data = request.form["data"]
    duracao = request.form["duracao"]
    capacidade = request.form["capacidade"]
    tipodoplano = request.form["tipo_plano"]
    ativo = request.form["ativo"]
    plano = conector_plano.get_one(tipodoplano)
    instrutor = conector_instrutor.get_one(instrutor)
    atualiza_atividade = Atividade(nome, instrutor, data, duracao, capacidade, plano, ativo, id)
    conector_atividade.edit(atualiza_atividade)
    return redirect("/atividades")

@atividades_blueprint.route("/atividades/<id>")
def mostra_detalhes(id):
    atividade = conector_atividade.get_one(id)
    tipodoplano = conector_plano.get_one(atividade.tipo_plano.id)
    membros_atividades = conector_atividade.get_members(id)
    no_members_booked = len(membros_atividades)
    instrutor = conector_instrutor.get_one(atividade.instrutor)
    return render_template("/atividades/mostrar.html", 
        atividade = atividade, 
        instrutor = instrutor, 
        membros_atividades = membros_atividades, 
        no_members_booked = no_members_booked, 
        tipodoplano = tipodoplano,
        title = "Detalhes da Atividade")

@atividades_blueprint.route("/atividades/<id>/delete")
def delet_actividade(id):
    conector_atividade.delete_one(id)
    return redirect("/atividades")



    