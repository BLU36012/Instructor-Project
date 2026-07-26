from fastapi import FastAPI
from pydantic import BaseModel
import instructor
from google import genai

app = FastAPI()
client = instructor.from_genai(genai.Client())

class UserProfile(BaseModel):
    name: str
    age: int
    role: str

class UserRequest(BaseModel):
    user_input: str

@app.post("/extract-profile")
def extract_profile(request: UserRequest):
    response = client.chat.completions.create(
        model="gemini-3.5-flash",
        response_model=UserProfile,
        messages=[{"role": "user", "content": request.user_input}]
    )
    # FastAPI automatically converts the Pydantic object to a JSON response
    return response