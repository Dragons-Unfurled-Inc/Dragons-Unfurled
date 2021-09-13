from lancerDe import LancerDe
import requests as req
import json

D=LancerDe("Moi",2,6)
print(D)
r = req.get('https://www.dnd5eapi.co/api/races')
d=r.json()
