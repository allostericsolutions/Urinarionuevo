import openai

def call_gpt(prompt):
    """Llama a la API de OpenAI con el prompt dado y devuelve la respuesta."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # Mensaje del sistema (opcional)
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,  # Ajusta según tus necesidades
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()
