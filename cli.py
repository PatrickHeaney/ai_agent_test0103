import asyncio
from agent import ConversationalAgent

async def main():
    """
    Main function to run the command-line interface for the agent.
    """
    print("Starting agent... Type 'exit' to end the conversation.")
    agent = ConversationalAgent()

    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            break
        response = await agent.chat(user_input)
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
