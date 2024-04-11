import openai


# Set up OpenAI API key
openai.api_key = ""

# Load article
with open("art.txt", "r") as f:
    article = f.read()

# Summarize using OpenAI GPT-3
openai_response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"Summarize the following article in 3 sentences:\n{article}",
    temperature=0.5,
    max_tokens=60,
    n = 1,
    stop=None,
)
#print(openai_response) # print API response to check its structure
openai_summary = openai_response.choices[0].text
print("OpenAI GPT-3 Summary:\n", openai_summary)
