__author__ = 'Liliia'

from selenium.webdriver.support.ui import Select
from model.project import Project
import re


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_option(self, field_name, text):
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
        self.select_option("status", project.status)
        self.checkbox("enabled", project.enabled)
        self.select_option("view_state", project.view_status)
        self.change_field_value("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.project_cache = None

    def open_project(self, id):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id={}')]".format(id)).click()

    def delete_project(self, id):
        wd = self.app.wd
        self.open_projects_page()
        self.open_project(id)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            for row in wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]/../.."):
                cells = row.find_elements_by_tag_name("td")
                id = re.sub(".*=", "", cells[0].find_element_by_css_selector('a').get_attribute('href'))
                name = cells[0].text
                status = cells[1].text
                if cells[2].text == 'X':
                    enabled = True
                else:
                    enabled = False
                view_status = cells[3].text
                description = cells[4].text
                self.project_cache.append(Project(id=id,name=name, status=status, enabled=enabled,
                                                  view_status=view_status, description=description))
        return list(self.project_cache)

    def count(self):
        wd = self.app.wd
        self.open_projects_page()
        return len(self.get_project_list())

