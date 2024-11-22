from dataclasses import dataclass

from google_service import GoogleCredentials, GoogleServiceProvider, GoogleStorage
from azure_service import AzureCredentials, AzureServiceProvider, AzureStorage


@dataclass
class GoogleCloudService:
    auth_provider: GoogleCredentials
    service: GoogleServiceProvider
    storage_manager: GoogleStorage

    def connect(self) -> None:
        print("Connecting to the cloud service.")
        credentials = self.auth_provider.get_credentials()
        self.service.authenticate(credentials)
        context = self.service.get_context()
        self.storage_manager.initialize(context)
        print("Cloud service connected.")


@dataclass
class AzureCloudService:
    auth_provider: AzureCredentials
    service: AzureServiceProvider
    storage_manager: AzureStorage

    def connect(self) -> None:
        print("Connecting to the cloud service.")
        credentials = self.auth_provider.fetch_credentials()
        self.service.authenticate(credentials)
        context = self.service.get_context()
        self.storage_manager.setup(context)
        print("Cloud service connected.")


def connect_to_cloud_service(
    cloud_service: AzureCloudService | GoogleCloudService,
) -> None:
    if isinstance(cloud_service, AzureCloudService):
        print("Connecting to the Azure cloud service.")
        credentials = cloud_service.auth_provider.fetch_credentials()
        cloud_service.service.authenticate(credentials)
        context = cloud_service.service.get_context()
        cloud_service.storage_manager.setup(context)
    else:
        print("Connecting to the Google cloud service.")
        credentials = cloud_service.auth_provider.get_credentials()
        cloud_service.service.authenticate(credentials)
        context = cloud_service.service.get_context()
        cloud_service.storage_manager.initialize(context)

    print("Cloud service connected.")


def main() -> None:
    credentials = GoogleCredentials()
    service = GoogleServiceProvider()
    storage = GoogleStorage()
    cloud_service = GoogleCloudService(credentials, service, storage)
    connect_to_cloud_service(cloud_service)

    credentials = AzureCredentials()
    service = AzureServiceProvider()
    storage = AzureStorage()
    cloud_service = AzureCloudService(credentials, service, storage)
    connect_to_cloud_service(cloud_service)


if __name__ == "__main__":
    main()
