logging_level = 'DEBUG'
logging_file = ''

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