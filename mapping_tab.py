# filepath: /Users/hp/Documents/MyDev/mapping_tab.py
import flet as ft
def mapping_tab():
    source_columns = ["Source Column 1", "Source Column 2", "Source Column 3"]
    target_columns = ["Target Column A", "Target Column B", "Target Column C"]
    mappings = []

    def add_mapping(e):
        source_dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(col) for col in source_columns],
            width=200,
        )
        target_dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(col) for col in target_columns],
            width=200,
        )
        delete_button = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=lambda e: remove_mapping(e, mapping_row),
        )
        mapping_row = ft.Row(
            controls=[source_dropdown, target_dropdown, delete_button],
            spacing=10,
        )
        mappings.append(mapping_row)
        mapping_container.controls.append(mapping_row)
        page.update()

    def remove_mapping(e, mapping_row):
        mappings.remove(mapping_row)
        mapping_container.controls.remove(mapping_row)
        page.update()

    def save_mappings(e):
        mapping_results = []
        for mapping_row in mappings:
            source_value = mapping_row.controls[0].value
            target_value = mapping_row.controls[1].value
            if source_value and target_value:
                mapping_results.append({"source": source_value, "target": target_value})
        print("Mappings:", mapping_results)
        result_text.value = f"Saved Mappings: {mapping_results}"
        page.update()

    mapping_container = ft.Column(spacing=10)
    add_button = ft.ElevatedButton("Add Mapping", on_click=add_mapping)
    save_button = ft.ElevatedButton("Save Mappings", on_click=save_mappings)
    result_text = ft.Text("")

    return ft.Column(
        controls=[
            ft.Text("Data Mapping", size=24, weight="bold"),
            ft.Row([add_button, save_button], spacing=10),
            mapping_container,
            result_text,
        ]
    )