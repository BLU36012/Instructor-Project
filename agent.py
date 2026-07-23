import os
import instructor
import google.generativeai as genai
from pydantic import BaseModel

# 1. The SDK will automatically use the GEMINI_API_KEY environment variable 
# you just set in PowerShell.
genai.configure() 

# 2. Initialize the Gemini model and patch it with Instructor
# Note: You can change the model name to gemini-1.5-pro if needed
client = instructor.from_gemini(
    client=genai.GenerativeModel(
        model_name="models/gemini-1.5-flash" 
    )
)

# 3. Define the structure you want the AI to return using Pydantic
class UserInfo(BaseModel):
    name: str
    age: int
    occupation: str

# 4. Prompt the model
response = client.chat.completions.create(
    response_model=UserInfo,
    messages=[
        {"role": "user", "content": "My name is Ryan, I'm 21, and I am a Project Manager."}
    ]
)

# 5. The response is now a strongly typed Python object!
print(f"Name: {response.name}")
print(f"Age: {response.age}")
print(f"Occupation: {response.occupation}")
