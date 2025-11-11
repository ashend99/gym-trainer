# Workout AI

An AI-powered fitness assistant that creates personalized workout and nutrition plans using LangGraph and OpenAI.

## Overview

Workout AI is an intelligent agent-based system that generates customized fitness plans tailored to individual user profiles. The system analyzes user information including age, gender, fitness goals, current fitness level, available equipment, and dietary preferences to create comprehensive workout routines and nutrition plans.

## Features

- **Personalized Workout Plans**: AI-generated exercise routines based on user goals, fitness level, and available equipment
- **Custom Nutrition Plans**: Tailored meal plans that support fitness objectives and accommodate dietary restrictions
- **Multi-Agent System**: Built with LangGraph for coordinated workflow between workout and nutrition planning agents
- **Flexible Planning**: Choose between workout-only, nutrition-only, or combined plans

## Project Structure

```
workout_ai/
├── agents/           # AI agents for workout and nutrition planning
├── models/           # Data models and LLM configurations
├── utils/            # Helper functions and formatters
└── workflows/        # LangGraph workflow definitions
```

## Technology Stack

- **LangGraph**: Agent orchestration and workflow management
- **LangChain**: LLM integration and chain management
- **OpenAI GPT-4**: Language model for generating personalized plans
- **Python 3.x**: Core programming language
