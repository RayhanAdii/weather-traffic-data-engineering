
# import requests
# import pandas as pd

# api_url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/relative/10/xml?key=GyrwSRUHGsEJP9wCFTGyvWx2LSCGaOtN&point=52.40476,4.844318&format=json"  # Replace with the API URL you want to fetch data from
# response = requests.get(api_url)


# if response.status_code == 200:
#     print(response.json())
#     #data = response.json()  # Assuming the API returns JSON data
#     #df = pd.DataFrame(data)
# else:
#     print("Failed to fetch data from the API.")



# #print(data)

import requests
import xml.etree.ElementTree as ET

# Make an HTTP GET request to the API
api_url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/relative/10/xml?key=GyrwSRUHGsEJP9wCFTGyvWx2LSCGaOtN&point=52.40476,4.844318"  # Replace with the actual API URL
response = requests.get(api_url)

# Check the response status code
if response.status_code == 200:
    print("bisa")
    # Access the XML content from the response
    print(response.content)
    xml_data = response.content
    
    # Parse the XML data using xml.etree.ElementTree
    root = ET.fromstring(xml_data)

    # Now you can work with the XML data, for example, extracting elements
    for element in root.findall("./flowSegmentData"):
        # Process and use the XML data
        print("hello")
        print(element.text)

else:
    print("Failed to fetch data from the API.")

