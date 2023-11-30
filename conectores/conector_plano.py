from classes.plano import TipoPlano
from database.run_sql import run_sql

def get_all():

    tipos_planos = []

    sql = "SELECT * FROM public.tb_planos"
    results = run_sql(sql)

    for row in results:
        tipo_plano = TipoPlano(row["plano"], row["id"])
        tipos_planos.append(tipo_plano)

    return tipos_planos

def get_one(id):
    
    sql = "SELECT * FROM public.tb_planos WHERE id = %s"
    value = [id]
    
    result = run_sql(sql, value)[0]

    if result is not None:
        tipodoplano = TipoPlano(result["plano"], result["id"])

    return tipodoplano

def new(tipodoplano):
    
    sql = "INSERT INTO public.tb_planos ( plano ) VALUES ( %s ) RETURNING *;"
    values = [tipodoplano.plano]
    
    results = run_sql(sql, values)
    
    tipodoplano.id = results[0]["id"]

    return tipodoplano

def delete_one(id):
    
    sql = "DELETE FROM public.tb_planos WHERE id = %s"
    value = [id]
    
    run_sql(sql, value)

def edit(tipodoplano):
    
    sql = "UPDATE public.tb_planos SET (plano) = (%s) WHERE id = %s;"
    values = [tipodoplano.plano, tipodoplano.id]

    run_sql(sql, values)


