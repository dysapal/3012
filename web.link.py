from flask import Flask
import random

app = Flask(__name__)
dato1 = "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos"
dato2= "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna"
dato3= "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo"
facts_list=[dato1,dato2,dato3]

@app.route("/")

def hello_world():
    return '<h1>hola esta es una pagina de datos aleatorios</h1><br> <a href="/random_fact">¡Ver un dato aleatorio!</a><h2 href="/password">¿deseas una contraseña?</h2>'

@app.route("/random_fact")
def route():
    return f'<p>{random.choice(facts_list)}</p>'
letras = "ABCDEFGHIJKLMNOPQRVXZTW/&%$#"
password = ""
for i in range(8):
    x =random.choice(letras)
    password += x 
@app.route("/password")
 
def password():
    return f'<p>{password}</p>'
app.run(debug=True)
