from fastmcp import Client
import asyncio
from google import genai
from fastmcp.client.transports import StreamableHttpTransport
from google.genai.types import Tool as GenaiTool
from google.genai.types import FunctionDeclaration, Schema

# Convert MCP tool to Gemini tool format
def convert_tool(tool):
    # Get safe schema fields
    input_schema = tool.inputSchema or {}

    return GenaiTool(
        function_declarations=[
            FunctionDeclaration(
                name=tool.name,
                description=tool.description,
                parameters=Schema(
                    type=input_schema.get("type", "object"),
                    properties=input_schema.get("properties", {}),
                    required=input_schema.get("required", []),
                    # DO NOT include "additionalProperties"
                )
            )
        ]
    )


# MCP and Gemini setup
transport = StreamableHttpTransport(url="http://127.0.0.1:8000/mcp")
mcp_client = Client(transport)
gemini_client = genai.Client(api_key="AIzaSyBfe4M4mc0AsTXEhAyoJrnaSrG2HUo1jcc")

# Async main
async def main():
    async with mcp_client:
        tools = await mcp_client.list_tools()
        genai_tools = [convert_tool(tool) for tool in tools]

        response = await gemini_client.aio.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents="Register user Sachin with email sachin@gmail.com and DOB 2002-01-01.",
            config=genai.types.GenerateContentConfig(
                tools=genai_tools,
                temperature=0
            )
        )
        print("\nGemini response:")
        print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
