# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './flua-ide.ui'
#
# Created: Tue Nov 27 16:34:26 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/languages/flua.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.mainMenuBar = QtGui.QMenuBar(MainWindow)
        self.mainMenuBar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.mainMenuBar.setObjectName(_fromUtf8("mainMenuBar"))
        self.menuFile = QtGui.QMenu(self.mainMenuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuModule = QtGui.QMenu(self.mainMenuBar)
        self.menuModule.setObjectName(_fromUtf8("menuModule"))
        self.menuHelp = QtGui.QMenu(self.mainMenuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.mainMenuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuWindows = QtGui.QMenu(self.mainMenuBar)
        self.menuWindows.setObjectName(_fromUtf8("menuWindows"))
        self.menuRepository = QtGui.QMenu(self.mainMenuBar)
        self.menuRepository.setObjectName(_fromUtf8("menuRepository"))
        self.menuUtilities = QtGui.QMenu(self.mainMenuBar)
        self.menuUtilities.setObjectName(_fromUtf8("menuUtilities"))
        self.menuWindow = QtGui.QMenu(self.mainMenuBar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        self.menuEnvironment = QtGui.QMenu(self.mainMenuBar)
        self.menuEnvironment.setObjectName(_fromUtf8("menuEnvironment"))
        MainWindow.setMenuBar(self.mainMenuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setStatusTip(_fromUtf8(""))
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/system-log-out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon3)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/apps/help-browser.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionRun = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/media-playback-start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon5)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/document-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/document-save-as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon7)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionUndo = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/edit-undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon8)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/edit-redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon9)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionViewDependencies = QtGui.QAction(MainWindow)
        self.actionViewDependencies.setCheckable(True)
        self.actionViewDependencies.setChecked(False)
        self.actionViewDependencies.setEnabled(True)
        self.actionViewDependencies.setObjectName(_fromUtf8("actionViewDependencies"))
        self.actionViewXML = QtGui.QAction(MainWindow)
        self.actionViewXML.setCheckable(True)
        self.actionViewXML.setChecked(False)
        self.actionViewXML.setEnabled(True)
        self.actionViewXML.setObjectName(_fromUtf8("actionViewXML"))
        self.actionProperties = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/document-properties.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProperties.setIcon(icon10)
        self.actionProperties.setObjectName(_fromUtf8("actionProperties"))
        self.actionCopy = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/edit-copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon11)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/edit-paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon12)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionCut = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/edit-cut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon13)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/categories/preferences-system.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon14)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionAutoComplete = QtGui.QAction(MainWindow)
        self.actionAutoComplete.setObjectName(_fromUtf8("actionAutoComplete"))
        self.actionClose = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/window-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon15)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionAutoComplete_2 = QtGui.QAction(MainWindow)
        self.actionAutoComplete_2.setObjectName(_fromUtf8("actionAutoComplete_2"))
        self.actionThanksTo = QtGui.QAction(MainWindow)
        self.actionThanksTo.setObjectName(_fromUtf8("actionThanksTo"))
        self.actionDownloadUpdates = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/go-down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownloadUpdates.setIcon(icon16)
        self.actionDownloadUpdates.setObjectName(_fromUtf8("actionDownloadUpdates"))
        self.actionReopenLastFile = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/tab-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReopenLastFile.setIcon(icon17)
        self.actionReopenLastFile.setObjectName(_fromUtf8("actionReopenLastFile"))
        self.actionIntroduction = QtGui.QAction(MainWindow)
        self.actionIntroduction.setObjectName(_fromUtf8("actionIntroduction"))
        self.actionRunOptimized = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/media-seek-forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRunOptimized.setIcon(icon18)
        self.actionRunOptimized.setObjectName(_fromUtf8("actionRunOptimized"))
        self.actionRunDebug = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/docks/debugger.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRunDebug.setIcon(icon19)
        self.actionRunDebug.setObjectName(_fromUtf8("actionRunDebug"))
        self.actionToggleFullscreen = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/view-fullscreen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionToggleFullscreen.setIcon(icon20)
        self.actionToggleFullscreen.setObjectName(_fromUtf8("actionToggleFullscreen"))
        self.actionChangeLog = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/apps/accessories-text-editor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChangeLog.setIcon(icon21)
        self.actionChangeLog.setObjectName(_fromUtf8("actionChangeLog"))
        self.actionRun_module_test = QtGui.QAction(MainWindow)
        self.actionRun_module_test.setObjectName(_fromUtf8("actionRun_module_test"))
        self.actionRunModuleTests = QtGui.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/places/start-here.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRunModuleTests.setIcon(icon22)
        self.actionRunModuleTests.setObjectName(_fromUtf8("actionRunModuleTests"))
        self.actionCleanAllTargets = QtGui.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/edit-clear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCleanAllTargets.setIcon(icon23)
        self.actionCleanAllTargets.setObjectName(_fromUtf8("actionCleanAllTargets"))
        self.actionResetLocalChanges = QtGui.QAction(MainWindow)
        self.actionResetLocalChanges.setIcon(icon23)
        self.actionResetLocalChanges.setObjectName(_fromUtf8("actionResetLocalChanges"))
        self.actionSearch = QtGui.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/actions/edit-find.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon24)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionRegExSearch = QtGui.QAction(MainWindow)
        self.actionRegExSearch.setIcon(icon24)
        self.actionRegExSearch.setObjectName(_fromUtf8("actionRegExSearch"))
        self.actionReportBug = QtGui.QAction(MainWindow)
        self.actionReportBug.setIcon(icon19)
        self.actionReportBug.setObjectName(_fromUtf8("actionReportBug"))
        self.actionRepositoryList = QtGui.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/apps/internet-web-browser.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRepositoryList.setIcon(icon25)
        self.actionRepositoryList.setObjectName(_fromUtf8("actionRepositoryList"))
        self.actionConnectWithGitHub = QtGui.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/apps/github.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnectWithGitHub.setIcon(icon26)
        self.actionConnectWithGitHub.setObjectName(_fromUtf8("actionConnectWithGitHub"))
        self.actionResetLocalFileChanges = QtGui.QAction(MainWindow)
        self.actionResetLocalFileChanges.setIcon(icon23)
        self.actionResetLocalFileChanges.setObjectName(_fromUtf8("actionResetLocalFileChanges"))
        self.actionFAQUpdate = QtGui.QAction(MainWindow)
        self.actionFAQUpdate.setObjectName(_fromUtf8("actionFAQUpdate"))
        self.actionFAQCompiling = QtGui.QAction(MainWindow)
        self.actionFAQCompiling.setObjectName(_fromUtf8("actionFAQCompiling"))
        self.actionViewSource = QtGui.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/mimetypes/text-x-generic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewSource.setIcon(icon27)
        self.actionViewSource.setObjectName(_fromUtf8("actionViewSource"))
        self.actionFAQTabs = QtGui.QAction(MainWindow)
        self.actionFAQTabs.setObjectName(_fromUtf8("actionFAQTabs"))
        self.actionDebug = QtGui.QAction(MainWindow)
        self.actionDebug.setObjectName(_fromUtf8("actionDebug"))
        self.actionCreateDefaultImplementation = QtGui.QAction(MainWindow)
        self.actionCreateDefaultImplementation.setObjectName(_fromUtf8("actionCreateDefaultImplementation"))
        self.actionJumpToDefinition = QtGui.QAction(MainWindow)
        self.actionJumpToDefinition.setObjectName(_fromUtf8("actionJumpToDefinition"))
        self.actionDuplicateLine = QtGui.QAction(MainWindow)
        self.actionDuplicateLine.setObjectName(_fromUtf8("actionDuplicateLine"))
        self.actionToggleComment = QtGui.QAction(MainWindow)
        self.actionToggleComment.setObjectName(_fromUtf8("actionToggleComment"))
        self.actionFindPossibleParallelizationPoints = QtGui.QAction(MainWindow)
        self.actionFindPossibleParallelizationPoints.setObjectName(_fromUtf8("actionFindPossibleParallelizationPoints"))
        self.actionFindNext = QtGui.QAction(MainWindow)
        self.actionFindNext.setObjectName(_fromUtf8("actionFindNext"))
        self.actionCommand = QtGui.QAction(MainWindow)
        self.actionCommand.setObjectName(_fromUtf8("actionCommand"))
        self.actionWorkspace_1 = QtGui.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/places/user-desktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWorkspace_1.setIcon(icon28)
        self.actionWorkspace_1.setObjectName(_fromUtf8("actionWorkspace_1"))
        self.actionWorkspace_2 = QtGui.QAction(MainWindow)
        self.actionWorkspace_2.setIcon(icon28)
        self.actionWorkspace_2.setObjectName(_fromUtf8("actionWorkspace_2"))
        self.actionWorkspace_3 = QtGui.QAction(MainWindow)
        self.actionWorkspace_3.setIcon(icon28)
        self.actionWorkspace_3.setObjectName(_fromUtf8("actionWorkspace_3"))
        self.actionWorkspace_4 = QtGui.QAction(MainWindow)
        self.actionWorkspace_4.setIcon(icon28)
        self.actionWorkspace_4.setObjectName(_fromUtf8("actionWorkspace_4"))
        self.actionWorkspace_Q = QtGui.QAction(MainWindow)
        self.actionWorkspace_Q.setIcon(icon28)
        self.actionWorkspace_Q.setObjectName(_fromUtf8("actionWorkspace_Q"))
        self.actionWorkspace_W = QtGui.QAction(MainWindow)
        self.actionWorkspace_W.setIcon(icon28)
        self.actionWorkspace_W.setObjectName(_fromUtf8("actionWorkspace_W"))
        self.actionWorkspace_E = QtGui.QAction(MainWindow)
        self.actionWorkspace_E.setIcon(icon28)
        self.actionWorkspace_E.setObjectName(_fromUtf8("actionWorkspace_E"))
        self.actionWorkspace_R = QtGui.QAction(MainWindow)
        self.actionWorkspace_R.setIcon(icon28)
        self.actionWorkspace_R.setObjectName(_fromUtf8("actionWorkspace_R"))
        self.actionHideMainMenu = QtGui.QAction(MainWindow)
        self.actionHideMainMenu.setObjectName(_fromUtf8("actionHideMainMenu"))
        self.actionEnvNone = QtGui.QAction(MainWindow)
        self.actionEnvNone.setCheckable(True)
        self.actionEnvNone.setChecked(False)
        self.actionEnvNone.setObjectName(_fromUtf8("actionEnvNone"))
        self.actionEnvFlua = QtGui.QAction(MainWindow)
        self.actionEnvFlua.setCheckable(True)
        self.actionEnvFlua.setIcon(icon)
        self.actionEnvFlua.setVisible(True)
        self.actionEnvFlua.setObjectName(_fromUtf8("actionEnvFlua"))
        self.actionEnvPython = QtGui.QAction(MainWindow)
        self.actionEnvPython.setCheckable(True)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/languages/python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnvPython.setIcon(icon29)
        self.actionEnvPython.setObjectName(_fromUtf8("actionEnvPython"))
        self.actionEnvCPP = QtGui.QAction(MainWindow)
        self.actionEnvCPP.setCheckable(True)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(_fromUtf8("../images/icons/languages/c++.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnvCPP.setIcon(icon30)
        self.actionEnvCPP.setObjectName(_fromUtf8("actionEnvCPP"))
        self.actionEnvGLSL = QtGui.QAction(MainWindow)
        self.actionEnvGLSL.setObjectName(_fromUtf8("actionEnvGLSL"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionReopenLastFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuModule.addAction(self.actionRun)
        self.menuModule.addSeparator()
        self.menuModule.addAction(self.actionRunOptimized)
        self.menuModule.addAction(self.actionRunDebug)
        self.menuModule.addAction(self.actionRunModuleTests)
        self.menuModule.addSeparator()
        self.menuModule.addAction(self.actionCleanAllTargets)
        self.menuModule.addAction(self.actionViewSource)
        self.menuModule.addSeparator()
        self.menuModule.addAction(self.actionProperties)
        self.menuHelp.addAction(self.actionChangeLog)
        self.menuHelp.addAction(self.actionDownloadUpdates)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionResetLocalChanges)
        self.menuHelp.addAction(self.actionResetLocalFileChanges)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionReportBug)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionThanksTo)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSearch)
        self.menuEdit.addAction(self.actionRegExSearch)
        self.menuEdit.addAction(self.actionFindNext)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuWindows.addAction(self.actionWorkspace_1)
        self.menuWindows.addAction(self.actionWorkspace_2)
        self.menuWindows.addAction(self.actionWorkspace_3)
        self.menuWindows.addAction(self.actionWorkspace_4)
        self.menuWindows.addSeparator()
        self.menuWindows.addAction(self.actionWorkspace_Q)
        self.menuWindows.addAction(self.actionWorkspace_W)
        self.menuWindows.addAction(self.actionWorkspace_E)
        self.menuWindows.addAction(self.actionWorkspace_R)
        self.menuRepository.addAction(self.actionRepositoryList)
        self.menuRepository.addAction(self.actionConnectWithGitHub)
        self.menuUtilities.addAction(self.actionCommand)
        self.menuUtilities.addSeparator()
        self.menuUtilities.addAction(self.actionJumpToDefinition)
        self.menuUtilities.addSeparator()
        self.menuUtilities.addAction(self.actionCreateDefaultImplementation)
        self.menuUtilities.addAction(self.actionDuplicateLine)
        self.menuUtilities.addAction(self.actionToggleComment)
        self.menuUtilities.addSeparator()
        self.menuUtilities.addAction(self.actionFindPossibleParallelizationPoints)
        self.menuWindow.addAction(self.actionToggleFullscreen)
        self.menuEnvironment.addAction(self.actionEnvFlua)
        self.menuEnvironment.addAction(self.actionEnvPython)
        self.menuEnvironment.addAction(self.actionEnvCPP)
        self.menuEnvironment.addAction(self.actionEnvGLSL)
        self.menuEnvironment.addSeparator()
        self.menuEnvironment.addAction(self.actionEnvNone)
        self.mainMenuBar.addAction(self.menuFile.menuAction())
        self.mainMenuBar.addAction(self.menuEdit.menuAction())
        self.mainMenuBar.addAction(self.menuUtilities.menuAction())
        self.mainMenuBar.addAction(self.menuModule.menuAction())
        self.mainMenuBar.addAction(self.menuRepository.menuAction())
        self.mainMenuBar.addAction(self.menuWindows.menuAction())
        self.mainMenuBar.addAction(self.menuEnvironment.menuAction())
        self.mainMenuBar.addAction(self.menuWindow.menuAction())
        self.mainMenuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Flua Studio 0.4.6 (27 Nov 2012)", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuModule.setTitle(QtGui.QApplication.translate("MainWindow", "Module", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindows.setTitle(QtGui.QApplication.translate("MainWindow", "Workspaces", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRepository.setTitle(QtGui.QApplication.translate("MainWindow", "Repository", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUtilities.setTitle(QtGui.QApplication.translate("MainWindow", "Utilities", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindow.setTitle(QtGui.QApplication.translate("MainWindow", "Window", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEnvironment.setTitle(QtGui.QApplication.translate("MainWindow", "Environments", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Exit program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Y", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewDependencies.setText(QtGui.QApplication.translate("MainWindow", "Dependencies", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewXML.setText(QtGui.QApplication.translate("MainWindow", "XML View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setText(QtGui.QApplication.translate("MainWindow", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setShortcut(QtGui.QApplication.translate("MainWindow", "F9", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("MainWindow", "F10", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoComplete.setText(QtGui.QApplication.translate("MainWindow", "Auto Complete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoComplete.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoComplete_2.setText(QtGui.QApplication.translate("MainWindow", "Auto Complete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoComplete_2.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionThanksTo.setText(QtGui.QApplication.translate("MainWindow", "Thanks to...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownloadUpdates.setText(QtGui.QApplication.translate("MainWindow", "Download updates", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReopenLastFile.setText(QtGui.QApplication.translate("MainWindow", "Reopen last file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReopenLastFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIntroduction.setText(QtGui.QApplication.translate("MainWindow", "Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRunOptimized.setText(QtGui.QApplication.translate("MainWindow", "Run optimized", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRunOptimized.setShortcut(QtGui.QApplication.translate("MainWindow", "F6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRunDebug.setText(QtGui.QApplication.translate("MainWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRunDebug.setShortcut(QtGui.QApplication.translate("MainWindow", "F7", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggleFullscreen.setText(QtGui.QApplication.translate("MainWindow", "Toggle fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggleFullscreen.setShortcut(QtGui.QApplication.translate("MainWindow", "F11", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChangeLog.setText(QtGui.QApplication.translate("MainWindow", "Changelog", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_module_test.setText(QtGui.QApplication.translate("MainWindow", "Run module test", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRunModuleTests.setText(QtGui.QApplication.translate("MainWindow", "Run module tests", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRunModuleTests.setShortcut(QtGui.QApplication.translate("MainWindow", "F8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCleanAllTargets.setText(QtGui.QApplication.translate("MainWindow", "Clean all targets", None, QtGui.QApplication.UnicodeUTF8))
        self.actionResetLocalChanges.setText(QtGui.QApplication.translate("MainWindow", "Reset all local changes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegExSearch.setText(QtGui.QApplication.translate("MainWindow", "RegEx Search", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegExSearch.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReportBug.setText(QtGui.QApplication.translate("MainWindow", "Submit a Bug Report", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRepositoryList.setText(QtGui.QApplication.translate("MainWindow", "Repository list", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRepositoryList.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnectWithGitHub.setText(QtGui.QApplication.translate("MainWindow", "Connect with GitHub", None, QtGui.QApplication.UnicodeUTF8))
        self.actionResetLocalFileChanges.setText(QtGui.QApplication.translate("MainWindow", "Reset changes for this module", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFAQUpdate.setText(QtGui.QApplication.translate("MainWindow", "Why does updating fail?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFAQCompiling.setText(QtGui.QApplication.translate("MainWindow", "Why does the compiler not work?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewSource.setText(QtGui.QApplication.translate("MainWindow", "View generated source code", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewSource.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFAQTabs.setText(QtGui.QApplication.translate("MainWindow", "Why can\'t I use spaces instead of tabs?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDebug.setText(QtGui.QApplication.translate("MainWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreateDefaultImplementation.setText(QtGui.QApplication.translate("MainWindow", "Create default implementation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreateDefaultImplementation.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJumpToDefinition.setText(QtGui.QApplication.translate("MainWindow", "Jump to definition", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJumpToDefinition.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDuplicateLine.setText(QtGui.QApplication.translate("MainWindow", "Duplicate line", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDuplicateLine.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggleComment.setText(QtGui.QApplication.translate("MainWindow", "Toggle comment", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggleComment.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPossibleParallelizationPoints.setText(QtGui.QApplication.translate("MainWindow", "Find possible parallelization points", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setText(QtGui.QApplication.translate("MainWindow", "Find next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setShortcut(QtGui.QApplication.translate("MainWindow", "F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCommand.setText(QtGui.QApplication.translate("MainWindow", "Command", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCommand.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_1.setText(QtGui.QApplication.translate("MainWindow", "Workspace 1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_1.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_2.setText(QtGui.QApplication.translate("MainWindow", "Workspace 2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_2.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_3.setText(QtGui.QApplication.translate("MainWindow", "Workspace 3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_3.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_4.setText(QtGui.QApplication.translate("MainWindow", "Workspace 4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_4.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_Q.setText(QtGui.QApplication.translate("MainWindow", "Workspace Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_Q.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_W.setText(QtGui.QApplication.translate("MainWindow", "Workspace W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_W.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_E.setText(QtGui.QApplication.translate("MainWindow", "Workspace E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_E.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_R.setText(QtGui.QApplication.translate("MainWindow", "Workspace R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWorkspace_R.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHideMainMenu.setText(QtGui.QApplication.translate("MainWindow", "Hide main menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnvNone.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnvFlua.setText(QtGui.QApplication.translate("MainWindow", "Flua", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnvPython.setText(QtGui.QApplication.translate("MainWindow", "Python 3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnvCPP.setText(QtGui.QApplication.translate("MainWindow", "C++", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnvGLSL.setText(QtGui.QApplication.translate("MainWindow", "GLSL", None, QtGui.QApplication.UnicodeUTF8))

