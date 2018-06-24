import jinja2
from pprint import pprint

class Template:

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def render(self, **kwargs):
        self.logger.info('Render Template')
        self.text = self.template.render(kwargs)

    def save(self):
        self.logger.info('Save Template')
        with open("www/index.html", "w") as f:
            f.write(self.text)
        self.logger.info('Save Complete')

    def get(self, template_file):
        self.logger.info("Getting Template")
        self.logger.debug("Template File: " + template_file)
        template_loader = jinja2.FileSystemLoader(searchpath="tfsrep/templates")
        template_env = jinja2.Environment(loader=template_loader)
        self.template = template_env.get_template(template_file)
