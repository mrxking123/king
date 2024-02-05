from kivy.app import App  # Importing the main Kivy application class
from kivy.uix.boxlayout import BoxLayout  # Importing a layout container
from kivy.uix.label import Label  # Importing a label widget
from kivy.uix.textinput import TextInput  # Importing a text input widget
from kivy.uix.button import Button  # Importing a button widget
from kivy.uix.popup import Popup  # Importing a popup widget
from kivy.uix.scrollview import ScrollView  # Importing a scroll view widget
import base64  # Importing the base64 encoding/decoding module

class MyApp(App):
    def build(self):
        # Declare global variables
        self.code = TextInput(multiline=False, font_size=25, password=True)  # Entry for password
        self.text_input = TextInput(font_size=20, multiline=True)  # Text input for the main message
        self.screen = BoxLayout(orientation='vertical', spacing=10, padding=10)  # Main layout container

        # Display labels, text input fields, and buttons for the main screen
        label1 = Label(text="Enter text for encryption and decryption", color="white", font_size=13)  # Label for message input
        self.screen.add_widget(label1)

        scroll_view = ScrollView()  # Scroll view to allow scrolling for long text
        scroll_view.add_widget(self.text_input)  # Adding text input to scroll view
        self.screen.add_widget(scroll_view)

        label2 = Label(text="Enter secret key for encryption and decryption", color="white", font_size=23)  # Label for password entry
        self.screen.add_widget(label2)

        self.screen.add_widget(self.code)  # Adding password entry field to the layout

        encrypt_button = Button(text="ENCRYPT", height='40dp', background_color=(0.93, 0.22, 0.20, 1), color=(1, 1, 1, 1),
                                on_press=self.encrypt)  # Button for encryption
        decrypt_button = Button(text="DECRYPT", height='40dp', background_color=(0, 0.74, 0.34, 1), color=(1, 1, 1, 1),
                                on_press=self.decrypt)  # Button for decryption
        reset_button = Button(text="RESET", height='40dp', background_color=(0.06, 0.54, 1, 1), color=(1, 1, 1, 1),
                              on_press=self.reset)  # Button to reset fields

        self.screen.add_widget(encrypt_button)
        self.screen.add_widget(decrypt_button)
        self.screen.add_widget(reset_button)

        return self.screen  # Returning the main layout as the root of the application

    def reset(self, instance):
        self.code.text = ""  # Resetting the password entry field
        self.text_input.text = ""  # Resetting the message text input field

    def decrypt(self, instance):
        # Retrieve password from the entry widget
        password = self.code.text

        # Check if the password is '1234'
        if password == '1234':
            # Create a new window for decryption
            popup_content = BoxLayout(orientation='vertical', spacing=10, padding=10)

            # Retrieve the text from the Text widget
            message = self.text_input.text

            # Encode the message into ASCII
            decode_message = message.encode('ascii')

            # Decode the Base64-encoded message
            base64_bytes = base64.b64decode(decode_message)
            decrypt = base64_bytes.decode('ascii')

            # Display 'DECRYPT' label
            decrypt_label = Label(text="DECRYPT", color=(1, 1, 1, 1), font_size=20)
            popup_content.add_widget(decrypt_label)

            # Create a Text widget for displaying decrypted text
            text2 = TextInput(text=decrypt, readonly=True, font_size=15, multiline=True)
            popup_content.add_widget(text2)

            # Create Popup
            popup = Popup(title="Decryption", content=popup_content, size_hint=(None, None), size=(400, 200))
            popup.open()

        # Check if the password is empty
        elif password == "":
            popup_content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            popup_content.add_widget(Label(text="Input Password", color=(1, 0, 0, 1), font_size=15))

            popup = Popup(title="Decryption", content=popup_content, size_hint=(None, None), size=(300, 150))
            popup.open()

        # Check if the password is not '1234'
        elif password != "1234":
            popup_content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            popup_content.add_widget(Label(text="Invalid Password", color=(1, 0, 0, 1), font_size=15))

            popup = Popup(title="Decryption", content=popup_content, size_hint=(None, None), size=(300, 150))
            popup.open()

    def encrypt(self, instance):
        # Retrieve password from the entry widget
        password = self.code.text

        # Check if the password is '1234'
        if password == '1234':
            # Create a new window for encryption
            popup_content = BoxLayout(orientation='vertical', spacing=10, padding=10)

            # Retrieve the text from the Text widget
            message = self.text_input.text

            # Encode the message into ASCII
            encode_message = message.encode('ascii')

            # Encode the message using Base64
            base64_bytes = base64.b64encode(encode_message)
            encrypt = base64_bytes.decode('ascii')

            # Display 'ENCRYPT' label
            encrypt_label = Label(text="ENCRYPT", color=(1, 1, 1, 1), font_size=20)
            popup_content.add_widget(encrypt_label)

            # Create a Text widget for displaying encrypted text
            text2 = TextInput(text=encrypt, readonly=True, font_size=15, multiline=True)
            popup_content.add_widget(text2)

            # Create Popup
            popup = Popup(title="Encryption", content=popup_content, size_hint=(None, None), size=(400, 200))
            popup.open()

        # Check if the password is empty
        elif password == "":
            popup_content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            popup_content.add_widget(Label(text="Input Password", color=(1, 0, 0, 1), font_size=15))

            popup = Popup(title="Encryption", content=popup_content, size_hint=(None, None), size=(300, 150))
            popup.open()

        # Check if the password is not '1234'
        elif password != "1234":
            popup_content = BoxLayout(orientation='vertical', spacing=10, padding=10)
            popup_content.add_widget(Label(text="Invalid Password", color=(1, 0, 0, 1), font_size=15))

            popup = Popup(title="Encryption", content=popup_content, size_hint=(None, None), size=(300, 150))
            popup.open()

# Run the Kivy app
MyApp().run()



