# Assignment 1: AI Chatbot

## Overview

A web-based AI chatbot built using **FastAPI** and **Groq Cloud**.

This project demonstrates:

- Prompt Engineering
- Conversation History Management
- Multi-turn Context
- Pydantic Validation
- Failure-mode Handling
- Security Practices

## Use Cases

### 1. Restaurant Ordering Bot
Provides assistance with restaurant and food-ordering related requests.

### 2. Movie Ticket Booking Bot
Provides assistance with movie tickets, showtimes and booking-related questions.

### 3. IT Helpdesk Support Bot
Provides troubleshooting guidance for common IT problems such as login, VPN, network and software issues.

### 4. Bank Credit Card Assistant Bot
Provides general information about credit cards, payments, fees, applications and card-related support.

### 5. College Course Advisor Bot
Provides general information about courses, admissions, eligibility, academic planning and career paths.

## Technologies Used

- Python
- FastAPI
- Groq Cloud
- Groq Python SDK
- Pydantic
- Uvicorn
- Jinja2
- python-dotenv
- HTML
- CSS
- JavaScript

## Project Structure

```text
Assignment1_AI_Chatbot/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── usecase_1_restaurant/
│   ├── main.py
│   ├── system_prompt.txt
│   ├── test_log.md
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
│
├── usecase_2_movie/
│   ├── main.py
│   ├── system_prompt.txt
│   ├── test_log.md
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
│
├── usecase_3_it_helpdesk/
│   ├── main.py
│   ├── system_prompt.txt
│   ├── test_log.md
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
│
├── usecase_4_bank_credit_card/
│   ├── main.py
│   ├── system_prompt.txt
│   ├── test_log.md
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
│
└── usecase_5_college_course_advisor/
    ├── main.py
    ├── system_prompt.txt
    ├── test_log.md
    ├── templates/
    │   └── index.html
    └── static/
        ├── style.css
        └── script.js