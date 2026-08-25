In this exercise, you'll work with composition and abstraction. The goal of the exercise is to improve code that is used by a famous YouTuber to manage backing up his video files.

The code below is part of a script that this famous YouTuber uses to search through video backups, which are stored in a bucket (= file storage location) in the cloud:

```python
class ACCloud(CloudProvider):
  def __init__(self, bucket_name: str, region: str) -> None:
    authentication = GoogleAuth("service_key.json")
    super().__init__(
      region=region,
      http_auth=authentication,
      secure=True,
    )
    self.bucket_name = bucket_name

  def find_files(
    self,
    query: str,
    max_result: int
  ) -> list[str]:
    response = self.filter_by_query(
      bucket=self.bucket_name,
      query=query,
      max=max_result
    )
    return response["result"]["data"][0]

class VideoStorage(ACCloud):
  def __init__(self) -> None:
    super().__init__(
      bucket_name="video-backup.arjancodes.com",
      region="eu-west-1c",
    )
```

The main (fake) dependency is the cloudengine package which contains the CloudProvider abstract base class.

The classes in this example are nested, in other words multiple levels of inheritance. VideoStorage. inherits from ACCloud which in turn inherits CloudProvider.

The problem with these layers of inheritance is that the code becomes hard to read.

a) Refactor this code so that it no longer uses inheritance, but relies on composition instead.

b) Refactor the code once more so that find_files is no longer dependent on the cloudengine package.

Compatible Python Versions: 3.9+