
from suds.client import Client
from suds import WebFault
from model.project import Project

client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        projects = []
        for project in client.service.mc_projects_get_user_accessible(username, password):
            dict = Client.dict(project)
            id = dict['id']
            name = dict['name']
            status = dict['status']['name']
            enabled = dict['enabled']
            view_status = dict['view_state']['name']
            description = dict['description']
            projects.append(Project(id=str(id), name=str(name), status=str(status), enabled=enabled,
                                    view_status=str(view_status), description=str(description)))
        return projects

