import pandas as pd
from django.conf import settings
import os

"""
College And School Data with sorting applied
"""
scl_url = os.path.join(settings.BASE_DIR, 'api_data/schools.csv')

scl_data = pd.read_csv(scl_url, low_memory=False)

req_data_school = scl_data[['udise_code', 'school_name', 'state', 'district']]

# sorting methods
class SchoolData:
    def __init__(self, data=req_data_school) -> None:
        self.req_data = data

    def get_state_data(self, state: str):
        return self.req_data[self.req_data['state'] == state]

    def get_district_data(self, district, state):
        
        return self.get_state_data(state)[self.get_state_data(state)['district'] == district]
    

    def get_unique_state(self):
        return self.req_data['state'].unique()
    
    def get_unique_district(self, state):
        return self.req_data[self.req_data['state'] == state]['district'].unique()



# college Data
clg_URL = os.path.join(settings.BASE_DIR, 'api_data/College.csv')

clg_data = pd.read_csv(clg_URL)

req_data_clg = clg_data[['State', 'District', 'University Name','College Name']]


# sorting methods
class CollegeData:

    def __init__(self, data=req_data_clg) -> None:
        self.req_data = data

    def get_state_data(self, state: str):
        return self.req_data[self.req_data['State'] == state]

    def get_district_data(self, district: str, state: str):
        return self.get_state_data(state)[self.get_state_data(state)['District'] == district]
    
    def get_university_data(self, university: str):
        return self.req_data[self.req_data['University Name'] == university]
    
    def get_unique_state(self):
        return self.req_data['State'].unique()


    def get_unique_district(self, state):
        distrct_data = self.get_state_data(state)

        return distrct_data['District'].unique()


import requests

url = "http://127.0.0.1:8000/institute/api/getClg/Bihar"

payload = {}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)



