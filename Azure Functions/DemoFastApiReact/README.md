# FastAPI + React Demo with Azure Functions

This is a simple demo project that showcases how to build a web application using FastAPI for the backend and React for the frontend, all hosted on Azure Functions. The backend provides an API endpoint that returns a random number, which is then displayed on the React frontend.

## Prerequisites

- Python
- Node.js
- Azure Functions Core Tools

## Setup

The project is divided into two main parts: the backend (Azure Function + FastAPI) and the frontend (React). The azure function runs an ASGI server to serve the FastAPI app. The fast api app serves the API endpoint and the React app. The frontend is statically served by the FastAPI app using Jinja2 templates. Meaning you only need to deploy the Azure Function to host both the backend and frontend.

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install the required dependencies:

   ```bash
   npm install
   ```

3. Build the React app to generate static files:
   ```bash
   npm run build
   ```

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd ../
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Azure Functions host:

   ```bash
   func host start
   ```

5. Open your browser and navigate to `http://localhost:7071` to see the React app in action. Or run the main.py file directly with uvicorn for local testing:
   ```bash
   python main.py
   ```
