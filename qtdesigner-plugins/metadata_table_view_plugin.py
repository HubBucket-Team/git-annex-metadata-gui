# Git-Annex-Metadata-Gui
# Copyright (C) 2017 Alper Nebi Yasak
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtDesigner

from metadata_table_view import MetadataTableView

class MetadataTableViewPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._initialized = False

    def initialize(self, formEditor):
        self._initialized = True

    def isInitialized(self):
        return self._initialized

    def createWidget(self, parent):
        return MetadataTableView(parent)

    def name(self):
        return "MetadataTableView"

    def group(self):
        return "Git-Annex Metadata Gui Widgets"

    def icon(self):
        return QtGui.QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "git_annex_metadata_gui.metadata_table_view"

    def domXml(self):
        cls = self.name()
        name = 'view_metadata_table'
        xml = '<widget class="{}" name="{}"></widget>'
        return xml.format(cls, name)

