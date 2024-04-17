from nicegui import events, ui


def vm_list(vms: list):
    COLUMNS = [
        {"name": "name", "label": "VM name", "field": "name", "align": "left"},
        {"name": "status", "label": "Status", "field": "status", "align": "left"},
        {
            "name": "environment",
            "label": "Environment",
            "field": "environment",
            "align": "left",
        },
    ]
    table = ui.table(columns=COLUMNS, rows=vms, row_key="uuid").classes("w-full")
    table.add_slot(
        "header",
        r"""
        <q-tr :props="props">
            <q-th v-for="col in props.cols" :key="col.name" :props="props">
                {{ col.label }}
            </q-th>
            <q-th />
        </q-tr>
    """,
    )
    table.add_slot(
        "body",
        r"""
        <q-tr :props="props">
            <q-td key="name" :props="props">
                {{ props.row.name }}
            </q-td>
            <q-td key="status" :props="props">
                {{ props.row.status }}
            </q-td>
            <q-td key="environment" :props="props">
                {{ props.row.environment }}
            </q-td>
            <q-td>
                <q-btn color="positive" icon="play_circle" round
                    @click="() => $parent.$emit('start', props.row)" />
                <q-btn color="negative" icon="stop_circle" round
                    @click="() => $parent.$emit('stop', props.row)" />
                <q-btn color="warning" icon="restart_alt" round
                    @click="() => $parent.$emit('restart', props.row)" />
            </q-td>
        </q-tr>
    """,
    )
    table.on("start", start_vm)
    table.on("stop", stop_vm)
    table.on("restart", restart_vm)


def start_vm(e: events.GenericEventArguments) -> None:
    ui.notify(f"Starting vm {e.args['name']}", type="positive", close_button=True)


def stop_vm(e: events.GenericEventArguments) -> None:
    ui.notify(f"Stopping vm {e.args['name']}", type="negative", close_button=True)


def restart_vm(e: events.GenericEventArguments) -> None:
    ui.notify(f"Restarting vm {e.args['name']}", type="warning", close_button=True)
