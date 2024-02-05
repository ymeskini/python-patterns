from dataclasses import dataclass, field
from enum import Enum


class DeviceStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    ERROR = "Error"


class DeviceType(Enum):
    LIGHT = "Smart Light"
    THERMOSTAT = "Smart Thermostat"
    SECURITY_CAMERA = "Security Camera"
    DOOR_LOCK = "Smart Door Lock"
    SPEAKER = "Smart Speaker"


@dataclass
class DeviceConfig:
    configuration: dict[str, str] = field(default_factory=dict)

    def update_config(self, key: str, value: str):
        """Update or add a configuration setting for the device."""
        self.configuration[key] = value


@dataclass
class IoTDevice:
    name: str
    device_type: DeviceType
    status: DeviceStatus
    config: DeviceConfig = field(default_factory=DeviceConfig)
    firmware_version: int = field(default=1, init=False)

    def __post_init__(self):
        """Post-initialization to set dynamic defaults."""
        # For example, automatically activate new devices if they are certain types
        if self.device_type in [DeviceType.LIGHT, DeviceType.SPEAKER]:
            self.status = DeviceStatus.ACTIVE
        # Initialize a firmware version based on the device type
        if self.device_type == DeviceType.THERMOSTAT:
            self.firmware_version = (
                2  # Example of setting a default value conditionally
            )

    def activate(self):
        if self.status != DeviceStatus.ACTIVE:
            self.status = DeviceStatus.ACTIVE
            print(f"{self.name} activated.")
        else:
            print(f"{self.name} is already active.")

    def deactivate(self):
        if self.status != DeviceStatus.INACTIVE:
            self.status = DeviceStatus.INACTIVE
            print(f"{self.name} deactivated.")
        else:
            print(f"{self.name} is already inactive.")


@dataclass
class SmartHome:
    devices: list[IoTDevice] = field(default_factory=list)

    def add_device(self, device: IoTDevice):
        """Add a new IoT device to the smart home system."""
        self.devices.append(device)
        print(f"Added {device.name} to the smart home system.")

    def list_devices(self):
        """List all devices in the smart home system."""
        for device in self.devices:
            print(f"{device.name} ({device.device_type}) - {device.status.value}")


# Example usage
smart_home = SmartHome()

smart_home.add_device(
    IoTDevice(
        name="Living Room Light",
        device_type=DeviceType.LIGHT,
        status=DeviceStatus.INACTIVE,
    )
)
smart_home.add_device(
    IoTDevice(
        name="Door Security Camera",
        device_type=DeviceType.SECURITY_CAMERA,
        status=DeviceStatus.INACTIVE,
    )
)

smart_home.list_devices()

# Demonstrating post-init customization
for device in smart_home.devices:
    print(
        f"{device.name}: Firmware Version {device.firmware_version}, Status: {device.status.value}"
    )
