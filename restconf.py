import requests
import json
from requests.auth import HTTPBasicAuth
import urllib
from pprint import pprint

# Disable warnings from SSL/TLS certificates (use valid certs in production)
requests.packages.urllib3.disable_warnings()

# Device details
HOST = '192.168.1.252'
USER = 'admin'
PASS = 'realtito2'

# RESTCONF API URL for the hostname (IOS XE Native model example)
# The exact URL path depends on the device OS and YANG model
URL = f"https://{HOST}/restconf/data/Cisco-IOS-XE-native:native/interface"

# HTTP headers for RESTCONF with JSON data
HEADERS = {
#    "Content-Type": "application/yang-data+json",
#    "Accept": "application/yang-data+json"
     "Accept": "*/*"
}

try:
    # Perform the GET request
    response = requests.get(
        URL,
        auth=HTTPBasicAuth(USER, PASS),
        headers=HEADERS,
        verify=False # Do not verify SSL certificates (change for production)
    )

    # Check for a successful response (HTTP status code 200)
    if response.status_code == 200:
        hostname_data = response.json()
        # The structure of the JSON response depends on the device
        print(f"Hostname retrieved: {hostname_data['Cisco-IOS-XE-native:hostname']}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
