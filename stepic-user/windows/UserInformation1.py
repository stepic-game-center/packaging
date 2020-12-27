# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInformation.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserInformationWindow(object):
    def setupUi(self, UserInformationWindow):
        UserInformationWindow.setObjectName("UserInformationWindow")
        UserInformationWindow.resize(1000, 800)
        UserInformationWindow.setMinimumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/游戏.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UserInformationWindow.setWindowIcon(icon)
        UserInformationWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(UserInformationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.level_Area = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.level_Area.sizePolicy().hasHeightForWidth())
        self.level_Area.setSizePolicy(sizePolicy)
        self.level_Area.setMinimumSize(QtCore.QSize(0, 0))
        self.level_Area.setStyleSheet("border: none;")
        self.level_Area.setWidgetResizable(True)
        self.level_Area.setAlignment(QtCore.Qt.AlignCenter)
        self.level_Area.setObjectName("level_Area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 591, 257))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.level = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.level.sizePolicy().hasHeightForWidth())
        self.level.setSizePolicy(sizePolicy)
        self.level.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.level.setFont(font)
        self.level.setAlignment(QtCore.Qt.AlignCenter)
        self.level.setObjectName("level")
        self.gridLayout.addWidget(self.level, 0, 0, 1, 1)
        self.change_Button = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.change_Button.sizePolicy().hasHeightForWidth())
        self.change_Button.setSizePolicy(sizePolicy)
        self.change_Button.setMinimumSize(QtCore.QSize(180, 30))
        self.change_Button.setMaximumSize(QtCore.QSize(180, 30))
        self.change_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_Button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.change_Button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.change_Button.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.change_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.change_Button.setArrowType(QtCore.Qt.NoArrow)
        self.change_Button.setObjectName("change_Button")
        self.gridLayout.addWidget(self.change_Button, 2, 0, 1, 1)
        self.exper = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.exper.sizePolicy().hasHeightForWidth())
        self.exper.setSizePolicy(sizePolicy)
        self.exper.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.exper.setObjectName("exper")
        self.gridLayout.addWidget(self.exper, 1, 0, 1, 1)
        self.level_Area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.level_Area, 0, 1, 1, 1)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(380, 200))
        self.logo.setMaximumSize(QtCore.QSize(380, 200))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../image/游戏大logo.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1)
        self.infornation_Area = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.infornation_Area.sizePolicy().hasHeightForWidth())
        self.infornation_Area.setSizePolicy(sizePolicy)
        self.infornation_Area.setStyleSheet("")
        self.infornation_Area.setWidgetResizable(True)
        self.infornation_Area.setAlignment(QtCore.Qt.AlignCenter)
        self.infornation_Area.setObjectName("infornation_Area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 976, 512))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.name_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.name_Edit.sizePolicy().hasHeightForWidth())
        self.name_Edit.setSizePolicy(sizePolicy)
        self.name_Edit.setReadOnly(True)
        self.name_Edit.setObjectName("name_Edit")
        self.gridLayout_3.addWidget(self.name_Edit, 0, 1, 1, 1)
        self.nick_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.nick_label.sizePolicy().hasHeightForWidth())
        self.nick_label.setSizePolicy(sizePolicy)
        self.nick_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nick_label.setObjectName("nick_label")
        self.gridLayout_3.addWidget(self.nick_label, 1, 0, 1, 1)
        self.name_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.gridLayout_3.addWidget(self.name_label, 0, 0, 1, 1)
        self.nick_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.nick_Edit.sizePolicy().hasHeightForWidth())
        self.nick_Edit.setSizePolicy(sizePolicy)
        self.nick_Edit.setObjectName("nick_Edit")
        self.gridLayout_3.addWidget(self.nick_Edit, 1, 1, 1, 1)
        self.birthday_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.birthday_label.sizePolicy().hasHeightForWidth())
        self.birthday_label.setSizePolicy(sizePolicy)
        self.birthday_label.setAlignment(QtCore.Qt.AlignCenter)
        self.birthday_label.setObjectName("birthday_label")
        self.gridLayout_3.addWidget(self.birthday_label, 3, 0, 1, 1)
        self.sex_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sex_label.sizePolicy().hasHeightForWidth())
        self.sex_label.setSizePolicy(sizePolicy)
        self.sex_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sex_label.setObjectName("sex_label")
        self.gridLayout_3.addWidget(self.sex_label, 2, 0, 1, 1)
        self.birthday_Edit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.birthday_Edit.sizePolicy().hasHeightForWidth())
        self.birthday_Edit.setSizePolicy(sizePolicy)
        self.birthday_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.birthday_Edit.setObjectName("birthday_Edit")
        self.gridLayout_3.addWidget(self.birthday_Edit, 3, 1, 1, 1)
        self.intro_Edit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.intro_Edit.sizePolicy().hasHeightForWidth())
        self.intro_Edit.setSizePolicy(sizePolicy)
        self.intro_Edit.setMinimumSize(QtCore.QSize(0, 0))
        self.intro_Edit.setObjectName("intro_Edit")
        self.gridLayout_3.addWidget(self.intro_Edit, 5, 1, 1, 1)
        self.sex_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sex_frame.sizePolicy().hasHeightForWidth())
        self.sex_frame.setSizePolicy(sizePolicy)
        self.sex_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sex_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sex_frame.setObjectName("sex_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sex_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.man_radio = QtWidgets.QRadioButton(self.sex_frame)
        self.man_radio.setObjectName("man_radio")
        self.horizontalLayout.addWidget(self.man_radio)
        self.woman_radio = QtWidgets.QRadioButton(self.sex_frame)
        self.woman_radio.setObjectName("woman_radio")
        self.horizontalLayout.addWidget(self.woman_radio)
        self.gridLayout_3.addWidget(self.sex_frame, 2, 1, 1, 1)
        self.phone_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.phone_Edit.sizePolicy().hasHeightForWidth())
        self.phone_Edit.setSizePolicy(sizePolicy)
        self.phone_Edit.setObjectName("phone_Edit")
        self.gridLayout_3.addWidget(self.phone_Edit, 4, 1, 1, 1)
        self.intro_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.intro_label.sizePolicy().hasHeightForWidth())
        self.intro_label.setSizePolicy(sizePolicy)
        self.intro_label.setAlignment(QtCore.Qt.AlignCenter)
        self.intro_label.setObjectName("intro_label")
        self.gridLayout_3.addWidget(self.intro_label, 5, 0, 1, 1)
        self.phone_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.phone_label.sizePolicy().hasHeightForWidth())
        self.phone_label.setSizePolicy(sizePolicy)
        self.phone_label.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_label.setObjectName("phone_label")
        self.gridLayout_3.addWidget(self.phone_label, 4, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.action = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.action.sizePolicy().hasHeightForWidth())
        self.action.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.action.setFont(font)
        self.action.setObjectName("action")
        self.verticalLayout.addWidget(self.action)
        self.score_table = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.score_table.sizePolicy().hasHeightForWidth())
        self.score_table.setSizePolicy(sizePolicy)
        self.score_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.score_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.score_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.score_table.setRowCount(0)
        self.score_table.setColumnCount(3)
        self.score_table.setObjectName("score_table")
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.score_table)
        self.score_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.score_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.gridLayout_3.addWidget(self.frame, 0, 2, 6, 1)
        self.infornation_Area.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.infornation_Area, 1, 0, 1, 2)
        UserInformationWindow.setCentralWidget(self.centralwidget)

        self.setWindowOpacity(0.95)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.retranslateUi(UserInformationWindow)
        QtCore.QMetaObject.connectSlotsByName(UserInformationWindow)

    def retranslateUi(self, UserInformationWindow):
        _translate = QtCore.QCoreApplication.translate
        UserInformationWindow.setWindowTitle(_translate("UserInformationWindow", "Stepic"))
        self.level.setText(_translate("UserInformationWindow", "1  级"))
        self.change_Button.setText(_translate("UserInformationWindow", "修改个人信息"))
        self.exper.setText(_translate("UserInformationWindow", "经验条"))
        self.nick_label.setText(_translate("UserInformationWindow", "用户昵称："))
        self.name_label.setText(_translate("UserInformationWindow", "用户名："))
        self.birthday_label.setText(_translate("UserInformationWindow", "用户生日："))
        self.sex_label.setText(_translate("UserInformationWindow", "用户性别："))
        self.man_radio.setText(_translate("UserInformationWindow", "男"))
        self.woman_radio.setText(_translate("UserInformationWindow", "女"))
        self.intro_label.setText(_translate("UserInformationWindow", "个人简介："))
        self.phone_label.setText(_translate("UserInformationWindow", "电话号码："))
        self.action.setText(_translate("UserInformationWindow", "最近动态"))
        item = self.score_table.horizontalHeaderItem(0)
        item.setText(_translate("UserInformationWindow", "游戏名"))
        item = self.score_table.horizontalHeaderItem(1)
        item.setText(_translate("UserInformationWindow", "游戏得分"))
        item = self.score_table.horizontalHeaderItem(2)
        item.setText(_translate("UserInformationWindow", "游玩日期"))
