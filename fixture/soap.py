from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.soap_url)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        project_list = []
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        projects = client.service.mc_projects_get_user_accessible(self.app.config["webadmin"]["username"],
                                                                  self.app.config["webadmin"]["password"])

        for ProjectData in projects:
            project_list.append(Project(name=ProjectData.name))
        return list(project_list)