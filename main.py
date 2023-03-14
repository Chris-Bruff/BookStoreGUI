from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import pandas as pd
from PyQt5 import QtWidgets

class Login(QMainWindow):
    def __init__(self):

        self.df_users = pd.read_excel('users.xlsx')
        self.df_BookOrder = pd.read_excel('BookOrder.xlsx' )
        super(Login,self).__init__()
        uic.loadUi('sign_in.ui', self)

        self.show()
        self.log_in.clicked.connect(self.loginPress)


    def loginPress(self):

        self.close()
        self.df_users = pd.read_excel('users.xlsx')
        try:
            currUser = self.le_username.text()
            currPass = self.le_password.text()
            print('test1')

            dfAdmin = self.df_users.loc[self.df_users.admin == True]
            print('test2')
            dfCurr = self.df_users.loc[self.df_users.username == currUser]
            print('test3')

            names = self.df_users.loc[(self.df_users.username == currUser) & (self.df_users.password == currPass)]
            print('test4')
            if len(names)>0:
                print('ok')

                if dfCurr.equals(dfAdmin):
                    self.adminFunc()

                else:
                    self.userFunc()
            else:
                print('not ok')
                uic.loadUi('sign_in.ui', self)
                #self.show

        except Exception as e:
            print(e)


    def adminFunc(self):
        print('adminFunc')
        try:
            super(Login, self).__init__()
            uic.loadUi('admin_screen.ui', self)
            self.show()
            self.le_books.clicked.connect(self.manageBooks)
            self.le_orders.clicked.connect(self.manageOrders)
            self.le_users.clicked.connect(self.manageUsers)
        except Exception as e:
            print(e)

    def userFunc(self):
        print('userFunc')

        super(Login, self).__init__()
        uic.loadUi('user_screen.ui', self)
        self.show()
        self.le_books.clicked.connect(self.manageBooks)
        self.le_orders.clicked.connect(self.manageOrders)

    def manageBooks(self):
        try:
            self.book_gui = UsersGui()
        except Exception as e:
            print(e)

    def manageUsers(self):
        try:
            self.user_gui = manageUsers()
        except Exception as e:
            print(e)

    def manageOrders(self):
        try:
            self.orders_gui = manageOrders()
        except Exception as e:
            print(e)

class manageUsers(QMainWindow):
    def __init__(self):
            super(manageUsers, self).__init__()
            self.id = 0
            uic.loadUi('user_Managment.ui', self)

            self.id = id
            self.loadUser()
            self.df_users = pd.read_excel('users.xlsx', sheet_name='users')

            self.le_search.textChanged.connect(self.loadUser)

            self.addbtn.clicked.connect(self.newUser)
            self.updatebtn.clicked.connect(self.updateUser)
            self.detebtn.clicked.connect(self.delete)
            self.show()

    def loadUser(self):
        self.df_users = pd.read_excel('users.xlsx', sheet_name='users')
        self.tableWidget.setRowCount(len(self.df_users))
        self.tableWidget.setColumnCount(4)
        row_index = 0
        self.tableWidget.setHorizontalHeaderLabels(('username','password','admin','id'))
        searchText = self.le_search.text()
        self.df_users = self.df_users[(self.df_users.username.str.contains(searchText) | self.df_users.password.str.contains(searchText))].reset_index(drop=True)

        for user in range(len(self.df_users)):
                print(user)
                self.tableWidget.setItem(row_index,0,QTableWidgetItem(str(self.df_users.iloc[user,0])))
                self.tableWidget.setItem(row_index,1,QTableWidgetItem(str(self.df_users.iloc[user,1])))
                self.tableWidget.setItem(row_index,2,QTableWidgetItem(str(self.df_users.iloc[user,2])))
                self.tableWidget.setItem(row_index,3,QTableWidgetItem(str(self.df_users.iloc[user,3])))
                row_index +=1


    def newUser(self):
        try:
            self.df_users = pd.read_excel('users.xlsx', sheet_name='users')
            currUser = self.le_user.text()
            currPass = self.le_pass.text()

            names = self.df_users.loc[(self.df_users.username == currUser)]

            print('names list')
            print(names)

            if(len(names) > 0):
                mb = QMessageBox()
                mb.setWindowTitle('Invalid user')
                mb.setText('User exists, please choose another')
                mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                res = mb.exec()
                return 0

            currID = len(self.df_users) + 1
            self.df_users.loc[len(self.df_users.index)] = [currUser,currPass,False,currID]
            print(self.df_users)
            self.df_users.to_excel('users.xlsx', sheet_name='users', index=False)
            self.close()
        except Exception as e:
            print(e)

    def updateUser(self):
        try:

            mb = QMessageBox()
            mb.setWindowTitle('you will update user')
            mb.setText('Are you sure?')
            mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            res = mb.exec()
            print('update user')
            self.df_users = pd.read_excel('users.xlsx', sheet_name='users')
            currUser = self.le_user.text()
            currPass = self.le_pass.text()

            updateU = self.le_U_Update.text()
            updateP = self.le_P_Update.text()
            self.df_users.replace(to_replace=self.le_user.text(), value=self.le_U_Update.text(), inplace=True)
            self.df_users.replace(to_replace=self.le_pass.text(), value=self.le_P_Update.text(), inplace=True)
            self.df_users.to_excel('users.xlsx', sheet_name='users', index=False)
            self.close()
        except Exception as e:
            print(e)


    def delete(self):
            self.df_users = pd.read_excel('users.xlsx', sheet_name='users')
            currUser = self.le_user.text()
            currPass = self.le_pass.text()
            ###
            # I am having trouble filtering.
            # I am trying to find the index and then iloc in the delete function.
            ###
            names = self.df_users.loc[(self.df_users.username == currUser) & (self.df_users.password == currPass)].index
            print(names)


            if(len(names) > 0):

                    mb = QMessageBox()
                    mb.setWindowTitle('Are you sure?')
                    mb.setText('The user will be removed!')
                    mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    res = mb.exec()
                    try:
                        if res == QMessageBox.Ok:
                            #print('exec')
                            self.df_users = self.df_users.drop(names[0])  # edits only this user

                            self.df_users.to_excel('users.xlsx', sheet_name='users', index=False)
                        #iloc
                    except Exception as e:
                        print(e)
                    return 0
            else:
                mb = QMessageBox()
                mb.setWindowTitle('Invalid User')
                mb.setText('The user does not exist')
                mb.setStandardButtons(QMessageBox.Ok )
                res = mb.exec()
                return 0


class manageOrders(QMainWindow):
    def __init__(self):
        super(manageOrders, self).__init__()
        self.id = 0
        uic.loadUi('Order_Managment.ui', self)
        self.loadUser()
        self.df_users = pd.read_excel('BookOrder.xlsx')
        self.addbtn.clicked.connect(self.newOrder)
        self.updatebtn.clicked.connect(self.updateOrder)
        self.detebtn.clicked.connect(self.deleteOrder)
        self.show()

    def loadUser(self):
        self.df_users = pd.read_excel('BookOrder.xlsx')
        self.tableWidget.setRowCount(len(self.df_users))
        self.tableWidget.setColumnCount(4)
        row_index = 0
        self.tableWidget.setHorizontalHeaderLabels(('customer_name','total_price','date','book_id'))
        for user in range(len(self.df_users)):
                print(user)
                self.tableWidget.setItem(row_index,0,QTableWidgetItem(str(self.df_users.iloc[user,0])))
                self.tableWidget.setItem(row_index,1,QTableWidgetItem(str(self.df_users.iloc[user,1])))
                self.tableWidget.setItem(row_index,2,QTableWidgetItem(str(self.df_users.iloc[user,2])))
                self.tableWidget.setItem(row_index,3,QTableWidgetItem(str(self.df_users.iloc[user,3])))
                row_index +=1


    def newOrder(self):
        print('new user')
    def updateOrder(self):
        print('update user')
    def deleteOrder(self):
        print('delete user')


class ShowUserGui(QMainWindow):

        def __init__(self, id, parent):#store id as an attribute
           # try:
                super(ShowUserGui,self).__init__()
                uic.loadUi('show_user.ui', self)
                self.id = id #the current user being selected
                self.parent = parent
                self.df_users = pd.read_excel('Assignment4.xlsx', sheet_name='users')
                self.user = self.df_users.loc[self.df_users.id == id].reset_index()
                self.le_noBooks.setText(str(self.user.no_books[0]))
                self.le_bookprice.setText(str(self.user.password[0]))
                self.le_username.setText(str(self.user.username[0]))
                self.le_author.setText(str(self.user.author[0]))
                self.lbl_photo.setPixmap(QPixmap(str(self.user.photo_path[0])))
                self.lbl_photo.setFixedWidth(400)
                self.lbl_photo.setFixedHeight(400)
                self.photo_path = self.user.photo_path[0]
                self.show()

                #currUser = self.le_username.text()
                #currPass = self.le_password.text()


                self.btn_update.clicked.connect(self.update)
                self.btn_delete.clicked.connect(self.delete)
                self.btn_browse.clicked.connect(self.browse)

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
                if (len(title) == 0 or len(author) == 0 or len(noBooks) == 0 or len(price) == 0 ):
                    mb = QMessageBox()
                    mb.setWindowTitle('empty data')
                    mb.setText('please fill in all the information')
                    mb.setStandardButtons(QMessageBox.Ok)
                    res = mb.exec()
                    if res == QMessageBox.Ok:
                        return 0
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
        uic.loadUi('book.ui', self)
        # self.user_labels = []
        self.row_length = 6
        self.le_search.textChanged.connect(self.load_users_data)
        self.addBookBtn.clicked.connect(self.addBook)
        self.show()
        self.load_users_data()
    def load_users_data(self):
        # for label in self.user_labels:
        #     label.setParent(None)
        while self.layout_users.count():
            self.layout_users.itemAt(0).widget().setParent(None)
        self.df_users = pd.read_excel('Assignment4.xlsx', sheet_name='users')

        searchText = self.le_search.text()
        self.df_users = self.df_users[(self.df_users.username.str.contains(searchText) |
                                       self.df_users.author.str.contains(searchText))].reset_index(drop=True)

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

    def addBook(self):
         try:
            self.close()
            print('book')
            self.show_addBook = addBook()
         except Exception as e:
            print(e)


    def show_user(self, id):#new window
        self.show_user_gui = ShowUserGui(id,self)#creates new window, self of the object of this class
        # (id,self) this self refers to the object of the userGUI/ working class
        self.load_users_data()


class addBook(QMainWindow):
        def __init__(self):
            super(addBook, self).__init__()
            uic.loadUi('newBook.ui', self)
            self.show()
            #self.load_users_data()

            bookName = self.le_username.text()
            bookPrice = self.le_bookprice.text()
            noBooks = self.le_noBooks.text()
            author = self.le_author.text()

            self.btn_browse.clicked.connect(self.browse)
            self.btn_update.clicked.connect(self.update)

            self.df_users = pd.read_excel('Assignment4.xlsx', sheet_name='users')

        def browse(self):
            #currPhoto = self.photo_path
            file = QFileDialog.getOpenFileName(self, 'Chose an image', '', 'PNG Files (*.png)')
            if file[0]:
                self.photo_path = file[0]



        def update(self):
            try:
                title = self.le_username.text()#gets texts
                author = self.le_author.text()
                noBooks = self.le_noBooks.text()
                price = self.le_bookprice.text()
                currID = len(self.df_users) + 1


                if (len(title) == 0 or len(author) == 0 or len(noBooks) == 0 or len(price) == 0 ):
                    mb = QMessageBox()
                    mb.setWindowTitle('empty data')
                    mb.setText('please fill in all the information')
                    mb.setStandardButtons(QMessageBox.Ok)
                    res = mb.exec()
                    if res == QMessageBox.Ok:
                        return 0
                print(self.df_users)
                currPhoto = self.photo_path

                self.df_users.loc[len(self.df_users.index)] = [currID,title,price,currPhoto,author,noBooks]

                #sends data back to excel
                print(self.df_users)
                self.df_users.to_excel('Assignment4.xlsx', sheet_name='users', index=False)
                #makes pathway to user data linked to the parent
                #self.parent.load_users_data()
                self.close()
            except Exception as e:
                print(e)


app = QApplication([])
window = Login()
app.exec()