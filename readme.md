# Weather App with MCP

## Prerequisites
Before diving in, make sure you have the following:
- Python 3.10 or later: Make sure it's installed on your computer.
- Basic Python Knowledge: You should know how to run Python scripts and install packages.
- OpenAI API Key: We'll use OpenAI's GPT-4o-mini. You can get your API key [here](https://platform.openai.com/).

## Step 1: Setting Up Your Environment
Let's set up a clean space for your project and install the necessary tools.

1. Create a Virtual Environment
   ```
   python -m venv mcp-env
   ```

2. Activate the Virtual Environment
   - On macOS/Linux:
     ```
     source mcp-env/bin/activate
     ```
   - On Windows:
     ```
     mcp-env\Scripts\activate
     ```

3. Install Required Packages:
   ```
   pip install mcp openai
   ```

4. Setup the .env file:
   Create a .env file in your project directory with the following content:
   ```
   OPENAI_API_KEY=your-openai-api-key
   MCP_SSE_URL=http://localhost:8080/sse
   ```

## Step 2: Running the Server
Once you have server.py ready, launch your server with:
```
python server.py --host localhost --port 8080
```

## Step 3: Running the Client
Once the server is running, launch the client by running:
```
python client.py
```
