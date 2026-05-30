import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a given city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city"
                }
            },
            "required": ["city"]
        }
    }
]

messages = [
    {"role": "user", "content": "What is the weather like in Paris right now?"}
]

print("--- TURN 1: Sending question + tool definition to Claude ---")
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    tools=tools,
    messages=messages
)

print(f"stop_reason: {response.stop_reason}")
print(f"content: {response.content}")

tool_use_block = response.content[0]
tool_name = tool_use_block.name
tool_input = tool_use_block.input
tool_use_id = tool_use_block.id

print(f"\nClaude wants to call: {tool_name}")
print(f"With input: {tool_input}")

print("\n--- Running the tool (faked result) ---")
fake_tool_result = "Sunny, 22 degrees celsius"
print(f"Tool returned: {fake_tool_result}")

messages.append({"role": "assistant", "content": response.content})
messages.append({
    "role": "user",
    "content": [
        {
            "type": "tool_result",
            "tool_use_id": tool_use_id,
            "content": fake_tool_result
        }
    ]
})

print("\n--- TURN 2: Sending tool result back to Claude ---")
response2 = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    tools=tools,
    messages=messages
)

print(f"stop_reason: {response2.stop_reason}")
print(f"\nFinal answer: {response2.content[0].text}")