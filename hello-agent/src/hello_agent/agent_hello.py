from agents import Agent, Runner, set_default_openai_client, set_tracing_disabled, OpenAIChatCompletionsModel
from openai import AsyncOpenAI  
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Gemini API key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Use AsyncOpenAI, not OpenAI
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Configure the agent SDK
set_default_openai_client(client)
set_tracing_disabled(True)

# Define model + agent
model = OpenAIChatCompletionsModel(
    model='gemini-2.0-flash',
    openai_client=client
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=model
)

# Entry point
def My_First_Agent():
    print("Welcome to Gemini Agent! (Type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "exit":
            print("Exiting... Thank you for using Gemini Agent!")
            break

        result = Runner.run_sync(agent, user_input)
        print("Agent:", result.final_output)
        
My_First_Agent()




# from agents import agent,Runner,set_default_openai_client, set_tracing_disabled,OpenAIChatCompletionsModel
# from dotenv import load_dotenv
# from openai import OpenAI
# import os

# #Load environment variable
# load_dotenv()
# #get key from env file avaialbe in system variable
# gemini_api_key=os.getenv("GEMINI_API_KEY")

# # Configure the OpenAI client to use Google's Gemini API
# client = OpenAI(
# api_key=gemini_api_key,
# base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# set_default_openai_client(client)
# set_tracing_disabled(True) #study later what is tracing

# def My_First_Agent():

#     while True:
#         user_input = input("\nYou: ")

#         # Check if user wants to exit
#         if user_input.lower() == "exit":
#             print("Exiting... Thank you for using OpenAi SDK Agent using Gemini Model!")
#             print("M.Shahid Ali ")
#             break

#             model = OpenAIChatCompletionsModel(
#             model = 'gemini-2.0-flash',
#             openai_client = client
#         )
            
#             agent = Agent(name="Assistant", instructions="You are a helpful assistant",model=model)

#             result = Runner.run_sync(agent, user_input)
#             print(result.final_output)


        # response = client.chat.completions.create(
        #     model="models/gemini-2.0-flash",
        #     messages=[{"role": "user", "content": user_input}]
        # )

        # print("\nGemini 2.0 Flash says:", response.choices[0].message.content)
