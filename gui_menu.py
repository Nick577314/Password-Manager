
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, \
    QPushButton, QLineEdit, QSizePolicy, QSpacerItem

from database_connect import store_info  # Your function to store info in the database
from passwordManager.database_connect import find_info
from passwordManager.encryption_handler import decrypt_password, encryption_key


class PasswordManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 300, 500, 500)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main Menu")
        self.layout = QVBoxLayout()

        # adding a spacer surrounding the buttons so that its in the middle
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)


        # Create a button to open the new entry window
        self.open_newentry_btn = QPushButton("Add Account", self)
        self.open_newentry_btn.clicked.connect(self.open_new_entries)
        self.layout.addWidget(self.open_newentry_btn, alignment= Qt.AlignCenter)

        # Create a button to open the search existing window (optional)
        self.open_search_btn = QPushButton("Search Existing Account", self)
        self.open_search_btn.clicked.connect(self.open_search_existing)
        self.layout.addWidget(self.open_search_btn,alignment= Qt.AlignCenter)
        # adding a spacer surrounding the buttons so that its in the middle
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

        # Set the main widget and layout
        central_widget = QWidget(self)  # Create a central widget for the QMainWindow
        central_widget.setLayout(self.layout)

        self.setCentralWidget(central_widget)  # Set the central widget
        self.resize(300, 200)

    def open_new_entries(self):
        self.new_entries = NewEntries(self)  # Pass reference to the main window
        self.new_entries.show()
        self.hide()  # Hide the main window

    def open_search_existing(self):
        self.search_existing = SearchExisting(self)  # Pass reference to the main window
        self.search_existing.show()
        self.hide()


class NewEntries(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Store a reference to the main window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("New Entries")
        self.layout = QVBoxLayout()

        self.platform_input = QLineEdit()
        self.platform_input.setPlaceholderText("Enter the platform: ")
        self.layout.addWidget(self.platform_input)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username: ")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password: ")
        self.layout.addWidget(self.password_input)

        # Create a button to submit the new entry
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_entries)
        self.layout.addWidget(self.submit_button)


        self.back_button = QPushButton("Back to main menu " )
        self.back_button.clicked.connect(self.back_to_main_menu)
        self.layout.addWidget(self.back_button)

        # Set the layout for this window
        self.setLayout(self.layout)

# function related to the back to main menu button
# that closes just closes the current window the user is on
    def back_to_main_menu(self):
        #Closing the existing window
        #Go back to the initial window
        self.main_window.show()
        self.close()


    def submit_entries(self):
        username = self.username_input.text()
        password = self.password_input.text()
        platform = self.platform_input.text()

        try:
            store_info(username,password,platform)
            print("submission successful!")
            self.main_window.show()
            self.close()
        except Exception as e:
            print(f"Failed to submit entries: {e}")

#window for the search screen
# This holds the UI for searching for your password
class SearchExisting(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Search for Account Info")
        self.layout = QVBoxLayout()


        self.username_input = QLineEdit()
        self.layout.addWidget(self.username_input)

        self.platform_input = QLineEdit()
        self.layout.addWidget(self.platform_input)
        # Create a button to search for existing accounts
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search)
        self.layout.addWidget(self.search_button)

        self.back_button = QPushButton("Back to main menu ")
        self.back_button.clicked.connect(self.back_to_main_menu)
        self.layout.addWidget(self.back_button)


        # Set the layout for this window
        self.setLayout(self.layout)

    def back_to_main_menu(self):
        # Closing the existing window
        # Go back to the initial window
        self.main_window.show()
        self.close()


    def search(self):
        username = self.username_input.text()
        platform = self.platform_input.text()
        password = find_info(platform,username)
        print(password)

#     def __init__(self):
#         super().__init__()
#         self.title("Password Manager")
#         self.geometry("400x300")
#
#         # Create a container frame to hold different pages (menu, form, etc.)
#         self.container = tk.Frame(self)
#         self.container.pack(fill="both", expand=True)
#
#         # Dictionary to hold pages (MenuPage and AddInfoPage)
#         self.frames = {}
#
#         # Add both frames (MenuPage and AddInfoPage)
#         for F in (MenuPage, AddInfoPage,SearchPage):
#             page_name = F.__name__
#             frame = F(parent=self.container, controller=self)
#             self.frames[page_name] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         # Show the menu page first
#         self.show_frame("MenuPage")
#
#     def show_frame(self, page_name):
#         """Show a frame for the given page name."""
#         frame = self.frames[page_name]
#         frame.tkraise()
#
#
# class MenuPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller
#
#         label = tk.Label(self, text="Main Menu", font=("Arial", 16))
#         label.pack(pady=10)
#
#         # Button to navigate to the Add Info form
#         add_info_button = tk.Button(self, text="Add Account Info", command=lambda: controller.show_frame("AddInfoPage"))
#         add_info_button.pack(pady=10)
#
#         search_button = tk.Button(self,text="Search",command=lambda: controller.show_frame("SearchPage"))
#         search_button.pack(pady=10)
#
#
#         Exit_button = tk.Button(self, text="Exit",command=self.quit_app)
#         Exit_button.pack(pady=5)
#
# #function to quit app by button click
#     def quit_app(self):
#         self.quit()
#         self.destroy()
#
# class SearchPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller
#
#
#         # Create a frame for input fields
#         input_frame = tk.Frame(self)
#         input_frame.grid(row=0, column=0, padx=10, pady=10)
#
#         # Create the input fields
#         tk.Label(input_frame, text="App Name:").grid(row=0, column=0, padx=(0, 10))  # Right padding for spacing
#         self.app_name_entry = tk.Entry(input_frame)
#         self.app_name_entry.grid(row=0, column=1)
#
#         tk.Label(input_frame, text="Username:").grid(row=1, column=0, padx=(0, 10))  # Right padding for spacing
#         self.username_entry = tk.Entry(input_frame)
#         self.username_entry.grid(row=1, column=1)
#
#         search_button = tk.Button(self, text="Search", command=self.Search)
#         search_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))  # Center the button
#
#         # Back button to return to the menu page
#         back_button = tk.Button(self, text="Back to Menu", command=lambda: controller.show_frame("MenuPage"))
#         back_button.grid(row=2, column=0, columnspan=2, pady=(10, 0)) # Add this line to define result_label
#
#     def Search(self):
#         app_name = self.app_name_entry.get()
#         username = self.username_entry.get()
#
#         password = find_info(app_name, username)
#
#         # Call the function to display the result
#         self.show_result_window(password)
#
#     def show_result_window(self, password):
#         # Create a new Toplevel window
#         result_window = tk.Toplevel(self)
#         result_window.title("Search Result")
#         result_window.geometry("300x150")  # Set the size of the window
#         # Style for result label
#         label_text = f'Password: {password}' if password else 'No result found or an error occurred.'
#         result_label = tk.Label(result_window, text=label_text, font=("Arial", 14), wraplength=250)
#         result_label.pack(pady=20)
#
#         # Add a close button to the results window
#         close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
#         close_button.pack(pady=10)
#
# class AddInfoPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller
#
#         # Create the input fields
#         tk.Label(self, text="Email").grid(row=0, column=0, padx=10, pady=5)
#         self.email_entry = tk.Entry(self)
#         self.email_entry.grid(row=0, column=1)  # Change to row 0
#
#         tk.Label(self, text="Username").grid(row=1, column=0, padx=10, pady=5)
#         self.username_entry = tk.Entry(self)
#         self.username_entry.grid(row=1, column=1)  # Change to row 1
#
#         tk.Label(self, text="Password").grid(row=2, column=0, padx=10, pady=5)
#         self.password_entry = tk.Entry(self, show='*')  # Typically show='*' for passwords
#         self.password_entry.grid(row=2, column=1)  # Change to row 2
#
#         tk.Label(self, text="URL").grid(row=3, column=0, padx=10, pady=5)
#         self.url_entry = tk.Entry(self)
#         self.url_entry.grid(row=3, column=1)  # Keep as row 3
#
#         tk.Label(self, text="App Name").grid(row=4, column=0, padx=10, pady=5)
#         self.app_name_entry = tk.Entry(self)
#         self.app_name_entry.grid(row=4, column=1)  # Keep as row 4
#
#         # Button to store the information
#         add_button = tk.Button(self, text="Add Info", command=self.add_new_entry)
#         add_button.grid(row=5, column=0, columnspan=2, pady=10)
#
#         # Button to go back to the menu
#         back_button = tk.Button(self, text="Back to Menu", command=lambda: controller.show_frame("MenuPage"))
#         back_button.grid(row=6, column=0, columnspan=2, pady=10)
#
#     def add_new_entry(self):
#         # Collect the data from the input fields
#         password = self.password_entry.get()
#         user_email = self.email_entry.get()
#         username = self.username_entry.get()
#         url = self.url_entry.get()
#         app_name = self.app_name_entry.get()
#
#         # Ensure no fields are empty
#         if not all([password, user_email, username, url, app_name]):
#             messagebox.showerror("Input Error", "All fields are required!")
#             return
#
#         # Call the store_info function to store the data in the database
#         try:
#             store_info(password, user_email, username, url, app_name)
#             messagebox.showinfo("Success", "Information added successfully!")
#             self.clear_fields()  # Clear the input fields after adding
#         except Exception as e:
#             messagebox.showerror("Error", str(e))
#
#
#     def clear_fields(self):
#         # Clear all the input fields
#         self.password_entry.delete(0, tk.END)
#         self.email_entry.delete(0, tk.END)
#         self.username_entry.delete(0, tk.END)
#         self.url_entry.delete(0, tk.END)
#         self.app_name_entry.delete(0, tk.END)






