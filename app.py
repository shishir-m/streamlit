import openai
import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]
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
    file = open("convo.txt","a")
    file.write(conversation_history)
    file.write("\n")
    file.close()
    
    # Print the response
    st.success(message)
    
    return conversation_history

f = open("convo.txt","w")
f.write("")
f.close()
conversation_history = ''''''
#UI
# Get the user's input
 
user_input = st.text_area("Enter your query:")
# Handle the input
if st.button("Ask The Bot"):
    file = open("convo.txt","r")
        conversation_history = file.read()
    file.close()
    conversation_history = handle_input(user_input, conversation_history)
    st.write("Present context:",conversation_history)  
