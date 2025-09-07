from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import json
import os
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="templates"), name="static")

clients = {}
HISTORY_FILE = "messages.json"


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)


message_history = load_history()


@app.get("/")
async def get():
    with open("templates/chat.html", encoding="utf-8") as f:
        return HTMLResponse(f.read())



@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    if username in clients:
        await websocket.accept()
        await websocket.close(code=4001, reason="Username already taken")
        return

    await websocket.accept()
    clients[username] = websocket

    # Send chat history
    for msg in message_history:
        await websocket.send_text(json.dumps(msg))

    try:
        while True:
            data = await websocket.receive_text()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message_obj = {
                "user": username,
                "message": data,
                "timestamp": timestamp
            }

            message_history.append(message_obj)
            save_history(message_history)

            for user, client_ws in clients.items():
                await client_ws.send_text(json.dumps(message_obj))

    except WebSocketDisconnect:
        del clients[username]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True)
