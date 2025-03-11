import datetime
from http.client import HTTPException

from fastapi import APIRouter

router = APIRouter(
    prefix="/api/chat",
    tags=["Chat Page"]
)


@router.get("" + "s", summary="Get All Chats")
def get_all_chats():
    return [
        {
            "type": "<PROJECT_TYPE>",
            "name": "<PROJECT_NAME>",
            "id": "<PROJECT_ID>",
            "chats": [
                {
                    "name": "<CHAT_NAME>",
                    "id": "<CHAT_ID>",
                    "avatar": "<CHAT_AVATAR>",
                    "lastMessage": "<LAST_MESSAGE_IN_CHAT>",
                    "status": "<STATUS_OF_LAST_MESSAGE_IN_CHAT>",
                },
            ],
        },
        {
            "type": "<TYPE_OF_MESSAGE>",
            "name": "<USER_NAME>",
            "id": "<USER_ID>",
            "avatar": "<USER_AVATAR>",
            "lastMessage": "<LAST_MESSAGE_FROM_USER_IN_CHAT>",
            "status": "<STATUS_OF_LAST_MESSAGE_FROM_USER_IN_CHAT>",
        },
    ]


@router.get("", description="Returns chat history")
def get_chat_history(chat_id: int, project_type: str, project_id: str, section_number: int):
    return {
        "recipient": {
            "type": project_type,
            "project_id": project_id,
            "id": chat_id,
            "name": "<CHAT_NAME>",
            "avatar": "<CHAT_AVATAR>",
        },
        "messages": [
            {
                "id": "<UNIQUE_MESSAGE_ID>",
                "sender": "<USER_SENDER_NAME>",
                "sender_profile_id": "<USER_SENDER_ID>",
                "content": "<MESSAGE_TEXT>",
                "timestamp": "<TIMESTAMP>",
                "avatar": "<MESSAGE_AVATAR>",
                "image_url": "<MESSAGE_IMAGE_URL>",
                "attachment": "<ATTACHMENT_URL>",
                "status": "<MESSAGE_STATUS>",
            },
        ],
    }


@router.delete("/delete", description="")
def delete_chat(chat_id: int):
    return {"status": "deleted"}
    raise HTTPException(status_code=401, detail="Something went wrong")
    raise HTTPException(status_code=403, detail="Access Denied")
    raise HTTPException(status_code=404, detail="Not Found")


@router.post("/sendmessage", description="Sending message method")
def send_message(chat_id: int, project_type: str, project_id: str, content: str, timestamp: datetime.datetime,
                 attachment: str):
    return {"status": "sent"}
    raise HTTPException(status_code=401, detail="Something went wrong")
    raise HTTPException(status_code=403, detail="Access Denied")
    raise HTTPException(status_code=404, detail="Not Found")


@router.delete("/deletemessage", description="")
def delete_message(chat_id: int, project_type: str, project_id: str, message_id: str):
    return {
        "chat_id": chat_id,
        "type": project_type,
        "project_id": project_id,
        "id": message_id,
        "status": "deleted",
    }
    raise HTTPException(status_code=401, detail="Something went wrong")
    raise HTTPException(status_code=403, detail="Access Denied")
    raise HTTPException(status_code=404, detail="Not Found")


@router.put("/editmessage", description="method for editing the message if user is sender")
def edit_message(chat_id: int, project_id: str, message_id: str, content: str, timestamp: datetime.datetime):
    return {
        "chat_id": chat_id,
        "id": message_id,
        "type": project_id,
        "project_id": project_id,
        "content": content,
        "timestamp": timestamp,
        "status": "edited"
    }
    raise HTTPException(status_code=401, detail="Something went wrong")
    raise HTTPException(status_code=403, detail="Access Denied")
    raise HTTPException(status_code=404, detail="Not Found")
