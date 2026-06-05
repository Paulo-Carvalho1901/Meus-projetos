from dataclasses import dataclass


@dataclass
class DeviceDTO:

    hostname: str
    ip: str
    platform: str
    version: str
    serial: str