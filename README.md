# 🧠 ClientLens AI

ClientLens AI is an AI-powered web application that analyzes health coaching conversations and generates structured client insights. The application helps coaches quickly understand a client's progress, identify potential health risks, and plan the next steps more efficiently.

This project was developed using **Streamlit** for the user interface and **Google Gemini 3.5 Flash** for AI-powered conversation analysis.

---

## ✨ Features

- Upload health coaching conversations in DOCX format
- Preview the uploaded conversation
- Generate an AI-powered weekly summary
- Analyze:
  - Nutrition
  - Sleep
  - Exercise
  - Water Intake
  - Stress
- Detect reported symptoms
- Highlight potential risk flags
- Suggest pending actions
- Generate coach recommendations
- Display supporting evidence for every insight
- Human review section for approval or feedback
- Save AI analysis and review results as JSON files

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini 3.5 Flash
- python-docx
- python-dotenv
- JSON

---

## 📁 Project Structure

```
ClientLensAI/
│
├── app.py
├── analyzer.py
├── prompts.py
├── utils.py
├── save_results.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sample_conversation.docx
│
└── outputs/
    ├── analysis_*.json
    └── review_*.json
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ClientLensAI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API Key

Create a `.env` file in the project folder.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🚀 Workflow

1. Upload a DOCX conversation.
2. Preview the conversation.
3. Click **Analyze Conversation**.
4. Gemini analyzes the conversation.
5. The application displays:
   - Weekly Summary
   - Health Metrics
   - Symptoms
   - Risk Flags
   - Pending Actions
   - Coach Recommendation
   - Supporting Evidence
6. Review the generated analysis.
7. Save the review.

---

## 📂 Output

The application automatically stores results inside the **outputs** folder.

Example:

```
outputs/
├── analysis_20260720_101530.json
└── review_20260720_101615.json
```

---

## ⚠️ Limitations

- Supports only DOCX conversation files.
- AI-generated insights depend on the quality of the uploaded conversation.
- Human review is recommended before making any health-related decisions.

---

## 🔮 Future Improvements

- PDF conversation support
- Chat-style conversation preview
- Export reports as PDF
- Dashboard with analytics
- User authentication

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Conversation Preview
- AI Analysis Dashboard
- Human Review Section

---

## 👨‍💻 Author

**Venkat Jyoshit Potnuru**

B.Tech Artificial Intelligence and Data Science

Amrita Vishwa Vidyapeetham, Amritapuri Campus