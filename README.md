# LLM-Product-Assistant: Your Intelligent Product Guide

## Overview

The LLM-Product-Assistant is an interactive Q&A system designed to help users understand and navigate the functionalities of a particular product. It features role-based conversations, adapting the dialogue to fit the user's level of expertise, be it a teenager or a mechanical engineer.

## Table of Contents

1. [Key Features](#key-features)
2. [Technologies Deployed](#technologies-deployed)
3. [Installation & Setup](#installation--setup)
4. [Usage](#usage)
5. [Contributors](#contributors)

## Key Features

- Role-Based Conversations: Tailored dialogues based on the user's expertise.
- Multilingual Support: Accessibility across language barriers.

## Technologies Deployed

- **Amazon Titan**: For text summarization.
- **Claude**: Handling the Q&A functionality.
- **AI21Labs**: For multilingual capabilities.
- **AWS Speech-to-Text**: Converts spoken content from videos to text.

## Installation & Setup

### Prerequisites

- Python version: 3.10.7
- Obtain the required API keys from a team member.

### Steps

1. **Clone the Repository:**
    ```bash
    git clone <repository-link>
    cd LLM-Product-Assistant
    ```

2. **Navigate to the Main Folder:**
    ```bash
    cd path/to/main/folder
    ```

3. **Build the Docker Image:**
    ```bash
    docker build -t chatbot -f 07_Docker/Dockerfile .
    ```

4. **Run the Docker Container:**
    ```bash
    docker run -p 5000:5000 chatbot
    ```

5. **Access the Application:**
    Click on the link that appears in the console to start interacting with the chatbot.

## Contributors

- **Sam Swain**: Project Lead
- **Donald Li**: Backend Developer
- **Brian Hong**: AI Specialist
- **Wencheng Zhang**: Frontend Developer
