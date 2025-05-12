# Chatbot Agent Service

A chatbot agent created using **OpenAI's Agent SDK**, hosted in a **Flask REST API** service.

## 🧠 Features

This intelligent chatbot agent offers the following capabilities:

- 📷 **Image-Based Transaction Analysis**  
  Extracts key information from user-uploaded transaction images using OCR and image processing tools.

- 📚 **RAG-Based Product Inquiry Handling**  
  Answers user questions related to a product by leveraging Retrieval-Augmented Generation (RAG).

- 💬 **Promise-to-Pay Assistance**  
  Guides customers through the process of making a promise to pay.

## 🛠️ Tech Stack

- **Flask REST API** – Web service framework  
- **OpenAI Agent SDK** – Core agent capabilities  
- **Langchain** – Orchestration and RAG integration  
- **Gemini Image Text Extractor** – Extract text from images  
- **OpenCV** – Image preprocessing and analysis  

## ⚙️ Installation Guidelines

1. **Clone this repository**  
   ```bash
   git clone https://github.com/FransAnth/chatbot-agent.git
   cd <repo-directory>
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv venv
   venv/Scripts/activate  # On Windows
   ```

   ```bash
   # Or for Unix/macOS
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   Create a `.env` file in the root directory with the following content:

   ```env
   # Model Choice ('openai' or 'gemini')
   MODEL_CHOICE="openai"

   # Model Name ('gpt-4o-mini' or 'gemini-2.0-flash')
   MODEL_NAME="gpt-4o-mini"

   # Model Keys
   OPENAI_API_KEY="Your Open AI API KEY"
   GEMINI_API_KEY="Your Google Gemini API KEY"
   ```

5. **Run the project**
   ```bash
   python main.py
   ```
