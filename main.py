
import flet as ft
import sqlite3

def init_db():
    conn = sqlite3.connect("techprojob_cards.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            device_model TEXT NOT NULL,
            issue_description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def main (page: ft.Page):
    init_db()
    page.title = "TechProServices Job Card Manager"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 800
    page.window_height = 600

    #Ui Components
    client_name = ft.TextField(label="Client Name", width=400)
    device_model = ft.TextField(label="Device Model", width=400)    
    issue_description = ft.TextField(label="Issue Description", width=400, multiline=True, min_lines=3)
    status_msg = ft.Text()

    def submit_job(e):
        if not client_name.value or not device_model.value or not issue_description.value:
            status_msg.value = "Please fill in all fields."
            status_msg.color = "red"
        else: 
        # Here you would typically save the job card data to a database or file
            conn = sqlite3.connect("techprojob_cards.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO job_cards (client_name, device_model, issue_description)
                VALUES (?, ?, ?)
            ''', (client_name.value, device_model.value, issue_description.value))
            conn.commit()
            conn.close()

            status_msg.value = f"Job card for {client_name.value} has been submitted!"
            status_msg.color = "green"

            client_name.value = ""
            device_model.value = ""
            issue_description.value = ""
        page.update()
    # Layoput
    page.add(
        ft.Column([
            ft.Text("TechProServices Job Card Manager", size=24, weight=ft.FontWeight.BOLD,color = "blue"),
            ft.Divider(),
            client_name,
            device_model,
            issue_description,
            ft.ElevatedButton(
                "Save to database", 
                on_click=submit_job,
                
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    padding=ft.Padding(20, 10),
                    color="white",
                    bgcolor="blue"
                )
            ),
            status_msg
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
        )
    
ft.app(target=main)