# case 2 - feedback for the next run

## Providing feeback to the next run: Using Max Turns
# pause the team for the user input/feedback


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



## Three agents for story telling

narrator = AssistantAgent(
    name = "narrator",
    model_client=model_client,
)

hero = AssistantAgent(
    name = "Hero",
    model_client=model_client,
)

guide = AssistantAgent(
    name = "Guide",
    model_client=model_client
)


### Team with mac turns 

team = RoundRobinGroupChat(
    participants=[narrator,hero,guide],
    max_turns=1
)

async def main():
    task = "Write a 3 part story about a mysterious forest in less than 30 words."
    while True:
        stream = team.run_stream(task=task)
        await Console(stream)
        
        # here we take the feedback from the user
        feedback = input("Please provide your feedback (type 'exit' to stop): ")
        
        if feedback.lower().strip() == 'exit':
            break
        task = feedback


if __name__=="__main__":
    asyncio.run(main())