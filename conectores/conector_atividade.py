from unittest import result

import conectores.conector_plano as plano
from database.run_sql import run_sql
from classes.atividade import Atividade
from classes.membro import Membro


def get_all():
    atividades = []

    sql = "SELECT * FROM public.tb_atividades"
    results = run_sql(sql)

    for row in results:
        tipo_plano = plano.get_one(row["tipo_plano"])

        atividade = Atividade(result["nome"],
                              result["instrutor"],
                              result["data"],
                              result["duracao"],
                              result["capacidade"],
                              result["tipodoplano"],
                              result["ativo"],
                              result["id"])

        atividades.append(atividade)

    return atividades

def get_members(id):
    membros = []

    sql = "SELECT webuser.TB_MEMBROS.* FROM webuser.TB_MEMBROS INNER JOIN webuser.TB_AGENDAMENTOS ON membros.id = webuser.TB_AGENDAMENTOS.membro WHERE webuser.TB_AGENDAMENTOS.atividade = %s"
    value = [id]

    results = run_sql(sql, value)

    for row in results:
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["telefone"],
                        row["email"],
                        row["tipodoplano"],
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])

        membros.append(membro)

    return membros

def get_all_active():
    atividades = []

    sql = "SELECT * FROM public.tb_atividades WHERE ativo = true ORDER BY data ASC"
    results = run_sql(sql)

    for row in results:
        tipodoplano = plano.get_one(row["tipodoplano"])

        atividade = Atividade(row["nome"],
                              row["instrutor"],
                              row["data"],
                              row["duracao"],
                              row["capacidade"],
                              row["tipodoplano"],
                              row["ativo"],
                              row["id"])

        atividades.append(atividade)

    return atividades
def get_all_inactive():
    atividades = []

    sql = "SELECT * FROM public.tb_atividades WHERE ativo = false ORDER BY data ASC"
    results = run_sql(sql)

    for row in results:
        tipodoplano = plano.get_one(row["tipodoplano"])

        atividade = Atividade(result["nome"],
                              result["instrutor"],
                              result["data"],
                              result["duracao"],
                              result["capacidade"],
                              result["tipodoplano"],
                              result["ativo"],
                              result["id"])

        atividades.append(atividade)

    return atividades

def get_one(id):
    sql = "SELECT * FROM public.tb_atividades WHERE ativo = true AND id = %s"
    value = [id]

    result = run_sql(sql, value)[0]

    if result is not None:
        tipodoplano = plano.get_one(result["tipodoplano"])

        atividade = Atividade(result["nome"],
                              result["instrutor"],
                              result["data"],
                              result["duracao"],
                              result["capacidade"],
                              result["tipodoplano"],
                              result["ativo"],
                              result["id"])

    return atividade

def new(atividade):
    sql = "INSERT INTO public.tb_atividades( nome, instrutor, data, duracao, capacidade, tipo_plano, ativo ) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *;"
    values = [atividade.nome, atividade.instrutor, atividade.data, atividade.duracao, atividade.capacidade,
              atividade.tipo_plano, atividade.ativo]

    results = run_sql(sql, values)

    atividade.id = results[0]["id"]

    return atividade

def delete_one(id):
    sql = "DELETE FROM public.tb_atividades WHERE id = %s"
    value = [id]

    run_sql(sql, value)

def edit(atividade):
    sql = "UPDATE public.tb_atividades SET ( nome, instrutor, data, duracao, capacidade, tipo_plano, ativo ) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s;"
    values = [atividade.nome, atividade.instrutor, atividade.data, atividade.duracao, atividade.capacidade,
              atividade.tipo_plano, atividade.ativo]

    run_sql(sql, values)
