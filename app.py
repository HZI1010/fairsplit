import streamlit as st
from random_word import RandomWords

# Set up the page with a fresh title
st.title('✨ Chareds Word Generator ✨')
st.write('Enter a number (max 15) to generate that many random words!')

# Initialize the random word generator
r = RandomWords()

# Create a number input
num_words = st.number_input('How many words do you want?', 
                          min_value=1, 
                          max_value=15, 
                          value=5)

# Add a generate button
if st.button('Generate Words!'):
    # Generate the words
    words = [r.get_random_word() for _ in range(int(num_words))]
    
    # Display each word in a nice format
    for i, word in enumerate(words, 1):
        st.write(f'{i}. {word}')
        
    # Add a fun element
    st.balloons()
