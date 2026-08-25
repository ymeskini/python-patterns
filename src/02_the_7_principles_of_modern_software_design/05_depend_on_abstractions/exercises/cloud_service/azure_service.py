class AzureCredentials:
    def fetch_credentials(self) -> str:
        return "AZURE_SECRET_KEY_12345"


class AzureServiceProvider:
    def authenticate(self, credentials: str) -> None:
        print("Connecting to Azure Cloud.")

    def get_context(self) -> str:
        return "azure_project_context"


class AzureStorage:
    def setup(self, context: str) -> None:
        print(f"Initializing Azure storage with context {context}.")
