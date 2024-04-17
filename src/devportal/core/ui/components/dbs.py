from nicegui import ui


def db_list(dbs: list):
    COLUMNS = [
        {"name": "env", "label": "DB env", "field": "env", "align": "center"},
        {"name": "host", "label": "Host", "field": "host", "align": "left"},
        {"name": "port", "label": "Port", "field": "port", "align": "center"},
        {"name": "server", "label": "Server", "field": "server", "align": "left"},
    ]
    ui.table(columns=COLUMNS, rows=dbs, row_key="uuid").classes("w-full")
