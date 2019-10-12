from model.project import Project


def test_add_project(app, json_projects):
    username = app.session.get_logged_user()
    password = 'root'
    old_projects = app.soap.get_project_list(username, password)
    project = json_projects
    app.project.create(project)
    new_projects = app.soap.get_project_list(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)