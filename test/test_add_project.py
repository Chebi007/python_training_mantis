from model.project import Project


def test_add_project(app, json_projects):
    username = app.session.get_logged_user()
    password = 'root'
    project = json_projects
    app.project.create(project)
    new_projects = app.project.get_project_list()
    soap_projects = app.soap.get_project_list(username, password)
    assert sorted(soap_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)