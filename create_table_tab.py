# filepath: /Users/hp/Documents/MyDev/create_table_tab.py
import flet as ft
def create_table_tab():
    table_data = []

    def add_row(e):
        table_data.append({"Column 1": "", "Column 2": ""})
        update_table()

    def update_table():
        table_container.controls.clear()
        for row in table_data:
            table_container.controls.append(
                ft.Row(
                    controls=[
                        ft.TextField(value=row["Column 1"], on_change=lambda e: update_cell(e, row, "Column 1")),
                        ft.TextField(value=row["Column 2"], on_change=lambda e: update_cell(e, row, "Column 2")),
                    ],
                    spacing=10,
                )
            )
        page.update()

    def update_cell(e, row, column):
        row[column] = e.control.value

    table_container = ft.Column(spacing=10)
    add_row_button = ft.ElevatedButton("Add Row", on_click=add_row)

    return ft.Column(
        controls=[
            ft.Text("Create Table", size=24, weight="bold"),
            add_row_button,
            table_container,
        ]
    )