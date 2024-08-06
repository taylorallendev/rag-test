#!/usr/bin/env python
from fastapi import FastAPI
from langserve import add_routes
from generate import generate_chain
import env

# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

add_routes(
    app,
    generate_chain,
    path="/generate",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)