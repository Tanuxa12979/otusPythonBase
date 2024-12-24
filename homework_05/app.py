from fastapi import FastAPI
import uvicorn
from homework_05.view import event_router
from homework_05.view.views import router as template_router

app = FastAPI()
app.include_router(template_router)
app.include_router(event_router, prefix='/api')


if __name__=="__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000)



