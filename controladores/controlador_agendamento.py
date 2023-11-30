from flask import render_template, request, redirect
from flask import Blueprint
from classes.agendamento import Agendamento
import conectores.conector_agendamento as conector_agendamento
import conectores.conector_membro as conector_membro
import conectores.conector_atividade as conector_atividade
import conectores.conector_plano as conector_plano


agendamentos_blueprint = Blueprint("agendamentos", __name__)


@agendamentos_blueprint.route("/agendamentos")
def agendamentos_index():
    agendamentos = conector_agendamento.get_all()
    return render_template("agendamentos/index.html", agendamentos = agendamentos, title = "agendamentos")

@agendamentos_blueprint.route("/agendamentos/novo/membro/<id>")
def novo_membro_agendamento(id):
    membro = conector_membro.get_one(id)
    atividades = conector_atividade.get_all_active()
    return render_template("agendamentos/novo-membro.html", membro = membro, atividades = atividades, title = "Novo Agendamento")

@agendamentos_blueprint.route("/agendamentos/novo/atividade/<id>")
def nova_atividade_agendamento(id):
    atividade = conector_atividade.get_one(id)
    membros = conector_membro.get_all_active()
    return render_template("agendamentos/nova-atividade.html", atividade = atividade, membros = membros, title = "Novo Agendamento")

@agendamentos_blueprint.route("/agendamentos/atividade", methods = ["POST"])
def cria_agendamento_from_atividade():
    atividade_id = request.form["atividade"]
    membro_id = request.form["membro"]
    atividade = conector_atividade.get_one(atividade_id)
    membro = conector_membro.get_one(membro_id)
    plano_membro = conector_plano.get_one(membro.tipo_plano.id)
    plano_atividade = conector_plano.get_one(atividade.tipo_plano.id)
    agendamentos_atuais = len(conector_atividade.get_members(atividade_id))
    atividades = conector_atividade.get_all_active()
    
    if conector_agendamento.verifica_agendamento(atividade_id, membro_id) == True:
        error = "Agendamento já criado!"
        return render_template("agendamentos/novo-membro.html", membro = membro, atividades = atividades, title = "Novo Agendamento", error = error)
    
    elif plano_membro.plano == "Mensal" and plano_atividade.plano == "Anual":
        error = "O Plano Deve Ser Anual!"
        return render_template("agendamentos/novo-membro.html", membro = membro, atividades = atividades, title = "Novo Agendamento", error = error)
    
    elif agendamentos_atuais >= atividade.capacidade:
        error = "Atividade Lotada!"
        return render_template("agendamentos/novo-membro.html", membro = membro, atividades = atividades, title = "Novo Agendamento", error = error)
    
    else:
      novo_agendamento = Agendamento( atividade, membro )
      conector_agendamento.new(novo_agendamento)
      pagina_atividade = "/atividades/" + atividade_id
      return redirect (pagina_atividade)


@agendamentos_blueprint.route("/agendamentos/membro", methods=["POST"])
def cria_agendamento_from_membro():
    atividade_id = request.form["atividade"]
    membro_id = request.form["membro"]
    atividade = conector_atividade.get_one(atividade_id)
    membro = conector_membro.get_one(membro_id)
    plano_membro = conector_plano.get_one(membro.tipo_plano.id)
    plano_atividade = conector_plano.get_one(atividade.tipo_plano.id)
    agendamentos_correntes = len(conector_atividade.get_members(atividade_id))
    atividades = conector_atividade.get_all_active()
    
    if conector_agendamento.verifica_agendamento(atividade_id, membro_id) == True:
        error = "Agendamento já criado!"
        return render_template("agendamentos/novo-membro.html", membro = membro, atividades = atividades, title = "Novo Agendamento", error = error)
    
    elif plano_membro.plano == "Mensal" and plano_atividade.plano == "Anual":
        error = "O Plano Deve Ser Anual!"
        return render_template("agendamentos/novo-membro.html", membro = membro, atividades = atividades, title = "Novo Agendamento", error = error)
    
    elif agendamentos_correntes >= atividade.capacidade:
        error = "Atividade Lotada!"
        return render_template("agendamentos/novo-membro.html", membro = membro, atividades = atividades, title = "Novo Agendamento", error = error)
    
    else:
        novo_agendamento = Agendamento( atividade, membro )
        conector_agendamento.new(novo_agendamento)
        pagina_membros = "/membros/" + membro_id
        return redirect (pagina_membros)

@agendamentos_blueprint.route("/agendamentos/<id>/delete")
def deleta_agendamento(id):
    conector_agendamento.delete_one(id)
    return redirect("/agendamentos")

@agendamentos_blueprint.route("/agendamentos/delete/membro/<membro_id>/<atividade_id>")
def deleta_agendamento_membro(membro_id, atividade_id):
    conector_agendamento.delete_agendamento(membro_id, atividade_id)
    pagina_membro = "/membros/" + membro_id
    return redirect (pagina_membro)

@agendamentos_blueprint.route("/agendamentos/delete/atividade/<membro_id>/<atividade_id>")
def deleta_agendamento_atividade(membro_id, atividade_id):
    conector_agendamento.delete_agendamento(membro_id, atividade_id)
    pagina_agendamento = "/atividades/" + atividade_id
    return redirect (pagina_agendamento)



