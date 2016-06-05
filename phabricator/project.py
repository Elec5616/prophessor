from .api import api_call


class Project():
    def add_user(self, user_phid, project_phid):
        return api_call.template("add_user_to_project", (user_phid, project_phid))

    def remove_user(self, user_phid, project_phid):
        return api_call.template("remove_user_from_project", (user_phid, project_phid))

    def create(self, name, icon="policy", color="red", members=[]):
        if members:
            return api_call.template("create_project",
                                     (name, icon, color, "&" + "&".join(["members[]=%s" % (m,) for m in members])))
        else:
            return api_call.template("create_project", (name, icon, color, ""))

project = Project()

