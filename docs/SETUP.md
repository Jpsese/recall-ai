## Features

- 🤖 **Discord Bot** - Interactive bot with command support
- 🧠 **AI Memory** - Store and recall information using embeddings
- 🚀 **FastAPI Backend** - RESTful API for data ingestion
- 📝 **Sentence Transformers** - State-of-the-art text embeddings

## Prerequisites

- Python 3.12 or higher (< 3.14)
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management
- A Discord Bot Token ([How to create a Discord bot](https://discord.com/developers/applications))

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/recall-ai.git
cd recall-ai
```

### 2. Install Poetry (if not already installed)

```bash
# macOS / Linux
curl -sSL https://install.python-poetry.org | python3 -

# Or with Homebrew (macOS)
brew install poetry
```

### 3. Install dependencies

```bash
poetry install
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Then edit `.env` with your credentials:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```

### 5. Activate the virtual environment

```bash
poetry shell
```

## Usage

### Running the Discord Bot

```bash
make run-bot
```

Or manually:

```bash
PYTHONPATH=src poetry run python src/recall_ai/run_bot.py
```

### Running the API Server

```bash
make run-api
```

Or manually:

```bash
PYTHONPATH=src poetry run uvicorn recall_ai.api.server:create_app --factory --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/ingest` | POST | Ingest text for processing |

## Bot Commands

| Command | Description |
|---------|-------------|
| `!ping` | Check if the bot is working |
| `!status` | Show bot uptime |
| `!save` | Save a memory |

## Development

### Running Tests

```bash
PYTHONPATH=src poetry run pytest tests/ -v
```

### Code Formatting

```bash
poetry run black src/ tests/
```

### Project Structure

```
recall-ai/
├── src/
│   └── recall_ai/
│       ├── ai/
│       │   ├── embeddings/      # Embedding service
│       │   ├── memory/          # Memory storage
│       │   └── vectorstore.py   # Vector operations
│       ├── api/
│       │   └── server.py        # FastAPI application
│       ├── bot/
│       │   ├── client.py        # Discord bot client
│       │   └── commands/        # Bot commands
│       ├── logging_config.py
│       └── run_bot.py           # Bot entry point
├── tests/
├── pyproject.toml
├── Makefile
└── README.md
```

## VSCode Setup

This project includes VSCode configuration files in `.vscode/`:

- **settings.json** - Python interpreter, formatting, and editor settings
- **launch.json** - Debug configurations for API and bot
- **extensions.json** - Recommended extensions

### Recommended Extensions

- Python (ms-python.python)
- Black Formatter (ms-python.black-formatter)
- Ruff (charliermarsh.ruff)
- Even Better TOML (tamasfe.even-better-toml)
