Suppose you have the following classes, which serves as a helper for managing access to a Google Cloud environment:

```python
from google_service import GoogleCredentials, GoogleServiceProvider, GoogleStorage
from azure_service import AzureCredentials, AzureServiceProvider, AzureStorage


@dataclass
class CloudService:
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
```

The connect_to_cloud_service function needs to handle the different cloud services that can be passed to it. The problem is that each service implements and behaves slightly differently. This issue arises because each class is directly coupled with the imported packages. To remove this direct coupling and improve the logic of connect_to_cloud_service to use a unified interface, you cannot change the imported classes from azure_service and google_service.

How do you solve this?

Compatible Python Versions: 3.8+