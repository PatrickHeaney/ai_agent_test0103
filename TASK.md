This document outlines the specific implementation tasks for building the AI Agent, organized by iteration as defined in `PLANNING.md`.

## Iteration 1: The Core Conversation Loop

### Project Setup
- [ ] Create initial `requirements.txt` file with major versions pinned (e.g., `pydantic-ai~=1.0`).
- [ ] If missing, create or modify the `.env.example` to include `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_CHOICE`.
- [ ] Create the initial file structure (`agent.py`, `cli.py`, `tests/`).
- [ ] Create a `pytest.ini` file in the root to configure `testpaths` and `pythonpath`.

### Agent Core (`agent.py`)
- [ ] Implement the agent's `__init__` method using `pydantic-ai`.
      - **Hint:** Use `from pydantic_ai.models.openai import OpenAIChatModel` and `from pydantic_ai.providers.openai import OpenAIProvider`.
      - **Hint:** The `Agent` class constructor uses the `model=` keyword argument (e.g., `Agent(model=...)`).
- [ ] Implement an `async def chat` method that calls the agent and returns the response.
      - **Hint:** Use the `agent.run()` method, which is asynchronous.
      - **Hint:** The result of `.run()` is an object; the text response is in the `.output` attribute.
- [ ] Load LLM configuration from environment variables.

### Terminal UI (`cli.py`)
- [ ] Create the main application entry point as an `async def main` function.
- [ ] Use `asyncio.run(main())` to start the application.
- [ ] Implement a `while` loop to continuously accept user input.
- [ ] Call the agent's `chat` method and print the response.
- [ ] Add a way for the user to exit the application (e.g., typing 'exit').

### Testing (`tests/`)
- [ ] Write a unit test in `tests/test_agent.py` to verify the agent can be initialized. Use `pytest` conventions (e.g., plain `assert`).
- [ ] Write an async `pytest` unit test to check the conversation loop, mocking the `agent.run` method.

### Documentation
- [ ] Update `README.md` with basic setup and usage instructions, using `uv` for all commands.

---

## Iteration 2: Adding Memory (Future)
- [ ] ...

## Iteration 3: Adding Web Search (Future)
- [ ] ...
