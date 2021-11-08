from client.service.monstre_service import MonstreService
import requests as req

#print(essai.__dict__())

#M = MonstreService.ImportMonstreWeb('aboleth')
#print(M)

req = MonstreService.web_monstre(nom)
req = requ.get('https://www.dnd5eapi.co/api/monsters/' + nom)
d=req.json()