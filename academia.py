from flask import Flask, render_template
from controladores.controlador_membro import membros_blueprint
from controladores.controlador_instrutor import instrutores_blueprint
from controladores.controlador_atividade import atividades_blueprint
from controladores.controlador_agendamento import agendamentos_blueprint

app = Flask(__name__)

app.register_blueprint(membros_blueprint)
app.register_blueprint(instrutores_blueprint)
app.register_blueprint(atividades_blueprint)
app.register_blueprint(agendamentos_blueprint)

@app.route("/", methods=["Get"])
def home():
    return render_template("index.html", title = "Home")

if __name__ == "__main__":
    app.run(debug = True)
