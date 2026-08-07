"""
TR-181 Sample Data (Part 1)
Generated placeholder hierarchy for USP Agent development.
"""

TR181_SAMPLE_DATA = {
    "Device": {
        "USP": {
            "LocalAgent": {
                "Enable": True,
                "EndpointID": "usp-agent-001",
                "MTP": {
                    "MQTT": {
                        "Enable": True,
                        "Broker": "mqtt://localhost:1883",
                        "ClientID": "usp-client"
                    }
                }
            }
        },

        "DeviceInfo": {
            "Manufacturer": "Dummy Networks",
            "ManufacturerOUI": "001A2B",
            "ModelName": "Virtual Router",
            "Description": "TR-181 Sample Device",
            "ProductClass": "Router",
            "SerialNumber": "SN123456789",
            "HardwareVersion": "1.0",
            "SoftwareVersion": "0.1.0",
            "BootloaderVersion": "1.0",
            "AdditionalHardwareVersion": "RevA",
            "AdditionalSoftwareVersion": "Build001",
            "SpecVersion": "2.16",
            "ProvisioningCode": "TEST",
            "UpTime": 12345,
            "FirstUseDate": "2026-01-01T00:00:00Z"
        },

        "Services": {
            "VoiceServiceNumberOfEntries": 1,
            "StorageServiceNumberOfEntries": 1,
            "DummyService": {
                "Enable": True,
                "Status": "Up"
            }
        },

        "Hosts": {
            "HostNumberOfEntries": 2,
            "Host": [
                {
                    "Alias": "Host1",
                    "HostName": "Laptop",
                    "IPAddress": "192.168.1.10",
                    "PhysAddress": "AA:BB:CC:DD:EE:01",
                    "Active": True
                },
                {
                    "Alias": "Host2",
                    "HostName": "Mobile",
                    "IPAddress": "192.168.1.11",
                    "PhysAddress": "AA:BB:CC:DD:EE:02",
                    "Active": True
                }
            ]
        },

        "Users": {
            "UserNumberOfEntries": 1,
            "User": [
                {
                    "Alias": "admin",
                    "Username": "admin",
                    "Enable": True,
                    "Status": "Enabled"
                }
            ]
        },

        "SmartCardReaders": {
            "ReaderNumberOfEntries": 1,
            "Reader": [
                {
                    "Alias": "Reader1",
                    "Status": "Idle"
                }
            ]
        },

        "PeriodicStatistics": {
            "Enable": True,
            "SampleInterval": 60,
            "ReportSamples": 10
        },

        "BulkData": {
            "Enable": True,
            "Profile": [
                {
                    "Alias": "DefaultProfile",
                    "EncodingType": "JSON",
                    "Protocol": "HTTP"
                }
            ]
        },

        "SoftwareModules": {
            "ExecutionUnit": [
                {
                    "Name": "USPAgent",
                    "Version": "1.0.0",
                    "Status": "Running"
                }
            ],
            "DeploymentUnit": [
                {
                    "UUID": "du-001",
                    "Version": "1.0"
                }
            ]
        }
    }
}
