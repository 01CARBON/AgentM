# intern-ai
Challenge for the Synera Intern AI


## Introduction

The task here is to create a Fastener Agent that takes in an image of a given geometry (ref. Sample Images), and suggest with a reason what is the best fastener type. As an additional context a guideline document with different fastener types is provided as well to the agent.


## Agent Setup 

OS - macOS/Linux
Python - 3.13.2

Setup the environment:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
source prepare_path.sh
```

For this task, current higest ranking model `gemini-2.0-flash-thinking-exp-01-21` on [Chatbot Arena](https://lmarena.ai/) (Vision Category) is selected. 

Get a free API Key for experimenting with this on - https://ai.google.dev/

```
export GEMINI_API_KEY="AIKEY...."
```

## Run the app
```
python3 app.py
```
