# LLM-Product-Assistant

## Description

LLM-Product-Assistant is a Q&A system designed to assist end users with questions about the functionalities of a product. The system is capable of holding a role-based conversation, catering the dialogue to the user's expertise level (e.g., teenager vs mechanical engineer).

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Team Members](#team-members)

## Technologies Used

- Amazon Titan for text summarization
- Claude for Q&A
- AI21labs for the multilingual aspect
- Speech-to-text AWS model to convert speech from videos to text

## Installation

py version: 310

```
git clone <repository-link>
cd LLM-Product-Assistant
pip install -r requirements.txt
```

## Usage

```
python main.py --product <product-name> --role <user-role>
```

## Team Members

- Sam Swain
- Donald Li
- Brian Hong
- Wencheng Zhang
