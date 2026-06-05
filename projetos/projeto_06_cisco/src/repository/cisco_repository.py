class CiscoRepository:

    def get_devices(self):

        return {
            "response": [
                {
                    "hostname": "SW-SP01",
                    "managementIpAddress": "10.10.1.10",
                    "platformId": "C9300",
                    "softwareVersion": "17.09.03",
                    "serialNumber": "ABC123"
                },
                {
                    "hostname": "RTR-RJ01",
                    "managementIpAddress": "10.20.1.1",
                    "platformId": "ISR4331",
                    "softwareVersion": "17.06.04",
                    "serialNumber": "XYZ456"
                }
            ]
        }