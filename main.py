from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import requests
import uuid
import os

app = FastAPI()

class Prompt(BaseModel):
    text: str

HUGGINGFACE_API_TOKEN = "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"

@app.post("/generate")
def generate_image(prompt: Prompt):
    # HuggingFace inference API call
    response = requests.post(
        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
        headers={"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"},
        json={"inputs": prompt.text},
    )

    if response.status_code == 200:
        # Unique filename for each image
        filename = f"{uuid.uuid4().hex}.jpg"
        with open(filename, "wb") as f:
            f.write(response.content)

        return FileResponse(filename, media_type="image/jpeg", filename=filename)
    
    else:
        return {
            "error": "Image generation failed",
            "details": response.json()
        }
