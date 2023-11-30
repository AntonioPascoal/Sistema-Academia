import conectores.conector_plano as plano
from database.run_sql import run_sql
from classes.membro import Membro
from classes.atividade import Atividade

def get_all():

    membros = []

    sql = "SELECT * FROM public.tb_membros ORDER BY nome ASC"
    results = run_sql(sql)

    for row in results:
        
        tipodoplano = plano.get_one(row["tipodoplano"])
        
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["numero"],
                        row["email"],
                        row["tipodoplano"],
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])

        membros.append(membro)

    return membros


def get_one(id):

    sql = "SELECT * FROM public.tb_membros WHERE id = %s"
    value = [id]
    
    result = run_sql(sql, value)[0]

    if result is not None:

        tipodoplano = plano.get_one(result["tipodoplano"])
        
        membro = Membro(result["nome"],
                        result["sobrenome"],
                        result["data_nascimento"],
                        result["endereco"],
                        result["numero"],
                        result["email"],
                        result["tipodoplano"],
                        result["data_inicio"],
                        result["ativo"],
                        result["id"])

    return membro

def get_activities(user_id):

    atividades = []

    sql = "SELECT webuser.TB_ATIVIDADES.* FROM webuser.TB_ATIVIDADES INNER JOIN webuser.TB_AGENDAMENTOS on webuser.TB_ATIVIDADES.id = webuser.TB_AGENDAMENTOS.atividade where webuser.TB_AGENDAMENTOS.membro = %s"
    value = [user_id]
    
    results = run_sql(sql, value)

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

def get_all_active():

    membros = []

    sql = "SELECT * FROM public.tb_membros where ativo = true ORDER BY nome ASC"
    results = run_sql(sql)

    for row in results:
        
        tipodoplano = plano.get_one(row["tipodoplano"])
        
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["numero"],
                        row["email"],
                        row["tipodoplano"],
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])

        membros.append(membro)

    return membros

def get_all_inactive():

    membros = []

    sql = "SELECT * FROM public.tb_membros where ativo = false ORDER BY nome ASC"
    results = run_sql(sql)

    for row in results:
        
        tipodoplano = plano.get_one(row["tipodoplano"])
        
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["numero"],
                        row["email"],
                        row["tipodoplano"],
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])

        membros.append(membro)

    return membros

def new(membro):
    sql = "INSERT INTO public.tb_membros( nome, sobrenome, data_nascimento, endereco, telefone, email, tipo_plano, data_inicio, ativo ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s ) RETURNING *;"
    values = [membro.nome, membro.sobrenome, membro.data_nascimento, membro.endereco, membro.telefone, membro.email, membro.tipo_plano.id, membro.data_inicio, membro.ativo]
    results = run_sql(sql, values)
    membro.id = results[0]["id"]
    
    return membro

def delete_one(id):
    sql = "DELETE FROM public.tb_membros WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def edit(membro):
    
    sql = "UPDATE public.tb_membros SET ( nome, sobrenome, data_nascimento, endereco, telefone, email, tipo_plano, data_inicio, ativo ) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s;"
    values = [membro.nome, membro.sobrenome, membro.data_nascimento, membro.endereco, membro.telefone, membro.email, membro.tipo_plano.id, membro.data_inicio, membro.ativo, membro.id]

    run_sql(sql, values)

    
