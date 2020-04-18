from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo
from bs4 import BeautifulSoup
import os , sys
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets , QtGui
from PyQt5.QtWidgets import QAction, QProgressDialog, QWidget, QPushButton, QVBoxLayout
from aqt import mw
from anki.hooks import addHook
from .anki_wiki_parser import *
from .wiki_french_verb_parser import *

language = CONFIG['lang']

def setVerbConjugationsForOneNote(note):

    word = BeautifulSoup(verb_note['word'].lower(),'html.parser').get_text()
    type = verb_note['type']
    if 'verb' in type and not 'adverb' in type:
     conj = verb_note['conj']
     if  conj == 'null' or conj == "":
         c = wiki_french_verb_parser.WikitionaryFrenchVerbParser(word)
         res = c.getVerbConj()
         verb_note['conj'] = json.dumps(res,ensure_ascii=False)
         verb_note.flush()
def populateEtymologyForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p =anki_wiki_parser.WikitionaryFrenchParser(word)
    etymology =  p.getEtymology()
    note.flush()
def populateIPAForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p =anki_wiki_parser.WikitionaryFrenchParser(word)
    IPA =  p.getIPA()
    if IPA is not None:
        note['IPA'] = IPA
        note.flush()
def populateAudioForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p =anki_wiki_parser.WikitionaryFrenchParser(word)
    audio = p.getAudio()
    if audio is not None:
        note['sound'] = audio
        note.flush()
def populatePosForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p =anki_wiki_parser.WikitionaryFrenchParser(word)
    pos = p.getPartOfSpeech()
    if pos is not None:
        note['type'] = pos
        note.flush()
def populatePluralForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p =anki_wiki_parser.WikitionaryFrenchParser(word)
    plural = p.getPlural()
    if plural is not None:
        note['plural'] = plural
        note.flush()
def populateFeminineForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p =anki_wiki_parser.WikitionaryFrenchParser(word)
    feminine = p.getFeminine()
    if feminine is not None:
        note['feminin version'] = feminine
        note.flush()
def populateExtraFieldsForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p =anki_wiki_parser.WikitionaryFrenchParser(word)
    etymology =  p.getEtymology()
    IPA = p.getIPA()
    audio = p.getAudio()
    pos = p.getPartOfSpeech()
    plural = p.getPlural()
    feminine = p.getFeminine()

    if etymology is not None:
        note['extra'] = etymology
    if IPA is not None:
        note['IPA'] = IPA
    if audio is not None:
        note['sound'] = audio
    if pos is not None:
        note['type'] = pos
    if plural is not None:
        note['plural'] = plural
    if feminine is not None:
        note['feminin version'] = feminine

    note.flush()


def setVerbConjugationsForOneNoteFromBrowser(self):

    mw = self.mw
    cids = self.selectedCards()
    if not cids:
        tooltip(_("No cards selected."), period=2000)
        return
    for nid in self.selectedNotes():
        frenchNote = mw.col.getNote(nid)
        setVerbConjugationsForOneNote(frenchNote)
    mw.col.reset()
    mw.reset()
def populateExtraFields(self):
    mw = self.mw
    cids = self.selectedCards()
    if not cids:
        tooltip(_("No cards selected."), period=2000)
        return
    for nid in self.selectedNotes():
        frenchNote = mw.col.getNote(nid)
        populateExtraFieldsForOneNote(frenchNote)
    mw.col.reset()
    mw.reset()
    showInfo('done')
def populateEtymology(self):
    mw = self.mw
    cids = self.selectedCards()
    if not cids:
        tooltip(_("No cards selected."), period=2000)
        return
    for nid in self.selectedNotes():
        frenchNote = mw.col.getNote(nid)
        populateEtymologyForOneNote(frenchNote)
    mw.col.reset()
    mw.reset()
    showInfo('done')
def populateIPA(self):
    mw = self.mw
    cids = self.selectedCards()
    if not cids:
        tooltip(_("No cards selected."), period=2000)
        return
    for nid in self.selectedNotes():
        frenchNote = mw.col.getNote(nid)
        populateIPAForOneNote(frenchNote)
    mw.col.reset()
    mw.reset()
    showInfo('done')
def populateAudio(self):
    mw = self.mw
    cids = self.selectedCards()
    if not cids:
        tooltip(_("No cards selected."), period=2000)
        return
    for nid in self.selectedNotes():
        frenchNote = mw.col.getNote(nid)
        populateAudioForOneNote(frenchNote)
    mw.col.reset()
    mw.reset()
    showInfo('done')
def populatePos(self):
    mw = self.mw
    cids = self.selectedCards()
    if not cids:
        tooltip(_("No cards selected."), period=2000)
        return
    for nid in self.selectedNotes():
        frenchNote = mw.col.getNote(nid)
        populatePosForOneNote(frenchNote)
    mw.col.reset()
    mw.reset()
    showInfo('done')
def populatePlural(self):
    mw = self.mw
    cids = self.selectedCards()
    if not cids:
        tooltip(_("No cards selected."), period=2000)
        return
    for nid in self.selectedNotes():
        frenchNote = mw.col.getNote(nid)
        populatePluralForOneNote(frenchNote)
    mw.col.reset()
    mw.reset()
    showInfo('done')
def populateFeminine(self):
    mw = self.mw
    cids = self.selectedCards()
    if not cids:
        tooltip(_("No cards selected."), period=2000)
        return
    for nid in self.selectedNotes():
        frenchNote = mw.col.getNote(nid)
        populateFeminineForOneNote(frenchNote)
    mw.col.reset()
    mw.reset()
    showInfo('done')

def run():

    def setupMenu(self):
        # menu = self.form.menuEdit
        menu = QtWidgets.QMenu('ExtraFields', self.form.menubar)

        if language == 'french':
            a = menu.addAction('Add Conjs to Selected Notes')
            a.triggered.connect(lambda _, b=self: setVerbConjugationsForOneNoteFromBrowser(b))
            # a.setIcon(refresh_note_icon)
            menu.addSeparator()

            b = menu.addAction('all extra fields')
            b.triggered.connect(lambda _, b=self: populateExtraFields(b))
            # b.setIcon(delete_icon)
            menu.addSeparator()

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

            h = menu.addAction('Feminine')
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


run()
