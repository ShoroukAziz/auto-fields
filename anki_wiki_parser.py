# import pprint
import requests , os , shutil , sys
from aqt import mw

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/WiktionaryParser')
from .WiktionaryParser.wiktionaryparser import WiktionaryParser


CONFIG = mw.addonManager.getConfig(__name__)

collection_media_path = CONFIG['collection_media_path']
language = CONFIG['lang']

class WikitionaryFrenchParser(object):
    def __init__(self , word='None'):
        self.word = word
        parser = WiktionaryParser()
        parser.set_default_language(language)
        try:
            self.wiki_word = parser.fetch(self.word )[0]
        except :
            self.wiki_word = None


    def getEtymology (self):
        if self.wiki_word == None:
            return None
        try:
            etymology = self.wiki_word['etymology']
            etymology =  ' '.join(etymology.split(' '))
            etymology = etymology.replace("\n", " ")
            return etymology
        except:
            return None


    def getIPA (self):
        if self.wiki_word == None:
            return None
        try:
            IPA = '/'+self.wiki_word['pronunciations']['text'][0].split('/')[1]+'/'
            return IPA
        except:
            return None

    def getAudio (self):
        if self.wiki_word == None:
            return None
        try:
            url = 'https:'+self.wiki_word['pronunciations']['audio'][0]
            cookies = requests.head(url)
            r = requests.get(url, verify=True, cookies=cookies, timeout=10)
            file_name = self.word+".mp3"
            with open(file_name, 'wb') as f:
                f.write(r.content)

            shutil.move("./"+file_name,collection_media_path+"/"+file_name)

            return '[sound:'+self.word+'.mp3]'
        except:
            return None


    def getPartOfSpeech (self):
        if self.wiki_word == None:
            return None
        try:
            partOfSpeech = self.wiki_word['definitions'][0]['partOfSpeech']
            if  partOfSpeech == 'noun' or  partOfSpeech == 'Noun':
                data  = self.wiki_word['definitions'][0]['text'][0].replace('\xa0',' ')

                if 'feminine' in data and self.word+'e' in data:
                    return 'masculine and feminine noun'
                elif ' m ' in data:
                    return "masculine noun"
                elif ' f 'in data:
                    return "feminine noun"
                else:
                    return partOfSpeech
            else:
                return partOfSpeech



        except:
            return None

    def getPlural (self):
        if self.wiki_word == None:
            return None
        try:
            pos = self.getPartOfSpeech()
            data  = self.wiki_word['definitions'][0]['text'][0]
            if 'noun' in pos or 'adjective' in pos:
                if 'plural' in data:
                    plural = data.split('plural')[1]
                    if ',' in plural :
                        plural = plural.split(',')[0]
                    elif ')' in data :
                        plural = plural.split(')')[0]
                    else:
                        plural = plural.split(' ')[0]
                else:
                    return None

            else :
                plural = None
            return plural
        except:
            return None

    def getFeminine (self):
        if self.wiki_word == None:
            return None
        try:
            pos = self.getPartOfSpeech()
            data  = self.wiki_word['definitions'][0]['text'][0]
            if 'masculine and feminine noun' in pos or 'adjective' in pos.lower() :
                if 'feminine singular' in data:
                    feminine = data.split('feminine singular')[1]
                    if ',' in feminine :
                        feminine = feminine.split(',')[0]
                    elif ')' in data :
                        feminine = feminine.split(')')[0]
                    else:
                        feminine = feminine.split(' ')[0]
                else:
                    return None
            else :
                feminine = None
            return feminine
        except:
            return None


# c = WikitionaryFrenchParser('beau')
# res = c.getPartOfSpeech()
# res1 = c.getPlural()
# res2 = c.getFeminine()
# res3 =  c.getAudio()

# pprint.pprint(res1)
# print( res , " - " , res1 , " - " , res2 , " - " , res3)
