import streamlit as st
import time
import openai
def get_response(prompt):
    """Returns the response for the given prompt using the OpenAI API."""
    completions = openai.Completion.create(
             engine = "text-davinci-003",
             prompt = prompt,
         max_tokens = 512,
        temperature = 0.7,
    )
    return completions.choices[0].text

def handle_input(
               input_str : str,
    conversation_history : str,
                 ):
    """Updates the conversation history and generates a response using GPT-3."""
    # Update the conversation history
    conversation_history += f"Q: {input_str}\nA:"
   
    # Generate a response using GPT-3
    message = get_response(conversation_history)

    # Update the conversation history
    conversation_history += f"{message}\n"
    # Print the response
    print(message)
    
    return conversation_history

st.set_page_config(layout="wide")

# creating a placeholder for the fixed sized textbox
txtbox = st.empty()
txt = ''
txtbox.text_area("Q:",txt, height = 500)

end_of_loop = False
counter = 1

while (end_of_loop==False):
    txt = txtbox.text_area("Enter your query:",txt, height = 500)
    if st.button("Ask The Bot"):
        output = handle_input(txt)
    txt += output
    txtbox.text_area("Enter your query:",txt, height=500)
    counter += 1
    if (counter > 100):
        end_of_loop = True

    time.sleep(0.2)
