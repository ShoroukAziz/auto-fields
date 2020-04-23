from bs4 import BeautifulSoup
from .anki_wiki_parser import *
from .wiki_french_verb_parser import *
from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo
from bs4 import BeautifulSoup
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets , QtGui
from PyQt5.QtWidgets import QAction, QProgressDialog, QWidget, QPushButton, QVBoxLayout
from aqt import mw
from anki.hooks import addHook
from .anki_wiki_parser import *
from .wiki_french_verb_parser import *


def progress(data, *args):
    """
    A very pythonic progress dialog.

    Iterate over progress(iterator)
    instead of iterator. That’s pretty much it.

    """
    # found at http://lateral.netmanagers.com.ar/weblog/posts/BB917.html
    # © 2000-2012 Roberto Alsina
    # Creative Commons Attribution-NonCommercial-ShareAlike 2.5 licence
    # http://creativecommons.org/licenses/by-nc-sa/2.5/
    it = iter(data)
    widget = QProgressDialog(*args + (0, it.__length_hint__()))
    c = 0
    for v in it:
        QCoreApplication.instance().processEvents()
        if widget.wasCanceled():
            raise StopIteration
        c += 1
        widget.setValue(c)
        yield(v)


def setVerbConjugationsForOneNote(verb_note):

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
    p =WikitionaryFrenchParser(word)
    etymology =  p.getEtymology()
    note.flush()
def populateIPAForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p = WikitionaryFrenchParser(word)
    IPA =  p.getIPA()
    if IPA is not None:
        note['IPA'] = IPA
        note.flush()
def populateAudioForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p = WikitionaryFrenchParser(word)
    audio = p.getAudio()
    if audio is not None:
        note['sound'] = audio
        note.flush()
def populatePosForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p = WikitionaryFrenchParser(word)
    pos = p.getPartOfSpeech()
    if pos is not None:
        note['type'] = pos
        note.flush()
def populatePluralForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p = WikitionaryFrenchParser(word)
    plural = p.getPlural()
    if plural is not None:
        note['plural'] = plural
        note.flush()
def populateFeminineForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p = WikitionaryFrenchParser(word)
    feminine = p.getFeminine()
    if feminine is not None:
        note['feminin version'] = feminine
        note.flush()
def populateExtraFieldsForOneNote(note):

    word = BeautifulSoup(note['word'].lower(),'html.parser').get_text()
    p =WikitionaryFrenchParser(word)
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
    ids = self.selectedNotes()
    for nid in progress(ids, _("getting conjs"), _("Stop!")):
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
    ids = self.selectedNotes()
    for nid in  progress(ids, _("getting all Extra Fields"), _("Stop!")):
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
    ids = self.selectedNotes()
    for nid in  progress(ids, _("getting etymologys"), _("Stop!")):
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
    ids = self.selectedNotes()
    for nid in  progress(ids, _("getting IPAs"), _("Stop!")):
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
    ids = self.selectedNotes()
    for nid in  progress(ids, _("getting Audio files"), _("Stop!")):
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
    ids = self.selectedNotes()
    for nid in  progress(ids, _("getting POSs"), _("Stop!")):
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
    ids = self.selectedNotes()
    for nid in  progress(ids, _("getting plurals"), _("Stop!")):
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
    ids = self.selectedNotes()
    for nid in  progress(ids, _("getting feminine forms"), _("Stop!")):
        frenchNote = mw.col.getNote(nid)
        populateFeminineForOneNote(frenchNote)
    mw.col.reset()
    mw.reset()
    showInfo('done')
