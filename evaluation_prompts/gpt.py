import openai

def call_gpt(prompt):
    """Llama a la API de OpenAI con el prompt dado y devuelve la respuesta."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."}, 
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,  
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()
