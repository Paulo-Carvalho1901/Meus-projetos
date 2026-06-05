import pandas as pd


class InventoryService:

    def __init__(self, repository):

        self.repository = repository

    def process(self):

        data = self.repository.get_devices()

        devices = []

        for device in data["response"]:

            devices.append({

                "hostname":
                    device["hostname"],

                "ip":
                    device["managementIpAddress"],

                "platform":
                    device["platformId"],

                "version":
                    device["softwareVersion"],

                "serial":
                    device["serialNumber"]
            })

        df = pd.DataFrame(devices)

        df.drop_duplicates(inplace=True)

        return df