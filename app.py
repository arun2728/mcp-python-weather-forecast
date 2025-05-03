import streamlit as st
import asyncio
import os
from client import MCPClient
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="MCP Chat Interface", layout="wide")
st.title("MCP Chat Interface")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.initialized = False

# Create a function to run async code
def run_async(func):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(func)
    finally:
        loop.close()

# Initialize client
async def initialize_client():
    client = MCPClient()
    await client.connect_to_sse_server(server_url=os.getenv("MCP_SSE_URL"))
    return client

# Handle sending messages
async def process_message(prompt):
    client = MCPClient()
    try:
        await client.connect_to_sse_server(server_url=os.getenv("MCP_SSE_URL"))
        response = await client.process_query(prompt)
        return response
    finally:
        await client.cleanup()

# Chat container
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Message input
prompt = st.chat_input("Enter your message")
if prompt:
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get and display assistant response
    with st.spinner("Thinking..."):
        response = run_async(process_message(prompt))
    
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Add a sidebar with information
with st.sidebar:
    st.header("About")
    st.write("This is an Weather Forecast application using MCP")
    
    if st.button("Reset Chat"):
        st.session_state.messages = []
        st.experimental_rerun() 