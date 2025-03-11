from fastapi import APIRouter

router = APIRouter(
    prefix="/api/project",
    tags=["Project Page"]
)


@router.get("", description="Method for displaying basic Project Page information")
def open_project(some_id: str):
    return {
        "id": some_id,
        "title": "Test Project",
        "description": "Project Description",
        "company": "Some Company",
        "startDate": "2023-06-01",
        "status": "In Progress",
        "invitationLink": "https://studentprojecthub.com/invite/ai/123456",
        "avatar": "/placeholder.svg?height=200&width=200",
        "isPrivate": "False",
        "maxMembers": 5,
        "roles": [
            {
                "id": "0",
                "name": "Project Owner",
                "permissions": ["*"],
            },
            {
                "id": "1",
                "name": "Project Manager",
                "permissions": [
                    "settings",
                    "participants",
                    "links",
                    "tasks",
                ],
            },
            {
                "id": "2",
                "name": "Developer",
                "permissions": ["tasks"]},
            {id: "3", "name": "Designer", "permissions": ["links"]},
            {id: "4", "name": "Worker", "permissions": []},
            {id: "5", "name": "Just a Chill Guy", "permissions": []},
        ],
        "tags": ["Web Development", "React", "Node.js"],
    }
