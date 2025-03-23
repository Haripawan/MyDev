import flet as ft

def welcome_tab(page, on_authenticated):
    def authenticate(e):
        # Simple authentication logic (replace with your own logic)
        if user_id.value == "admin" and password.value == "password":
            page.window_width = 800  # Resize to a larger window
            page.window_height = 600
            page.controls.clear()
            show_authenticated_view()  # Show authenticated view
        else:
            error_message.value = "Invalid credentials. Please try again."
            page.update()

    def clear_fields(e):
        # Clear the text fields
        user_id.value = ""
        password.value = ""
        error_message.value = ""
        page.update()

    def logout(e):
        # Log out and return to the login screen
        page.controls.clear()
        page.window_width = 400  # Resize back to smaller window
        page.window_height = 400
        page.add(login_view)
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.update()

    def show_authenticated_view():
        # Show the authenticated view with a welcome message and logout button
        welcome_message = ft.Text(f"Welcome, {user_id.value}!", size=16, weight="bold")
        logout_button = ft.ElevatedButton("Log Out", on_click=logout, bgcolor=ft.colors.RED)
        top_bar = ft.Row(
            controls=[welcome_message, logout_button],
            alignment="end",
            spacing=10,
        )
        page.add(top_bar)
        on_authenticated()  # Call the callback to show other tabs

    # Login form
    user_id = ft.TextField(label="User ID", width=200)
    password = ft.TextField(label="Password", password=True, width=200)
    login_button = ft.ElevatedButton("Log In", on_click=authenticate)
    clear_button = ft.ElevatedButton("Clear", on_click=clear_fields)
    error_message = ft.Text(value="", color="red")

    login_view = ft.Column(
        controls=[
            ft.Text("Login to Data Mapping App", size=20, weight="bold"),
            user_id,
            password,
            ft.Row(
                [ft.Row([login_button, clear_button], spacing=20)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            error_message,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return login_view