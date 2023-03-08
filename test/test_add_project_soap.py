from model.project import Project


def test_add_project_soap(app):
    app.session.login("administrator", "root")
    old_project_list= app.soap.get_project_list()
    app.project.create(Project(name="Test2", status="release", viewStatus="public",
                 description="test",inherit_global=True))
    # новый список проектов
    new_project_list = app.soap.get_project_list()
    assert len(old_project_list) + 1 == len(new_project_list)