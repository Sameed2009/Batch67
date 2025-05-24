import chainlit as cl
import json
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)
from my_secrets import Secrets
from typing import cast

secrets = Secrets()

@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Welcome to the Gemini Chatbot!").send()

    external_client = AsyncOpenAI(
        api_key=secrets.gemini_api_key,
        base_url=secrets.gemini_api_url
    )

    set_tracing_disabled(True)

    agent = Agent(
        name="Gemini Chatbot",
        instructions="You are a helpful assistant powered by Google's Gemini model.",
        model=OpenAIChatCompletionsModel(
            openai_client=external_client,
            model=secrets.gemini_api_model,
        ),
    )

    cl.user_session.set("agent", agent)
    cl.user_session.set("chat_history", [])

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    agent = cast(Agent, cl.user_session.get("agent"))
    chat_history: list = cl.user_session.get("chat_history") or []

    chat_history.append({"role": "user", "content": message.content})

    try:
        result = Runner.run_sync(starting_agent=agent, input=chat_history)
        msg.content = result.final_output
        cl.user_session.set("chat_history", result.to_input_list())
        await msg.update()
    except Exception as e:
        msg.content = f"❌ Error: {str(e)}"
        await msg.update()

@cl.on_chat_end
def end():
    chat_history: list = cl.user_session.get("chat_history") or []
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(chat_history, f, indent=4)
