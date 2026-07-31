from openai import OpenAI
client = OpenAI()
response = client.responses.create(
  model="gpt-3.5-turbo",
  input="What is cs50?"
)
print(response.output_text
      )

             