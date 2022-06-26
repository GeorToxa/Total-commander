from PyQt5.QtWidgets import QComboBox, QLineEdit, QListWidget, QPushButton, QWidget, QMessageBox
import os, shutil, win32api


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Параметры окна
        self.setFixedSize(1000, 612)
        self.setWindowTitle("Total Commander MEGA VERSION!!! - NOT REGISTERED - 2022 EDITION")
        self.setStyleSheet(self.CssLoader())  # Load CSS style in window

        # Вспомогательные финтифлюшки
        self.drives = win32api.GetLogicalDriveStrings()  # Получение данных о дисках
        self.drives = self.drives.split('\000')[:-1]  # Преобразование данных о дисках

        self.leftDir = ""
        self.rightDir = ""
        self.types = ["folder", ".py", ".txt"]

        # Виджеты
        self.leftComboBoxDrive = QComboBox(self)
        self.leftList = QListWidget(self)
        self.leftComboBoxType = QComboBox(self)
        self.leftInputLine = QLineEdit(self)
        self.createBtn = QPushButton("Create", self)
        self.removeBtn = QPushButton("Remove", self)
        self.renameBtn = QPushButton("Rename", self)
        self.leftToRightBtn = QPushButton("L to R", self)
        self.RigthToLeftBtn = QPushButton("R to L", self)
        self.rightComboBoxDrive = QComboBox(self)
        self.rightList = QListWidget(self)
        self.rightComboBoxType = QComboBox(self)
        self.rightInputLine = QLineEdit(self)

        # Расположение виджетов
        self.leftComboBoxDrive.setGeometry(10, 30, 69, 22)
        self.leftList.setGeometry(10, 60, 450, 500)
        self.leftComboBoxType.setGeometry(10, 575, 69, 22)
        self.leftInputLine.setGeometry(85, 575, 100, 22)
        self.createBtn.setGeometry(475, 125, 50, 50)
        self.removeBtn.setGeometry(475, 200, 50, 50)
        self.renameBtn.setGeometry(475, 275, 50, 50)
        self.leftToRightBtn.setGeometry(475, 350, 50, 50)
        self.RigthToLeftBtn.setGeometry(475, 425, 50, 50)
        self.rightComboBoxDrive.setGeometry(540, 30, 69, 22)
        self.rightList.setGeometry(540, 60, 450, 500)
        self.rightComboBoxType.setGeometry(540, 575, 69, 22)
        self.rightInputLine.setGeometry(615, 575, 100, 22)

        # Показ виджетов
        self.leftComboBoxDrive.show()
        self.leftList.show()
        self.leftComboBoxType.show()
        self.leftInputLine.show()
        self.createBtn.show()
        self.removeBtn.show()
        self.renameBtn.show()
        self.leftToRightBtn.show()
        self.RigthToLeftBtn.show()
        self.rightComboBoxDrive.show()
        self.rightList.show()
        self.rightComboBoxType.show()
        self.rightInputLine.show()

        # События
        self.infoHelp()
        self.loadDefaultDir()
        self.leftComboBoxDrive.activated.connect(self.chooseLeftComboDir)
        self.rightComboBoxDrive.activated.connect(self.chooseRightComboDir)
        self.leftList.doubleClicked.connect(self.chooseLeftListDir)
        self.rightList.doubleClicked.connect(self.chooseRightListDir)
        self.createBtn.clicked.connect(self.createFileBtn)
        self.removeBtn.clicked.connect(self.removeFileBtn)
        self.renameBtn.clicked.connect(self.renameFileBtn)
        self.leftToRightBtn.clicked.connect(self.moveLeftToRightBtn)
        self.RigthToLeftBtn.clicked.connect(self.moveRightToLeftBtn)

    # Оброботчики событий
    def loadDir(self):  # Выгрузка файлов папки по выбраному пути
        self.files_with = ["..."]
        self.files = []
        fileList = os.listdir(os.chdir(self.path))
        for i in fileList:
            if i.startswith("$"):
                pass
            else:
                self.files.append(i)
        self.files_with += self.files

    def loadDefaultDir(self):  # Вывод файлов из диска C в LISTWIDGETS
        self.path = "C:/"
        self.loadDir()

        self.leftComboBoxDrive.addItems(self.drives)
        self.leftComboBoxDrive.setCurrentIndex(0)
        self.leftList.addItems(self.files)

        self.rightComboBoxDrive.addItems(self.drives)
        self.rightComboBoxDrive.setCurrentIndex(0)
        self.rightList.addItems(self.files)

        self.leftDir = self.path
        self.rightDir = self.path

        self.leftComboBoxType.addItems(self.types)
        self.rightComboBoxType.addItems(self.types)

    def chooseLeftComboDir(self):  # Выгрузка файлов в левый LISTWIDGET в зависимости от выбраного диска
        try:
            self.leftList.clear()
            self.path = self.leftComboBoxDrive.currentText()
            self.loadDir()
            self.leftList.addItems(self.files)
            self.leftDir = self.path
        except Exception as e:
            self.logs(e)

    def chooseRightComboDir(self):  # Выгрузка файлов в правый LISTWIDGET в зависимости от выбраного диска
        try:
            self.rightList.clear()
            self.path = self.rightComboBoxDrive.currentText()
            self.loadDir()
            self.rightList.addItems(self.files)
            self.rightDir = self.path
        except Exception as e:
            self.logs(e)

    def chooseLeftListDir(self):  # Переход по папкам в левом LISTWIDGET
        try:
            if self.leftList.currentItem().text() == "...":
                a = ""
                self.path = (os.getcwd()).split("\\")
                del self.path[-1]
                for j in self.path:
                    x = j + "/"
                    a += x
                self.path = a
                self.leftList.clear()
                self.loadDir()
                if len(a) == 3 or len(a) == 4:
                    self.leftList.addItems(self.files)
                else:
                    self.leftList.addItems(self.files_with)
            else:
                if ".txt" in self.leftList.currentItem().text() or ".py" in self.leftList.currentItem().text():
                    self.openLeftFile()
                else:
                    self.path = f"{os.getcwd()}/{self.leftList.currentItem().text()}"
                    self.leftList.clear()
                    self.loadDir()
                    self.leftList.addItems(self.files_with)
            self.leftDir = self.path
        except Exception as e:
            self.logs(e)

    def chooseRightListDir(self):  # Переход по папкам в правом LISTWIDGET
        try:
            if self.rightList.currentItem().text() == "...":
                a = ""
                self.path = (os.getcwd()).split("\\")
                del self.path[-1]
                for j in self.path:
                    x = j + "/"
                    a += x
                self.path = a
                self.rightList.clear()
                self.loadDir()
                if len(a) == 3 or len(a) == 4:
                    self.rightList.addItems(self.files)
                else:
                    self.rightList.addItems(self.files_with)
            else:
                if ".txt" in self.rightList.currentItem().text() or ".py" in self.rightList.currentItem().text():
                    self.openRightFile()
                self.path = f"{os.getcwd()}/{self.rightList.currentItem().text()}"
                self.rightList.clear()
                self.loadDir()
                self.rightList.addItems(self.files_with)
            self.rightDir = self.path
        except Exception as e:
            self.logs(e)

    def createFileBtn(self):  # Создание файла
        try:
            if self.leftInputLine.text() != "":
                if self.leftComboBoxType.currentText() == "folder":
                    os.mkdir(f"{self.leftDir}/{self.leftInputLine.text()}")
                else:
                    with open(f"{self.leftDir}/{self.leftInputLine.text()}{self.leftComboBoxType.currentText()}", "w") as file:
                        file.write("")
            if self.rightInputLine.text() != "":
                if self.rightComboBoxType.currentText() == "folder":
                    os.mkdir(f"{self.rightDir}/{self.rightInputLine.text()}")
                else:
                    with open(f"{self.rightDir}/{self.rightInputLine.text()}{self.rightComboBoxType.currentText()}", "w") as file:
                        file.write("")
            self.update()
        except Exception as e:
            self.logs(e)

    def removeFileBtn(self):  # Удаление файла
        try:
            if ".txt" in self.leftList.currentItem().text():
                os.remove(f"{self.leftDir}/{self.leftList.currentItem().text()}")

            if ".py" in self.leftList.currentItem().text():
                os.remove(f"{self.leftDir}/{self.leftList.currentItem().text()}")

            if self.leftList.currentItem():
                shutil.rmtree(f"{self.leftDir}/{self.leftList.currentItem().text()}")

            elif self.rightList.currentItem():
                shutil.rmtree(f"{self.rightDir}/{self.rightList.currentItem().text()}")
            self.update()
        except Exception as e:
            self.logs(e)
            try:
                if self.leftList.currentItem():
                    os.remove(f"{self.leftDir}/{self.leftList.currentItem().text()}")
                elif self.rightList.currentItem():
                    os.remove(f"{self.rightDir}/{self.rightList.currentItem().text()}")
            except Exception as e:
                self.logs(e)
        finally:
            print("Successful removal")

    def renameFileBtn(self):  # Переименование файла
        try:
            if self.leftList.currentItem():
                os.rename(f"{self.leftDir}/{self.leftList.currentItem().text()}", f"{self.leftDir}/{self.leftInputLine.text()}")
            elif self.rightList.currentItem():
                os.rename(f"{self.rightDir}/{self.rightList.currentItem().text()}", f"{self.rightDir}/{self.rightInputLine.text()}")
            self.update()
        except Exception as e:
            self.logs(e)

    def moveLeftToRightBtn(self):  # Перемещение слева направо
        try:
            shutil.move(f"{self.leftDir}/{self.leftList.currentItem().text()}", f"{self.rightDir}")
            self.update()
        except Exception as e:
            self.logs(e)

    def moveRightToLeftBtn(self):  # Перемещение справа налево
        try:
            shutil.move(f"{self.rightDir}/{self.rightList.currentItem().text()}", f"{self.leftDir}")
            self.update()
        except Exception as e:
            self.logs(e)

    def update(self):  # Обновление программы после любых изменений
        try:
            self.leftList.clear()
            self.path = self.leftComboBoxDrive.currentText()
            self.loadDir()
            self.leftList.addItems(self.files)
            self.leftDir = self.path

            self.rightList.clear()
            self.path = self.rightComboBoxDrive.currentText()
            self.loadDir()
            self.rightList.addItems(self.files)
            self.rightDir = self.path
        except Exception as e:
            self.logs(e)

    def openLeftFile(self):  # Открытие файлов с расширениями .txt и .py в левом списке
        try:
            os.system(f"{self.leftDir}/{self.leftList.currentItem().text()}")
        except Exception as e:
            self.logs(e)

    def openRightFile(self):  # Открытие файлов с расширениями .txt и .py в правом списке
        try:
            os.system(f"{self.leftDir}/{self.rightList.currentItem().text()}")
        except Exception as e:
            self.logs(e)

    @staticmethod
    def logs(e):  # Запись логов с ошибками
        from datetime import datetime

        with open("C:/Users/krist/Desktop/Project/total comander/logs.txt", "a") as file:
            file.write(f"[{datetime.now()}]: {e}\n")

    @staticmethod
    def infoHelp():  # Вывод справки
        print("""
                Для создания файла выберите тип файла в COMBOBOX(1) и напишите название(без расширений) в LINEEDIT(2) после нажмите кнопку CREATE

                Для удаления файла выберите файл в LISTWIDGET и нажмите кнопку REMOVE

                Для переименования файла выберите файл в LISTWIDGET, напишите новое имя в LINEEDIT(3), после нажмите кнопку RENAME 

                Для перемещения выберите файл в одном из LISTWIDGET, а во втором LISTWIDGET выберите путь куда переместите файл, после выберите с какого листа вы хотите переместить файл(4)
                ===================================================
                1-Если файл создается в левом LISTWIDGET, то выбирать расширения в левом COMBOBOX, иначе в правом COMBOBOX
                2-Если файл создается в левом LISTWIDGET, то писать имя файла в левом LINEEDIT, иначе в правом LINEEDIT
                3-Если файл переименовывается в левом LISTWIDGET, то писать новое имя файла в левом LINEEDIT, иначе в правом LINEEDIT
                4-I(L to R-файлы перемещаются с пути левого LISTWIDGET на правый LISTWIDGET), II(R to L-файлы перемещаются с правого LISTWIDGET на левый LISTWIDGET)
                ===================================================
                ВНИМАНИЕ! ПОСЛЕ КАЖДЫХ ИЗМЕНЕНИЙ ЗАЙДИТЕ В ЛЮБУЮ ПАПКУ И ВЕРНИТЕСЬ НАЗАД ДЛЯ ОБНОВЛЕНИЯ СПИСКОВ!
                """)

    @staticmethod
    def CssLoader():  # Подключение css стилей
        with open("css/style.css", "r") as read:
            style = read.read()
            read.close()
        return style
