from pprint import pprint
import plotly.graph_objs as go
import plotly.offline as offline
from tfsrep.lib.template import Template


class Assets:

    def __init__(self, config, logger, data):
        self.config = config
        self.logger = logger
        self.data = data

    def generate(self):
        self.set_team()
        self.set_epics()
        self.set_stories()
        self.close()
        return self

    def close(self):
        del self.config
        del self.logger
        del self.data

    def set_team(self):
        self.logger.info('Set Team')
        self.logger.debug('Team: ' + self.config.api_project)
        team = type("team", (), {})
        team.name = self.config.api_project
        setattr(self, "team", team)

    def generate_boxes(self, items):


        pass

    def generate_bar_chart(self):
        pass

    def set_epics(self):
        epics = type("epics", (), {})
        epics.status_box_text = ''

        x = []
        y = []

        j = 0
        for key, value in self.data.epics.state_counts.items():
            x.append(key)
            y.append(value)

            box = Template(self.config, self.logger)
            box.get("status_box.html")
            box.render(title=key, number=value, background_color=self.config.box_color_list[j])
            epics.status_box_text = epics.status_box_text + box.text
            j = 0 if j == 4 else j + 1

        epics.status_bar_chart = offline.plot([go.Bar(x=x, y=y)], output_type='div', include_plotlyjs=False,
                                              show_link=False)

        setattr(self, "epics", epics)

    def set_stories(self):
        stories = type("stories", (), {})
        stories.status_box_text = ''

        x = []
        y = []

        j = 0
        for key, value in self.data.stories.state_counts.items():
            x.append(key)
            y.append(value)

            box = Template(self.config, self.logger)
            box.get("status_box.html")
            box.render(title=key, number=value, background_color=self.config.box_color_list[j])
            stories.status_box_text = stories.status_box_text + box.text
            j = 0 if j == 4 else j + 1

        stories.status_bar_chart = offline.plot([go.Bar(x=x, y=y)], output_type='div', include_plotlyjs=False,
                                              show_link=False)


        stories.assigned_box_text = ''
        x = []
        y = []

        j = 0
        for key, value in self.data.stories.assigned_counts.items():
            x.append(key)
            y.append(value)

            box = Template(self.config, self.logger)
            box.get("status_box.html")
            box.render(title=key, number=value, background_color=self.config.box_color_list[j])
            stories.assigned_box_text = stories.assigned_box_text + box.text
            j = 0 if j == 4 else j + 1

        stories.assigned_bar_chart = offline.plot([go.Bar(x=x, y=y)], output_type='div', include_plotlyjs=False,
                                                show_link=False)


        setattr(self, "stories", stories)
