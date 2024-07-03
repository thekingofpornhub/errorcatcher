import openai
from openai import AzureOpenAI
import config

openai.api_key = config.API_KEY

client = AzureOpenAI(
    azure_endpoint=config.ENDPOINT,
    api_key=config.API_KEY,  
    api_version=config.API_VERSION,
)

def start_conversation(message):
    try:
        response = client.chat.completions.create(
            model=config.MODEL,
            messages=[{"role": "user", "content": message}],
            temperature=0,
            top_p=1,
            frequency_penalty=0,
            max_tokens=2000,
            stop=None
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error during API call: {e}")
        return None

def autodeal(input_text, template):
    formatted_text = template.format(body=input_text)
    response = start_conversation(formatted_text)
    if response:
        print("--------------------------------------------------")
        return response
    else:
        print(f"no response")
