import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio
from uvicorn import run
from dotenv import load_dotenv
from .sculptor import Sculptor

load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Nexum DAO Core", version="0.1.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Socket.IO server
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
socket_app = socketio.ASGIApp(sio, app)

# Initialize Sculptor
sculptor = Sculptor()

@app.get("/")
async def root():
    return {"message": "Nexum DAO Core is running"}

@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")
    # Send current state to new client
    current_state = await sculptor.get_current_state()
    await sio.emit('state_update', current_state, to=sid)

@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

@sio.event
async def propose_change(sid, data):
    """
    Handle incoming change proposals from users.
    data format: {"user_id": str, "message": str}
    """
    print(f"Received proposal from {sid}: {data}")
    user_id = data.get("user_id", "anonymous")
    message = data.get("message", "")

    try:
        # Process the input using the Sculptor
        result = await sculptor.process_input(user_id, message)
        
        # Broadcast the updated state and contribution info
        await sio.emit('state_update', result['new_state'])
        await sio.emit('contribution_update', result['contribution_delta'])
        
    except Exception as e:
        print(f"Error processing input: {e}")
        await sio.emit('error', {"message": str(e)}, to=sid)

if __name__ == "__main__":
    run("core.main:socket_app", host="0.0.0.0", port=8000, reload=True)
