__author__ = 'Liliia'

from selenium.webdriver.support.ui import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select(self, field_name, text):
        wd = self.app.wd
        select = Select(wd.find_element_by_name(field_name))
        select.select_by_visible_text(text)

    def checkbox(self, name, active):
        wd = self.app.wd
        if active is False:
            wd.find_element_by_name(name).click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.select("status", project.status)
        self.checkbox("inherit_global", project.inherit_global)
        self.select("view_state", project.view_status)
        self.change_field_value("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.fill_project_form(project)
        wd.find_element_by_name("submit").click()
        #self.group_cache = None