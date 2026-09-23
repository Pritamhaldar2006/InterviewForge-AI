# 🤖 AI Interview Simulator

An AI-powered technical interview simulator that creates personalized interviews based on a candidate's **resume** and a **job description (JD)**.

The system analyzes the candidate's skills against the requirements of the job, creates a structured interview plan, generates technical questions, evaluates answers, and maintains the interview state throughout the session.

> 🚧 **Project Status:** Under active development

---

## 📌 Overview

The **AI Interview Simulator** is designed to simulate a real technical interview using AI.

Instead of asking the same predefined questions to every candidate, the system uses the candidate's:

* Resume
* Job description
* Skills
* Relevant experience
* Strengths and weaknesses

to dynamically construct an interview.

The project currently focuses on building a robust **FastAPI backend** with session-based interview management, document processing, RAG-based retrieval, FAISS vector stores, and LLM-powered analysis.

The frontend and additional interview capabilities will be added as the project progresses.

---

## 🎯 What Problem Does It Solve?

Traditional interview preparation platforms generally rely on:

* Predefined question banks
* Generic questions
* Fixed difficulty levels
* Limited personalization

This project attempts to make technical interview practice more personalized.

For example, if a candidate's resume contains:

```text
Python
FastAPI
Machine Learning
SQL
Docker
```

and the job description requires:

```text
Python
FastAPI
Machine Learning
PostgreSQL
Docker
AWS
```

the system can identify the overlap and gaps between the candidate and the job requirements.

It can then use this information to create an interview plan around relevant technical areas.

---

# ✨ Key Features

### 📄 Resume Processing

Upload a candidate's resume in PDF format.

The system:

1. Loads the PDF
2. Extracts its contents
3. Splits the document into chunks
4. Generates embeddings
5. Stores the embeddings in FAISS

---

### 💼 Job Description Processing

Upload a job description as a text file.

The system processes the JD and creates a separate vector store.

---

### 🔍 Resume–JD Analysis

The system retrieves relevant information from both:

* Resume
* Job Description

and uses an LLM to analyze the candidate's relevance to the position.

---

### 🧠 AI-Generated Interview Plan

The system generates a structured interview plan based on the analysis.

The plan contains:

```text
Skill
 ├── Subtopic
 │    └── Difficulty
 ├── Subtopic
 │    └── Difficulty
 └── ...
```

For example:

```text
Python
 ├── Functions              → Easy
 ├── OOP                    → Medium
 └── Memory Management     → Hard

Machine Learning
 ├── Regression             → Medium
 ├── Classification         → Medium
 └── Model Evaluation       → Hard
```

---

### 🎤 Dynamic Interview

Questions are generated dynamically instead of relying entirely on a static question bank.

The interview can consider:

* Current topic
* Current subtopic
* Difficulty
* Previous answers
* Candidate strengths
* Candidate weaknesses
* Follow-up requirements

---

### 📝 Answer Evaluation

Candidate answers can be evaluated by the AI.

The evaluation system can consider:

* Technical correctness
* Completeness
* Understanding
* Relevance
* Missing concepts
* Follow-up requirements

---

### 💾 Session-Based Architecture

Each interview receives a unique session ID.

Example:

```text
3dae7d29-04f9-4716-9646-9485921c94da
```

All interview-related data is stored inside that session.

This allows multiple interviews to exist independently.

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │      Frontend        │
                         │   React (Planned)    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      FastAPI         │
                         │       Backend        │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
        ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
        │ Session        │  │ Document       │  │ Interview      │
        │ Management     │  │ Processing     │  │ Engine         │
        └────────────────┘  └───────┬────────┘  └───────┬────────┘
                                    │                    │
                                    ▼                    ▼
                           ┌────────────────┐   ┌────────────────┐
                           │ Embeddings     │   │ LLM            │
                           │ HuggingFace    │   │ Groq / Qwen    │
                           └───────┬────────┘   └────────────────┘
                                   │
                                   ▼
                           ┌────────────────┐
                           │ FAISS          │
                           │ Vector Store   │
                           └────────────────┘
```

---

# 🔄 How the Project Works

The complete workflow currently looks like this:

```text
1. Create Interview Session
            │
            ▼
2. Upload Resume
            │
            ▼
3. Upload Job Description
            │
            ▼
4. Build FAISS Indexes
            │
            ▼
5. Retrieve Resume + JD Information
            │
            ▼
6. Analyze Resume Against JD
            │
            ▼
7. Generate Interview Plan
            │
            ▼
8. Create Interview State
            │
            ▼
9. Generate Interview Questions
            │
            ▼
10. Candidate Answers
            │
            ▼
11. Evaluate Answer
            │
            ▼
12. Update Interview State
            │
            ▼
13. Continue Until Interview Completes
```

---

# 🧠 Why FAISS and Embeddings?

The project uses a RAG-style architecture for document processing.

Instead of sending an entire resume or job description to the LLM every time, the documents are converted into vector representations.

### Process

```text
Resume PDF
    │
    ▼
Text Extraction
    │
    ▼
Text Chunks
    │
    ▼
Embeddings
    │
    ▼
FAISS Vector Store
```

The same process is applied to the job description.

When information is needed, the system retrieves the most relevant chunks.

This helps reduce unnecessary context sent to the LLM and makes document retrieval more structured.

---

# 📁 Project Structure

Current backend structure:

```text
AI Interview Simulator/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── api/
│   │   │   ├── sessions.py
│   │   │   └── interview.py
│   │   │
│   │   ├── chains/
│   │   │
│   │   ├── config/
│   │   │
│   │   ├── embeddings/
│   │   │   └── embedding_model.py
│   │   │
│   │   ├── loaders/
│   │   │   ├── pdf_loader.py
│   │   │   └── text_loader.py
│   │   │
│   │   ├── models/
│   │   │   ├── interview_plan.py
│   │   │   └── interview_state.py
│   │   │
│   │   ├── services/
│   │   │   ├── analysis_services.py
│   │   │   ├── interview_service.py
│   │   │   ├── session_service.py
│   │   │   ├── session_file_service.py
│   │   │   ├── session_index_service.py
│   │   │   ├── state_service.py
│   │   │   └── storage_service.py
│   │   │
│   │   ├── splitters/
│   │   │   └── resume_splitter.py
│   │   │
│   │   ├── vectorstore/
│   │   │   ├── faiss_manager.py
│   │   │   └── indexing.py
│   │   │
│   │   └── main.py
│   │
│   ├── data/
│   │   ├── resumes/
│   │   └── job_description/
│   │
│   ├── storage/
│   │   └── sessions/
│   │
│   ├── tests/
│   │
│   ├── requirements.txt
│   └── ...
│
└── README.md
```

> The project structure will evolve as additional interview features and the frontend are added.

---

# ⚙️ Tech Stack

## Backend

* **Python**
* **FastAPI**
* **Uvicorn**
* **Pydantic**

## AI / LLM

* **LangChain**
* **LangGraph** *(planned/being integrated)*
* **Groq**
* **Qwen**
* **HuggingFace**

## RAG / Vector Search

* **FAISS**
* **HuggingFace Embeddings**
* **RecursiveCharacterTextSplitter**

## Document Processing

* **PyPDFLoader**
* **LangChain Document**

## Frontend

* **React** *(planned/in development)*

## Storage

Currently the project uses:

* Local filesystem
* JSON
* FAISS

No database is required at the current development stage.

---

# 🚀 Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Pritamhaldar2006/InterviewForge-AI.git
```

Move into the project:

```bash
cd AI-Interview-Simulator
```

Then enter the backend:

```bash
cd backend
```

---

# 🐍 2. Create a Virtual Environment

It is recommended to use Python 3.12 for this project.

Create the environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

---

# 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, install the required packages according to the project's dependency configuration.

---

# 🔑 4. Configure Environment Variables

Create a `.env` file inside the backend directory.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

Additional environment variables may be added as the project evolves.

> Never commit your `.env` file or API keys to GitHub.

Add this to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
storage/
```

---

# ▶️ 5. Start the FastAPI Server

From the `backend` directory:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

Swagger can be used to test the API without building the frontend.

---

# 🔌 Current API Flow

## 1. Create a Session

```http
POST /sessions
```

Example response:

```json
{
    "session_id": "3dae7d29-04f9-4716-9646-9485921c94da"
}
```

Save the returned session ID because it is used for subsequent requests.

---

## 2. Upload Resume

```http
POST /sessions/{session_id}/resume
```

Upload:

```text
resume.pdf
```

Only PDF resumes are currently supported.

Example response:

```json
{
    "message": "Resume uploaded successfully.",
    "session_id": "SESSION_ID",
    "filename": "resume.pdf",
    "path": "storage/sessions/SESSION_ID/resume.pdf"
}
```

---

## 3. Upload Job Description

```http
POST /sessions/{session_id}/jd
```

Upload:

```text
jd.txt
```

Currently, job descriptions are accepted as text files.

Once both the resume and JD are available, the system builds the vector indexes.

---

## 4. Start Interview

```http
POST /sessions/{session_id}/start
```

This triggers:

```text
Resume Index
      +
JD Index
      │
      ▼
Resume-JD Analysis
      │
      ▼
Interview Plan
      │
      ▼
Interview State
```

The state is persisted for the session.

---

# 💾 Session Storage

Instead of using a database at this stage, each interview session has its own directory.

Example:

```text
storage/
└── sessions/
    └── <session_id>/
        │
        ├── resume.pdf
        ├── jd.txt
        │
        ├── resume_index/
        │   ├── index.faiss
        │   └── index.pkl
        │
        ├── jd_index/
        │   ├── index.faiss
        │   └── index.pkl
        │
        └── interview_state.json
```

This approach keeps the development architecture simple while maintaining separation between interview sessions.

---

# 🧩 Interview State

The interview maintains a state throughout the session.

Conceptually:

```text
InterviewState
│
├── Resume-JD Analysis
│
├── Interview Plan
│
├── Current Topic
│
├── Current Subtopic
│
├── Interview History
│
├── Follow-up Count
│
├── Completed Topics
│
└── Interview Completion Status
```

The state is persisted as:

```text
interview_state.json
```

This allows the backend to continue an interview without keeping the entire state only in memory.

---

# 🗂️ Interview Plan Structure

The interview plan is represented using Pydantic models.

Conceptually:

```python
InterviewPlan
    └── topics
          └── InterviewTopic
                ├── skill
                └── subtopics
                      └── InterviewSubTopic
                            ├── name
                            └── difficulty
```

Example:

```json
{
    "topics": [
        {
            "skill": "Python",
            "subtopics": [
                {
                    "name": "Object Oriented Programming",
                    "difficulty": "Medium"
                },
                {
                    "name": "Memory Management",
                    "difficulty": "Hard"
                }
            ]
        }
    ]
}
```

---

# 🔄 Why Sessions Instead of Global Data?

A session-based architecture allows:

```text
User A
   │
   └── Session A
         ├── Resume A
         ├── JD A
         └── Interview State A


User B
   │
   └── Session B
         ├── Resume B
         ├── JD B
         └── Interview State B
```

This prevents data belonging to different interviews from being mixed together.

---

# 🧪 Running Tests

Tests are stored inside:

```text
backend/tests/
```

Run a test module using:

```bash
python -m tests.<test_module>
```

For example:

```bash
python -m tests.test_session_service
```

Running tests as Python modules also ensures the project root is correctly available for imports such as:

```python
from app.services.session_service import ...
```

---

# 🛠️ Development Workflow

When adding a new feature, the preferred flow is:

```text
API Layer
    │
    ▼
Service Layer
    │
    ▼
Business Logic
    │
    ▼
Models / Storage / AI Components
```

For example:

```text
POST /sessions/{id}/start
            │
            ▼
     interview.py
            │
            ▼
   interview_service.py
            │
            ├── analysis_services.py
            │
            ├── interview_plan_service.py
            │
            └── state_service.py
```

This keeps the API layer thin and prevents business logic from being placed directly inside FastAPI routes.

---

# 🔐 Security Notes

The current version is intended primarily for development.

Before deploying publicly, additional security measures should be implemented, including:

* Authentication
* Authorization
* API rate limiting
* File size limits
* File validation
* Secure session handling
* Secure storage
* Secret management
* Input sanitization
* Production logging
* HTTPS

Uploaded files should also be validated carefully before being processed.

---

# ☁️ Production Architecture

The current local-storage architecture is intentionally simple.

A future production architecture could look like:

```text
                    ┌───────────────┐
                    │    React      │
                    │   Frontend    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    FastAPI    │
                    │      API      │
                    └───────┬───────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
     PostgreSQL          Redis          Object Storage
       Database          Cache          Resume/JD Files
          │
          ▼
      Interview
        State
                            │
                            ▼
                    ┌───────────────┐
                    │ Vector Store  │
                    │ FAISS / Cloud │
                    └───────────────┘
                            │
                            ▼
                         LLM API
```

The project does **not currently require MongoDB or PostgreSQL** for its local development architecture.

---

# 🗺️ Roadmap

## ✅ Completed

* [x] Project architecture
* [x] Resume PDF loading
* [x] Job description loading
* [x] Document chunking
* [x] HuggingFace embeddings
* [x] FAISS vector stores
* [x] Resume-JD retrieval
* [x] Resume-JD analysis
* [x] AI interview plan generation
* [x] Subtopic-based interview planning
* [x] Interview state model
* [x] Session management
* [x] Local session storage
* [x] JSON state persistence
* [x] FastAPI application
* [x] Swagger documentation
* [x] Session creation API
* [x] Resume upload API
* [x] Job description upload API
* [x] Automatic session indexing
* [x] Start interview API

## 🚧 In Progress

* [ ] Dynamic question generation API
* [ ] Answer submission API
* [ ] AI answer evaluation
* [ ] Follow-up question system
* [ ] Interview completion logic
* [ ] Interview report generation

## 🔮 Planned

* [ ] React frontend
* [ ] Real-time interview UI
* [ ] Authentication
* [ ] PostgreSQL integration
* [ ] Cloud file storage
* [ ] Production vector database
* [ ] Interview history
* [ ] Candidate performance dashboard
* [ ] Detailed interview reports
* [ ] Deployment
* [ ] Dockerization
* [ ] CI/CD
* [ ] Monitoring and logging

---

# 🧠 Future AI Architecture

The project is expected to evolve toward a more structured AI workflow.

Conceptually:

```text
                Resume + JD
                    │
                    ▼
             Document Analysis
                    │
                    ▼
            Interview Planner
                    │
                    ▼
             Question Generator
                    │
                    ▼
                Candidate
                    │
                    ▼
             Answer Evaluator
                    │
                    ▼
             Interview Controller
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
   Follow-up Question    Next Subtopic
          │                   │
          └─────────┬─────────┘
                    ▼
             Interview Report
```

LangGraph can be used to orchestrate these stateful AI workflows as the system becomes more complex.

---

# 🐛 Troubleshooting

## `ModuleNotFoundError: No module named 'app'`

Run commands from the `backend` directory.

Instead of:

```bash
python tests/test_session_service.py
```

use:

```bash
python -m tests.test_session_service
```

---

## FastAPI cannot import `app.main`

Make sure you are running the command from:

```text
AI Interview Simulator/backend
```

Then run:

```bash
python -m uvicorn app.main:app --reload
```

---

## FAISS index not found

Make sure both the resume and JD have been uploaded before starting the interview.

The expected structure is:

```text
storage/sessions/<session_id>/
├── resume.pdf
├── jd.txt
├── resume_index/
└── jd_index/
```

---

## API key errors

Check that your `.env` file exists and contains the required API key.

Example:

```env
GROQ_API_KEY=your_api_key
```

Also make sure the `.env` file is not committed to GitHub.

---

# 🤝 Contributing

Contributions are welcome.

If you want to contribute:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/new-feature
```

3. Make your changes
4. Test your changes
5. Commit your changes

```bash
git commit -m "Add new feature"
```

6. Push the branch

```bash
git push origin feature/new-feature
```

7. Open a Pull Request

---

# 📄 License

This project is currently intended for educational and development purposes.

A formal open-source license can be added as the project matures.

---

# 👨‍💻 Author

**Pritam Haldar**

Building an AI-powered technical interview platform with:

* Python
* FastAPI
* LangChain
* LangGraph
* RAG
* FAISS
* LLMs
* React

---

# ⭐ Support the Project

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

Feedback, suggestions, and contributions are welcome.

---

## 🚀 Project Vision

The long-term goal of this project is to build a complete AI technical interviewer that can:

```text
Understand the candidate
        ↓
Understand the job
        ↓
Identify relevant skills
        ↓
Build an interview plan
        ↓
Ask technical questions
        ↓
Evaluate answers
        ↓
Ask intelligent follow-ups
        ↓
Adapt the interview
        ↓
Generate a detailed performance report
```

The goal is not simply to create an LLM chatbot, but to build a **structured, stateful AI interview system** capable of managing an entire technical interview workflow.
