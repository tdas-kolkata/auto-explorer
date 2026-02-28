---
name: "find_share_price"
description: "Briefly explain what this skill does so the LLM knows when to use it"
metadata:
  priority: "high"
  always_include: false
---
# Price Finding Skill
Use this skill to get the current share price. You must use the `web_search` tool to find this information.

**Triggers:** 
- "what is the price of [entity] today"
- "find the share price [entity]"

**Instructions:**
1. Identify the entity name.
2. Use the `web_search` tool with the query "current share price [entity]".
3. If the Brave API key is missing use this `free_search` tool . It uses a Python script to fetch results from DuckDuckGo for free.