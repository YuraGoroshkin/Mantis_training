from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, inherit_global=None, viewStatus=None,
                 description=None, id=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.viewStatus = viewStatus
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s" % (self.name)

    def __eq__(self, other):
        return self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
