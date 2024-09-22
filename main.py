import openai

def generate_workout(biotype, days, exercise_type):
    # Configure your OpenAI API key
    openai.api_key = 'your-api-key'

    prompt = f"""
    Eu sou um personal trainer virtual. Eu preciso criar um plano de treino baseado nas seguintes informações:
    - Biotipo corporal: {biotype}
    - Dias disponíveis para treino: {days}
    - Tipo de exercício preferido: {exercise_type}

    Crie um plano de treino personalizado para maximizar os resultados.
    """

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=150
    )

    return response.choices[0].text.strip()

# Exemplos de uso
biotype = "Mesomorfo"
days = 3
exercise_type = "Peso Livre"

plan = generate_workout(biotype, days, exercise_type)
print("Plano de Treino Sugerido:")
print(plan)
