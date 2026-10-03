import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="CodeSentinel AI - Code Auditor & Refactoring Assistant",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CodeSentinel AI")
st.subheader("Automated Code Security Auditor & Refactoring Assistant")
st.write("Upload or paste your code snippet to analyze vulnerabilities, performance issues, and generate clean, production-ready code.")

# Sidebar Configuration
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Groq API Key:", type="password", value=os.getenv("GROQ_API_KEY", ""))

if not api_key:
    st.info("💡 Please enter your Groq API key in the sidebar or set it in a .env file.")

# Input Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 Source Code Input")
    language = st.selectbox("Select Programming Language", ["Python", "JavaScript", "C++", "Java", "SQL", "Go", "HTML/CSS"])
    
    code_input = st.text_area(
        "Paste your code snippet here:",
        height=350,
        placeholder="e.g., def get_user(user_id):\n    query = f'SELECT * FROM users WHERE id = {user_id}'\n    return db.execute(query)"
    )
    
    analyze_btn = st.button("🚀 Analyze & Refactor Code", use_container_width=True)

# System Prompt
SYSTEM_PROMPT = """
You are an expert Senior Code Auditor and Security Specialist. Your job is to analyze code provided by the user for:
1. Security Vulnerabilities (e.g., SQL injections, hardcoded secrets, unsafe operations).
2. Code Anti-patterns & Smells.
3. Performance Bottlenecks.

Output your response using the following structured layout:

### 📊 Audit Summary & Vulnerabilities
- Highlight severity (Critical, High, Medium, Low) for each issue found.
- Explain precisely why the code is unsafe or sub-optimal.

### 🛠️ Refactored & Optimized Code
Provide the complete fixed, secure, and production-ready code inside a code block.

### 💡 Key Improvements Made
Bullet points explaining what was changed and why.
"""

# Output Section
with col2:
    st.markdown("### 🛡️ Audit Report & Refactored Output")
    if analyze_btn:
        if not api_key:
            st.error("Error: Missing Groq API Key!")
        elif not code_input.strip():
            st.warning("Please paste some code first.")
        else:
            try:
                with st.spinner("Auditing code and generating fix..."):
                    client = Groq(api_key=api_key)
                    
                    # 1. Fetch live models and filter out third-party models requiring terms
                    all_models = [m.id for m in client.models.list().data]
                    valid_models = [m for m in all_models if not m.startswith("canopylabs")]
                    
                    # 2. Preferred standard models in priority order
                    preference_order = [
                        "llama-3.3-70b-versatile",
                        "llama-3.1-70b-versatile",
                        "llama3-70b-8192",
                        "llama-3.1-8b-instant",
                        "llama3-8b-8192",
                        "mixtral-8x7b-32768"
                    ]
                    
                    selected_model = None
                    for pref in preference_order:
                        if pref in valid_models:
                            selected_model = pref
                            break
                    
                    # Fallback to first non-canopylabs model if no preference matches
                    if not selected_model and valid_models:
                        selected_model = valid_models[0]

                    if not selected_model:
                        st.error("No valid LLM models available on your Groq account.")
                    else:
                        response = client.chat.completions.create(
                            model=selected_model,
                            messages=[
                                {"role": "system", "content": SYSTEM_PROMPT},
                                {"role": "user", "content": f"Language: {language}\n\nCode Snippet:\n```{language.lower()}\n{code_input}\n```"}
                            ],
                            temperature=0.2,
                            max_tokens=2048
                        )
                        
                        result = response.choices[0].message.content
                        st.markdown(result)
                        st.caption(f"⚡ *Audited using model: `{selected_model}`*")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")