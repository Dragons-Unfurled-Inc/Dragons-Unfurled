from client.service.monstre_service import MonstreService
import requests as req

#print(essai.__dict__())

#M = MonstreService.ImportMonstreWeb('aboleth')
#print(M)

monstres = req.get('https://www.dnd5eapi.co/api/monsters')
monstres = monstres.json()
nom_monstres = [d["index"] for d in monstres["results"]]
monstres_par_types = {}
for monstre in nom_monstres : 
    dic_monstre = req.get('https://www.dnd5eapi.co/api/monsters/' + monstre)
    dic_monstre = dic_monstre.json()
    type_monstre = dic_monstre["type"]
    if type_monstre not in monstres_par_types:
        monstres_par_types[type_monstre] = [monstre]
    else :
        monstres_par_types.update({type_monstre : monstres_par_types[type_monstre]+[monstre]})
    print(monstres_par_types)
print(monstres_par_types)
