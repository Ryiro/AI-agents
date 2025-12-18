from google import genai

# Initialize the client
client = genai.Client(api_key="AIzaSyA1N_ceyVhgF2NVdRzWvZkAPtqbKP1XC2c")

# Use the Gemini models to generate content
response = client.models.generate_content(
    # model="gemini-flash-latest",
    model="models/gemini-3-flash-preview",
    contents="what's the latest news in automated cars?",
)

print(response.text)

# List available models
# for model in client.models.list():
#     print(model.name)
