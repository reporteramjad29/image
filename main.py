from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Prompt(BaseModel):
    text: str

DEEPAI_API_KEY = "your_deepai_api_key_here"  # Replace with your real key

@app.post("/generate")
def generate_image(prompt: Prompt):
    response = requests.post(
        "https://api.deepai.org/api/text2img",
        data={'text': prompt.text},
        headers={'api-key': 5190ca90-6102-4fd2-8863-030c14747be1}
    )

    result = response.json()
    if "output_url" in result:
        return {"image_url": result["output_url"]}
    else:
        return {"error": "Image generation failed", "details": result}
