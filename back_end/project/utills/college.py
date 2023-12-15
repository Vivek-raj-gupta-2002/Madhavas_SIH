import requests

url = "https://aishe.gov.in/aishe/instDirectoryCollegeIndex"

payload = {'flag': 'false',
'stateId': '-1',
'districtCode': '-1',
'universitytypeId': '-1',
'universityId': '-1',
'collegeType': '-1',
'reportFormatType': '3'}
files=[

]
headers = {
  'Cookie': 'JSESSIONID=9DDFC3A3B507551EB6233317AB507F8F; SERVERID=aishe5'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files, timeout=10)

print(response.text)
