# 🛡️ CodeSentinel AI

**CodeSentinel AI** is an automated, high-performance security code auditor and refactoring assistant built for developers and security engineers. Powered by Groq-accelerated Llama models, CodeSentinel AI analyzes codebases in real time to identify critical vulnerabilities, anti-patterns, and performance bottlenecks—delivering production-grade, refactored code instantly.

---

## ✨ Features

- **⚡ Real-Time Security Auditing:** Detects SQL Injection, plain-text credential handling, missing resource cleanups, and timing attack risks.
- **🛠️ Production-Ready Refactoring:** Generates clean, parameterized, and secure refactored code using modern security primitives (e.g., `bcrypt`, context managers, type hints).
- **🤖 Smart Dynamic Model Fallback:** Automatically fetches active Groq models at runtime and selects optimal Llama variants while filtering unauthorized third-party endpoints.
- **🌐 Multi-Language Support:** Analyzes Python, JavaScript, C++, Java, SQL, Go, and HTML/CSS snippets.

---

## 🛠️ Tech Stack

- **Frontend / UI:** Streamlit
- **LLM Engine:** Groq API (Llama 3.3 / Llama 3.1 70B & 8B variants)
- **Language:** Python 3.10+
- **Security & Libraries:** `bcrypt`, `python-dotenv`

---

## 🚀 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/alihassan449/codesentinel-ai.git](https://github.com/alihassan449/codesentinel-ai.git)
   cd codesentinel-ai
