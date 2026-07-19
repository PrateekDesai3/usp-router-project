class SupportedDataModel:

    @staticmethod
    def get():

        return {

            "Device": {

                "DeviceInfo": {

                    "Parameters": [

                        "Manufacturer",
                        "ManufacturerOUI",
                        "ModelName",
                        "Description",
                        "SoftwareVersion",
                        "HardwareVersion",
                        "SerialNumber",
                        "HostName",
                        "UpTime"

                    ]

                },

                "IP": {

                    "Interface": [

                        "Name",
                        "Enable",
                        "Status",
                        "Type",
                        "MACAddress",
                        "IPv4Address",
                        "IPv6Address"

                    ]

                },

                "Routing": {

                    "Routes": True

                }

            }

        }