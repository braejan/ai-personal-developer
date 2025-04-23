from app.core.mcp.time.client import get_mcp_client
from app.core.langgraph.agents.supervisor import create_workflow
from typing import List
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import BaseMessage


class ChatCLI:
    def __init__(self):
        self.chat_history: List[BaseMessage] = []

        # Initialize LangGraph workflow
        self.checkpointer = InMemorySaver()
        self.config = {"configurable": {"thread_id": "1"}}

    async def main(self):
        checkpointer = InMemorySaver()
        
        async with get_mcp_client() as mcp_time_client:
            workflow = await create_workflow(mcp_time_client)
            app = workflow.compile(checkpointer)
            config = {"configurable": {"thread_id": "1"}}

            # Main interaction loop
            while True:
                user_input = input("\nEnter your query (or 'exit' to quit): ")

                if user_input.lower() == "exit":
                    print("Goodbye!")
                    break

                # Use streaming to get real-time updates
                async for output in app.astream(
                    {"messages": [{"role": "user", "content": user_input}]},
                    config=config,
                    stream_mode=[
                        "messages",
                    ],  # Stream both messages and state updates
                ):
                    if isinstance(output, tuple):
                        mode, data = output
                        if mode == "messages":
                            # Print messages as they come in
                            for message in data:
                                if hasattr(message, "content"):
                                    print(message.content, end="", flush=True)
                            if not data:
                                print()
                        elif mode == "updates":
                            # You can handle state updates here if needed
                            pass
                    else:
                        # Handle other types of output if needed
                        pass


import asyncio

if __name__ == "__main__":
    chat = ChatCLI()
    asyncio.run(chat.main())
