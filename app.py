from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitprot/inicio.html')

@app.route('/contenido')
def contenido():
    return render_template('sitprot/contenido.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitprot/nosotros.html')

@app.route('/ofrecemos')
def ofrecemos():
    return render_template('sitprot/ofrecemos.html')
    
if __name__ =='__main__':
    app.run(debug=True)