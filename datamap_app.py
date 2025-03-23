import flet as ft
from welcome_tab import welcome_tab
from create_table_tab import create_table_tab
from mapping_tab import mapping_tab

def main(page: ft.Page):
    page.title = "Data Mapping App"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Set initial window size for login
    page.window_width = 400
    page.window_height = 400

    def show_tabs():
        # Show tabs after authentication
        welcome_message = ft.Text(f"Welcome, {user_id}!", size=16, weight="bold")
        logout_button = ft.ElevatedButton("Log Out", on_click=logout, bgcolor=ft.colors.RED)
        top_bar = ft.Row(
            controls=[welcome_message, logout_button],
            alignment="end",
            spacing=10,
        )

        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text="Welcome", content=ft.Text("Welcome to the Data Mapping App!")),
                ft.Tab(text="Create Table", content=create_table_tab()),
                ft.Tab(text="Mapping", content=mapping_tab()),
            ],
            expand=1,
        )
        page.controls.clear()
        page.add(top_bar, tabs)
        page.update()

    def logout(e):
        # Log out and return to the login screen
        page.controls.clear()
        page.window_width = 400  # Resize back to smaller window
        page.window_height = 400
        page.add(welcome_tab(page, on_authenticated=show_tabs))
        page.update()

    # Show the login screen initially
    user_id = None  # Placeholder for storing the logged-in username

    def on_authenticated():
        nonlocal user_id
        user_id = "admin"  # Replace with the actual username from the login logic
        page.window_width = 800  # Resize to a larger window
        page.window_height = 600
        show_tabs()

    page.add(welcome_tab(page, on_authenticated=on_authenticated))

# Run the app
ft.app(target=main)