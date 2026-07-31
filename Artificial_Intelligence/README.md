# Artificial Intelligence

## Overview & Tech Stack

This module explores how modern AI systems are designed and evaluated: prompt engineering, system and user prompts, generative AI, decision trees, minimax, machine learning, reinforcement learning, exploration versus exploitation, deep learning, neural networks, large language models, transformer architecture, and hallucinations.

**Tech stack:** Python, the OpenAI Python SDK, environment-based API credentials, and terminal-based experimentation.

## Problem Sets Breakdown

This folder currently contains lecture practice rather than a separate submitted problem set.

- **`Lecture_Practice/chat.py`** — creates an `OpenAI` client, sends the question “What is cs50?” through the Responses API, and prints the returned text. Under the hood, the SDK reads authentication configuration from the environment and handles the HTTP request/response cycle. The model name is kept as it appeared in the coursework snapshot and may need updating for a current API account.

## Challenges & Reflections

I found AI practice deceptively different from the deterministic C exercises. The code is short, but the result depends on external credentials, SDK behavior, network access, and model availability. That forced me to think about configuration and reproducibility as part of the program itself. I also had to separate what the model generated from what my program actually controlled: the client, prompt, request, and output handling are mine, while the response is probabilistic.
