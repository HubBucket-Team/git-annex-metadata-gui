# Git-Annex-Metadata-Gui Views
# Copyright (C) 2016 Alper Nebi Yasak
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

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QTreeView


class GitAnnexView(QTreeView):
    def __init__(self):
        super().__init__()

        self.setSortingEnabled(True)
        self.setSelectionBehavior(self.SelectRows)
        self.setUniformRowHeights(True)

    def setModel(self, model):
        super().setModel(model)

        self.expandAll()
        header = self.header()
        header.setStretchLastSection(False)
        header.resizeSections(QHeaderView.ResizeToContents)
        self.collapseAll()

    def viewportSizeHint(self):
        orig_size = super().viewportSizeHint()
        max_file_length = self.columnWidth(0)
        return QSize(max_file_length * 1.05, orig_size.height())

    def toggle_header_field(self, field, visible):
        fields = list(zip(*self.model().headers))[0]
        field_index = fields.index(field)
        header = self.header()
        header.setSectionHidden(field_index, not visible)
