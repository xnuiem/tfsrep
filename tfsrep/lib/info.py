class TFSInfo:

    def __init__(self, config, logger, data):
        self.config = config
        self.logger = logger
        self.data = data.result

    def create_info(self):
        setattr(self, 'count', len(self.data.workitems))
        setattr(self, 'ids', self.data.workitem_ids)
        setattr(self, 'items', self.data.workitems)

        current_count = {}
        current_items = {}

        self.logger.info('Start Item Loop')
        for item in self.items:
            self.logger.debug('Start Item')

            for key, value in self.config.field_map.items():
                self.logger.debug('Key: ' + key)

                if key in item.fields:
                    new_key = self.config.field_map[key]['field_name']
                    if "handler" in self.config.field_map[key]:
                        map_value = getattr(self, self.config.field_map[key]["handler"])(key, item)
                    elif key in item.fields:
                        map_value = item.fields[key]

                    if new_key not in current_count:
                        current_count[new_key] = {}
                        current_items[new_key] = {}

                    if map_value in current_count[new_key]:
                        current_count[new_key][map_value] = current_count[new_key][map_value] + 1
                    else:
                        current_count[new_key][map_value] = 1
                        current_items[new_key][map_value] = []

                    current_items[new_key][map_value].append(item)
            self.logger.debug('============================')

        for key, value in current_count.items():
            setattr(self, key + '_counts', value)
            setattr(self, key + '_items', current_items[key])

        self.close()
        return self

    def handle_assigned(self, key, item):
        if key in item.fields:
            assignee = item.fields[key].split('<')[0].strip()
        else:
            assignee = self.config.field_map[key]["default_value"]
        return assignee

    def close(self):
        del self.logger
        del self.config
