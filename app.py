import os
import requests
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, function_tool, set_tracing_disabled , OpenAIChatCompletionsModel, WebSearchTool
from agents.model_settings import ModelSettings 
from pydantic import BaseModel, Field
from typing import Dict
from IPython.display import Markdown, display
from messenger import send_email, push



load_dotenv(override=True)
set_tracing_disabled(True)

openrouter_key = os.getenv("OPENROUTER_API_KEY")
openrouter_url = os.getenv("OPENROUTER_URL")
USE_EMAIL = True
HOW_MANY_SEARCHES = 5


client = AsyncOpenAI(base_url=openrouter_url, api_key=openrouter_key)

model = OpenAIChatCompletionsModel(model="gpt-5.4-mini",openai_client=client)



Instruction = """
    You are a research assistant , Given a search term, you search the web for that term and 
    produce a concise summary of the results.Summary must be 2-3 paragraph and maximum 300 words.
    Capture the main point and be succint. reply only with the summary.
"""

task = "Most popular ai agent in 2026"

settings = ModelSettings(tool_choice="required")
tools = [WebSearchTool()]

search_agent = Agent("Websearch_agent",instructions=Instruction,tools=tools,model=model, model_settings=settings)


async def main():
    result = await Runner.run(search_agent,task)
    print(result.final_output)


asyncio.run(main())