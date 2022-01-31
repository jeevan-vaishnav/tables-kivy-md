from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

# Display Pixles


class Tables(MDApp):
    def build(self):
        # Define Screen
        screen = Screen()
        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, "center_y": 0.5},
            size_hint=(0.9, 0.6),
            check=True,
            use_pagination=True,
            rows_num=3,
            pagination_menu_height="250dp",
            # pagination_menu_pos="auto",
            # background_color=[12, 15, 1, 1],
            column_data=[
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Address", dp(30)),
                ("Phone Number", dp(30))
            ],
            row_data=[
                ("Jeevan", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan1", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan2", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan3", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan1", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan2", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan3", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan1", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan2", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan3", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan1", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan2", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan3", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan1", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan2", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan3", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan1", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan2", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan3", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan1", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan2", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan3", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan1", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan2", "Vaishnav", "jee@gmail.com", "9630903355"),
                ("Jeevan3", "Vaishnav", "jee@gmail.com", "9630903355"),

            ]
        )

        # BInd the table
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.load_file('main.kv')
        # Add table widet to screen
        screen.add_widget(table)
        return screen
    # Function for check press

    def checked(self, instance_table, current_row):
        print(instance_table, current_row)
    # Function for row presss

    def row_checked(self, instance_table, instance_row):
        print(instance_table, instance_row)


        # Start
if __name__ == "__main__":
    Tables().run()
