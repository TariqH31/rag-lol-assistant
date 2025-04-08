from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
import os
import textwrap

#Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#Create some basic documents to work with
documents = [
    """Champion: Yasuo
Counters: Malphite, Rammus, Lissandra
Build Against: Armor and anti-crit (e.g., Thornmail, Frozen Heart)
Abilities to Wait Out: Wind Wall (W), Last Breath (R)
Combat Tips: Avoid extended trades. Bait out Wind Wall before engaging. CC and burst him before he can stack his passive shield or land a multi-target ultimate.
""",
    """Champion: Zed
Counters: Kayn, Lissandra, Malzahar
Build Against: Armor and anti-burst (e.g., Zhonya's Hourglass, Seeker's Armguard)
Abilities to Wait Out: Death Mark (R), Living Shadow (W)
Combat Tips: Time your defensive tools (e.g., stasis or CC) after he ults. Vision control helps track his shadow movement. Deny him early kills to delay his power spikes.
"""

]
#Set up the Embeddings Engine
embeddings = OpenAIEmbeddings()

#Create a vector DB using Chroma
db = Chroma.from_texts(documents, embeddings)

#Set up the Language Model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

#Connect it all with RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm = llm,
    chain_type = "stuff",
    retriever = db.as_retriever()
)

#time to ask question test
query = "How do I counter Zed?"
answer = qa_chain.invoke(query)

print("Q:", query)
print("A:", answer["result"])

print(f"\n🧠 Answer:\n{textwrap.fill(answer['result'], width=80)}")
