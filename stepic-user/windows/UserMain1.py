# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserMainWindow(object):
    def setupUi(self, UserMainWindow):
        UserMainWindow.setObjectName("UserMainWindow")
        UserMainWindow.resize(1000, 750)
        UserMainWindow.setMinimumSize(QtCore.QSize(500, 500))
        UserMainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/游戏.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UserMainWindow.setWindowIcon(icon)
        UserMainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(UserMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Leaderboard_Area = QtWidgets.QScrollArea(self.centralwidget)
        self.Leaderboard_Area.setStyleSheet("border: none;")
        self.Leaderboard_Area.setWidgetResizable(True)
        self.Leaderboard_Area.setObjectName("Leaderboard_Area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Leaderboard = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Leaderboard.sizePolicy().hasHeightForWidth())
        self.Leaderboard.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.Leaderboard.setFont(font)
        self.Leaderboard.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Leaderboard.setObjectName("Leaderboard")
        self.gridLayout_3.addWidget(self.Leaderboard, 0, 0, 1, 1)
        self.menu_Button = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.menu_Button.sizePolicy().hasHeightForWidth())
        self.menu_Button.setSizePolicy(sizePolicy)
        self.menu_Button.setMinimumSize(QtCore.QSize(131, 31))
        self.menu_Button.setMaximumSize(QtCore.QSize(131, 31))
        self.menu_Button.setIcon(icon)
        self.menu_Button.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.menu_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.menu_Button.setObjectName("menu_Button")

        self.menu_Button.setAutoRaise(True)
        self.menu = QtWidgets.QMenu()

        self.information = QtWidgets.QAction('查看我的个人资料', parent=self.menu)
        self.logout = QtWidgets.QAction('注销帐户:', parent=self.menu)
        self.exit = QtWidgets.QAction('退出系统', parent=self.menu)

        self.menu.addAction(self.information)
        self.menu.addAction(self.logout)
        self.menu.addSeparator()
        self.menu.addAction(self.exit)
        self.menu_Button.setMenu(self.menu)

        self.gridLayout_3.addWidget(self.menu_Button, 0, 1, 1, 1)
        self.score_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.score_table.sizePolicy().hasHeightForWidth())
        self.score_table.setSizePolicy(sizePolicy)
        self.score_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.score_table.setObjectName("score_table")
        self.score_table.setColumnCount(4)
        self.score_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(3, item)
        self.gridLayout_3.addWidget(self.score_table, 1, 0, 1, 1)
        self.score_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.score_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.Leaderboard_Area.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.Leaderboard_Area, 0, 1, 2, 1)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMinimumSize(QtCore.QSize(400, 200))
        self.logo.setMaximumSize(QtCore.QSize(400, 200))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../image/游戏大logo.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.gridLayout_2.addWidget(self.logo, 0, 0, 2, 1)
        self.Game_Area = QtWidgets.QScrollArea(self.centralwidget)
        self.Game_Area.setWidgetResizable(True)
        self.Game_Area.setObjectName("Game_Area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        url = "https://stepic-api.redcountry.top/api/game/query_all_pub"
        r = requests.post(url=url, data="")
        games = json.loads(r.text)

        self.game_Button = []
        index = 0
        maxX = 10
        for game in games:
            game_Button = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
            game_Button.setMinimumSize(QtCore.QSize(101, 171))
            game_Button.setMaximumSize(QtCore.QSize(101, 171))
            game_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            game_Button.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
            game_Button.setLayoutDirection(QtCore.Qt.LeftToRight)
            game_Button.setStyleSheet("background-color: rgb(245, 245, 245); border-radius: 5px; opacity: 0.8;\n"
                                      "box-shadow: rgb(0,0,0) 3px 3px 3px;")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("../image/game/" + game['image'].split('/')[-1]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            game_Button.setIcon(icon1)
            game_Button.setIconSize(QtCore.QSize(100, 150))
            game_Button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            game_Button.setObjectName("game_Button_" + str(game['gid']))
            self.game_Button.append(game_Button)
            self.gridLayout.addWidget(game_Button, index // maxX, index % maxX, 1, 1)

            index += 1

        self.setWindowOpacity(0.95)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.Game_Area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.Game_Area, 2, 0, 1, 2)
        self.Game_Area.raise_()
        self.logo.raise_()
        self.Leaderboard_Area.raise_()

        UserMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserMainWindow)
        QtCore.QMetaObject.connectSlotsByName(UserMainWindow)

    def retranslateUi(self, UserMainWindow):
        _translate = QtCore.QCoreApplication.translate
        UserMainWindow.setWindowTitle(_translate("UserMainWindow", "Stepic"))
        self.menu_Button.setText(_translate("UserMainWindow", "..."))
        self.Leaderboard.setText(_translate("UserMainWindow", "排行榜"))
        item = self.score_table.horizontalHeaderItem(0)
        item.setText(_translate("UserMainWindow", "游戏名"))
        item = self.score_table.horizontalHeaderItem(1)
        item.setText(_translate("UserMainWindow", "用户名"))
        item = self.score_table.horizontalHeaderItem(2)
        item.setText(_translate("UserMainWindow", "最高分"))
        item = self.score_table.horizontalHeaderItem(3)
        item.setText(_translate("UserMainWindow", "得分日期"))
        url = "http://106.13.236.185:5000/api/game/query_all_pub"
        r = requests.post(url=url, data="")
        games = json.loads(r.text)
        index = 0
        for game in games:
            self.game_Button[index].setText(_translate("UserMainWindow", game['gname']))
            index += 1
