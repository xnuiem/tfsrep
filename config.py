logging_level = 'DEBUG'
logging_file = ''

box_color_list = ['#7e9a9a','#f6d8ac','#db9833','#2a6592','#8ec3eb']


field_map = {
    "System.State" : {
        "field_name": "state"
    },
    "System.BoardColumn" : {
        "field_name": "column"
    },
    "System.IterationPath" : {
        "field_name": "iteration"
    },
    "System.AssignedTo" : {
        "field_name": "assigned",
        "default_value": "unassigned",
        "handler": "handle_assigned"
    }
}