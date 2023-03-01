import random

from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_projects_list()
    c = str(random.randrange(10))
    app.project.create(Project(name="Test_name_" + c, status="release", viewStatus="public",
                               description="test", inherit_global=True))
    new_projects = app.project.get_projects_list()
    assert len(old_projects) + 1 == len(new_projects)
