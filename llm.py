import streamlit as st
import asyncio
from google import genai
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

gemini_client = genai.Client( api_key ="add api key here")
transport = StreamableHttpTransport(url="http://127.0.0.1:8000/mcp")
mcp_client = Client(transport)

st.title("Smart Registration Chat")

# User prompt input
user_input = st.text_input("Ask me something (e.g. 'Register Harsh with harsh@gmail.com')")

if st.button("Submit") and user_input:
    async def process_input():
        async with mcp_client:
            prompt = f"""Your job is to choose and call the appropriate tool from the available tools below to fulfill the user's request.
                        Respond ONLY by calling the tool, DO NOT answer directly.You can only call the `store_data` tool one time per request.",
                        "If the user is already registered, do not call the tool again.",
                        User Input:{user_input}"""
            response = await gemini_client.aio.models.generate_content(
                model="models/gemini-1.5-flash",
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=0.2,
                    tools=[mcp_client.session],
                )
            )
            return response

    llm_response = asyncio.run(process_input())

    st.subheader("LLM Output (Tool call):")
    st.code("Registered data")
