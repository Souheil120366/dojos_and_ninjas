from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def ninjas_list():
    ninjas = Ninja.get_all()
    return render_template("ninjas.html",ninja_list=ninjas)

@app.route("/ninjas/<int:id>")
def ninja_show(id):
    ninjas = Ninja.get_ninja(id)
    return render_template("ninja_show.html",ninja=ninjas)

@app.route("/dojos/<int:id>/edit")
def user_edit(id):
    ninjas = Ninja.get_ninja(id)
    return render_template("edit_ninja.html",ninja=ninjas)

@app.route('/ninjas/new')
def create_ninja():
    dojos = Dojo.get_all()
    return render_template("ninjas.html",dojos_list=dojos)

@app.route("/ninjas/create",methods=['POST'])
def new_ninja():
    print("rquest-form",request.form)
    Ninja.save(request.form)
    return redirect('/dojos')

@app.route("/ninjas/<int:id>/update",methods=['POST'])
def update_ninja():
    Ninja.update_ninja(request.form)
    return redirect('/dojos')

@app.route("/delete_ninja/<int:id>")
def delete_ninja(id):
    Ninja.del_ninja(id)
    return redirect('/dojos')