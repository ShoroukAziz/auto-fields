from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo
from bs4 import BeautifulSoup
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets , QtGui
from PyQt5.QtWidgets import QAction, QProgressDialog, QWidget, QPushButton, QVBoxLayout
from aqt import mw
from anki.hooks import addHook
from .gui import run
import os , sys , shutil , json
#
# CONFIG = mw.addonManager.getConfig(__name__)
#
# collection_media_path = CONFIG['collection_media_path']
#
# language = CONFIG['lang']


run()
