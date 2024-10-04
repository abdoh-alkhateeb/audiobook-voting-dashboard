# Audiobook Voting Dashboard

This repository contains a full-stack developer test task focused on building a simple Audiobook Voting Dashboard.

## Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask development server:
   ```bash
   python run.py
   ```

   The backend will be served at `http://localhost:5000`.

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install npm requirements:
   ```bash
   npm install
   ```

3. Set a custom API URL (optional):
   If you need to set a custom API URL other than `http://localhost:5000`, you can do so by setting the `NEXT_PUBLIC_API_URL` environment variable:
   ```bash
   export NEXT_PUBLIC_API_URL=http://your-custom-api-url
   ```

4. Start the Next.js server:
   ```bash
   npm run dev
   ```

   The frontend will be served at `http://localhost:3000`.
