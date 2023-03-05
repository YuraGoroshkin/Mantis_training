import random

from model.project import Project


def test_add_project(app):
    old_projects = app.project.get_projects_list()
    c = str(random.randrange(10))
    project = Project(name="Test_name_13579" + c, status="release", viewStatus="public",
                               description="test", inherit_global=True)
    app.project.create(project)
    new_projects = app.project.get_projects_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=(lambda x: x.name)) == sorted(new_projects, key=(lambda x: x.name))