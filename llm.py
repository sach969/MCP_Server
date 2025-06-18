from fastmcp import Client
import asyncio
from google import genai
from fastmcp.client.transports import StreamableHttpTransport

transport = StreamableHttpTransport(url="http://127.0.0.1:8000/mcp")
mcp_client = Client(transport)

gemini_client = genai.Client( api_key ="")

# Async main
async def main():
    async with mcp_client:
        print(await mcp_client.list_tools())
        response = await gemini_client.aio.models.generate_content(
            model = "gemini-1.5-flash",
            contents=("Call the tool using this JSON format:\n"
    "{\n"
    "  \"data\": {\n"
    "    \"name\": \"harsh\",\n"
    "    \"email\": \"@gmail.com\",\n"
    "    \"dob\": \"2002-01-01\"\n"
    "  }\n"
    "}\n"
    "Do not respond directly. Only call the tool with this exact format."
)
,
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[mcp_client.session],
            )
        )
        print("\nGemini response:")
        print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
 


