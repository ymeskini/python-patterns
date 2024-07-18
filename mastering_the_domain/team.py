from dataclasses import dataclass, field


# Entity: Represents a person who can be part of teams and projects
@dataclass
class Member:
    member_id: int
    name: str
    email: str


@dataclass
class ProjectMember:
    member_id: int
    role: str


@dataclass
class TeamMember:
    member_id: int


# Aggregate Root: Manages members and behaviors related to a project
@dataclass
class Project:
    project_id: int
    name: str
    members: list[ProjectMember] = field(default_factory=list)

    def add_member(self, member: Member, role: str) -> None:
        project_member = ProjectMember(member.member_id, role)
        self.members.append(project_member)

    def remove_member(self, member_id: int) -> None:
        self.members = [m for m in self.members if m.member_id != member_id]


@dataclass
class Team:
    team_id: int
    name: str
    members: list[TeamMember] = field(default_factory=list)
    projects: list[Project] = field(default_factory=list)

    def add_member(self, member: Member) -> None:
        team_member = TeamMember(member.member_id)
        self.members.append(team_member)

    def remove_member(self, member_id: int) -> None:
        self.members = [m for m in self.members if m.member_id != member_id]

    def add_project(self, project: Project) -> None:
        self.projects.append(project)

    def remove_project(self, project_id: int) -> None:
        self.projects = [p for p in self.projects if p.project_id != project_id]


def main() -> None:
    # Create some members
    alice = Member(1, "Alice", "alice@example.com")
    bob = Member(2, "Bob", "bob@example.com")

    # Create a team and add members
    team = Team(1, "Development Team")
    team.add_member(alice)
    team.add_member(bob)

    # Create a project and add members to the project
    project = Project(1, "New Website")
    project.add_member(alice, "Developer")
    project.add_member(bob, "Designer")

    # Add the project to the team
    team.add_project(project)

    # Display team and project information
    print(f"Team: {team.name}")
    for member in team.members:
        print(f"Team Member ID: {member.member_id}")

    print(f"Project: {project.name}")
    for member in project.members:
        print(f"Project Member ID: {member.member_id}, Role: {member.role}")


# Example Usage
if __name__ == "__main__":
    main()
