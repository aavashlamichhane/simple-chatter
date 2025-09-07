# Simple Chatter

A minimal, real-time chat room web application built with FastAPI and WebSockets. Perfect for hackathons, small teams, or friends. The frontend uses Tailwind CSS for a modern look and supports dark mode and fullscreen chat.

## Features

- Real-time messaging using WebSockets
- Persistent chat history (saved in `messages.json`)
- Unique username enforcement
- Responsive, modern UI with dark mode and fullscreen toggle
- Copy-to-clipboard for messages

## Getting Started

### Prerequisites

- Python 3.11+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone the repository:
	```sh
	git clone <repo-url>
	cd simple-chatter
	```

2. Install dependencies:
	```sh
	pip install -r requirements.txt
	```

### Running the Server

```sh
python main.py
```
Or with Uvicorn:
```sh
uvicorn main:app --host 0.0.0.0 --port 8010 --reload
```

### Accessing the Chat

Open your browser and go to [http://localhost:8010](http://localhost:8010). Enter a unique username to join the chat.

## Deployment

You can use tools like [cloudflared](https://github.com/cloudflare/cloudflared) to expose your local server to the internet for hackathons or remote collaboration.

## File Structure

- `main.py` — FastAPI backend and WebSocket logic
- `templates/chat.html` — Frontend UI
- `messages.json` — Chat history storage
- `requirements.txt` — Python dependencies

## License

MIT