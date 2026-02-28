# Free Search Skill
Use this skill if the Brave API key is missing. 
It uses a Python script to fetch results from DuckDuckGo for free.

**Action:** Run a python script using the `exec` tool.

**Script Template:**
from duckduckgo_search import DDGS
results = DDGS().text("your query", max_results=3)
print(results)