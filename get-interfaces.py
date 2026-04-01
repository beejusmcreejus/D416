import xmltodict
import json
from ncclient import manager

# Connection parameters
HOST = '192.168.1.252'
PORT = 830 # Default NETCONF port over SSH
USER = 'admin'
PASS = 'realtito2'

# NETCONF filter using the ietf-interfaces YANG model
# This filter requests all configuration and state data for all interfaces
NETCONF_FILTER = """
<filter>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    </interfaces-state>
</filter>
"""
# Note: For configuration data, you'd use <get-config> and adjust the filter accordingly,
# e.g., using the "native" model for specific Cisco parameters.

try:
    # Connect to the device using ncclient
    with manager.connect(
        host=HOST,
        port=PORT,
        username=USER,
        password=PASS,
        device_params={'name': 'iosxe'}, # Specify the device type
        timeout=60
    ) as m:
        print(f"Connected to device: {m.connected}")

        # Perform the <get> operation to retrieve data
        # Use m.get() for both configuration and operational data
        result = m.get(NETCONF_FILTER)

        # Print the raw XML output (optional, for debugging)
        # print(result.xml_pretty)

        # Convert the XML output to a Python dictionary for easier parsing
        xml_data = result.xml
        data_dict = xmltodict.parse(xml_data)

        # Convert dictionary to a formatted JSON string for readability
        json_output = json.dumps(data_dict, indent=4)
        print("\nInterface Data (JSON format):")
        print(json_output)

except Exception as e:
    print(f"An error occurred: {e}")
