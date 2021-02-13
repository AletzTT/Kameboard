from flask import render_template, redirect, url_for, request, flash, abort, jsonify
from flask_login import login_required, current_user
from . import admin_bp
from .models import Project, CollaboratorProject
from .forms import NewProjectForm
from coreapp.auth.decorators import admin_required, owner_required
from coreapp.auth.models import User
from datetime import date

@admin_bp.route('/dashboard/')
@login_required
def dashboard():
    img = url_for('static', filename='img/person.svg')
    l = jsonify({"mouse" : 300, "keyboard": 200, "pc" : 2500})
    return render_template('admin/dashboard.html', user_img=img, l= l)

@admin_bp.route('/collaborators/')
@login_required
def collaborators():
    collabs = User.query.order_by('username')
    return render_template('admin/collaborators.html', collabs=collabs)

@admin_bp.route('/projects/')
@login_required
def projects():
    collab=[]
    for c in current_user.collaborations:
        if c.project.author is not User.get_by_id(current_user.id):
            collab.append(c.project)
    return render_template('admin/projects.html', collab=collab)

@admin_bp.route('/projects/new', methods=['GET','POST'])
@login_required
@admin_required
def show_new_project_form():
    form = NewProjectForm()
    #Cargar Usuarios al Select
    form.collaborators.choices = [(c.id, c.username+' - '+c.email) for c in User.query.filter(User.id != current_user.id).order_by('username')]
    if form.validate_on_submit():
        project = Project(title=form.title.data,
            description=form.description.data,
            public=form.public.data)
        project.author_id = current_user.id
        project.creation_date = date.today()
        project.limit_date = form.limit_date.data
        project.color = request.form['color']
        #Añadir Administrador
        admin = CollaboratorProject(add_task=True,
            delete_task=True,
            done_task=True,
            store_task=True,
            add_collaborator=True,
            delete_collaborator=True,
            update_charges=True)
        admin.collaborator = current_user
        project.collaborators.append(admin)
        #Añadir Colaboradores
        for c in form.collaborators.data:
            collab = CollaboratorProject()
            collab.collaborator = User.get_by_id(c)
            project.collaborators.append(collab)
        project.save()
        flash(f'El Proyecto {project.title} se ha creado con éxito', 'info')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/new_project_form.html', form=form)

@admin_bp.route('/projects/<int:project_id>')
@login_required
@owner_required
def admin_project(project_id):
    project = Project.get_by_id(project_id)
    return render_template('admin/admin_project.html', project=project)