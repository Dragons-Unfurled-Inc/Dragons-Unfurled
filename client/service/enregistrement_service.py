import os
import json

class Enregistre():
    
    @staticmethod
    def enregistrejson(dic):
        with open('table.txt', 'w') as outfile:
            json.dump(dic, outfile)

            