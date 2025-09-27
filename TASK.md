This document outlines the specific implementation tasks for building the AI Agent, organized by iteration as defined in `PLANNING.md`.

## Iteration 1: The Core Conversation Loop

### Project Setup
- [ ] Create initial `requirements.txt` file
      e.g. example_code/ai-agent-mastery/4_Pydantic_AI_Agent/requirements.txt
- [ ] If missing, create or modify the `.env.example` to include `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_CHOICE`.  If file and these terms are present, move on to next the next step.
      e.g. example_code/ai-agent-mastery/4_Pydantic_AI_Agent/.env.example
- [ ] Create the initial file structure (`agent.py`, `cli.py`, `tests/`).

### Agent Core (`agent.py`)
- [ ] Implement the agent using `pydantic-ai` with an `async def chat` method.
- [ ] The implementation must use the `Agent` and `OpenAIChatModel` classes.
- [ ] Load LLM configuration from environment variables.

### Terminal UI (`cli.py`)
- [ ] Create the main application entry point as an `async def main` function.
- [ ] Use `asyncio.run(main())` to start the application.
- [ ] Implement a `while` loop to continuously accept user input.
- [ ] Call the agent with the user's input and print the response.
- [ ] Add a way for the user to exit the application (e.g., typing 'exit').

### Testing (`tests/`)
- [ ] Create a `pytest.ini` file in the root to configure `testpaths` and `pythonpath`.
- [ ] Write a unit test to verify the agent can be initialized.
- [ ] Write an async unit test to check the conversation loop (mocking the LLM call).

### Documentation
- [ ] Update `README.md` with basic setup and usage instructions for running the terminal UI.

---

## Iteration 2: Adding Web Search (Future)
- [ ] ...

## Iteration 3: Adding Memory (Future)
- [ ] ...
