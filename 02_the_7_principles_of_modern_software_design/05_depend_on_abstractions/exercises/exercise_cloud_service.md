Suppose you have the following class that is a helkper class for managing access to a Google Cloud environment:

```python
@dataclass
class CloudService:
    auth_provider: GoogleCredentials
    service: GoogleServiceProvider
    storage_manager: GoogleStorage

    def connect(self) -> None:
        print("Connecting to the cloud service.")
        credentials = self.auth_provider.retrieve_credentials()
        self.service.connect(credentials)
        context = self.service.get_context()
        self.storage_manager.initialize(context)
        print("Cloud service connected.")
```

As you can see, the class directly depends on Google-specific classes: `GoogleCredentials`, `GoogleService`, and `GoogleStorage`. You want to remove this direct dependency. However, you can't change the original classes provided by Google. In fact, you don't even have access to the source code of those classes. How do you solve this? Refactor your code to remove the direct dependency.