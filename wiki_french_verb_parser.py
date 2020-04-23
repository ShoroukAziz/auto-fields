import re, requests
from aqt import mw
from bs4 import BeautifulSoup
import json
import time
import pprint as pp
import os
import sys
import shutil
from .static_data import *    #from static_data import *
CONFIG = mw.addonManager.getConfig(__name__)

collection_media_path = CONFIG['collection_media_path']


class WikitionaryFrenchVerbParser(object):
    def __init__(self , word='None'):
        self.word = word
        self.url = "https://en.wiktionary.org/wiki/{}#Conjugation?printable=yes"
        # self.soup = None
        self.session = requests.Session()
        self.session.mount("http://", requests.adapters.HTTPAdapter(max_retries = 2))
        self.session.mount("https://", requests.adapters.HTTPAdapter(max_retries = 2))
        self.current_word = None
        def getFrenchSoup():
            response = self.session.get(self.url.format(self.word))
            soup = BeautifulSoup(response.text.replace('>\n<', '><'), 'html.parser')
            french = soup.find(id="French")
            return french
        self.frenchSoup = getFrenchSoup()





    def  getVerbConj(self):

        def getIPA(element):
            try:
                return div.find_all(class_=element)[0].findNext(class_='IPA').text
            except:
                return ""

        try:
            try:
                conjugation = self.frenchSoup.findNext(id='Conjugation')
            except:
                conjugation = self.frenchSoup.findNext(id='Conjugation_2')
            div = conjugation.findNext('div')
            pp = div.find_all(class_='pp-form-of') [0].text
            pp_IPA = getIPA('pp-form-of')
        except:
            return

        if(div.find(title='avoir')):
            pres ,impf ,phis,futr,cond,subj_p,subj_impf,imperative = auxiliary_avoir
            pres_IPA ,impf_IPA ,phis_IPA,futr_IPA,cond_IPA,subj_p_IPA,subj_impf_IPA,imperative_IPA = auxiliary_avoir_IPA
        elif(div.find(title='être')):
            pres ,impf ,phis,futr,cond,subj_p,subj_impf,imperative = auxiliary_etre
            pres_IPA ,impf_IPA ,phis_IPA,futr_IPA,cond_IPA,subj_p_IPA,subj_impf_IPA,imperative_IPA = auxiliary_etre_IPA
        else:
            return

        inner_html = lambda element :div.find_all(class_=element)[0].text
        startsWithVowel = lambda word : not word.startswith(("a","e","i","o","u","h"))



        conjs = {}
        for name in conjugations_names :
            conjs[name] = {}
            conjs[name]['conjs']=[]
            conjs[name]['IPA']=["","","","","",""]
            conjs[name]['audio']=["","","","","",""]
            conjs[name]['example_fr']=["","","","","",""]
            conjs[name]['example_en']=["","","","","",""]
            conjs[name]['example_audio']=["","","","","",""]



        def generateConjugation(simple , pronoun , pronounx, conjugatedVerb=None , auxilary=None ,pastParticiple=None ):
            if simple == True:
                try:
                    if startsWithVowel(inner_html(conjugatedVerb)):
                        return pronoun+inner_html(conjugatedVerb)
                    else :
                        return pronounx+inner_html(conjugatedVerb)
                except:
                    return ""
            else:
                if startsWithVowel(auxilary):
                    return  pronoun+auxilary+" "+pastParticiple
                else:
                    return pronounx+auxilary+" "+pastParticiple


        def generateCompoundConjugation(auxilary,pronoun,pronounx,pastParticiple):
            try:
                if startsWithVowel(auxilary):
                    conj =  pronoun+auxilary+" "+pastParticiple
                else:
                    conj = pronounx+auxilary+" "+pastParticiple
            except:
                conj = ""
            return conj


        def getIndicativeSimpleTenses():
            tenses1 = ['pres' , 'impf' ]
            tenses2 =  ['phis' , 'futr' , 'cond']
            classes_names= ['1|s|tense|mod-form-of','2|s|tense|mod-form-of','3|s|tense|mod-form-of',
            '1|p|tense|mod-form-of','2|p|tense|mod-form-of','3|p|tense|mod-form-of']
            classes1 = [[c.replace('tense',tense1).replace('mod','indc') for c in classes_names  ]  for tense1 in tenses1]
            classes =classes1+ [[c.replace('tense|mod',tense2) for c in classes_names  ]  for tense2 in tenses2]
            for i in range(5):
                conjs[conjugations_names[i]]['conjs'] = [generateConjugation(True ,conjugatedVerb= element ,pronoun= p1 ,pronounx= p1x) for (element,p1,p1x) in zip(classes[i], pronouns, pronounsx) ]
                conjs[conjugations_names[i]]['IPA'] = [getIPA(element) for element in classes[i]]
        def getIndicativeCompoundTenses():
            for i , auxiliary_list ,auxiliary_list_IPA  in zip(range(5,10) , [pres,impf,phis,futr,cond] ,[pres_IPA,impf_IPA,phis_IPA,futr_IPA,cond_IPA] ):
                conjs[conjugations_names[i]]['conjs']  = [generateConjugation(False,p1,p1x,auxilary=a ,pastParticiple=pp) for (p1,p1x,a) in zip(pronouns,pronounsx ,auxiliary_list)]
                conjs[conjugations_names[i]]['IPA'] = [auxilary_ipa+" "+pp_IPA for auxilary_ipa in auxiliary_list_IPA]

        def getSubjunctiveSimpleTenses():
            tenses = ['pres' , 'impf' ]
            classes_names= ['1|s|tense|subj-form-of','2|s|tense|subj-form-of','3|s|tense|subj-form-of',
            '1|p|tense|subj-form-of','2|p|tense|subj-form-of','3|p|tense|subj-form-of']
            classes = [[c.replace('tense',tense) for c in classes_names  ]  for tense in tenses]
            conjs["subj_pres"]['conjs'] = [generateConjugation(True ,conjugatedVerb= element ,pronoun= p1 ,pronounx= p1x) for (element,p1,p1x) in zip(classes[0] , que_pronouns , que_pronounsX)]
            conjs["subj_impf"]['conjs'] = [generateConjugation(True ,conjugatedVerb= element ,pronoun= p1 ,pronounx= p1x) for (element,p1,p1x) in zip(classes[1], que_pronouns , que_pronounsX)]

            conjs["subj_pres"]['IPA'] =  [getIPA(element) for element in classes[0]]
            conjs["subj_impf"]['IPA'] =  [getIPA(element) for element in classes[1]]


        def getSubjunctiveCompoundTenses():
            conjs["subj_p"]['conjs'] = [generateConjugation(False,p1,p1x,auxilary=a ,pastParticiple=pp) for (p1,p1x,a) in zip(que_pronouns,que_pronounsX , subj_p)]
            conjs["subj_pqf"]['conjs'] = [p1+" "+pp for p1 in subj_impf]

            conjs["subj_p"]['IPA'] = [ipa +" "+pp_IPA for ipa in  subj_p_IPA  ]
            conjs["subj_pqf"]['IPA'] = [ipa +" "+pp_IPA for ipa in  subj_impf_IPA  ]

        def getImperativeSimple():
            classses = ['2|s|impr-form-of' , '1|p|impr-form-of' , '2|p|impr-form-of']
            try:
                conjs["imperative_smpl"]['conjs'] = [inner_html(class_name) for class_name in classses]
                conjs["imperative_smpl"]['IPA'] = [getIPA(element) for element in classses]

            except :
                conjs["imperative_smpl"]['conjs'] = []
                conjs["imperative_smpl"]['IPA'] = []


        def getImperativeCompound():
            conjs["imperative_comp"]['conjs'] = [p1+" "+pp for p1 in imperative]
            conjs["imperative_comp"]['IPA'] = [ipa +" "+pp_IPA for ipa in  imperative_IPA  ]



        getIndicativeSimpleTenses()
        getIndicativeCompoundTenses()
        getSubjunctiveSimpleTenses()
        getSubjunctiveCompoundTenses()
        getImperativeSimple()
        getImperativeCompound()
        return(conjs)


# c = WikitionaryFrenchVerbParser('salut')
# res = c.getIPA()
# pp.pprint(res)
