
***

# ADR 001: Backend API Framework Choice

| | |
| :--- | :--- |
| **Status** | Accepted |
| **Date** | 2025-08-17 |
| **Deciders** | Simon, Dora |

---
## Context and Problem Statement

For the "Dora Mission Control" application, we need a Python backend server to expose the local AI model (Mistral 7B) as an API that the future GUI frontend can communicate with. The two primary candidates considered were Flask and FastAPI. We need to choose the framework that best aligns with the long-term goals of the project.

## Decision

We have decided to use **FastAPI** as the backend framework for our local AI server.

## Consequences

* **Positive:**
    * **Automatic Documentation:** FastAPI automatically generates interactive API documentation (Swagger UI). This directly supports our "Living Documentation" philosophy.
    * **Asynchronous Support:** Native `async` and `await` support is ideal for handling long-running AI model inference tasks without blocking the server.
    * **High Performance:** FastAPI is one of the fastest Python web frameworks available.
    * **Data Validation:** Built-in data validation using Pydantic will lead to a more robust and error-resistant API.

* **Negative:**
    * The initial learning curve is slightly steeper than Flask's, as it encourages the use of modern Python features like type hints. This is considered an acceptable trade-off for the long-term benefits.

***