# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:/extensions/studioTools/python/arxPublisher/ui.ui'
#
# Created: Sat Nov 22 23:01:27 2014
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_arxPublishWindow(object):
    def setupUi(self, arxPublishWindow):
        arxPublishWindow.setObjectName("arxPublishWindow")
        arxPublishWindow.resize(972, 692)
        self.centralwidget = QtGui.QWidget(arxPublishWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 951, 661))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.app_label = QtGui.QLabel(self.frame)
        self.app_label.setGeometry(QtCore.QRect(750, 6, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.app_label.setFont(font)
        self.app_label.setObjectName("app_label")
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 500, 341, 111))
        self.frame_4.setFrameShape(QtGui.QFrame.Box)
        self.frame_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.comment_textEdit = QtGui.QTextEdit(self.frame_4)
        self.comment_textEdit.setEnabled(True)
        self.comment_textEdit.setGeometry(QtCore.QRect(10, 30, 321, 71))
        self.comment_textEdit.setObjectName("comment_textEdit")
        self.label_2 = QtGui.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.label_2.setObjectName("label_2")
        self.shotgun_checkBox = QtGui.QCheckBox(self.frame)
        self.shotgun_checkBox.setGeometry(QtCore.QRect(20, 420, 70, 17))
        self.shotgun_checkBox.setToolTip("")
        self.shotgun_checkBox.setWhatsThis("")
        self.shotgun_checkBox.setChecked(True)
        self.shotgun_checkBox.setObjectName("shotgun_checkBox")
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 50, 931, 81))
        self.frame_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.task_label = QtGui.QLabel(self.frame_3)
        self.task_label.setGeometry(QtCore.QRect(570, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.task_label.setFont(font)
        self.task_label.setObjectName("task_label")
        self.data2_label = QtGui.QLabel(self.frame_3)
        self.data2_label.setGeometry(QtCore.QRect(280, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.data2_label.setFont(font)
        self.data2_label.setObjectName("data2_label")
        self.data3_label = QtGui.QLabel(self.frame_3)
        self.data3_label.setGeometry(QtCore.QRect(420, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.data3_label.setFont(font)
        self.data3_label.setObjectName("data3_label")
        self.data1_label = QtGui.QLabel(self.frame_3)
        self.data1_label.setGeometry(QtCore.QRect(140, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.data1_label.setFont(font)
        self.data1_label.setObjectName("data1_label")
        self.project_label = QtGui.QLabel(self.frame_3)
        self.project_label.setGeometry(QtCore.QRect(10, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.project_label.setFont(font)
        self.project_label.setObjectName("project_label")
        self.entity_label = QtGui.QLabel(self.frame_3)
        self.entity_label.setGeometry(QtCore.QRect(10, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entity_label.setFont(font)
        self.entity_label.setObjectName("entity_label")
        self.publish_label = QtGui.QLabel(self.frame_3)
        self.publish_label.setGeometry(QtCore.QRect(200, 13, 671, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.publish_label.setFont(font)
        self.publish_label.setObjectName("publish_label")
        self.task_comboBox = QtGui.QComboBox(self.frame_3)
        self.task_comboBox.setGeometry(QtCore.QRect(800, 50, 121, 22))
        self.task_comboBox.setObjectName("task_comboBox")
        self.task2_label = QtGui.QLabel(self.frame_3)
        self.task2_label.setGeometry(QtCore.QRect(730, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.task2_label.setFont(font)
        self.task2_label.setObjectName("task2_label")
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 140, 341, 271))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.snapViewport_pushButton = QtGui.QPushButton(self.frame_2)
        self.snapViewport_pushButton.setGeometry(QtCore.QRect(120, 240, 101, 23))
        self.snapViewport_pushButton.setObjectName("snapViewport_pushButton")
        self.preview_label = QtGui.QLabel(self.frame_2)
        self.preview_label.setGeometry(QtCore.QRect(20, 30, 300, 200))
        self.preview_label.setObjectName("preview_label")
        self.task_label_3 = QtGui.QLabel(self.frame_2)
        self.task_label_3.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.task_label_3.setFont(font)
        self.task_label_3.setObjectName("task_label_3")
        self.publish_pushButton = QtGui.QPushButton(self.frame)
        self.publish_pushButton.setGeometry(QtCore.QRect(10, 620, 161, 31))
        self.publish_pushButton.setObjectName("publish_pushButton")
        self.frame_5 = QtGui.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(360, 180, 361, 431))
        self.frame_5.setFrameShape(QtGui.QFrame.Box)
        self.frame_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.publish_listWidget = QtGui.QListWidget(self.frame_5)
        self.publish_listWidget.setGeometry(QtCore.QRect(10, 30, 341, 391))
        self.publish_listWidget.setObjectName("publish_listWidget")
        self.display_label = QtGui.QLabel(self.frame_5)
        self.display_label.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.display_label.setFont(font)
        self.display_label.setObjectName("display_label")
        self.status_label = QtGui.QLabel(self.frame)
        self.status_label.setGeometry(QtCore.QRect(180, 624, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.status_label.setFont(font)
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.logo_label = QtGui.QLabel(self.frame)
        self.logo_label.setGeometry(QtCore.QRect(10, 6, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.logo_label.setFont(font)
        self.logo_label.setObjectName("logo_label")
        self.frame_6 = QtGui.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(360, 140, 581, 31))
        self.frame_6.setFrameShape(QtGui.QFrame.Box)
        self.frame_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")
        self.saveWork_radioButton = QtGui.QRadioButton(self.frame_6)
        self.saveWork_radioButton.setGeometry(QtCore.QRect(40, 6, 100, 17))
        self.saveWork_radioButton.setChecked(True)
        self.saveWork_radioButton.setObjectName("saveWork_radioButton")
        self.publish_radioButton = QtGui.QRadioButton(self.frame_6)
        self.publish_radioButton.setGeometry(QtCore.QRect(210, 6, 91, 17))
        self.publish_radioButton.setObjectName("publish_radioButton")
        self.playblast_checkBox = QtGui.QCheckBox(self.frame)
        self.playblast_checkBox.setGeometry(QtCore.QRect(110, 420, 131, 17))
        self.playblast_checkBox.setToolTip("")
        self.playblast_checkBox.setWhatsThis("")
        self.playblast_checkBox.setChecked(True)
        self.playblast_checkBox.setObjectName("playblast_checkBox")
        self.upload_checkBox = QtGui.QCheckBox(self.frame)
        self.upload_checkBox.setGeometry(QtCore.QRect(250, 420, 91, 17))
        self.upload_checkBox.setToolTip("")
        self.upload_checkBox.setWhatsThis("")
        self.upload_checkBox.setChecked(True)
        self.upload_checkBox.setObjectName("upload_checkBox")
        self.frame_7 = QtGui.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(730, 180, 211, 431))
        self.frame_7.setFrameShape(QtGui.QFrame.Box)
        self.frame_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.status_listWidget = QtGui.QListWidget(self.frame_7)
        self.status_listWidget.setGeometry(QtCore.QRect(10, 30, 191, 391))
        self.status_listWidget.setObjectName("status_listWidget")
        self.display_label_2 = QtGui.QLabel(self.frame_7)
        self.display_label_2.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.display_label_2.setFont(font)
        self.display_label_2.setObjectName("display_label_2")
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(730, 620, 211, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        arxPublishWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(arxPublishWindow)
        self.statusBar.setObjectName("statusBar")
        arxPublishWindow.setStatusBar(self.statusBar)

        self.retranslateUi(arxPublishWindow)
        QtCore.QMetaObject.connectSlotsByName(arxPublishWindow)

    def retranslateUi(self, arxPublishWindow):
        arxPublishWindow.setWindowTitle(QtGui.QApplication.translate("arxPublishWindow", "Arxanima Asset Publish v.1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.app_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Maya Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("arxPublishWindow", "Comment : ", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_checkBox.setText(QtGui.QApplication.translate("arxPublishWindow", "Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.task_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Task", None, QtGui.QApplication.UnicodeUTF8))
        self.data2_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Parent", None, QtGui.QApplication.UnicodeUTF8))
        self.data3_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Variation", None, QtGui.QApplication.UnicodeUTF8))
        self.data1_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.project_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Entity type", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Publish version", None, QtGui.QApplication.UnicodeUTF8))
        self.task2_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Anim Task : ", None, QtGui.QApplication.UnicodeUTF8))
        self.snapViewport_pushButton.setText(QtGui.QApplication.translate("arxPublishWindow", "Snap Viewport", None, QtGui.QApplication.UnicodeUTF8))
        self.preview_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.task_label_3.setText(QtGui.QApplication.translate("arxPublishWindow", "Thumbnail : ", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_pushButton.setText(QtGui.QApplication.translate("arxPublishWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.display_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Publish Files : ", None, QtGui.QApplication.UnicodeUTF8))
        self.logo_label.setText(QtGui.QApplication.translate("arxPublishWindow", "Logo", None, QtGui.QApplication.UnicodeUTF8))
        self.saveWork_radioButton.setText(QtGui.QApplication.translate("arxPublishWindow", "Save increment", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_radioButton.setText(QtGui.QApplication.translate("arxPublishWindow", "Publish Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.playblast_checkBox.setText(QtGui.QApplication.translate("arxPublishWindow", "Attach playblast to RV", None, QtGui.QApplication.UnicodeUTF8))
        self.upload_checkBox.setText(QtGui.QApplication.translate("arxPublishWindow", "Upload Online", None, QtGui.QApplication.UnicodeUTF8))
        self.display_label_2.setText(QtGui.QApplication.translate("arxPublishWindow", "Status : ", None, QtGui.QApplication.UnicodeUTF8))

