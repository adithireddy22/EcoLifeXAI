
# EcoLifeXAI — Developer Implementation Roadmap

**Project Title:** EcoLifeXAI: An Explainable AI Platform for Sustainable Living and Personalized Well-Being

**Technology Stack:** React.js, Tailwind CSS, Recharts, Python, FastAPI, MongoDB Atlas, Scikit-learn, SHAP, LIME, Open Food Facts API, Gemini API

**Suggested Timeline:** 8 Weeks

**Development Approach:** Backend Setup → Database Connection → Data Models → APIs → External Integrations → AI/ML and Explainable AI → Frontend → Testing → Deployment

---

## Project Overview

EcoLifeXAI is a full-stack AI-powered platform designed to help users make sustainable shopping decisions, reduce waste, and understand their lifestyle habits.

The application combines product nutrition analysis, sustainability recommendations, personalized wellness insights, and an AI-powered sustainability chatbot. Explainable AI techniques help users understand the factors influencing supported model predictions and recommendations.

### Core Modules

1. **Eco Shopping Assistant** — Analyzes product information, nutrition facts, and available sustainability indicators.
2. **DIY Sustainability Assistant** — Suggests practical reuse, recycling, and waste-reduction activities.
3. **Personalized Health Report** — Provides general wellness insights based on user-provided lifestyle information.
4. **Explainable AI Engine** — Explains model predictions and scoring factors using suitable XAI techniques.
5. **AI Sustainability Chatbot** — Answers sustainability-related questions and provides personalized guidance.
6. **User Dashboard** — Displays saved products, previous reports, and saved sustainability activities.

---

# Project Status

🚧 **In Development — Initial Setup Pending**

The project will be implemented incrementally, starting with the FastAPI backend and its configuration.

The initial goal is to establish a working backend before adding MongoDB persistence, feature APIs, external services, AI/ML functionality, and the React frontend.

---

# Development Roadmap

## PHASE 1
### Backend Project Setup

- Python environment
- Virtual environment
- FastAPI
- Uvicorn
- Environment variables
- Health-check endpoint
- CORS configuration

↓

## PHASE 2
### MongoDB Atlas Setup

- Create MongoDB Atlas cluster
- Create database
- Configure database credentials
- Connect FastAPI to MongoDB
- Test database connectivity

↓

## PHASE 3
### Database Models and Schemas

- User preferences
- Product history
- Health reports
- DIY activities
- Chat history
- Pydantic validation schemas

↓

## PHASE 4
### User Management

- Create user profile
- Retrieve user preferences
- Update preferences
- Save user settings
- Input validation

↓

## PHASE 5
### Eco Shopping APIs

- Product lookup
- Barcode-based search
- Nutrition information
- Sustainability information
- Product analysis
- Alternative product suggestions
- Product history

↓

## PHASE 6
### Open Food Facts Integration

- External API requests
- Product data normalization
- Nutrition data extraction
- Environmental indicator extraction
- Missing-data handling
- Request timeout and error handling

↓

## PHASE 7
### DIY Sustainability APIs

- Retrieve DIY recommendations
- Categorize sustainability activities
- Generate step-by-step instructions
- Save activities
- Retrieve saved activities
- Mark activities as completed

↓

## PHASE 8
### Personalized Health Reports

- Lifestyle input forms
- Input validation
- Wellness scoring
- Lifestyle recommendations
- Report generation
- Report persistence

↓

## PHASE 9
### AI/ML and Recommendation Engine

- Data preprocessing
- Feature engineering
- Nutrition scoring
- Sustainability scoring
- Lifestyle analysis
- Model training where suitable datasets are available
- Model evaluation

↓

## PHASE 10
### Explainable AI Engine

- SHAP integration
- LIME integration
- Feature importance
- Explanation generation
- Model limitations
- Structured explanation responses

↓

## PHASE 11
### Gemini API Integration

- API configuration
- Sustainability chatbot
- DIY guidance
- Natural-language explanations
- Response validation
- API failure handling

↓

## PHASE 12
### React Frontend Setup

- React.js with Vite
- Tailwind CSS
- React Router
- Axios
- Recharts
- Environment configuration
- API service layer

↓

## PHASE 13
### Dashboard and Feature Interfaces

- Home dashboard
- Eco Shopping Assistant
- Product results
- DIY Sustainability Assistant
- Personalized Health Report
- Explainable AI results
- Sustainability chatbot
- User profile and history

↓

## PHASE 14
### Frontend–Backend Integration

- Connect React to FastAPI
- Connect feature forms to endpoints
- Display API responses
- Add loading indicators
- Add error messages
- Verify database persistence
- Test complete user workflows

↓

## PHASE 15
### Backend TDD and Testing

- API unit tests
- Service tests
- Database tests
- Input validation tests
- External API failure tests
- AI/ML evaluation
- XAI explanation tests
- Test coverage report

↓

## PHASE 16
### Frontend Testing

- Component testing
- Form validation
- API integration tests
- Responsive design
- Accessibility checks
- Error-state testing
- End-to-end workflows

↓

## PHASE 17
### Documentation and Deployment

- README
- Architecture diagram
- API documentation
- Environment setup instructions
- Project report
- Screenshots
- Test report
- Frontend deployment
- Backend deployment
- Production configuration

↓

## PHASE 18
### Final Git Cleanup and Demonstration

- Review Git history
- Remove unused files
- Verify `.gitignore`
- Remove exposed secrets
- Validate production environment
- Test deployed application
- Prepare presentation and demo
- Document limitations and future enhancements

---

# Phase 1 — Backend Project Setup

## Objective

Create a working FastAPI backend foundation for EcoLifeXAI.

## 1. Check Python Installation

Open PowerShell or the VS Code terminal and run:

```powershell
python --version
python -m pip --version
```

If Python is not recognized, install Python for Windows from:

https://www.python.org/downloads/windows/

## 2. Create the Project

```powershell
mkdir ecolifexai
cd ecolifexai

mkdir backend
cd backend
```

## 3. Create a Virtual Environment

```powershell
python -m venv venv
```

Activate it in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

For Command Prompt:

```cmd
venv\Scripts\activate.bat
```

After activation, the terminal should display `(venv)`.

## 4. Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install fastapi "uvicorn[standard]" python-dotenv
```

### Dependencies

- **FastAPI** — Backend web framework.
- **Uvicorn** — Runs the FastAPI application.
- **python-dotenv** — Loads configuration from environment variables.

Save dependencies:

```powershell
pip freeze > requirements.txt
```

## 5. Create the Backend Structure

```text
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── routers/
│   │   └── __init__.py
│   ├── services/
│   │   └── __init__.py
│   └── database/
│       └── __init__.py
├── tests/
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
```

## 6. Configure Environment Variables

Create `.env`:

```dotenv
APP_NAME=EcoLifeXAI
APP_ENV=development
DEBUG=true
```

Create `.env.example` with the same placeholder configuration.

Add the following to `.gitignore`:

```gitignore
venv/
__pycache__/
*.py[cod]
.env
.env.*
!.env.example
.pytest_cache/
.coverage
node_modules/
dist/
```

Never commit real credentials or API keys.

## 7. Create the Configuration File

Open `app/core/config.py`:

```python
import os
from pathlib import Path

from dotenv import load_dotenv

BACKEND_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BACKEND_DIR / ".env")

APP_NAME = os.getenv("APP_NAME", "EcoLifeXAI")
APP_ENV = os.getenv("APP_ENV", "development")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
```

## 8. Create the FastAPI Application

Open `app/main.py`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import APP_NAME, APP_ENV, DEBUG

app = FastAPI(
    title=APP_NAME,
    description=(
        "Backend API for sustainable living "
        "and personalized well-being."
    ),
    version="1.0.0",
    debug=DEBUG,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to EcoLifeXAI",
        "environment": APP_ENV,
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": APP_NAME,
    }
```

The CORS origins above are for local React development. Configure trusted production origins separately before deployment.

## 9. Run FastAPI

From the `backend` directory:

```powershell
python -m uvicorn app.main:app --reload
```

The application should start at:

http://127.0.0.1:8000

## 10. Test the Application

### Root Endpoint

Open:

http://127.0.0.1:8000/

Expected response:

```json
{
    "message": "Welcome to EcoLifeXAI",
    "environment": "development"
}
```

### Health-Check Endpoint

Open:

http://127.0.0.1:8000/health

Expected response:

```json
{
    "status": "healthy",
    "application": "EcoLifeXAI"
}
```

### Swagger UI

Open:

http://127.0.0.1:8000/docs

Use Swagger UI to inspect and test the available endpoints.

## Phase 1 Completion Criteria

- Python environment configured.
- Virtual environment created.
- Required packages installed.
- Backend folder structure created.
- Environment configuration implemented.
- FastAPI application running.
- Root and health-check endpoints tested.
- Swagger documentation accessible.
- CORS configured for local frontend development.
- `.gitignore` configured.

**Deliverable:** A running FastAPI backend ready for database integration.

---

# Phase 2 — MongoDB Atlas Setup

## Objective

Create a MongoDB database and connect it to FastAPI.

## 1. Create a MongoDB Atlas Account

Open:

https://www.mongodb.com/atlas

Create an account and a database deployment.

## 2. Create the Database

Use the database name:

```text
ecolifexai
```

Suggested collections:

```text
users
product_history
health_reports
diy_activities
chat_history
```

## 3. Install Database Dependencies

From the activated backend environment:

```powershell
pip install pymongo
pip freeze > requirements.txt
```

Use PyMongo to connect to MongoDB Atlas. An asynchronous driver can be considered later if required by the application architecture.

## 4. Configure the Database URL

Add the connection string to `.env`:

```dotenv
MONGODB_URI=your_mongodb_atlas_connection_string
MONGODB_DATABASE=ecolifexai
```

Replace the placeholder with the connection string supplied by MongoDB Atlas.

Do not commit the actual connection string.

## 5. Implement the Database Connection

Create:

```text
app/database/mongodb.py
```

This module will:

- Load the MongoDB connection string.
- Initialize the MongoDB client.
- Select the `ecolifexai` database.
- Provide access to database collections.
- Handle connection errors.
- Close the client during application shutdown.

## 6. Verify Connectivity

Create a database connectivity test or health-check extension that performs a MongoDB ping.

A successful connection should confirm that FastAPI can communicate with MongoDB Atlas.

## Phase 2 Completion Criteria

- MongoDB Atlas deployment created.
- Database name configured.
- Connection string stored securely.
- FastAPI connection established.
- Database ping successful.

**Deliverable:** A working MongoDB Atlas connection.

---

# Phase 3 — Database Models and Schemas

## Objective

Define the data structures required by EcoLifeXAI.

MongoDB stores documents rather than relational tables. Pydantic schemas will validate incoming API data and outgoing responses.

## 1. User Preferences

Suggested fields:

```text
UserPreferences
├── id
├── user_id
├── dietary_preferences
├── sustainability_preferences
├── lifestyle_preferences
├── created_at
└── updated_at
```

## 2. Product History

Suggested fields:

```text
ProductHistory
├── id
├── user_id
├── barcode
├── product_name
├── nutrition_summary
├── sustainability_summary
├── analysis_result
└── analyzed_at
```

## 3. Health Reports

Suggested fields:

```text
HealthReport
├── id
├── user_id
├── lifestyle_inputs
├── wellness_summary
├── recommendations
└── created_at
```

## 4. DIY Activities

Suggested fields:

```text
DIYActivity
├── id
├── user_id
├── title
├── category
├── instructions
├── difficulty
├── completion_status
└── created_at
```

## 5. Chat History

Suggested fields:

```text
ChatHistory
├── id
├── user_id
├── messages
└── updated_at
```

These are initial design suggestions. Final fields should be determined by the actual features and privacy requirements.

## 6. Create Pydantic Schemas

Create separate schemas for:

- Request payloads.
- Response payloads.
- User preferences.
- Product analysis.
- Health reports.
- DIY activities.
- Chat messages.

## Phase 3 Completion Criteria

- Schemas defined.
- Required fields validated.
- Invalid inputs rejected.
- Database documents can be created and retrieved.
- MongoDB ObjectIds are handled correctly in API responses.

**Deliverable:** Validated data structures for all core modules.

---

# Phase 4 — User Management

## Objective

Allow users to save preferences and retrieve their personalized information.

## APIs

```text
GET    /api/v1/users/{user_id}/preferences
PUT    /api/v1/users/{user_id}/preferences
```

Additional endpoints may be added for profile creation and retrieval.

## Tasks

- Define the user preferences schema.
- Implement preference retrieval.
- Implement preference updates.
- Validate dietary and sustainability preferences.
- Handle missing user records.
- Add appropriate access controls before exposing personal information.

**Deliverable:** Working user preference APIs.

Authentication must be implemented before treating a user-supplied ID as proof of identity.

---

# Phase 5 — Eco Shopping APIs

## Objective

Build the backend services for product lookup and analysis.

## Suggested APIs

```text
GET    /api/v1/products/{barcode}
POST   /api/v1/products/analyze
GET    /api/v1/products/history/{user_id}
```

## Tasks

- Accept barcode or product search inputs.
- Retrieve product information.
- Normalize product fields.
- Extract available nutrition data.
- Extract available environmental indicators.
- Generate an initial rule-based analysis.
- Return missing-data indicators.
- Save analysis history when appropriate.
- Support alternative-product recommendations when sufficient comparable data is available.

**Deliverable:** A working Eco Shopping Assistant backend.

---

# Phase 6 — Open Food Facts Integration

## Objective

Retrieve real product data from Open Food Facts.

## Tasks

- Create a dedicated external API service.
- Fetch products by barcode.
- Normalize product names, ingredients, and nutrition facts.
- Retrieve environmental indicators when available.
- Handle missing or incomplete data.
- Handle invalid barcodes, timeouts, and service errors.
- Avoid inventing unavailable nutrition or sustainability information.
- Cache responses when appropriate and consistent with API terms.

**Deliverable:** An external product data integration service.

---

# Phase 7 — DIY Sustainability APIs

## Objective

Recommend practical activities that help users reduce waste and reuse household materials.

## Suggested APIs

```text
GET    /api/v1/diy/recommendations
POST   /api/v1/diy/activities
GET    /api/v1/diy/activities/{user_id}
PATCH  /api/v1/diy/activities/{activity_id}
```

## Tasks

- Define DIY categories.
- Build a curated initial recommendation dataset.
- Add material and difficulty filters.
- Return step-by-step instructions.
- Save activities to user history.
- Track activity completion.
- Add Gemini-generated guidance in Phase 11.
- Review recommendations for practical safety.

**Deliverable:** A functional DIY Sustainability Assistant.

---

# Phase 8 — Personalized Health Reports

## Objective

Generate general wellness insights from user-provided lifestyle information.

## Suggested APIs

```text
POST /api/v1/health/analyze
GET  /api/v1/health/reports/{user_id}
```

## Tasks

- Define the required lifestyle inputs.
- Validate user-provided data.
- Implement transparent rule-based wellness insights initially.
- Add suitable scoring only when its calculation is defined.
- Generate practical lifestyle suggestions.
- Store reports only when needed and with appropriate privacy protections.
- Explain the limitations of the analysis.

Health recommendations should not be presented as medical diagnoses or substitutes for professional care.

**Deliverable:** A personalized wellness reporting service.

---

# Phase 9 — AI/ML and Recommendation Engine

## Objective

Add data-supported analysis and recommendations.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost, if suitable

## Tasks

- Identify appropriate datasets.
- Clean and preprocess data.
- Define input features and target variables.
- Develop nutrition and sustainability scoring logic.
- Train predictive models only when the task and data justify them.
- Evaluate models using suitable metrics.
- Test recommendations against representative cases.
- Document limitations and potential bias.
- Expose analysis through reusable Python services.

A deterministic scoring method may be more appropriate than a trained model for some features. Do not claim that a model is trained unless training and evaluation have actually been completed.

**Deliverable:** Tested scoring and recommendation services.

---

# Phase 10 — Explainable AI Engine

## Objective

Make suitable AI predictions understandable to users.

## Technologies

- SHAP
- LIME

## Tasks

- Select a compatible predictive model.
- Generate SHAP explanations where supported.
- Generate LIME explanations where appropriate.
- Identify influential input features.
- Convert explanations into understandable language.
- Return explanations through backend services.
- Test whether explanations match model behavior.
- Clearly distinguish model explanations from general AI-generated text.

Example response:

```json
{
    "prediction": "Example result",
    "explanation": [
        "The result was influenced by the available input features."
    ],
    "model_version": "example-version"
}
```

The example is illustrative. Actual output fields must match the implemented model.

**Deliverable:** An explainability service integrated with supported AI/ML features.

---

# Phase 11 — Gemini API Integration

## Objective

Add conversational sustainability guidance and natural-language responses.

## Tasks

- Obtain an API key from the appropriate Google AI developer service.
- Store the key in backend environment variables.
- Implement a dedicated Gemini service.
- Add request timeouts and error handling.
- Build the sustainability chatbot endpoint.
- Generate DIY guidance where appropriate.
- Validate and structure model outputs.
- Add sensible input and output limits.
- Avoid sending unnecessary personal information to external services.

Suggested endpoint:

```text
POST /api/v1/chatbot/chat
```

Example request:

```json
{
    "message": "How can I reuse an old glass jar?"
}
```

Example response:

```json
{
    "reply": "You could clean the jar and reuse it for storage."
}
```

**Deliverable:** A working sustainability chatbot service.

---

# Phase 12 — React Frontend Setup

## Objective

Set up the frontend and its connection to the backend.

## Technologies

- React.js
- Vite
- Tailwind CSS
- Axios
- Recharts
- React Router

## Tasks

- Create the React project.
- Configure Tailwind CSS using the instructions for the selected version.
- Install routing and API client dependencies.
- Create shared layouts and reusable components.
- Configure frontend environment variables.
- Create an API service layer.
- Establish communication with FastAPI.
- Build a shared error-handling strategy.

## Suggested Setup

```bash
npm create vite@latest frontend -- --template react
cd frontend
npm install
npm install axios recharts react-router-dom
```

Configure Tailwind CSS using the current official installation guide for your selected version.

**Deliverable:** A running React frontend with reusable components and API configuration.

---

# Phase 13 — Dashboard and Feature Interfaces

## Objective

Build the user-facing application.

## Suggested Pages

```text
Home Dashboard
├── Eco Shopping Assistant
├── Product Analysis Results
├── DIY Sustainability Assistant
├── Personalized Health Report
├── Explainable AI Results
├── Sustainability Chatbot
└── User Preferences and History
```

## Tasks

- Create responsive navigation.
- Build product search and barcode input.
- Display nutrition and available sustainability data.
- Show recommendation explanations.
- Build DIY activity cards and detail screens.
- Create health input forms and reports.
- Display charts using Recharts when meaningful.
- Implement chatbot messaging.
- Display saved history and preferences.
- Add loading, empty, and error states.

**Deliverable:** A functional EcoLifeXAI user interface.

---

# Phase 14 — Frontend–Backend Integration

## Objective

Connect all implemented frontend modules to their corresponding backend endpoints.

## Tasks

- Connect product forms to product APIs.
- Connect dashboard components to saved history.
- Connect DIY screens to recommendation APIs.
- Connect health forms to report endpoints.
- Connect the chatbot interface to Gemini-backed APIs.
- Display API errors clearly.
- Verify database persistence across sessions.
- Test complete user journeys.
- Ensure production API URLs are configurable.

**Deliverable:** An integrated full-stack application.

---

# Phase 15 — Backend TDD and Testing

## Objective

Verify backend correctness and prevent regressions.

## Testing Tools

- Pytest
- FastAPI TestClient
- Mocking utilities

## Tasks

- Write unit tests for service functions.
- Test request and response schemas.
- Test API success cases.
- Test invalid inputs and missing fields.
- Test database operations.
- Mock external API responses.
- Test timeout and failure handling.
- Test AI scoring and explanation outputs.
- Measure test coverage.
- Fix discovered defects.

**Deliverable:** A tested backend with documented test results.

---

# Phase 16 — Frontend Testing

## Objective

Validate user interface behavior and complete workflows.

## Tasks

- Test reusable components.
- Test form validation.
- Test loading and error states.
- Test API integration.
- Check mobile and desktop layouts.
- Verify keyboard navigation and accessibility.
- Test product lookup and report workflows.
- Test chatbot interaction.
- Check browser console errors.
- Fix frontend defects.

Suitable tools include Vitest and React Testing Library. An end-to-end testing tool can be added if needed.

**Deliverable:** A tested and responsive frontend.

---

# Phase 17 — Documentation and Deployment

## Objective

Prepare EcoLifeXAI for demonstration and external access.

## Documentation

- Project overview
- Technology stack
- Architecture diagram
- Installation instructions
- Environment variable reference
- API documentation
- Test report
- Screenshots
- Known limitations
- Future enhancements

## Deployment Tasks

- Deploy the React frontend to Vercel or a suitable alternative.
- Deploy FastAPI to a compatible backend hosting platform.
- Configure production environment variables.
- Restrict database access appropriately.
- Configure trusted production CORS origins.
- Verify all deployed endpoints.
- Test external API connectivity.
- Check application logs and error handling.

**Deliverable:** A deployed application with setup and usage documentation.

---

# Phase 18 — Final Git Cleanup and Demonstration

## Objective

Prepare the final repository and presentation.

## Tasks

- Review the project structure.
- Remove unused files and dependencies.
- Confirm that `.env` and secrets are not committed.
- Review Git history and commit messages.
- Update `requirements.txt` and frontend lockfiles.
- Verify clean installation instructions.
- Run the final test suite.
- Test deployed workflows.
- Prepare the final demonstration.
- Record known limitations and future improvements.

**Deliverable:** A clean repository and demonstration-ready EcoLifeXAI application.

---

# Suggested Project Structure

```text
ecolifexai/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   └── mongodb.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routers/
│   │   │   ├── users.py
│   │   │   ├── products.py
│   │   │   ├── health.py
│   │   │   ├── diy.py
│   │   │   └── chatbot.py
│   │   ├── services/
│   │   │   ├── product_service.py
│   │   │   ├── health_service.py
│   │   │   ├── diy_service.py
│   │   │   └── chatbot_service.py
│   │   └── ai/
│   │       ├── scoring.py
│   │       └── explainability.py
│   ├── tests/
│   ├── .env
│   ├── .env.example
│   ├── .gitignore
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   ├── .env.example
│   └── package.json
│
├── README.md
└── .gitignore
```

The directory structure can evolve as implementation progresses. Create files when their corresponding modules are needed rather than implementing every module at the beginning.

---

# Current Architecture

```text
React.js + Tailwind CSS
            ↓
        HTTP / JSON
            ↓
      FastAPI Backend
            ↓
   ┌────────┼─────────┐
   ↓        ↓         ↓
MongoDB   AI/ML    External APIs
 Atlas    + XAI    ├── Open Food Facts
                   └── Gemini API
```

The React frontend communicates with FastAPI. The backend coordinates database operations, external service calls, scoring, and explainability.

---

# Suggested 8-Week Schedule

| Week | Planned Work |
|---|---|
| Week 1 | Backend setup and MongoDB connection |
| Week 2 | Database schemas, user preferences, and initial APIs |
| Week 3 | Product APIs and Open Food Facts integration |
| Week 4 | DIY and health-report services |
| Week 5 | AI/ML, XAI, and Gemini integration |
| Week 6 | React frontend and feature interfaces |
| Week 7 | Frontend–backend integration and testing |
| Week 8 | Final testing, deployment, documentation, and demo |

This is an approximate schedule. If you are implementing the project alone, prioritize a complete working product-analysis workflow before expanding to all modules.

---

# Recommended First Milestone

Implement the following in order:

1. Set up FastAPI.
2. Verify the `/health` endpoint.
3. Connect MongoDB Atlas.
4. Implement one product lookup endpoint.
5. Integrate Open Food Facts.
6. Display the retrieved product information in React.
7. Add transparent nutrition and sustainability analysis.
8. Add persistent history.
9. Expand to DIY, health reports, and chatbot functionality.
10. Add suitable XAI methods, tests, and deployment.

**The first major milestone is a complete end-to-end Eco Shopping Assistant**, from searching for a product in React to retrieving data through FastAPI and displaying the result with clear explanations.
