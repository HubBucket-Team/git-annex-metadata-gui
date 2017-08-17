# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner-ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.widget_tabs.setObjectName("widget_tabs")
        self.tab_keys = QtWidgets.QWidget()
        self.tab_keys.setObjectName("tab_keys")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_keys)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_filter_keys = QtWidgets.QLabel(self.tab_keys)
        self.label_filter_keys.setObjectName("label_filter_keys")
        self.gridLayout_2.addWidget(self.label_filter_keys, 1, 0, 1, 1)
        self.edit_filter_keys = QtWidgets.QLineEdit(self.tab_keys)
        self.edit_filter_keys.setObjectName("edit_filter_keys")
        self.gridLayout_2.addWidget(self.edit_filter_keys, 1, 1, 1, 1)
        self.combo_filter_keys = QtWidgets.QComboBox(self.tab_keys)
        self.combo_filter_keys.setObjectName("combo_filter_keys")
        self.combo_filter_keys.addItem("")
        self.combo_filter_keys.addItem("")
        self.combo_filter_keys.addItem("")
        self.gridLayout_2.addWidget(self.combo_filter_keys, 1, 2, 1, 1)
        self.view_keys = MetadataTableView(self.tab_keys)
        self.view_keys.setAlternatingRowColors(True)
        self.view_keys.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.view_keys.setShowGrid(False)
        self.view_keys.setSortingEnabled(True)
        self.view_keys.setWordWrap(False)
        self.view_keys.setCornerButtonEnabled(False)
        self.view_keys.setObjectName("view_keys")
        self.view_keys.horizontalHeader().setDefaultSectionSize(150)
        self.view_keys.verticalHeader().setDefaultSectionSize(20)
        self.view_keys.verticalHeader().setMinimumSectionSize(20)
        self.gridLayout_2.addWidget(self.view_keys, 0, 0, 1, 3)
        self.widget_tabs.addTab(self.tab_keys, "")
        self.tab_head = QtWidgets.QWidget()
        self.tab_head.setObjectName("tab_head")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_head)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_set_treeish = QtWidgets.QLabel(self.tab_head)
        self.label_set_treeish.setObjectName("label_set_treeish")
        self.gridLayout_3.addWidget(self.label_set_treeish, 1, 0, 1, 1)
        self.edit_set_treeish = QtWidgets.QLineEdit(self.tab_head)
        self.edit_set_treeish.setObjectName("edit_set_treeish")
        self.gridLayout_3.addWidget(self.edit_set_treeish, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_head)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 1, 2, 1, 1)
        self.view_head = MetadataTreeView(self.tab_head)
        self.view_head.setUniformRowHeights(True)
        self.view_head.setSortingEnabled(True)
        self.view_head.setObjectName("view_head")
        self.view_head.header().setDefaultSectionSize(150)
        self.view_head.header().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.view_head, 0, 0, 1, 3)
        self.widget_tabs.addTab(self.tab_head, "")
        self.horizontalLayout.addWidget(self.widget_tabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_headers = QtWidgets.QMenu(self.menubar)
        self.menu_headers.setEnabled(False)
        self.menu_headers.setObjectName("menu_headers")
        self.menu_docks = QtWidgets.QMenu(self.menubar)
        self.menu_docks.setObjectName("menu_docks")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dock_preview = QtWidgets.QDockWidget(MainWindow)
        self.dock_preview.setObjectName("dock_preview")
        self.dock_preview_contents = QtWidgets.QWidget()
        self.dock_preview_contents.setObjectName("dock_preview_contents")
        self.gridLayout = QtWidgets.QGridLayout(self.dock_preview_contents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stack_preview = FilePreview(self.dock_preview_contents)
        self.stack_preview.setObjectName("stack_preview")
        self.text_preview = QtWidgets.QPlainTextEdit()
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.text_preview.setFont(font)
        self.text_preview.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.text_preview.setReadOnly(True)
        self.text_preview.setObjectName("text_preview")
        self.stack_preview.addWidget(self.text_preview)
        self.graphics_preview = QtWidgets.QGraphicsView()
        self.graphics_preview.setObjectName("graphics_preview")
        self.stack_preview.addWidget(self.graphics_preview)
        self.gridLayout.addWidget(self.stack_preview, 0, 0, 1, 1)
        self.dock_preview.setWidget(self.dock_preview_contents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_preview)
        self.dock_metadata = QtWidgets.QDockWidget(MainWindow)
        self.dock_metadata.setObjectName("dock_metadata")
        self.dock_metadata_contents = QtWidgets.QWidget()
        self.dock_metadata_contents.setObjectName("dock_metadata_contents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dock_metadata_contents)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.metadata_edit = MetadataEdit(self.dock_metadata_contents)
        self.metadata_edit.setObjectName("metadata_edit")
        self.gridLayout_4.addWidget(self.metadata_edit, 0, 0, 1, 1)
        self.dock_metadata.setWidget(self.dock_metadata_contents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_metadata)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_refresh = QtWidgets.QAction(MainWindow)
        self.action_refresh.setObjectName("action_refresh")
        self.action_dock_preview = QtWidgets.QAction(MainWindow)
        self.action_dock_preview.setCheckable(True)
        self.action_dock_preview.setChecked(True)
        self.action_dock_preview.setObjectName("action_dock_preview")
        self.action_dock_metadata = QtWidgets.QAction(MainWindow)
        self.action_dock_metadata.setCheckable(True)
        self.action_dock_metadata.setChecked(True)
        self.action_dock_metadata.setObjectName("action_dock_metadata")
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_refresh)
        self.menu_file.addAction(self.action_exit)
        self.menu_docks.addAction(self.action_dock_preview)
        self.menu_docks.addAction(self.action_dock_metadata)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_headers.menuAction())
        self.menubar.addAction(self.menu_docks.menuAction())
        self.label_filter_keys.setBuddy(self.edit_filter_keys)
        self.label_set_treeish.setBuddy(self.edit_set_treeish)

        self.retranslateUi(MainWindow)
        self.widget_tabs.setCurrentIndex(0)
        self.action_exit.triggered.connect(MainWindow.close)
        self.action_refresh.triggered.connect(MainWindow.refresh_repo)
        self.action_open.triggered.connect(MainWindow.open_repo)
        self.action_dock_metadata.toggled['bool'].connect(self.dock_metadata.setVisible)
        self.action_dock_preview.toggled['bool'].connect(self.dock_preview.setVisible)
        self.dock_metadata.visibilityChanged['bool'].connect(self.action_dock_metadata.setChecked)
        self.dock_preview.visibilityChanged['bool'].connect(self.action_dock_preview.setChecked)
        self.view_head.item_selected['QStandardItem'].connect(self.stack_preview.preview_item)
        self.view_keys.item_selected['QStandardItem'].connect(self.stack_preview.preview_item)
        self.view_head.item_selected['QStandardItem'].connect(self.metadata_edit.set_item)
        self.view_keys.item_selected['QStandardItem'].connect(self.metadata_edit.set_item)
        self.view_keys.header_created['QString'].connect(MainWindow.create_header_menu_action)
        self.view_head.header_created['QString'].connect(MainWindow.create_header_menu_action)
        self.view_head.model_reset.connect(MainWindow.clear_header_menu)
        self.view_keys.model_reset.connect(MainWindow.clear_header_menu)
        self.edit_filter_keys.textEdited['QString'].connect(self.view_keys.set_filter_pattern)
        self.combo_filter_keys.activated['QString'].connect(self.view_keys.set_filter_type)
        self.edit_set_treeish.textEdited['QString'].connect(self.view_head.set_treeish_to_build)
        self.edit_set_treeish.returnPressed.connect(self.view_head.rebuild_treeish)
        self.pushButton.clicked.connect(self.view_head.rebuild_treeish)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git-Annex Metadata Gui"))
        self.label_filter_keys.setText(_translate("MainWindow", "Filter Keys:"))
        self.combo_filter_keys.setItemText(0, _translate("MainWindow", "Fixed"))
        self.combo_filter_keys.setItemText(1, _translate("MainWindow", "Regex"))
        self.combo_filter_keys.setItemText(2, _translate("MainWindow", "Wildcard"))
        self.widget_tabs.setTabText(self.widget_tabs.indexOf(self.tab_keys), _translate("MainWindow", "All Keys"))
        self.label_set_treeish.setText(_translate("MainWindow", "Set Treeish:"))
        self.pushButton.setText(_translate("MainWindow", "Build Treeish"))
        self.widget_tabs.setTabText(self.widget_tabs.indexOf(self.tab_head), _translate("MainWindow", "Work Tree"))
        self.menu_file.setTitle(_translate("MainWindow", "&File"))
        self.menu_headers.setTitle(_translate("MainWindow", "Headers"))
        self.menu_docks.setTitle(_translate("MainWindow", "Docks"))
        self.dock_preview.setWindowTitle(_translate("MainWindow", "File Preview"))
        self.dock_metadata.setWindowTitle(_translate("MainWindow", "Metadata Editor"))
        self.action_open.setText(_translate("MainWindow", "&Open"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_exit.setText(_translate("MainWindow", "E&xit"))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_refresh.setText(_translate("MainWindow", "&Refresh"))
        self.action_refresh.setShortcut(_translate("MainWindow", "F5"))
        self.action_dock_preview.setText(_translate("MainWindow", "File Preview"))
        self.action_dock_metadata.setText(_translate("MainWindow", "Metadata Editor"))

from git_annex_metadata_gui.file_preview import FilePreview
from git_annex_metadata_gui.metadata_edit import MetadataEdit
from git_annex_metadata_gui.metadata_table_view import MetadataTableView
from git_annex_metadata_gui.metadata_tree_view import MetadataTreeView
