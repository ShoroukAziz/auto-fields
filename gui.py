from .auto_fields import *
from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo
from bs4 import BeautifulSoup
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets , QtGui
from PyQt5.QtWidgets import QAction, QProgressDialog, QWidget, QPushButton, QVBoxLayout
from aqt import mw
from anki.hooks import addHook




def run():

    def setupMenu(self):
        # menu = self.form.menuEdit
        menu = QtWidgets.QMenu('AutoFields', self.form.menubar)

        if language == 'french':
            a = menu.addAction('Conjugate French Verbs')
            a.triggered.connect(lambda _, b=self: setVerbConjugationsForOneNoteFromBrowser(b))
            # a.setIcon(refresh_note_icon)
            menu.addSeparator()

            b = menu.addAction('Get all extra fields')
            b.triggered.connect(lambda _, b=self: populateExtraFields(b))
            # b.setIcon(delete_icon)
            menu.addSeparator()

            c = menu.addAction('Get Etymology')
            c.triggered.connect(lambda _, c=self: populateEtymology(c))
            # b.setIcon(delete_icon)

            d = menu.addAction('Get IPA')
            d.triggered.connect(lambda _, d=self: populateIPA(d))
            # b.setIcon(delete_icon)

            e = menu.addAction('Get Audio')
            e.triggered.connect(lambda _, e=self: populateAudio(e))
            # b.setIcon(delete_icon)

            f = menu.addAction('Get POS')
            f.triggered.connect(lambda _, f=self: populatePos(f))
            # b.setIcon(delete_icon)

            g = menu.addAction('Get Plural')
            g.triggered.connect(lambda _, g=self: populatePlural(g))
            # b.setIcon(delete_icon)

            h = menu.addAction('Get Feminine')
            h.triggered.connect(lambda _, h=self: populateFeminine(h))
            # b.setIcon(delete_icon)

            self.form.menubar.addMenu(menu)

        else:
            c = menu.addAction('Etymology')
            c.triggered.connect(lambda _, c=self: populateEtymology(c))
            # b.setIcon(delete_icon)

            d = menu.addAction('IPA')
            d.triggered.connect(lambda _, d=self: populateIPA(d))
            # b.setIcon(delete_icon)

            e = menu.addAction('Audio')
            e.triggered.connect(lambda _, e=self: populateAudio(e))
            # b.setIcon(delete_icon)

            f = menu.addAction('POS')
            f.triggered.connect(lambda _, f=self: populatePos(f))
            # b.setIcon(delete_icon)

            g = menu.addAction('Plural')
            g.triggered.connect(lambda _, g=self: populatePlural(g))
            # b.setIcon(delete_icon)
            self.form.menubar.addMenu(menu)

    addHook("browser.setupMenus", setupMenu)
