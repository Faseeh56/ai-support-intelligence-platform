# Architecture v0

## Main Components

### 1. Customer / Admin
Customers ask support questions.
Admins upload or update company policies, FAQs, and support documents.

### 2. User Interface
Provides the chat/support interface for customers and a simple management interface for admins.

### 3. FastAPI Backend
Acts as the central application layer.
It receives requests, applies business logic, talks to the database, coordinates retrieval, and communicates with the LLM provider.

### 4. PostgreSQL
Stores application data such as users, documents, conversations, feedback, and support-related records.

### 5. Knowledge Retrieval Layer
Stores and searches document chunks using embeddings and vector similarity.
It retrieves the most relevant company knowledge for a customer question.

### 6. LLM Provider
Receives the customer question together with retrieved company knowledge and generates a grounded response.

---

## Customer Question Flow

1. Customer submits a support question through the UI.
2. The UI sends the question to the FastAPI backend.
3. The backend searches the knowledge retrieval layer for relevant document chunks.
4. The most relevant chunks are sent with the question to the LLM.
5. The LLM generates an answer based on the retrieved company knowledge.
6. The backend returns the answer and relevant sources to the customer.

---

## Admin Knowledge Update Flow

1. Admin uploads or updates a company policy, FAQ, or support document.
2. The backend receives and validates the document.
3. The document is cleaned and divided into smaller chunks.
4. Embeddings are created for those chunks.
5. The chunks, embeddings, and document metadata are stored for future retrieval.