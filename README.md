# AutoTestGen AI

## Overview
AutoTestGen AI is an AI-powered tool designed to automate the generation of test cases for ETL data pipelines. It reads mapping documents in Excel format and generates SQL-based test cases with relevant metadata.

## Features
- Upload Excel mapping sheets
- Generate test cases using GPT-5 Nano
- Export results in CSV, Excel, or JSON formats
- Web-based UI for easy interaction

## Tech Stack
- **Frontend:** React.js
- **Backend:** Python (FastAPI)
- **LLM Integration:** GPT-5 Nano

## Setup Instructions

### Backend
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend
1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

## Deployment
- **Frontend Hosting:** Vercel
- **Backend Hosting:** Render or Railway

## Usage
1. Upload an Excel mapping sheet via the web UI.
2. Wait for the test cases to be generated.
3. Download the results in your preferred format.

## Security
- File uploads are sanitized to prevent directory traversal attacks.
- Data is processed locally to ensure security.

## License
MIT License