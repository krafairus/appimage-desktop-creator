import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QFileDialog, QMessageBox

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de .desktop")
        self.setGeometry(100, 100, 400, 250)  # Tamaño de la ventana (x, y, ancho, alto)
        self.layout = QVBoxLayout()

        self.name_label = QLabel("Nombre:")
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)

        self.category_label = QLabel("Categoría:")
        self.category_combobox = QComboBox()
        self.category_combobox.addItems(["Application", "Development", "Education", "Game", "Graphics", "Network", "Utility", "Video", "Audio", "AudioVideo", "Office", "System", "Utility", "Science"])
        self.layout.addWidget(self.category_label)
        self.layout.addWidget(self.category_combobox)

        self.desc_label = QLabel("Descripción:")
        self.desc_input = QLineEdit()
        self.layout.addWidget(self.desc_label)
        self.layout.addWidget(self.desc_input)

        self.icon_label = QLabel("Icono:")
        self.icon_input = QLineEdit()
        self.layout.addWidget(self.icon_label)
        self.layout.addWidget(self.icon_input)

        self.icon_button = QPushButton("Seleccionar Icono")
        self.icon_button.clicked.connect(self.select_icon)
        self.layout.addWidget(self.icon_button)

        self.file_label = QLabel("Archivo AppImage:")
        self.file_input = QLineEdit()
        self.layout.addWidget(self.file_label)
        self.layout.addWidget(self.file_input)

        self.file_button = QPushButton("Seleccionar AppImage")
        self.file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.file_button)

        self.save_button = QPushButton("Guardar en...")
        self.save_button.clicked.connect(self.select_save_location)
        self.layout.addWidget(self.save_button)

        self.generate_button = QPushButton("Generar .desktop")
        self.generate_button.clicked.connect(self.generate_desktop)
        self.layout.addWidget(self.generate_button)

        self.setLayout(self.layout)

        if not self.load_no_show_again_config():
            self.show_warning_dialog()

    def show_warning_dialog(self):
        warning_msg = """
        Advertencia: este programa no copia el AppImage y el icono a otra carpeta. Utiliza los directorios en los cuales tienes los archivos actualmente del AppImage y el icono. Si cambias la ubicación del icono o el AppImage, el programa dejará de aparecer en el menú de aplicaciones.

        Recomendación: crea una carpeta aparte, puede ser en tu carpeta de usuario u otra ubicación. Lo importante es que sepas que no la eliminarás y que crees dos subdirectorios llamados "appimages" e "iconos" (o cualquier otro nombre que desees) para mantener el orden.
        """
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Advertencia")
        msg_box.setText(warning_msg)
        no_show_again_button = msg_box.addButton("No mostrar de nuevo", QMessageBox.YesRole)
        msg_box.addButton("Continuar", QMessageBox.NoRole)
        msg_box.setDefaultButton(no_show_again_button)
        result = msg_box.exec()

        if msg_box.clickedButton() == no_show_again_button:
            self.save_no_show_again_config()

    def save_no_show_again_config(self):
        config_file = os.path.join(os.path.expanduser("~"), ".desktop_generator_config.txt")
        with open(config_file, "w") as file:
            file.write("no_show_again=true\n")

    def load_no_show_again_config(self):
        config_file = os.path.join(os.path.expanduser("~"), ".desktop_generator_config.txt")
        if os.path.exists(config_file):
            with open(config_file, "r") as file:
                config = file.read()
                if "no_show_again=true" in config:
                    return True
        return False

    def select_icon(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        icon, _ = QFileDialog.getOpenFileName(self, "Seleccionar Icono", "", "Icon Files (*.png *.ico *.svg)", options=options)
        if icon:
            self.icon_input.setText(icon)

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file, _ = QFileDialog.getOpenFileName(self, "Seleccionar AppImage", "", "AppImage Files (*.appimage)", options=options)
        if file:
            self.file_input.setText(file)

    def select_save_location(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        default_location = os.path.join(os.path.expanduser("~"), ".local/share/applications/")
        save_location, _ = QFileDialog.getSaveFileName(self, "Guardar archivo .desktop", default_location, "Desktop Files (*.desktop)", options=options)
        if save_location:
            self.save_location = save_location

    def generate_desktop(self):
        name = self.name_input.text()
        category = self.category_combobox.currentText()
        icon = self.icon_input.text()
        desc = self.desc_input.text()

        desktop_file = os.path.join(os.path.expanduser("~"), ".local/share/applications/", f"{name}.desktop") if not hasattr(self, "save_location") else self.save_location

        with open(desktop_file, "w") as file:
            file.write(f"[Desktop Entry]\n")
            file.write(f"Type=Application\n")
            file.write(f"Name={name}\n")
            file.write(f"Categories={category}\n")
            file.write(f"Exec={self.file_input.text()}\n")

            if icon:
                file.write(f"Icon={icon}\n")
            else:
                file.write(f"Icon=\n")  # Icono vacío si no se especifica

            file.write(f"Comment={desc}\n")
            file.write(f"Terminal=false\n")

        os.chmod(desktop_file, 0o755)
        os.system(f"chmod +x {self.file_input.text()}")

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Éxito")
        msg_box.setText(f"El archivo {desktop_file} ha sido generado exitosamente.")
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
