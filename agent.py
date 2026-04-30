import json
import os
from openai import OpenAI

# Streamlit Cloud securely injects the API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def load_knowledge():
    with open("knowledge_base.json", "r") as f:
        return json.load(f)

def generate_inference(patient_input):
    kb = load_knowledge()
    
    system_prompt = """
    You are an evidence-driven genomic reasoning assistant for thoracic oncology. 
    Map the patient's genomic input to the provided knowledge base.
    Output a structured 'Ranked Resistance Report' including:
    1. The identified resistance mechanism.
    2. A therapeutic recommendation or clinical trial match.
    3. The exact citation from the knowledge base.
    4. A simulated 'Confidence Score' based on the match quality.
    Do NOT make autonomous treatment decisions. Remind the user to consult the attending physician.
    """
    
    user_prompt = f"Patient Input: {patient_input}\n\nAvailable Knowledge Base: {json.dumps(kb)}"

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.1, # Low temperature prevents hallucinations
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    
    return response.choices[0].message.content
