from openai import OpenAI
import os
import asyncio  # Import asyncio library
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("openAiKey")
print(key)

client = OpenAI(
    api_key=key,
)

async def callApi(data):
    chat_completion =  client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": data,  # Use the passed data in the content
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

# Define an async main function to call your async API function
async def main():
    val = await callApi("what is 3 + 3")
    print(val)  # Print the entire response object

# Use asyncio.run() to run the main function
if __name__ == "__main__":
    asyncio.run(main())
