run-api:
	PYTHONPATH=src poetry run uvicorn recall_ai.api.server:create_app --factory --reload

run-bot:
	PYTHONPATH=src poetry run python src/recall_ai/run_bot.py