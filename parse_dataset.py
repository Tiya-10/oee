
import pandas as pd
from langchain.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

# Load dataset (you can also pass df externally if you prefer)
df = pd.read_csv("oee_data.csv")  # make sure OEE & Month_Name are preprocessed

# Core function to process query
def get_oee_from_query(parse_description):
    dom_chunks = df.apply(lambda row: row.to_string(), axis=1).tolist()

    template = (
        "You are a smart factory assistant. Below is a record from a packaging device:\n\n"
        "{dom_content}\n\n"
        "User query: \"{parse_description}\"\n\n"
        "Follow these strict rules:\n"
        "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}.\n"
        "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response.\n"
        "3. **Empty Response:** If no information matches the description, return an empty string ('').\n"
        "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
    )

    model = Ollama(model="llama3")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    results = []
    for chunk in dom_chunks:
        response = chain.invoke({
            "dom_content": chunk,
            "parse_description": parse_description
        })
        if response.strip():
            results.append(response.strip())

    return results
