import openai

def call_gpt(prompt):
    """Llama a la API de OpenAI con el prompt dado y devuelve la respuesta."""

    response = openai.Completion.create(
        engine="text-davinci-003",  # Puedes cambiar el modelo si lo deseas
        prompt=prompt,
        max_tokens=100,  # Ajusta el número máximo de tokens según tus necesidades
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip() 
