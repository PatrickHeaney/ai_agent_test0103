import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

load_dotenv()


class ConversationalAgent:
    """
    A simple conversational agent that uses Pydantic AI.
    """

    def __init__(self):
        """
        Initializes the agent with an OpenAI chat model.
        """
        llm_provider = OpenAIProvider(
            api_key=os.getenv("LLM_API_KEY"),
            base_url=os.getenv("LLM_BASE_URL"),
        )
        self.agent = Agent(
            model=OpenAIChatModel(
                model_name=os.getenv("LLM_CHOICE"),
                provider=llm_provider,
            ),
        )

    async def chat(self, message: str) -> str:
        """
        Sends a message to the agent and returns the response.

        Args:
            message (str): The user's message.

        Returns:
            str: The agent's response.
        """
        response = await self.agent.run(message)
        return response.output
