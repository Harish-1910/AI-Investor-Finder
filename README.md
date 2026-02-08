# 🚀 AI Investor Finder (Flask + LLaMA)

[![Live on Render](https://img.shields.io/badge/Live-Render-success)](https://ai-investor-finder.onrender.com)

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
## 🔑 How to Create a Groq API Key

This project uses the **Groq API** to access the LLaMA model.  
Follow the steps below to generate your API key.

### Step 1: Sign up / Log in to Groq
- Visit 👉 https://console.groq.com
- Sign up using GitHub or Google, or log in if you already have an account

### Step 2: Create an API Key
- After logging in, go to the **API Keys** section
- Click **Create API Key**
- Copy the generated key

### Step 3: Store the API Key Securely
Create a `.env` file in the project root and add:

GROQ_API_KEY=your_groq_api_key_here

⚠️ Never commit your API key to GitHub.  
The `.gitignore` file already prevents this.

### Step 4: Add API Key on Render
When deploying on Render:
- Go to your Render service dashboard
- Navigate to **Environment**
- Add a new variable:
  - Key: GROQ_API_KEY
  - Value: your_groq_api_key_here
- Save changes and redeploy

---

## 🌱 Future Enhancements

- Advanced investor categorization and filtering
- Region-wise and funding-stage filters
- Database integration for caching results
- User authentication and saved searches
- UI/UX improvements and animations
- Custom prompt tuning for different domains
- MIT License support and open-source contributions

---

## 🤝 Contributions

Contributions are **welcome and encouraged** 🎉  
Feel free to fork the repository, open issues, or submit pull requests to improve features, UI, or performance.

---

## 📄 License

This project is licensed under the **MIT License**, allowing free use, modification, and distribution.

---
