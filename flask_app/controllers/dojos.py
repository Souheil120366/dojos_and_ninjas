from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect('/dojos')

@app.route("/dojos")
def dojos_list():
    dojos = Dojo.get_all()
    return render_template("dojos.html",dojos_list=dojos)

@app.route("/dojos/<int:dojo_id>")
def dojo_show(dojo_id):
    dojo_to_show = Dojo.get_dojo_ninjas({'id':dojo_id})
    dojos = Dojo.get_dojo_name({'id':dojo_id})
    
    return render_template("dojo_show.html",ninjas_list_dojo=dojo_to_show,dojo=dojos)

@app.route("/dojos/<int:id>/edit")
def dojo_edit(id):
    dojos = Dojo.get_dojo(id)
    return render_template("edit_dojo.html",dojo=dojos)

@app.route('/dojos/new')
def create_dojo():
    return render_template("dojos.html")

@app.route("/dojos/create",methods=['POST'])
def new_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route("/dojos/<int:id>/update",methods=['POST'])
def update_dojo():
    Dojo.update_dojo(request.form)
    return redirect('/dojos')

@app.route("/delete_dojo/<int:id>")
def delete_dojo(id):
    Dojo.del_dojo(id)
    return redirect('/dojos')