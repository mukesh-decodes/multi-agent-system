# Multi-Agent System

This project is  building AI-powered multi-agent systems using LangChain, OpenAI models, structured outputs, and retrieval-augmented generation (RAG).

## What we have done so far

### 1. LangChain + OpenAI setup
The project started with a basic integration to OpenAI models using LangChain. This included:
- loading environment variables with `python-dotenv`
- initializing a chat model using `ChatOpenAI`
- invoking prompts and inspecting model responses

This gave us the foundation for building model-driven workflows without hardcoding credentials into the code.

### 2. Prompt templating
We created reusable prompt templates using LangChain's `ChatPromptTemplate` to generate structured input for the model.

Example pattern:
- input: country and state
- output: a short response prompt

This is useful for prompt reuse and cleaner orchestration across different agent tasks.

### 3. Structured output with Pydantic
We defined a structured response schema using `BaseModel` and `Field` from Pydantic.

The `Answer` model includes:
- `ans`: the model answer text
- `topic`: main topics covered
- `confidence`: a confidence score

This allows the model to return structured data instead of unformatted text, which is ideal for downstream automation.

### 4. RAG foundations
We also explored the basics of Retrieval-Augmented Generation (RAG):
- loading documents
- splitting text into chunks with `RecursiveCharacterTextSplitter`
- generating embeddings with `OpenAIEmbeddings`
- storing vectors in Chroma
- retrieving relevant documents via similarity search

This is the foundation for building AI systems that answer using external knowledge instead of relying only on model memory.

### 5. Notebook-based experimentation
The repository includes learning notebooks for:
- LangChain basics
- RAG basics
- embeddings and vector retrieval

These notebooks help prototype ideas quickly before turning them into reusable application logic.

## Current project structure

```text
multi-agent-system/
├── src/
│   ├── main.py
│   ├── langchain_basics.ipynb
│   ├── rag/
│   │   └── rag_basics.ipynb
│   └── utils/
│       ├── promt_template.py
│       └── structured_response.py
├── .gitignore
├── requirements.txt
├── README.md
└── .venv/
```

## Key learning goals

This project is designed to learn and combine the following patterns:
- LLM orchestration with LangChain
- OpenAI model access and evaluation
- structured response handling
- prompt engineering
- retrieval with embeddings
- tool use and agent design

## Future direction: MCP + multi-agent automation

The next phase of this project focuses on building an MCP-enabled multi-agent system for autonomous task execution.

### Planned roadmap

1. MCP integration
   - connect tools and external resources through MCP servers
   - expose capabilities such as file access, retrieval, search, or domain tools

2. Agent orchestration
   - multiple specialized agents working together
   - a coordinator agent delegating tasks to sub-agents

3. Workflow automation
   - agents performing structured tasks with clear inputs and outputs
   - model-driven decisions for routing, planning, and summarization

4. Evaluation and observability
   - track prompt behavior, tool usage, and response quality
   - measure success on reliability, correctness, and latency

5. Real-world application patterns
   - document intelligence
   - research assistant workflows
   - automated content pipelines
   - task execution across tools and data sources

## Example future architecture

```text
User request
    ↓
Coordinator Agent
    ├── Research Agent
    ├── Retrieval / MCP Agent
    ├── Analysis Agent
    └── Response Agent
    ↓
Final answer / action
```

This direction moves the project from basic LLM experimentation toward real autonomous workflows using tools, retrieval, and multi-agent collaboration.

## Notes

This repository is currently a foundation for experimentation and learning. The next stage is to turn these individual patterns into a production-style agent system centered on MCP and multi-agent automation.

## Suggested next step

Start by building a small orchestration flow where:
- one agent plans a task
- one agent retrieves data through MCP tools
- one agent produces a structured answer
- one coordinator validates the final output

That will provide a clean bridge from prompt-based learning to autonomous agent workflows.

