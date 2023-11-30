from database.run_sql import run_sql
from classes.agendamento import Agendamento

def get_all():

    agendamentos = []

    sql = "SELECT * FROM webuser.TB_AGENDAMENTOS"
    results = run_sql(sql)

    for row in results:
        agendamento = Agendamento(row["atividade"], row["membro"], row["id"])
        agendamentos.append(agendamento)

    return agendamentos

def get_one(id):

    sql = "SELECT * FROM webuser.TB_AGENDAMENTOS WHERE id = %s"
    value = [id]

    result = run_sql(sql, value)[0]

    if result is not None:
        agendamento = Agendamento(result["atividade"], result["membro"], result["id"])

    return agendamento

def new(agendamento):

    sql = "INSERT INTO webuser.TB_AGENDAMENTOS ( atividade, membro ) VALUES ( %s, %s) RETURNING *;"
    values = [ agendamento.atividade.id, agendamento.membro.id ]

    results = run_sql(sql, values)
    
    agendamento.id = results[0]["id"]

    return agendamento

def delete_one(id):

    sql = "DELETE FROM webuser.TB_AGENDAMENTOS WHERE id = %s"
    value = [id]

    run_sql(sql, value)

def verifica_agendamento(atividade, membro):
    
    sql = "SELECT * FROM webuser.TB_AGENDAMENTOS WHERE atividade = %s AND membro = %s"
    values = [atividade, membro]
    
    results = run_sql(sql, values)
    
    if len(results) == 0:
        return False
    else:
        return True

def delete_agendamento(membro, atividade):
    
    sql = "DELETE  FROM webuser.TB_AGENDAMENTOS WHERE membro = %s and atividade = %s"
    values = [membro, atividade]
    
    run_sql(sql, values)


    