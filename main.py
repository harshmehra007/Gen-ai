from google import genai

client = genai.Client(api_key="AIzaSyA-D0IDBrDBfyCGE47BA8_oEkZsmPBV5AI")

messages = []

while True:
    user_input = input("You:")
    messages.append("user: " + user_input)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = messages,
     )
    
    messages.append("AI:" + response.text)

    print("AI:" + response.text)