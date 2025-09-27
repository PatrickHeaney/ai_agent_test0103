import pytest
from unittest.mock import AsyncMock, patch
from agent import ConversationalAgent


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent can be initialized."""
    with patch("os.getenv") as mock_getenv:
        mock_getenv.return_value = "test_value"
        agent = ConversationalAgent()
        assert agent is not None
        assert agent.agent is not None


@pytest.mark.asyncio
async def test_chat_loop():
    """Test the conversation loop of the agent."""
    with patch("os.getenv") as mock_getenv:
        mock_getenv.return_value = "test_value"
        agent = ConversationalAgent()

        # Mock the agent's run method
        result_mock = AsyncMock()
        result_mock.output = "Test response"
        agent.agent.run = AsyncMock(return_value=result_mock)

        response = await agent.chat("Hello")
        assert response == "Test response"
        agent.agent.run.assert_called_once_with("Hello")
