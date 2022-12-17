import os
import json 

class Database:
    def read(tabel = 'obat'):
        path = os.path.join(os.path.dirname(__file__), 'db_'+tabel+'.json')
        opendata = open(path)
        data = json.load(opendata)
        return data
    
    def save(tabel, data):
        path = os.path.join(os.path.dirname(__file__), 'db_'+tabel+'.json')
        opendata = open(path, 'w')
        
        data = json.dump(data, opendata, indent=4)
        return data
    
    def delete(tabel, id):
        path = os.path.join(os.path.dirname(__file__), 'db_'+tabel+'.json')
        opendata = open(path)
        
        data = json.load(opendata)
        
        data.pop(id)
        
        opendata = open(path, 'w')
        data = json.dump(data, opendata, indent=4)
        return data