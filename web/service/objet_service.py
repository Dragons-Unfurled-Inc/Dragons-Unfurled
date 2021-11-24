import requests as requ

class ObjetService():
    
    @staticmethod
    def getNetObjet():
        query = """query{
        monsters(limit : 500){name,type}
        }
        """
        endpoint="https://www.dnd5eapi.co/graphql"
        r = requ.post(endpoint,json={"query":query})
        noms_types = r.json()
        return(noms_types['data']['monsters'])