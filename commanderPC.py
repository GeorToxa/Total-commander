from PyQt5.QtWidgets import QComboBox, QLineEdit, QListWidget, QPushButton, QWidget
import os, shutil, win32api


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Window Options
        self.setFixedSize(1000, 612)  # Window size
        self.setWindowTitle("Total Commander MEGA VERSION!!! - NOT REGISTERED - 2022 EDITION")  # Window title
        self.setStyleSheet(self.CssLoader())  # Load CSS style in window

        # Working with disks
        self.drives = win32api.GetLogicalDriveStrings()  # Getting information about disks
        self.drives = self.drives.split('\000')[:-1]  # Disk Data Conversion

        # Directory variables
        self.leftDir = ""
        self.rightDir = ""
        self.types = ["folder", ".py", ".txt"]  # List of file extensions
        self.types2 = ".py.txt.exe.zip.rar"  # File extension string

        # Widgets

        # Creating combo boxes
        self.leftComboBoxDrive = QComboBox(self)  # Creating a left combo box with disks
        self.rightComboBoxDrive = QComboBox(self)  # Creating a right combo box with disks
        self.leftComboBoxType = QComboBox(self)  # Creating a left combo box with extensions
        self.rightComboBoxType = QComboBox(self)  # Creating a right combo box with extensions

        # Combo box layout
        self.leftComboBoxDrive.move(10, 30)  # Setting the position of the left combo box with disks
        self.rightComboBoxDrive.move(540, 30)  # Setting the position of the right combo box with disks
        self.leftComboBoxType.move(10, 575)  # Setting the position of the left combo box with extensions
        self.rightComboBoxType.move(540, 575)  # Setting the position of the right combo box with extensions

        # Sizing combo boxes
        self.leftComboBoxDrive.setFixedSize(69, 22)  # Setting the size of the left combo box with disks
        self.rightComboBoxDrive.setFixedSize(69, 22)  # Setting the size of the right combo box with disks
        self.leftComboBoxType.setFixedSize(69, 22)  # Setting the size of the left combo box with extensions
        self.rightComboBoxType.setFixedSize(69, 22)  # Setting the size of the right combo box with extensions

        # Show combo boxes
        self.leftComboBoxDrive.show()  # Showing the left combo box with disks
        self.rightComboBoxDrive.show()  # Showing the right combo box with disks
        self.leftComboBoxType.show()  # Show left combo box with extensions
        self.rightComboBoxType.show()  # Show right combo box with extensions

        # Creating lists
        self.leftList = QListWidget(self)  # Creating the left list
        self.rightList = QListWidget(self)  # Creating the right list

        # Lists layout
        self.leftList.move(10, 60)  # Setting the position of the left list
        self.rightList.move(540, 60)  # Setting the position of the right list

        # Sizing lists
        self.leftList.setFixedSize(450, 500)  # Setting the size of the left list
        self.rightList.setFixedSize(450, 500)  # Setting the size of the right list

        # Show lists
        self.leftList.show()  # Showing the left list
        self.rightList.show()  # Showing the right list

        # Creating input lines
        self.leftInputLine = QLineEdit(self)  # Creating the left input line
        self.rightInputLine = QLineEdit(self)  # Creating the right input line

        # Input lines layout
        self.leftInputLine.move(85, 575)  # Setting the position of the left input line
        self.rightInputLine.move(615, 575)  # Setting the position of the right input line

        # Sizing input lines
        self.leftInputLine.setFixedSize(100, 22)  # Setting the size of the left input line
        self.rightInputLine.setFixedSize(100, 22)  # Setting the size of the right input line

        # Show input lines
        self.leftInputLine.show()  # Showing the left input line
        self.rightInputLine.show()  # Showing the right input line

        # Creating buttons
        self.createBtn = QPushButton("Create", self)  # Creating a create button
        self.removeBtn = QPushButton("Remove", self)  # Creating a remove button
        self.renameBtn = QPushButton("Rename", self)  # Creating a rename button
        self.leftToRightBtn = QPushButton("L to R", self)  # Creating a move "left-to-right" button
        self.rightToLeftBtn = QPushButton("R to L", self)  # Creating a move "right-to-left" button
        self.openBtn = QPushButton("Open", self)  # Creating an open files button
        self.copyLeftLinkBtn = QPushButton("Copy", self)  # Creating a left copy link button
        self.copyRightLinkBtn = QPushButton("Copy", self)  # Creating a right copy link button

        # Buttons layout
        self.createBtn.move(475, 100)  # Setting the position of the create button
        self.removeBtn.move(475, 175)  # Setting the position of the remove button
        self.renameBtn.move(475, 250)  # Setting the position of the rename button
        self.leftToRightBtn.move(475, 325)  # Setting the position of the move "left-to-right" button
        self.rightToLeftBtn.move(475, 400)  # Setting the position of the move "right-to-left" button
        self.openBtn.move(475, 475)  # Setting the position of the open files button
        self.copyLeftLinkBtn.move(400, 30)  # Setting the position of the left copy link button
        self.copyRightLinkBtn.move(930, 30)  # Setting the position of the right copy link button

        # Buttons sizing
        self.createBtn.setFixedSize(50, 50)  # Setting the size of the create button
        self.removeBtn.setFixedSize(50, 50)  # Setting the size of the remove button
        self.renameBtn.setFixedSize(50, 50)  # Setting the size of the rename button
        self.leftToRightBtn.setFixedSize(50, 50)  # Setting the size of the move "left-to-right" button
        self.rightToLeftBtn.setFixedSize(50, 50)  # Setting the size of the move "right-to-left" button
        self.openBtn.setFixedSize(50, 50)  # Setting the size of the open files button
        self.copyLeftLinkBtn.setFixedSize(60, 22)  # Setting the size of the left copy link button
        self.copyRightLinkBtn.setFixedSize(60, 22)  # Setting the size of the right copy link button

        # Show buttons
        self.createBtn.show()  # Showing the create button
        self.removeBtn.show()  # Showing the remove button
        self.renameBtn.show()  # Showing the rename button
        self.leftToRightBtn.show()  # Showing the move "left-to-right" button
        self.rightToLeftBtn.show()  # Showing the move "right-to-left" button
        self.openBtn.hide()  # Hiding the open files button
        self.copyLeftLinkBtn.show()  # Showing the left copy link button
        self.copyRightLinkBtn.show()  # Showing the right copy link button

        # Events
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
        self.rightToLeftBtn.clicked.connect(self.moveRightToLeftBtn)
        self.leftList.clicked.connect(self.checker)
        self.rightList.clicked.connect(self.checker)
        self.openBtn.clicked.connect(self.openFile)
        self.copyLeftLinkBtn.clicked.connect(self.clipboardLeft)
        self.copyRightLinkBtn.clicked.connect(self.clipboardRight)

    # Event handlers
    def checker(self):  # Type check: folder or file
        try:
            if os.path.isfile(self.leftDir + "/" + self.leftList.currentItem().text()) or os.path.isfile(self.rightDir + "/" + self.rightList.currentItem().text()):
                self.openBtn.show()
            else:
                self.openBtn.hide()
        except:
            self.openBtn.hide()

    def loadDir(self):  # Upload folder files to the selected path
        self.files_with = ["..."]
        self.files = []
        fileList = os.listdir(os.chdir(self.path))
        for i in fileList:
            if i.startswith("$"):
                pass
            else:
                self.files.append(i)
        self.files_with += self.files

    def loadDefaultDir(self):  # Default loading of files to lists
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

    def chooseLeftComboDir(self):  # Uploading files to the left list depending on the selected drive
        try:
            self.leftList.clear()
            self.path = self.leftComboBoxDrive.currentText()
            self.loadDir()
            self.leftList.addItems(self.files)
            self.leftDir = self.path
        except Exception as e:
            self.logs(e)

    def chooseRightComboDir(self):  # Uploading files to the right list depending on the selected drive
        try:
            self.rightList.clear()
            self.path = self.rightComboBoxDrive.currentText()
            self.loadDir()
            self.rightList.addItems(self.files)
            self.rightDir = self.path
        except Exception as e:
            self.logs(e)

    def chooseLeftListDir(self):  # Navigating folders in the left list
        try:
            if os.path.isdir(self.leftDir + "/" + self.leftList.currentItem().text()):
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
                    self.path = f"{os.getcwd()}/{self.leftList.currentItem().text()}"
                    self.leftList.clear()
                    self.loadDir()
                    self.leftList.addItems(self.files_with)
                self.leftDir = self.path
        except Exception as e:
            self.logs(e)

    def chooseRightListDir(self):  # Navigating folders in the right list
        try:
            if os.path.isdir(self.rightDir + "/" + self.rightList.currentItem().text()):
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
                    self.path = f"{os.getcwd()}/{self.rightList.currentItem().text()}"
                    self.rightList.clear()
                    self.loadDir()
                    self.rightList.addItems(self.files_with)
                self.rightDir = self.path
        except Exception as e:
            self.logs(e)

    def createFileBtn(self):  # Creating files and folders
        try:
            if self.leftInputLine.text() != "":
                if self.leftComboBoxType.currentText() == "folder":
                    os.mkdir(f"{self.leftDir}/{self.leftInputLine.text()}")
                else:
                    with open(f"{self.leftDir}/{self.leftInputLine.text()}{self.leftComboBoxType.currentText()}",
                              "w") as file:
                        file.write("")
            if self.rightInputLine.text() != "":
                if self.rightComboBoxType.currentText() == "folder":
                    os.mkdir(f"{self.rightDir}/{self.rightInputLine.text()}")
                else:
                    with open(f"{self.rightDir}/{self.rightInputLine.text()}{self.rightComboBoxType.currentText()}",
                              "w") as file:
                        file.write("")
            self.update()
        except Exception as e:
            self.logs(e)

    def removeFileBtn(self):  # Deleting files and folders
        try:
            if os.path.isfile(f"{self.leftDir}/{self.leftList.currentItem().text()}"):
                os.remove(f"{self.leftDir}/{self.leftList.currentItem().text()}")

            if os.path.isfile(f"{self.rightDir}/{self.rightList.currentItem().text()}"):
                os.remove(f"{self.rightDir}/{self.rightList.currentItem().text()}")

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

    def renameFileBtn(self):  # Renaming files and folders
        try:
            if self.leftList.currentItem():
                os.rename(f"{self.leftDir}/{self.leftList.currentItem().text()}",
                          f"{self.leftDir}/{self.leftInputLine.text()}")
            elif self.rightList.currentItem():
                os.rename(f"{self.rightDir}/{self.rightList.currentItem().text()}",
                          f"{self.rightDir}/{self.rightInputLine.text()}")
            self.update()
        except Exception as e:
            self.logs(e)

    def moveLeftToRightBtn(self):  # Moving "left-to-right"
        try:
            shutil.move(f"{self.leftDir}/{self.leftList.currentItem().text()}",
                        f"{self.rightDir}")
            self.update()
        except Exception as e:
            self.logs(e)

    def moveRightToLeftBtn(self):  # Moving "right-to-left"
        try:
            shutil.move(f"{self.rightDir}/{self.rightList.currentItem().text()}",
                        f"{self.leftDir}")
            self.update()
        except Exception as e:
            self.logs(e)

    def update(self):  # Updating after any operation in program
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

    def openFile(self):  # Opening files with extensions
        try:
            if os.path.isfile(self.leftDir + "/" + self.leftList.currentItem().text()):
                os.system(f"{self.leftDir}/{self.leftList.currentItem().text()}")
            elif os.path.isfile(self.rightDir + "/" + self.rightList.currentItem().text()):
                os.system(f"{self.rightDir}/{self.rightList.currentItem().text()}")
        except Exception as e:
            self.logs(e)

    def clipboardLeft(self):  # Copying left directory link to clipboard
        import win32clipboard

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        try:
            if self.leftList.currentItem().text() != "":
                win32clipboard.SetClipboardText(f"{self.leftDir}/{self.leftList.currentItem().text()}")
            elif self.leftList.currentItem().text() == "":
                win32clipboard.SetClipboardText(self.leftDir)
            win32clipboard.CloseClipboard()
        except Exception as e:
            self.logs(e)

    def clipboardRight(self):  # Copying right directory link to clipboard
        import win32clipboard

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        try:
            if self.rightList.currentItem().text() != "":
                win32clipboard.SetClipboardText(f"{self.rightDir}/{self.rightList.currentItem().text()}")
            elif self.rightList.currentItem().text() == "":
                win32clipboard.SetClipboardText(self.rightDir)
        except Exception as e:
            self.logs(e)

    @staticmethod
    def logs(e):  # Writing logs with errors
        from datetime import datetime

        with open("C:/Users/krist/Desktop/Project/total comander/logs.txt", "a") as file:
            file.write(f"[{datetime.now()}]: {e}\n")

    @staticmethod
    def infoHelp():  # Printing info
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
    def CssLoader():  # Adding css styles
        with open("css/style.css", "r") as read:
            style = read.read()
            read.close()
        return style
