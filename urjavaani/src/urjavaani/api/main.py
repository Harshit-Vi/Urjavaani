"""UrjaVaani FastAPI app. Run with: uvicorn urjavaani.api.main:app --reload."""

from fastapi import FastAPI

app = FastAPI(title="UrjaVaani")


@app.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}
