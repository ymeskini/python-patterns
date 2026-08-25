from enum import IntEnum, auto, StrEnum

class HTTPStatus(IntEnum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501


class RESTMethod(StrEnum):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()


for status in HTTPStatus:
    print(f"{status.name}: {status.value}")


print(f"Name of the enum member: {HTTPStatus.OK.name}")

print(f"Enum member from value: {HTTPStatus(404).name}")

print(f"value of the enum member: {HTTPStatus.NOT_FOUND.value}")


def response_description(status: HTTPStatus) -> str:
    if status == HTTPStatus.OK:
        return "Request succeeded"
    elif status == HTTPStatus.NOT_FOUND:
        return "Resource not found"
    else:
        return "Error occurred"


def main() -> None:
    description = response_description(HTTPStatus.OK)
    print(description)

    if 400 <= HTTPStatus.BAD_REQUEST < 500:
        print("HTTPStatus.BAD_REQUEST is an error response.")

    if HTTPStatus.INTERNAL_SERVER_ERROR in HTTPStatus:
        print("500 Internal Server Error is a valid HTTP status code.")


if __name__ == "__main__":
    main()
