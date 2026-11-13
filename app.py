import os
import requests
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, function_tool, set_tracing_disabled , OpenAIChatCompletionsModel 
from openai.types.responses import function_tool



load_dotenv(override=True)
set_tracing_disabled(True)

openrouter_key = os.getenv("OPENROUTER_API_KEY")
openrouter_url = os.getenv("OPENROUTER_URL")


client = AsyncOpenAI(base_url=openrouter_url, api_key=openrouter_key)

model = OpenAIChatCompletionsModel(model="gpt-5.4-mini",openai_client=client)


agent = Agent("sample agent",model=model)


async def main():
    result = await Runner.run(agent,"say hello")
    print(result.final_output)


asyncio.run(main())