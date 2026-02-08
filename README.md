# 🚀 AI Investor Finder (Flask + LLaMA)

AI Investor Finder is a simple and elegant Flask-based web application that helps users discover potential investors based on a given sector and country.  
The application uses the LLaMA 3.1 model via Groq API to generate AI-powered investor suggestions.

This project is intentionally small, clean, and learning-focused — perfect for interviews and portfolio demonstration.

---

## ✨ Features

- 🔍 Search investors by sector and country
- 🤖 AI-powered suggestions using LLaMA
- 🎨 Clean and minimal UI
- ⚡ Fast inference with Groq free tier
- 🔐 Secure API key handling using environment variables

---

## 🛠️ Tech Stack

- Backend: Python, Flask
- Frontend: HTML, CSS (Bootstrap supported)
- AI Model: LLaMA 3.1
- AI Provider: Groq
- Environment Management: python-dotenv

---

## 🚀 How to Run the Project

1. Clone the repository

   git clone https://github.com/your-username/ai-investor-finder.git  
   cd ai-investor-finder

2. Create and activate a virtual environment

   python -m venv venv  
   source venv/bin/activate  
   (Windows: venv\Scripts\activate)

3. Install required dependencies

   pip install flask groq python-dotenv

4. Create a .env file in the project root and add your API key

   GROQ_API_KEY=your_groq_api_key_here

5. Run the Flask application

   python app.py

6. Open your browser and visit

   http://127.0.0.1:5000

---

## 🤖 AI API Used

- Provider: Groq
- Model: llama-3.1-8b-instant
- API Type: Chat Completions

The AI prompt and logic are fully handled in the backend, keeping the frontend clean and secure.

---

## 🔑 Where to Place the API Key

Create a file named .env in the root directory and add:

GROQ_API_KEY=your_groq_api_key_here

The API key is loaded using environment variables and is never hardcoded in the source code.

---

## 🎯 Project Objective

- Learn Flask by building a real AI-powered application
- Understand AI API integration
- Follow secure backend practices
- Build an interview-ready mini project

---

## 🌱 Future Enhancements

- Investor category badges (AI / FinTech / SaaS)
- Database integration
- Deployment to Render or Railway
- Advanced filtering and search
- User authentication

---

## 👤 Author

Harish S  
AI & Data Science Enthusiast  
Python | Flask | LLaMA | AI Projects
