from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse

api_router = APIRouter()

@api_router.get("/ping/")
async def test_view():
    return JSONResponse({"message": "pong"}, 200)

