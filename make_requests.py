import requests
import json
import time

i = 0
offset = 1
limit = 1000
headers = {'Token': 'iPUFLyvvyzixkBcMRarLLeoLASMlWkEE'
           }
payload = {'limit': limit,
           'offset': offset}
data_set_name = 'locations'
r = requests.get(f'https://www.ncdc.noaa.gov/cdo-web/api/v2/{data_set_name}', headers=headers, params=payload)
r_dict = r.json()
total_results = r_dict['metadata']['resultset']['count']
r_str = json.dumps(r_dict, indent=4)
while offset <= total_results:
    time.sleep(.75)
    with open(f'{data_set_name}_{i}.json', 'w') as outfile:
        outfile.write(r_str)
    i += 1
    offset = offset + limit
    payload = {'limit': limit,
               'offset': offset}
    r = requests.get(f'https://www.ncdc.noaa.gov/cdo-web/api/v2/{data_set_name}', headers=headers, params=payload)
    r_dict = r.json()
    r_str = json.dumps(r_dict, indent=4)
