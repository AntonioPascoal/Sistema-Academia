from database.run_sql import run_sql
from classes.instrutor import Instrutor
from classes.atividade import Atividade

def get_all():

    instrutores = []

    sql = "SELECT * FROM public.tb_instrutores"
    results = run_sql(sql)

    for row in results:

        instrutor = Instrutor(row["nome"],
                              row["sobrenome"],
                              row["data_nascimento"],
                              row["endereco"],
                              row["numero"],
                              row["id"])

        instrutores.append(instrutor)

    return instrutores

def get_one(id):
    
    sql = "SELECT * FROM public.tb_instrutores WHERE id = %s"
    value = [id]
    
    result = run_sql(sql, value)[0]

    if result is not None:
        instrutor = Instrutor(result["nome"],
                              result["sobrenome"],
                              result["data_nascimento"],
                              result["endereco"],
                              result["numero"],
                              result["id"])
    return instrutor

def get_activities(instructor_id):
    
    atividades = []

    sql = "SELECT * FROM webuser.TB_ATIVIDADES WHERE instrutor = %s"
    value = [instructor_id]

    results = run_sql(sql, value)

    for row in results:
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

def new(instrutor):
    
    sql = "INSERT INTO public.tb_instrutores( nome, sobrenome, data_nascimento, endereco, telefone ) VALUES ( %s, %s, %s, %s, %s ) RETURNING *;"
    values = [instrutor.nome, instrutor.sobrenome, instrutor.data_nascimento, instrutor.endereco, instrutor.telefone]
    
    results = run_sql(sql, values)
    
    instrutor.id = results[0]["id"]
    
    return instrutor

def delete_one(id):
    
    sql = "DELETE FROM public.tb_instrutores WHERE id = %s"
    value = [id]
    
    run_sql(sql, value)

def edit(instrutor):
    
    sql = "UPDATE public.tb_instrutores SET ( nome, sobrenome, data_nascimento, endereco, telefone ) = (%s, %s, %s, %s, %s) WHERE id = %s;"
    values = [instrutor.nome, instrutor.sobrenome, instrutor.data_nascimento, instrutor.endereco, instrutor.telefone, instrutor.id]
    
    run_sql(sql, values)



