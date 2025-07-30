import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

# Initialize history list
history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "model": "codehelp",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = response.json()
        actual_response = response_json['response']
        return actual_response
    else:
        print("Error:", response.text)
        return "Error occurred: " + response.text

# Gradio interface
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your Prompt"),
    outputs="text"
)

interface.launch()
