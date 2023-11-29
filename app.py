from flask import Flask, render_template
from bd import motores

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("produtos.html")

def obter_motor_por_id(motor_id):
    for motor in motores:
        if motor['id'] == motor_id:
            return motor
    return None

@app.route("/motor/<int:motor_id>")
def exibir_motor(motor_id):
    motor = obter_motor_por_id(motor_id)
    return render_template("motor.html", motor=motor)

if __name__ == "__main__":
    app.run(debug=True)