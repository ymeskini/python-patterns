from dataclasses import dataclass
from logging import Logger
from typing import Optional
import jwt

logger = Logger(__name__)


@dataclass
class User:
    username: str
    email: Optional[str] = None


@dataclass
class TokenData:
    username: str | None


# Define the credentials exception
class CredentialsException(Exception):
    pass


def get_current_user(token: str) -> User:
    token_data = get_token_data(token)

    if token_data.username is None:
        raise CredentialsException("Token does not contain a username")

    return User(username=token_data.username)


def get_token_data(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])  # type: ignore

        if payload is None:
            raise CredentialsException("Invalid token data")

        return TokenData(username=payload.get("sub"))
    except jwt.ExpiredSignatureError as e:
        logger.info(msg=f"Token expired, {e}")
        raise CredentialsException("Token expired")
    except jwt.InvalidTokenError:
        logger.info(msg="Invalid token")
        raise CredentialsException("Invalid token")


def main() -> None:
    token = ""

    try:
        user = get_current_user(token)
        print(f"User: {user}")
    except CredentialsException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
