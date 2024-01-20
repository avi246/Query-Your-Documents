from lang_imports import *
import docx2txt
import pandas as pd

def load_text_from_file(file):
    
  all_text = ""
  _, file_extension = os.path.splitext(file.name.lower())

  if file_extension == ".pdf":
      pdf_reader = PdfReader(file)
      text = ""
      for page in pdf_reader.pages:
          text += page.extract_text()
  elif file_extension == ".txt":
      text = file.read().decode("utf-8")
  elif file_extension == ".docx":
      text = docx2txt.process(file)
  elif file_extension in [".csv", ".xls", ".xlsx"]:
      df = pd.read_csv(file)
      text = df.to_string()
  else:
      st.write(f"Unsupported file type: {file.name}")
  all_text += text
  return all_text

st.title("Document QA System")
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "docx",".csv",".xls", ".xlsx"])

if uploaded_file is not None:
    raw_t = load_text_from_file(uploaded_file)
    embeddings = OpenAIEmbeddings()

    
    _, file_extension = os.path.splitext(uploaded_file.name.lower())
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_t)
    docsearch = FAISS.from_texts(texts, embeddings)
    

    retriever = docsearch.as_retriever()

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        verbose=True
    )

    tools = [
        Tool(
            name="Doc_Chatter",
            func=qa.run,
            description="Use this tool to answer questions related to the document provided by the users."
        )
    ]

    agent = initialize_agent(
        tools, llm, agent='zero-shot-react-description', verbose=True, max_iterations=3,
    )

    query = st.text_input("Enter a query:")
    if query:
        st.write("\nQuery:", query)
        ans = agent.run(query)
        st.write("\nAnswer:", ans)
