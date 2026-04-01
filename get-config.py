from ncclient import manager
import xml.dom.minidom as dom

# Connection parameters
HOST = '192.168.1.252'
PORT = 830  # Default NETCONF port
USER = 'admin'
PASS = 'realtito2'

# The 'name=csr' parameter is often needed for Cisco IOS XE devices
DEVICE_PARAMS = {'name': 'csr'} 

def get_running_config():
    """Retrieves the running configuration from the device."""
    try:
        with manager.connect(host=HOST, port=PORT, username=USER, password=PASS,
                             device_params=DEVICE_PARAMS, hostkey_verify=False) as m:
            print(f"Connected to {HOST} successfully.")
            
            # Retrieve the running configuration
            result = m.get_config('running')
            
            # Pretty print the XML response
            xml_data = dom.parseString(result.xml)
            pretty_xml = xml_data.toprettyxml(indent="  ")
            print("\n--- Running Configuration ---")
            print(pretty_xml)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_running_config()
