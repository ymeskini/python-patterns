from dataclasses import dataclass

from google_service import GoogleCredentials, GoogleServiceProvider, GoogleStorage
from azure_service import AzureCredentials, AzureServiceProvider, AzureStorage


@dataclass
class GoogleCloudService:
    auth_provider: GoogleCredentials
    service: GoogleServiceProvider
    storage_manager: GoogleStorage


@dataclass
class AzureCloudService:
    auth_provider: AzureCredentials
    service: AzureServiceProvider
    storage_manager: AzureStorage


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
    google_credentials = GoogleCredentials()
    google_service = GoogleServiceProvider()
    google_storage = GoogleStorage()
    google_cloud_service = GoogleCloudService(
        google_credentials, google_service, google_storage
    )
    connect_to_cloud_service(google_cloud_service)

    azure_credentials = AzureCredentials()
    azure_service = AzureServiceProvider()
    azure_storage = AzureStorage()
    azure_cloud_service = AzureCloudService(
        azure_credentials, azure_service, azure_storage
    )
    connect_to_cloud_service(azure_cloud_service)


if __name__ == "__main__":
    main()
