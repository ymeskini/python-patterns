from abc import ABC

from google_service import (
    GoogleCredentials,
    GoogleServiceProvider,
    GoogleStorage,
)

from azure_service import (
    AzureCredentials,
    AzureServiceProvider,
    AzureStorage,
)


class CloudAdapter(ABC):
    def retrieve_credentials(self) -> str:
        raise NotImplementedError

    def connect(self, credentials: str) -> None:
        raise NotImplementedError

    def get_context(self) -> str:
        raise NotImplementedError

    def initialize_storage(self, context: str) -> None:
        raise NotImplementedError


# Google-specific Cloud Adapter implementation
class GoogleCloudAdapter(CloudAdapter):
    def __init__(
        self,
        google_credentials: GoogleCredentials,
        google_service_provider: GoogleServiceProvider,
        google_storage: GoogleStorage,
    ):
        self.google_credentials = google_credentials
        self.google_service_provider = google_service_provider
        self.google_storage = google_storage

    def retrieve_credentials(self) -> str:
        print("Retrieving credentials from Google.")
        return self.google_credentials.get_credentials()

    def connect(self, credentials: str) -> None:
        print("Connecting to Google service.")
        self.google_service_provider.authenticate(credentials)

    def get_context(self) -> str:
        print("Getting context from Google service.")
        return self.google_service_provider.get_context()

    def initialize_storage(self, context: str) -> None:
        print("Initializing Google storage with context.")
        self.google_storage.initialize(context)


class AzureCloudAdapter(CloudAdapter):
    def __init__(
        self,
        azure_credentials: AzureCredentials,
        azure_service_provider: AzureServiceProvider,
        azure_storage: AzureStorage,
    ):
        self.azure_credentials = azure_credentials
        self.azure_service_provider = azure_service_provider
        self.azure_storage = azure_storage

    def retrieve_credentials(self) -> str:
        print("Retrieving credentials from Azure.")
        return self.azure_credentials.fetch_credentials()

    def connect(self, credentials: str) -> None:
        print("Connecting to Azure service.")
        self.azure_service_provider.authenticate(credentials)

    def get_context(self) -> str:
        print("Getting context from Azure service.")
        return self.azure_service_provider.get_context()

    def initialize_storage(self, context: str) -> None:
        print("Initializing Azure storage with context.")
        self.azure_storage.setup(context)


# Unified Cloud Service class


# The adapter pattern needs to adhere to the CloudAdapter interface
def connect(adapter: CloudAdapter) -> None:
    print("Connecting to the cloud service.")
    credentials = adapter.retrieve_credentials()
    adapter.connect(credentials)
    context = adapter.get_context()
    adapter.initialize_storage(context)
    print("Cloud service connected.")


# Main function
def main() -> None:
    # Using the Google Cloud Adapter
    google_credentials = GoogleCredentials()
    google_service_provider = GoogleServiceProvider()
    google_storage = GoogleStorage()

    google_adapter = GoogleCloudAdapter(
        google_credentials=google_credentials,
        google_service_provider=google_service_provider,
        google_storage=google_storage,
    )

    connect(google_adapter)

    # Using the Azure Cloud Adapter
    azure_credentials = AzureCredentials()
    azure_service_provider = AzureServiceProvider()
    azure_storage = AzureStorage()

    azure_adapter = AzureCloudAdapter(
        azure_credentials=azure_credentials,
        azure_service_provider=azure_service_provider,
        azure_storage=azure_storage,
    )

    connect(azure_adapter)


if __name__ == "__main__":
    main()
