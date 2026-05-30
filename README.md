# Web Search Agent

An AI agent that answers questions using real-time web search.
Built with Claude claude-sonnet-4-6 + Tavily Search + FastAPI.

## How it works

1. User sends a question via HTTP POST
2. Claude decides to call the web_search tool
3. Tavily searches the web and returns results
4. Claude reads the results and returns a grounded answer

## Run locally

pip install anthropic tavily-python fastapi uvicorn

export ANTHROPIC_API_KEY=your-key
export TAVILY_API_KEY=your-key

python3 03_search_agent.py

## Ask a question

curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the latest news about OpenAI?"}'