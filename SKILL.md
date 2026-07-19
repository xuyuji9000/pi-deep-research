---
name: pi-deep-research
description: Conducts comprehensive, multi-step web research. Uses a Python tool to search the web, scrape page contents, iterate on missing knowledge, and synthesize detailed, cited reports.
---

# Deep Research Skill

This skill allows you (the agent) to emulate a "Deep Research" workflow by autonomously searching the web, reading full pages, identifying knowledge gaps, and writing comprehensive, cited reports.

## Setup

The dependencies have already been installed in a local virtual environment (`venv`).

## Tools

You have access to a Python script that provides search and read capabilities. Execute it using the virtual environment's Python binary.

### 1. Search the Web
```bash
.pi/agent/skills/pi-deep-research/venv/bin/python .pi/agent/skills/pi-deep-research/scripts/research.py search "your search query"
```
Returns a list of search results with Titles, URLs, and Snippets.

### 2. Read a Webpage
```bash
.pi/agent/skills/pi-deep-research/venv/bin/python .pi/agent/skills/pi-deep-research/scripts/research.py read "https://example.com"
```
Extracts and prints the readable text content from the URL.

## Deep Research Workflow (Instructions for the Agent)

When a user asks you to perform "deep research" or use this skill, follow these steps autonomously:
1. **Initial Search:** Formulate 1-2 broad search queries and execute them using the `search` command.
2. **Read Sources:** Identify the most promising URLs from the search results and `read` them.
3. **Iterate:** Analyze what you've read. Identify knowledge gaps or conflicting information. Run follow-up, more specific `search` queries and `read` additional sources to dig deeper.
4. **Synthesize:** Compile the gathered information into a structured, comprehensive Markdown report (using the `write` tool to save it, or outputting it directly).
5. **Cite Sources:** Ensure every section includes clear inline citations and a "References" section with the URLs you actually read.
