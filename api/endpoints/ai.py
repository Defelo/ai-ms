from fastapi import APIRouter, Depends
from pydantic import BaseModel
from api.services.ai_handler import AIHandler
from fastapi import APIRouter, HTTPException, status
from api.auth import admin_auth
from api.exceptions.auth import admin_responses

router = APIRouter()


class AIRequest(BaseModel):
    system_prompt: str
    user_prompt: str


class AIResponse(BaseModel):
    output: str


ai_handler = AIHandler()


@router.post("/ai", response_model=AIResponse, dependencies=[admin_auth], responses=admin_responses(AIResponse))
async def ai_endpoint(request: AIRequest) -> AIResponse:
    """
    Post a message and get a response from the AI.

    *Requirements:* **ADMIN**
    """
    try:
        output = ai_handler.get_ai_response(request.system_prompt, request.user_prompt)
        return AIResponse(output=output)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
