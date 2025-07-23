import streamlit as st
import random

st.set_page_config(page_title="🎲 Family Game", page_icon="🧩", layout="wide")

# === GLOBAL CSS ===
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        header, footer, .stDeployButton {
            visibility: hidden;
        }
        .stButton>button {
            font-size: 1.2rem;
            background-color: #ffcf66;
            color: black;
            padding: 0.7rem 1.2rem;
            border-radius: 10px;
            border: none;
        }
        h1, h2, h3 {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# === SESSION STATE INIT ===
if "page" not in st.session_state:
    st.session_state.page = "rules"
if "players" not in st.session_state:
    st.session_state.players = []
if "num_players" not in st.session_state:
    st.session_state.num_players = 0
if "scores" not in st.session_state:
    st.session_state.scores = {}
if "questions" not in st.session_state:
    st.session_state.questions = []
if "custom_questions" not in st.session_state:
    st.session_state.custom_questions = []
if "custom_q_list" not in st.session_state:
    st.session_state.custom_q_list = [""]
if "current_question" not in st.session_state:
    st.session_state.current_question = ""
if "question_queue" not in st.session_state:
    st.session_state.question_queue = []
if "winning_score" not in st.session_state:
    st.session_state.winning_score = 10

# === PRESET QUESTIONS ===
preset_questions = [
    "What is {name}'s favorite color?",
    "What food does {name} love the most?",
    "What cartoon does {name} like best?",
    "What is {name}'s favorite animal?",
    "What makes {name} laugh the most?",
    "What toy does {name} play with the most?",
    "What song does {name} always sing?",
    "What is {name}'s favorite game?",
    "What does {name} want to be when they grow up?",
    "If {name} had a superpower, what would it be?",
    "What superhero does {name} like the most?",
    "What would {name} bring to a picnic?",
    "What is the silliest thing {name} ever did?",
    "What is something {name} always says?",
    "What does {name} like to wear?",
    "What fruit does {name} eat the most?",
    "What is {name}'s favorite thing to draw?",
    "What is {name}'s favorite drink?",
    "What animal would {name} be?",
    "What’s {name}’s favorite place to go?",
    "If {name} could fly anywhere, where would they go?",
    "What is {name}'s favorite thing to do outside?",
    "If {name} found a treasure chest, what would be inside?",
    "What would {name} build with LEGO?",
    "What is {name}'s favorite holiday?",
    "What is {name}'s favorite snack?",
    "What color are most of {name}’s clothes?",
    "If {name} could have any pet, what would it be?",
    "What is {name}'s favorite bedtime story?",
    "What is {name}'s favorite ice cream flavor?",
    "If {name} had a magic wand, what would they do first?",
    "What makes {name} feel happy?",
    "What makes {name} feel brave?",
    "What would {name} name a robot?",
    "What sport does {name} like to play?",
    "What is {name} really good at?",
    "What is {name} most afraid of?",
    "What would {name} take on a camping trip?",
    "What’s {name}’s favorite time of day?",
    "What game does {name} never get tired of?",
    "What does {name} do first after school?",
    "If {name} could be invisible, what would they do?",
    "If {name} could live in a movie, which one would it be?",
    "What color does {name} use the most when coloring?",
    "What is {name}'s favorite breakfast?",
    "What’s the funniest face {name} can make?",
    "What’s {name}’s favorite sound?",
    "What’s the best gift {name} ever got?",
    "What is {name} most proud of?",
    "What would {name} put on a pizza?"
]

# === RULES PAGE ===
if st.session_state.page == "rules":
    st.title("📜 How to Play – Family Game")
    st.markdown("""
    Welcome to *How Well Do You Know Your Family?* 👨‍👩‍👧‍👦

    **🎯 Goal:**  
    Try to guess fun facts about your family members and earn points!

    ---
    ### 🕹️ Game Steps:
    1. Choose how many players are playing.
    2. Enter everyone’s names.
    3. Set how many points are needed to win.
    4. Add your own fun questions (optional).
    5. Play and award points. First to win gets confetti! 🎉
    ---
    """)
    if st.button("✅ Got it! Let's start"):
        st.session_state.page = "start"

# === START PAGE ===
elif st.session_state.page == "start":
    st.title("🎉 Let's Set Up!")
    with st.form("setup_form"):
        num = st.number_input("👥 How many players?", min_value=1, max_value=99, step=1)
        win_score = st.number_input("🏆 How many points to win?", min_value=1, max_value=99, step=1, value=10)
        submitted = st.form_submit_button("Next →")
        if submitted:
            st.session_state.num_players = num
            st.session_state.winning_score = win_score
            st.session_state.page = "names"

# === NAME INPUT PAGE ===
elif st.session_state.page == "names":
    st.markdown("# ✍️ Enter Player Names")
    with st.form("name_form"):
        names = st.session_state.players or ["" for _ in range(st.session_state.num_players)]
        for i in range(len(names)):
            names[i] = st.text_input(f"Player {i+1} name", value=names[i], key=f"name_{i}")
        st.session_state.players = names

        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("✅ Continue"):
                if all(name.strip() != "" for name in names):
                    st.session_state.page = "custom"
                else:
                    st.warning("⚠️ Please enter all player names.")
        with col2:
            if st.form_submit_button("➕ Add New Player"):
                st.session_state.players.append("")
                st.rerun()

# === CUSTOM QUESTIONS PAGE ===
elif st.session_state.page == "custom":
    st.markdown("## ✨ Add Your Own Questions (Optional)")
    st.info("You can add fun questions here! Use **{name}** where the player's name should appear.")

    def add_question():
        st.session_state.custom_q_list.append("")

    def insert_name_tag(idx):
        current = st.session_state.custom_q_list[idx]
        if "{name}" not in current:
            st.session_state.custom_q_list[idx] = current + " {name}"

    for idx, val in enumerate(st.session_state.custom_q_list):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.session_state.custom_q_list[idx] = st.text_input(f"Question {idx+1}", value=val, key=f"q_{idx}")
        with col2:
            if st.button(f"Insert {{name}} to Q{idx+1}", key=f"insert_{idx}"):
                insert_name_tag(idx)

    if st.button("➕ Add another question"):
        add_question()

    if st.button("✅ Start Game 🎮"):
        valid_questions = [q.strip() for q in st.session_state.custom_q_list if q.strip()]
        st.session_state.custom_questions = valid_questions
        st.session_state.questions = preset_questions + valid_questions
        st.session_state.scores = {name: 0 for name in st.session_state.players}
        st.session_state.question_queue = random.sample(st.session_state.players, len(st.session_state.players))
        st.session_state.page = "question"

# === GAME PAGE ===
elif st.session_state.page == "question":
    st.markdown("## 🧠 Family Challenge Time!")

    if st.button("🛑 Stop Game and Restart"):
        st.session_state.page = "names"
        st.rerun()

    winners = [name for name, score in st.session_state.scores.items() if score >= st.session_state.winning_score]
    if winners:
        st.balloons()
        st.markdown("## 🏁 Game Over!")
        st.markdown(f"### 🏆 Winner: **{', '.join(winners)}** 🎉")
        st.markdown("### Final Scores:")
        for name in st.session_state.players:
            st.markdown(f"- {name}: **{st.session_state.scores[name]}** points")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔁 Restart Completely"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
        with col2:
            if st.button("✏️ Change Names Only"):
                st.session_state.page = "names"
                st.rerun()
        st.stop()

    if st.button("🔁 Next Question"):
        if not st.session_state.question_queue:
            st.session_state.question_queue = random.sample(st.session_state.players, len(st.session_state.players))
        player = st.session_state.question_queue.pop(0)
        question_template = random.choice(st.session_state.questions)
        st.session_state.current_question = question_template.format(name=player)

    if st.session_state.current_question:
        st.markdown(f"### ❓ {st.session_state.current_question}")

    st.markdown("---")
    st.markdown("### 🧮 Scoreboard")
    lead_score = max(st.session_state.scores.values()) if st.session_state.scores else 0
    for name in st.session_state.players:
        score = st.session_state.scores.get(name, 0)
        if score == lead_score and score > 0:
            st.markdown(f"✅ **{name}**: {score} points (Leader!)")
        else:
            st.markdown(f"{name}: {score} points")

    st.markdown("### ✅ Add Points")
    for name in st.session_state.players:
        if st.button(f"➕ Give 1 point to {name}"):
            st.session_state.scores[name] += 1
            st.rerun()
