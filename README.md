<<<<<<< HEAD
# LangChain Learning Journey 🚀

This repository contains my daily progress while learning **LangChain** as part of my **20-Day Professional LangChain Roadmap**. Each day focuses on a specific concept with practical examples.

---

# Day 1 – Introduction to LangChain & First LLM

## 📚 Topics Covered

- What is LangChain?
- LangChain Ecosystem
- Installing LangChain Packages
- Setting up a Virtual Environment
- Using `.env` for API Keys
- Loading Environment Variables using `python-dotenv`
- Connecting with Groq LLM
- Creating the First AI Application
- Invoking an LLM using `invoke()`

## 🛠 Packages Used

```python
langchain
langchain-core
langchain-groq
python-dotenv
```

## 📂 Files

```
day1.py
```

## 📖 Concepts Learned

- Chat Models
- Environment Variables
- API Integration
- invoke()
- LLM Response

## 🎯 Learning Outcome

After completing Day 1, I can:

- Connect LangChain with Groq.
- Secure API keys using `.env`.
- Send prompts to an LLM.
- Receive AI-generated responses.

---

# Day 2 – Prompt Templates & Output Parsers

## 📚 Topics Covered

- ChatPromptTemplate
- Prompt Variables
- System Message
- Human Message
- StrOutputParser
- LCEL (LangChain Expression Language)
- Chain Creation
- invoke()
- batch()

## 🛠 Packages Used

```python
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
```

## 📂 Files

```
day2.py
```

## 📖 Concepts Learned

### ChatPromptTemplate

Creates reusable prompts with variables.

Example:

```python
ChatPromptTemplate.from_messages([
    ("system", "You are a Python teacher."),
    ("human", "{question}")
])
```

---

### StrOutputParser

Converts the AI response into a normal Python string.

---

### LCEL Chain

Created using the pipe (`|`) operator.

```python
prompt | model | parser
```

---

### invoke()

Executes the chain for a single input.

```python
chain.invoke({
    "question": "Explain loops in Python."
})
```

---

### batch()

Executes multiple prompts in one call.

```python
chain.batch([
    {"question": "Explain Functions"},
    {"question": "Explain OOP"},
    {"question": "Explain Decorators"}
])
```

## 🎯 Learning Outcome

After completing Day 2, I can:

- Create reusable prompt templates.
- Pass dynamic variables into prompts.
- Build LangChain pipelines using LCEL.
- Parse AI responses into strings.
- Process single and multiple prompts using `invoke()` and `batch()`.

---

## 🚀 Next Topics

- Streaming (`stream()`)
- Async Streaming (`astream()`)
- RunnableLambda
- RunnableSequence
- RunnableParallel
=======
# LangChain Learning Journey 🚀

This repository contains my daily progress while learning **LangChain** as part of my **20-Day Professional LangChain Roadmap**. Each day focuses on a specific concept with practical examples.

---

# Day 1 – Introduction to LangChain & First LLM

## 📚 Topics Covered

- What is LangChain?
- LangChain Ecosystem
- Installing LangChain Packages
- Setting up a Virtual Environment
- Using `.env` for API Keys
- Loading Environment Variables using `python-dotenv`
- Connecting with Groq LLM
- Creating the First AI Application
- Invoking an LLM using `invoke()`

## 🛠 Packages Used

```python
langchain
langchain-core
langchain-groq
python-dotenv
```

## 📂 Files

```
day1.py
```

## 📖 Concepts Learned

- Chat Models
- Environment Variables
- API Integration
- invoke()
- LLM Response

## 🎯 Learning Outcome

After completing Day 1, I can:

- Connect LangChain with Groq.
- Secure API keys using `.env`.
- Send prompts to an LLM.
- Receive AI-generated responses.

---

# Day 2 – Prompt Templates & Output Parsers

## 📚 Topics Covered

- ChatPromptTemplate
- Prompt Variables
- System Message
- Human Message
- StrOutputParser
- LCEL (LangChain Expression Language)
- Chain Creation
- invoke()
- batch()

## 🛠 Packages Used

```python
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
```

## 📂 Files

```
day2.py
```

## 📖 Concepts Learned

### ChatPromptTemplate

Creates reusable prompts with variables.

Example:

```python
ChatPromptTemplate.from_messages([
    ("system", "You are a Python teacher."),
    ("human", "{question}")
])
```

---

### StrOutputParser

Converts the AI response into a normal Python string.

---

### LCEL Chain

Created using the pipe (`|`) operator.

```python
prompt | model | parser
```

---

### invoke()

Executes the chain for a single input.

```python
chain.invoke({
    "question": "Explain loops in Python."
})
```

---

### batch()

Executes multiple prompts in one call.

```python
chain.batch([
    {"question": "Explain Functions"},
    {"question": "Explain OOP"},
    {"question": "Explain Decorators"}
])
```

## 🎯 Learning Outcome

After completing Day 2, I can:

- Create reusable prompt templates.
- Pass dynamic variables into prompts.
- Build LangChain pipelines using LCEL.
- Parse AI responses into strings.
- Process single and multiple prompts using `invoke()` and `batch()`.

---

## 🚀 Next Topics

- Streaming (`stream()`)
- Async Streaming (`astream()`)
- RunnableLambda
- RunnableSequence
- RunnableParallel
>>>>>>> 6e300c7 (Langchain first AI agent using chat models created)
