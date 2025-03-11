from fastapi import APIRouter

router = APIRouter(
    prefix="/api/projects",
    tags=["Dashbord Page"]
)


@router.get("", summary="Get Projects")
def get_projects():
    return [{
        "id": "<PROJECT_ID>",
        "title": "<PROJECT_TITLE>",
        "company": "<PROJECT_COMPANY>",
        "category": "<PROJECT_CATEGORY>",
        "tags": "<PROJECT_TAGS>",
        "description": "<PROJECT_DESCRIPTION>"
    }, ]
