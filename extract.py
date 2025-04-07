import requests
import json
from collections import defaultdict
import pandas as pd


class Extractor:
    def __init__(self):
        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?'
        self.url2 = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'
        self._keys = ['Title', 'Summary', 'Organism', 'Type', 'Overall Design']


    def _request_data(self, id):
        params = {
            "db":"gds",
            "linkname":"pubmed_gds",
            "id":id,
            "retmode": "json"
        }
        
        response = requests.get(self.url, params=params)
        data = response.json()
        ids = (",").join(data['linksets'][0]['linksetdbs'][0]['links'])

        params2 = {
            "db":"gds",
            "id":ids
        }

        response = requests.get(self.url2, params=params2)
        return self._preprocesing(response.text)


    def _preprocesing(self, data: str):
        data = data.replace("\t\t", " ")
        data = data.replace("\t", " ")
        data = data.replace("  ", " ")
        data_split = data.split("\n")
        return data_split
        

    def _parse(self, id, data: list):
        counter = 0
        result = {'id': id,
                  'data': []
                 }

        for index, line in enumerate(data):
            if line:
                if counter == 0:
                    splitted = data[index][3:]
                    result['data'].append(splitted)

                elif counter == 1:
                    splitted = data[index]
                    result['data'].append(splitted)

                else:
                    splitted = data[index].split(": ")
                    if len(splitted) < 2 or splitted[0] not in self._keys:
                        pass
                    else:
                        result['data'].append(splitted[1])

                counter += 1
            else:
                ",".join(result['data'])
                counter = 0

        return pd.DataFrame.from_dict(result)   
        

    def _postprocess(self, data:dict):
        new_data = {}
        for key in data.keys():
            if key in self._keys:
                new_data[key] = data[key]
        return new_data


    def exe_file(self, file):
        res_df = pd.DataFrame()
        for id in file:
            print(f'processing {id}')
            id = id.decode().replace('\n','')
            surowiec = self._request_data(id)
            fried = self._parse(id, surowiec)
            res_df = pd.concat([res_df, fried])
        res_df.to_csv('out.csv', index=False)  
        return res_df.reset_index(drop=True)
