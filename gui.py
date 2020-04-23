from .auto_fields import *
from aqt import mw
from aqt.qt import *
from PyQt5 import QtWidgets , QtGui
from PyQt5.QtWidgets import QAction,  QVBoxLayout
from anki.hooks import addHook

ADDON = os.path.dirname(os.path.abspath(__file__))
ICONS = ADDON+'/icons'

conj_icon = QtGui.QIcon()
conj_icon.addFile( ICONS+'/conj.png')

all_icon = QtGui.QIcon()
all_icon.addFile(ICONS+'/all.png')

etymology_icon = QtGui.QIcon()
etymology_icon.addFile(ICONS+'/etymology.png')

ipa_icon = QtGui.QIcon()
ipa_icon.addFile(ICONS+'/ipa.png')

audio_icon = QtGui.QIcon()
audio_icon.addFile(ICONS+'/audio.png')

pos_icon = QtGui.QIcon()
pos_icon.addFile(ICONS+'/pos.png')

plural_icon = QtGui.QIcon()
plural_icon.addFile(ICONS+'/plural.png')

feminine_icon = QtGui.QIcon()
feminine_icon.addFile(ICONS+'/feminine.png')

about_icon = QtGui.QIcon()
about_icon.addFile(ICONS+'/about.png')



def show_info():
    parent = aqt.mw.app.activeWindow() or aqt.mw
    diag = QDialog(parent)
    diag.setWindowTitle(ADDON_NAME)

    about_icon = QtGui.QIcon()
    about_icon.addFile(ICONS+'/about.png')
    diag.setWindowIcon(about_icon)

    layout = QVBoxLayout(diag)
    diag.setLayout(layout)

    text = QTextBrowser()
    text.setOpenExternalLinks(True)
    txt = '''
    <body bgcolor="#f3f3f3">
    <center>
    <img  src='''+ICONS+'/logo.png'+'''>
    </center>
    <center>
    <big>
    <b><i><a href="href="https://github.com/ShoroukAziz/multiple-examples-per-note"> Multiple Examples per Note</a> </i></b> is an addon that allows you to have more than one example with audio for each note. that can be randomly changed<br>
    Detailed description of the addon and the models can be found in the <a href="https://github.com/ShoroukAziz/multiple-examples-per-note/wiki"> Github Wiki </a>
    <br>Develped By : <a href="https://shorouk.xyz"> Shorouk Abdelaziz </a>
    <big>
    </center>
    <center>
    <br>
    <a href='https://ko-fi.com/B0B51L5RI'>Support Me on Ko-fi</a>
    <br>
    Icons made by <a href="https://www.flaticon.com/authors/freepik"
     title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>

     </center>
    </body>
    '''
    text.setHtml(txt)
    text.toHtml()
    layout.addWidget(text)
    diag.setMinimumHeight(600)
    diag.setMinimumWidth(800)
    diag.exec_()




def run():

    def setupMenu(self):
        # menu = self.form.menuEdit
        menu = QtWidgets.QMenu('AutoFields', self.form.menubar)

        if language == 'french':
            a = menu.addAction('Conjugate French Verbs')
            a.triggered.connect(lambda _, b=self: setVerbConjugationsForOneNoteFromBrowser(b))
            a.setIcon(conj_icon)
            menu.addSeparator()

            b = menu.addAction('Get all extra fields')
            b.triggered.connect(lambda _, b=self: populateExtraFields(b))
            b.setIcon(all_icon)
            menu.addSeparator()

            c = menu.addAction('Get Etymology')
            c.triggered.connect(lambda _, c=self: populateEtymology(c))
            c.setIcon(etymology_icon)

            d = menu.addAction('Get IPA')
            d.triggered.connect(lambda _, d=self: populateIPA(d))
            d.setIcon(ipa_icon)

            e = menu.addAction('Get Audio')
            e.triggered.connect(lambda _, e=self: populateAudio(e))
            e.setIcon(audio_icon)

            f = menu.addAction('Get POS')
            f.triggered.connect(lambda _, f=self: populatePos(f))
            f.setIcon(pos_icon)

            g = menu.addAction('Get Plural')
            g.triggered.connect(lambda _, g=self: populatePlural(g))
            g.setIcon(plural_icon)

            h = menu.addAction('Get Feminine')
            h.triggered.connect(lambda _, h=self: populateFeminine(h))
            h.setIcon(feminine_icon)
            menu.addSeparator()


            showAbout = QAction("About", mw)
            showAbout.triggered.connect(show_info)
            showAbout.setIcon(about_icon)
            menu.addAction(showAbout)


            self.form.menubar.addMenu(menu)

        else:
            c = menu.addAction('Etymology')
            c.triggered.connect(lambda _, c=self: populateEtymology(c))
            c.setIcon(etymology_icon)

            d = menu.addAction('IPA')
            d.triggered.connect(lambda _, d=self: populateIPA(d))
            d.setIcon(ipa_icon)

            e = menu.addAction('Audio')
            e.triggered.connect(lambda _, e=self: populateAudio(e))
            e.setIcon(audio_icon)

            f = menu.addAction('POS')
            f.triggered.connect(lambda _, f=self: populatePos(f))
            f.setIcon(pos_icon)

            g = menu.addAction('Plural')
            g.triggered.connect(lambda _, g=self: populatePlural(g))
            g.setIcon(plural_icon)
            self.form.menubar.addMenu(menu)


            showAbout = QAction("About", mw)
            showAbout.triggered.connect(show_info)
            showAbout.setIcon(about_icon)
            menu.addAction(showAbout)

    addHook("browser.setupMenus", setupMenu)
