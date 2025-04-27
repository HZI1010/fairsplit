import streamlit as st
import random

# Dictionary of charades-friendly words in different languages
word_lists = {
    'English 🇬🇧': [
        'Swimming', 'Dancing', 'Cooking', 'Reading', 'Sleeping', 'Running', 'Eating',
        'Laughing', 'Crying', 'Jumping', 'Flying', 'Singing', 'Walking', 'Writing',
        'Painting', 'Driving', 'Climbing', 'Skating', 'Surfing', 'Playing guitar',
        'Taking photos', 'Brushing teeth', 'Washing dishes', 'Making coffee',
        'Playing piano', 'Playing tennis', 'Riding bike', 'Playing basketball'
    ],
    'Nederlands 🇳🇱': [
        'Zwemmen', 'Dansen', 'Koken', 'Lezen', 'Slapen', 'Rennen', 'Eten',
        'Lachen', 'Huilen', 'Springen', 'Vliegen', 'Zingen', 'Wandelen', 'Schrijven',
        'Schilderen', 'Rijden', 'Klimmen', 'Schaatsen', 'Surfen', 'Gitaar spelen',
        'Fotograferen', 'Tanden poetsen', 'Afwassen', 'Koffie zetten',
        'Piano spelen', 'Tennis spelen', 'Fietsen', 'Basketbal spelen'
    ],
    'Español 🇪🇸': [
        'Nadar', 'Bailar', 'Cocinar', 'Leer', 'Dormir', 'Correr', 'Comer',
        'Reír', 'Llorar', 'Saltar', 'Volar', 'Cantar', 'Caminar', 'Escribir',
        'Pintar', 'Conducir', 'Escalar', 'Patinar', 'Surfear', 'Tocar guitarra',
        'Fotografiar', 'Cepillarse los dientes', 'Lavar platos', 'Hacer café',
        'Tocar piano', 'Jugar tenis', 'Montar bicicleta', 'Jugar baloncesto'
    ],
    'Français 🇫🇷': [
        'Nager', 'Danser', 'Cuisiner', 'Lire', 'Dormir', 'Courir', 'Manger',
        'Rire', 'Pleurer', 'Sauter', 'Voler', 'Chanter', 'Marcher', 'Écrire',
        'Peindre', 'Conduire', 'Grimper', 'Patiner', 'Surfer', 'Jouer de la guitare',
        'Photographier', 'Se brosser les dents', 'Faire la vaisselle', 'Faire du café',
        'Jouer du piano', 'Jouer au tennis', 'Faire du vélo', 'Jouer au basket'
    ],
    'Deutsch 🇩🇪': [
        'Schwimmen', 'Tanzen', 'Kochen', 'Lesen', 'Schlafen', 'Rennen', 'Essen',
        'Lachen', 'Weinen', 'Springen', 'Fliegen', 'Singen', 'Gehen', 'Schreiben',
        'Malen', 'Fahren', 'Klettern', 'Schlittschuhlaufen', 'Surfen', 'Gitarre spielen',
        'Fotografieren', 'Zähne putzen', 'Abwaschen', 'Kaffee kochen',
        'Klavier spielen', 'Tennis spielen', 'Fahrrad fahren', 'Basketball spielen'
    ],
    'Italiano 🇮🇹': [
        'Nuotare', 'Ballare', 'Cucinare', 'Leggere', 'Dormire', 'Correre', 'Mangiare',
        'Ridere', 'Piangere', 'Saltare', 'Volare', 'Cantare', 'Camminare', 'Scrivere',
        'Dipingere', 'Guidare', 'Arrampicare', 'Pattinare', 'Fare surf', 'Suonare la chitarra',
        'Fotografare', 'Lavarsi i denti', 'Lavare i piatti', 'Fare il caffè',
        'Suonare il piano', 'Giocare a tennis', 'Andare in bicicletta', 'Giocare a basket'
    ]
}

# Set up the page with a fresh title
st.title('🎭 Charades Word Generator 🎭')

# Create two columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    # Language selector with flags
    language = st.selectbox(
        'Select Your Language / Choisissez Votre Langue / Wählen Sie Ihre Sprache:',
        list(word_lists.keys())
    )

with col2:
    # Create a number input
    num_words = st.number_input(
        'Number of Words:', 
        min_value=1, 
        max_value=15, 
        value=5
    )

# Tips in different languages
tips = {
    'English 🇬🇧': '✨ Act out these words without speaking! Have fun! ✨',
    'Nederlands 🇳🇱': '✨ Beeld deze woorden uit zonder te praten! Veel plezier! ✨',
    'Español 🇪🇸': '✨ ¡Representa estas palabras sin hablar! ¡Diviértete! ✨',
    'Français 🇫🇷': '✨ Mimez ces mots sans parler! Amusez-vous! ✨',
    'Deutsch 🇩🇪': '✨ Stell diese Wörter ohne zu sprechen dar! Viel Spaß! ✨',
    'Italiano 🇮🇹': '✨ Recita queste parole senza parlare! Divertiti! ✨'
}

# Generate button in the selected language
button_text = {
    'English 🇬🇧': 'Generate Words!',
    'Nederlands 🇳🇱': 'Genereer Woorden!',
    'Español 🇪🇸': '¡Generar Palabras!',
    'Français 🇫🇷': 'Générer des Mots!',
    'Deutsch 🇩🇪': 'Wörter Generieren!',
    'Italiano 🇮🇹': 'Genera Parole!'
}

# Add a generate button
if st.button(button_text[language]):
    try:
        # Generate the words
        selected_words = random.sample(word_lists[language], k=min(int(num_words), len(word_lists[language])))
        
        # Display each word in a nice format with larger text
        st.subheader('🎲 Your Words / Vos Mots / Deine Wörter:')
        for i, word in enumerate(selected_words, 1):
            st.markdown(f'### {i}. {word}')
        
        # Add a fun element
        st.balloons()
        
        # Add tips in the selected language
        st.markdown('---')
        st.write(tips[language])
        
    except Exception as e:
        st.error(f'Error: {str(e)}')
        st.write('Please try again! / Essayez à nouveau! / Versuchen Sie es erneut!')
    except Exception as e:
        st.error(f"Error generating words: {str(e)}")
        st.write("Please try again!")
