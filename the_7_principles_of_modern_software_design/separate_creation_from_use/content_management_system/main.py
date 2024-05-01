from dataclasses import dataclass


class UserAuthService:
    def authenticate_user(self, _username: str, _password: str):
        # Authentication logic
        return "User Authenticated"


class DatabaseAccess:
    def get_content(self, content_id: str):
        # Logic to retrieve content from the database
        return f"Content for {content_id}"


@dataclass
class ContentRenderer:
    user_auth_service: UserAuthService
    database_access: DatabaseAccess

    def render_page(self, username: str, password: str, content_id: str):
        # Use UserAuthService to authenticate
        if self.user_auth_service.authenticate_user(username, password):
            # If authenticated, use DatabaseAccess to fetch content
            content = self.database_access.get_content(content_id)
            print(f"Rendering: {content}")
        else:
            print("Authentication Failed")


def main() -> None:
    user_auth_service = UserAuthService()
    database_access = DatabaseAccess()

    content_renderer = ContentRenderer(user_auth_service, database_access)

    # Example use
    content_renderer.render_page("admin", "admin123", "101")


if __name__ == "__main__":
    main()
