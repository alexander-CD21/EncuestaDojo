from flask import Flask, render_template, redirect,session,request,flash

app=Flask(__name__)
app.secret_key="secretosecreto"

listaDojo=[]

@app.route('/')
def formulario():
    return render_template("index.html")

@app.route('/registroDojo',methods=['POST'])
def registro():
    Dojo={
        "nombre":request.form["name"],
        "dojo":request.form["dojoLocation"],
        "lenguaje":request.form["language"],
        "comentario":request.form["comment"]
    }

    if len(request.form["name"])<1:
        flash("!CAMPO NOMBRE VACIO!")
        return redirect('/')
    if len(request.form["dojoLocation"])<1:
        flash("!CAMPO DOJO VACIO!")
        return redirect('/')
    if len(request.form["language"])<1:
        flash("CAMPO LENGUAJE VACIO")
        return redirect('/')
    if len(request.form["comment"])<1:
        flash("CAMPO COMENTARIO VACIO")
        return redirect('/')

    listaDojo.append(Dojo)
    return redirect ('/process')

@app.route('/process',methods=['GET'])
def procesamiento():
    for usuario in listaDojo: 

        session["nombre"]= usuario["nombre"]
        session["dojo"]=usuario["dojo"]
        session["lenguaje"]=usuario["lenguaje"]
        session["comentario"]=usuario["comentario"]

    return redirect('/result')

@app.route('/result',methods=['GET'])
def resultados():
    return render_template("result.html")

@app.route('/regresar', methods=['GET'] )
def regresando():
    return redirect ('/')


if __name__=="__main__":
    app.run(debug=True)