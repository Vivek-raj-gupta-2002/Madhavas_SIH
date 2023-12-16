import requests

url = "https://aishe.gov.in/aishe/instDirectoryCollegeIndex"

params = {
    "flag": False,
    "stateId": -1,
    "districtCode": -1,
    "universitytypeId": -1,
    "universityId": -1,
    "collegeType": -1,
    "reportFormatType": 3
}

headers = {
    "User-Agent": "Your User Agent String",
    "Authorization": "Bearer YourAccessToken",
    # Add any other headers as needed
}

response = requests.get(url, params=params, headers=headers)

# Check the response status code and content
print(response.status_code)
print(response.text)
