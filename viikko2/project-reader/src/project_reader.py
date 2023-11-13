from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_toml = toml.loads(content)
        print(parsed_toml['tool']['poetry']['license'])


        print(parsed_toml)
        dependencies = list(parsed_toml['tool']['poetry']['dependencies'])
        dev_dependencies = list(parsed_toml['tool']['poetry']['group']['dev']['dependencies'])
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            parsed_toml['tool']['poetry']['name'], 
            parsed_toml['tool']['poetry']['description'], 
            dependencies, 
            dev_dependencies,
            parsed_toml['tool']['poetry']['license'],
            list(parsed_toml['tool']['poetry']['authors']),)
