from fastapi import APIRouter

router = APIRouter(
    prefix="/api/user",
    tags=["Header"]
)


@router.get("",
            summary="Get User",
            description="Get User")
def get_user():
    return {
        "id": "<USER_ID>",
        "name": "<USER_NAME>",
        "avatar": "<USER_AVATAR>"
    }


@router.get("/{user_id}",
            summary="Get Unique User",
            description="Just a basic information fot the header user button")
def get_unigue_user(user_id: int):
    return {
        "id": user_id,
        "name": "<NAME>",
        "avatar": "<USER_AVATAR>"
    }
    raise HTTPException(status_code=404, detail="User not found")
