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
        setattr(self, "epics", self.get_boxes(self.data.epics))
        setattr(self, "stories", self.get_boxes(self.data.stories))
        setattr(self, "features", self.get_boxes(self.data.features))
        self.close()
        return self

    def close(self):
        del self.config
        del self.logger
        del self.data

    def set_team(self):
        self.logger.info('Set Team')
        self.logger.debug('Team: ' + self.config.api_project)
        team = {}
        team['name'] = self.config.api_project
        setattr(self, "team", team)

    def get_boxes(self, items):
        parent = {}
        parent['chart_list'] = []
        for x in self.config.field_map:
            d = {}
            if hasattr(items, self.config.field_map[x]['field_name'] + '_counts'):
                data = getattr(items, self.config.field_map[x]['field_name'] + '_counts')
                self.generate_boxes(d, data)
                parent[self.config.field_map[x]['field_name']] = d
                parent['chart_list'].append(d['bar_chart'].split('"')[1])

        return parent

    def generate_boxes(self, obj, data):

        obj['box_text'] = ''

        x = []
        y = []

        j = 0
        for key, value in data.items():
            x.append(key)
            y.append(value)

            box = Template(self.config, self.logger)
            box.get("status_box.html")
            box.render(title=key, number=value, background_color=self.config.box_color_list[j])
            obj['box_text'] = obj['box_text'] + box.text
            j = 0 if j == 4 else j + 1

        obj['bar_chart'] = offline.plot([go.Bar(x=x, y=y)], output_type='div', validate=False, show_link=False, auto_open=False, include_plotlyjs=False)


        return obj

