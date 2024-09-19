Consider the following function that sends an email:

```python
def send_email(
    message: str, to_address: str, from_address: str = DEFAULT_EMAIL
) -> None:
    server = SMTP()
    server.connect(HOST, PORT)
    server.login(LOGIN, PASSWORD)
    server.sendmail(from_address, to_address, message)
    server.quit()
```

What external package does this function depend on? Refactor the code and remove the dependency.

Compatible Python Versions: 3.8+
