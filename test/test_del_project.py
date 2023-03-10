from model.project import Project
import random


def test_del_project(app):
    if len(app.project.get_projects_list()) == 0:
        app.project.create(Project(name="Test_name_13579", status="release", viewStatus="public",
                 description="test",inherit_global=True))
    old_projects = app.project.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.project.get_projects_list()
    assert len(old_projects) -1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=(lambda x: x.name)) == sorted(new_projects, key=(lambda x: x.name))