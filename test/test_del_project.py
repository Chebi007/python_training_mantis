from model.project import Project
import random


def test_add_project(app):
    username = app.session.get_logged_user()
    password = 'root'
    if app.project.count() == 0:
        app.project.create(Project(name="New project"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project.id)
    new_projects = app.project.get_project_list()
    soap_projects = app.soap.get_project_list(username, password)
    assert sorted(soap_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)