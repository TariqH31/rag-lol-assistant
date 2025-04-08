
# 🎮 League of Legends RAG Assistant

This is an AI-powered **Retrieval-Augmented Generation (RAG)** assistant built with **LangChain**, **OpenAI**, and **ChromaDB** that answers strategy questions about League of Legends champions like Zed and Yasuo.

Built by [@TariqH31](https://github.com/TariqH31) to showcase NLP, vector search, and LLM chaining in a real-world project. 💼

---

## 🧠 What It Does

- ✅ Loads custom strategy documents about LoL champions
- ✅ Embeds them using OpenAI’s embedding model
- ✅ Stores embeddings in Chroma vector store
- ✅ Uses GPT-3.5 to answer your questions based on those docs
- ✅ Example question:
  ```
  Q: How do I counter Zed?
  A: Try picking Kayn, Lissandra, or Malzahar. Use stasis or CC after he ults, and maintain vision to track shadows.
  ```

---

## 🛠 Tech Stack

- 🧱 LangChain
- 🤖 OpenAI (Chat + Embeddings)
- 💾 Chroma Vector Store
- 🐍 Python
- 🧠 RetrievalQA
- 🧠 RAG (Retrieval-Augmented Generation)

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/TariqH31/rag-lol-assistant.git
   cd rag-lol-assistant
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-...
   ```

4. Run the app:
   ```bash
   python app2.py
   ```

---

## 📌 Sample Documents

This project uses sample strategy notes for champions like Yasuo and Zed. You can expand this by adding more champs and uploading `.txt` or `.pdf` data.

---

## 📈 Skills Demonstrated

- Vector database indexing
- Prompt engineering
- LangChain RAG pipeline
- LLM + embedding integration
- NLP and search-based QA systems

---

## 👀 Future Add-ons

- ⏳ Streamlit UI (already built)
- ⏳ Upload `.txt`/`.pdf` files
- ⏳ Scale to full champion dataset
- ⏳ Integration with Riot API?

---

## 💼 For Recruiters

This project demonstrates:
- End-to-end AI app delivery
- Real use of vector search + embeddings
- Practical LangChain RAG integration
- API security and modular design

> 🔥 Great example of NLP + LLMs applied to gaming and real-world strategy!

---

## 📬 Contact

**Built by [Tariq H.](https://github.com/TariqH31)**  
Let's connect and build cool stuff 👇
💼 [LinkedIn](https://www.linkedin.com/in/tariq-hardan-46113921b/)