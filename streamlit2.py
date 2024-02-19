import openai
import streamlit as st

# Set OpenAI API key
# openai.api_key = "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"

# Input API key from user
api_key = st.text_input("Enter your OpenAI API key:", "")

# Set OpenAI API key
openai.api_key = api_key

# Function to interact with OpenAI model and get response
def get_response(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Let's do some arithmetic operations"},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app
def main():
    st.title("ChatGPT Demo")
    
    # Initialize session state
    if 'session_responses' not in st.session_state:
        st.session_state.session_responses = []

    # # Display previous prompts and responses
    # for prompt, response in st.session_state.session_responses:
    #     st.write("Prompt:", prompt)
    #     st.write("Generated Content:", response)
    #     st.write("---")  # Separator
        

    # Input prompt from user
    prompt = st.text_input("Enter your prompt:", "")

    if prompt.lower() == 'exit':
        st.write("Exited")
        st.empty()  # Remove all content
        return  # Exit the function

    if st.button("Generate"):
        if prompt:

            # Get response from OpenAI model
            response = get_response(prompt)

            # Store prompt and response in session state
            st.session_state.session_responses.append((prompt, response))
          
    # Display previous prompts and responses
    for prompt, response in st.session_state.session_responses:
        st.write("Prompt:", prompt)
        st.write("Generated Content:", response)
        st.write("---")  # Separator


# Run the Streamlit app
if __name__ == "__main__":
    main()