from model.project import Project


def test_add_project(app):
    project = Project(name="Zorro", status="stable", inherit_global=False, view_status="private", description="lalala")
    app.project.create(project)




    #group = json_groups
    #old_groups = db.get_group_list()
    #app.group.create(group)
    #new_groups = db.get_group_list()
    #old_groups.append(group)
    #assert old_groups == new_groups
