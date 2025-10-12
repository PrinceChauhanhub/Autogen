## The state of the team is unstable and the progress is hold up until the user provides a feedback or say error out. 
# Because of this blocking approach, it is not recommended that ,we use it only for short interactions


## whenever chatgpt ask for which response u prefer....it means there is human in the loop concept there... 
## most common is where we ask user for are u denied or approve


# case 1 -  the below code is when ask user during the run.

import asyncio
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.ui import Console

model_client = OllamaChatCompletionClient(model="gemma2:latest")


assistant = AssistantAgent(
    name = "Assistant",
    model_client=model_client,
    system_message="You are a helpful Assistant"
)

user_proxy_agent = UserProxyAgent(
    name = "UserProxy",
    description="A proxy agent that represents the user.",
    input_func=input   
)

termination_condition = TextMentionTermination("APPROVE")

## Creating team with the assistant and user proxy agent

team = RoundRobinGroupChat(
    participants=[assistant, user_proxy_agent],
    termination_condition=termination_condition
)

stream = team.run_stream(task = "Write a 4 line poem about the ocean")

async def main():
    await Console(stream)
    
if __name__ == "__main__":
    asyncio.run(main())