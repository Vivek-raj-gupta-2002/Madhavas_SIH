import requests

url = "https://aishe.gov.in/aishe/instDirectoryCollegeIndex"

data = {
    "flag": False,
    "stateId": -1,
    "districtCode": -1,
    "universitytypeId": -1,
    "universityId": -1,
    "collegeType": -1,
    "reportFormatType": 3
}

response = requests.post(url, data=data)

print(response.status_code)
print(response.text)
