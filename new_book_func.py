from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import pandas as pd

class ShowUserGui(QMainWindow):

    def __init__(self,parent, id = None):
        super(ShowUserGui,self).__init__()
        uic.loadUi('show_user.ui', self)
        self.id = id
        self.parent = parent
        self.df_users = pd.read_excel('Assignment4.xlsx', sheet_name='users')
        self.btn_browse.clicked.connect(self.browse)
        self.lbl_photo.setFixedWidth(300)
        self.lbl_photo.setFixedHeight(300)

        if id:
            self.setWindowTitle(f'User {id}')
            self.user = self.df_users.loc[self.df_users.id == id].reset_index()
            self.le_username.setText(str(self.user.username[0]))
            self.le_password.setText(str(self.user.password[0]))
            self.photo_path = str(self.user.photo_path[0])
            self.lbl_photo.setPixmap(QPixmap(self.photo_path))

            self.btn_delete.clicked.connect(self.delete)
            self.btn_save.clicked.connect(self.update)
        else:
            self.btn_delete.setVisible(False)
            self.btn_save.setText('Add New User')
            self.btn_save.clicked.connect(self.add)
            self.photo_path = 'images/default.png'
            self.lbl_photo.setPixmap(QPixmap(self.photo_path))

        self.show()
          #  except Exception as e:
               # print(e)



        def browse(self):
            #currPhoto = self.photo_path
            file = QFileDialog.getOpenFileName(self, 'Chose an image', '', 'PNG Files (*.png)')
            if file[0]:
                self.photo_path = file[0]
                self.lbl_photo.setPixmap(QPixmap(self.photo_path))

        def delete(self):
            mb = QMessageBox()
            mb.setWindowTitle('Are you sure?')
            mb.setText('The user will be removed!')
            mb.setIcon(QMessageBox.Warning)  # Warning, Critical, Information, Question
            # mb.setInformativeText('This is informative text.')
            # mb.setDetailedText('This is detailed text.')
            mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            res = mb.exec()
            if res == QMessageBox.Ok:
                self.df_users = self.df_users[self.df_users.id !=self.id] #edits only this user
            #
            self.df_users.to_excel('Assignment4.xlsx', sheet_name='users')
            self.parent.load_users_data()
            self.close()


        def update(self):
            try:
                title = self.le_username.text()#gets texts
                author = self.le_author.text()
                noBooks = self.le_noBooks.text()
                price = self.le_bookprice.text()
                currPhoto = self.photo_path
                self.df_users.loc[self.df_users.id == self.id, ['username', 'password','no_books','photo_path','author']] = [title,price, noBooks,currPhoto,author]
                #sends data back to excel
                self.df_users.to_excel('Assignment4.xlsx', sheet_name='users',index = False)
                #makes pathway to user data linked to the parent
                self.parent.load_users_data()
                self.close()
            except Exception as e:
                print(e)


class UsersGui(QMainWindow):

    def __init__(self):
        super(UsersGui,self).__init__()
        uic.loadUi('users_photo.ui', self)
        # self.user_labels = []
        self.row_length = 6
        self.show()
        self.load_users_data()

        self.addBookbtn.clicked.connect(self.addBook)

    def addBook(self):
         try:
            print('book')
            self.show_addBook = addBook()
         except Exception as e:
            print(e)

    def load_users_data(self):
        # for label in self.user_labels:
        #     label.setParent(None)
        while self.layout_users.count():
            self.layout_users.itemAt(0).widget().setParent(None)
        self.df_users = pd.read_excel('Assignment4.xlsx', sheet_name='users')
        row_index = -1
        for i in range(len(self.df_users)):
            column_index = i % self.row_length
            if column_index == 0:
                row_index += 1

            user = QLabel()
            user.setPixmap(QPixmap(self.df_users.photo_path[i]))
            user.setScaledContents(True)
            user.setFixedWidth(300)
            user.setFixedHeight(300)
            user.mousePressEvent = lambda e, id = self.df_users.id[i]: self.show_user(id)
            # self.user_labels.append(user)
            self.layout_users.addWidget(user, row_index, column_index)



    def show_user(self, id):#new window
        self.show_user_gui = ShowUserGui(id,self)#creates new window, self of the object of this class
        # (id,self) this self refers to the object of the userGUI/ working class
        self.load_users_data()





app = QApplication([])
window = UsersGui()
app.exec()
