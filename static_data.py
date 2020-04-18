pronouns = ['je ' , 'tu ' , 'il/elle ' , 'nous ' , 'vous ' , 'ils/ells ']
pronounsx = ['j’' , 'tu ' , 'il/elle ' , 'nous ' , 'vous ' , 'ils,ells ']
que_pronouns  = ['que je ' , 'que tu ' , 'qu’il / qu’elle ' , 'que nous ' , 'que vous ' , 'qu’ils / qu’elles ']
que_pronounsX = ['que j’' , 'que tu ' , 'qu’il / qu’elle ' , 'que nous ' , 'que vous ' , 'qu’ils / qu’elles ']

avoir_pres = ['ai' , 'as' , 'a' , 'avons' , 'aves' , 'ont']
avoir_impf = ['avais' , 'avais' , 'avait' , 'avions' , 'aviez' , 'avaient']
avoir_phis = ['eus' , 'eus' , 'eut' , 'eûmes' , 'eûtes' , 'eurent' ]
avoir_futr = ['aurai' , 'auras' , 'aura' , 'aurons' , 'aurez' , 'auront']
avoir_cond = ["aurais" , "aurais" , "aurait" , "aurions" , "auriez" , "auraient"]
avoir_subj_p = ["aie" , "aies" , "ait" , "ayons" ,"ayez" ,"aient" ]
avoir_subj_impf = ["eusse" , "eusses" , "eût" , "eussions" , "eussiez" , "eussent"]
avoir_imperative = ["aie" , "ayons" , "ayez"]

etre_pres = ['suis' , 'es' , 'est' , 'sommes' , 'êtes' , 'sont']
etre_impf = ['étais' , 'étais' , 'était' , 'étions' , 'étiez' , 'étaient']
etre_phis = ['fus' , 'fus' , 'fut' , 'fûmes' , 'fûtes' , 'furent' ]
etre_futr = ['serai' , 'seras' , 'sera' , 'serons' , 'serez' , 'seront']
etre_cond = ["serais" , "serais" , "serait" , "serions" , "seriez" , "seraient"]
etre_subj_p = ["sois" , "sois" , "soit" , "soyons" ,"soyez" ,"soient" ]
etre_subj_impf = ["fusse" , "fusses" , "fût" , "fussions" , "fussiez" , "fussent"]
etre_imperative =  ["sois" , " 	soyons" , "soyez"]

auxiliary_avoir = (avoir_pres, avoir_impf, avoir_phis,avoir_futr , avoir_cond, avoir_subj_p,avoir_subj_impf ,avoir_imperative)
auxiliary_etre = (etre_pres, etre_impf, etre_phis,etre_futr , etre_cond, etre_subj_p,etre_subj_impf ,etre_imperative )

avoir_pres_IPA = ['/e/' , '/a/' , '/a/' , '/a.vɔ̃/' , '/a.ve' , '/ɔ̃/']
avoir_impf_IPA = ['/a.vɛ/' , '/a.vɛ/' , '/a.vɛ/' , '/a.vjɔ̃/' , '/a.vje/' , '/a.vɛ/']
avoir_phis_IPA = ['/y/' , '/y/' , '/y/' , '/ym/' , '/yt/' , '/yʁ/' ]
avoir_futr_IPA = ['/o.ʁe/' , '/o.ʁa/' , '/o.ʁa/' , '/o.ʁɔ̃/' , '/o.ʁe/' , '/o.ʁɔ̃/']
avoir_cond_IPA = ["/o.ʁɛ/" , "/o.ʁɛ/" , "/o.ʁɛ/" , "/o.ʁjɔ̃/" , "/o.ʁje/" , "/o.ʁɛ/"]
avoir_subj_p_IPA = ["/ɛ/" , "/ɛ/" , "/ɛ/" , "/ɛ.jɔ̃/" ,"/ɛ.je/" ,"/ɛ/" ]
avoir_subj_impf_IPA = ["/ys/" , "/ys/" , "/y/" , "/y.sjɔ̃/" , "/y.sje/" , "/ys/"]
avoir_imperative_IPA = ["/ɛ/" , "/ɛ.jɔ̃/" , "/ɛ.je/"]

etre_pres_IPA = ['/sɥi/' , '/ɛ/' , '/ɛ/' , '/sɔm/' , '/ɛt/' , '/sɔ̃/']
etre_impf_IPA = ['/e.tɛ/' , '/e.tɛ/' , '/e.tɛ/' , '/e.tjɔ̃/' , '/e.tje/' , '/e.tɛ/']
etre_phis_IPA = ['/fy/' , '/fy/' , '/fy/' , '/fym/' , '/fyt/' , '/fyʁ/' ]
etre_futr_IPA = ['/sə.ʁe/' , '/sə.ʁa/' , '/sə.ʁa/' , '/sə.ʁɔ̃/' , '/sə.ʁe/' , '/sə.ʁɔ̃/']
etre_cond_IPA = ["/sə.ʁɛ/" , "/sə.ʁɛ/" , "/sə.ʁɛ/" , "/sə.ʁjɔ̃/" , "/sə.ʁje/" , "/sə.ʁɛ/"]
etre_subj_p_IPA = ["/swa/" , "/swa/" , "/swa/" , "/swa.jɔ̃/" ,"/swa.je/" ,"/swa/" ]
etre_subj_impf_IPA = ["/fys/" , "/fys/" , "/fy/" , "/fy.sjɔ̃/" , "/fy.sje/" , "/fys/"]
etre_imperative_IPA =  ["/swa/ " , "/swa.jɔ̃/" , "/swa.je/"]

auxiliary_avoir_IPA = (avoir_pres_IPA, avoir_impf_IPA, avoir_phis_IPA,avoir_futr_IPA , avoir_cond_IPA, avoir_subj_p_IPA,avoir_subj_impf_IPA ,avoir_imperative_IPA)
auxiliary_etre_IPA = (etre_pres_IPA, etre_impf_IPA, etre_phis,etre_futr_IPA , etre_cond_IPA, etre_subj_p_IPA,etre_subj_impf_IPA ,etre_imperative_IPA )

conjugations_names = ['indc_pres','indc_impf','indc_phis','indc_futr','indc_cond',
                      'indc_pp','indc_pqp','indc_pa','indc_fa','indc_condp' ,
                      'subj_pres' , 'subj_impf' , 'subj_p' , 'subj_pqf' ,
                       'imperative_smpl' , 'imperative_comp']
