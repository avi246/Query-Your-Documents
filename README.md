# Query-Your-Documents


Query-Your-Documents is a project that allows users to query documents in various formats (.pdf, .txt, .docx, .csv, .xls, .xlsx) using Open AI's Language Model (LLM). This tool leverages Open AI's powerful language capabilities to enable users to interactively search and retrieve information from their documents.

## Getting Started

To get started with Query-Your-Documents, follow the steps below:

### 1. Clone the Repository

Clone the Query-Your-Documents repository to your local machine using the following command:

```bash
git clone https://github.com/avi246/Query-Your-Documents.git

An alternative to cloning the repositroy is simply downloading the zipped Code file by clicking on the Green "Code" Option to the top right of the repository box.

### 2. Installing the Required Libraries

Move to the cloned folder and install all the required libraries for runningn the code using the following command in the terminal:

''' bash
pip install -r requirements.txt

### 3. Insertion of API Key

Acquire the OpenAI API key from https://platform.openai.com/api-keys and paste it in the commented line in the lang_imports.py file.

### 4. Run the code by using the following command in your teminal:

''' bash
streamlit run doc_reader.py

### 5. Use the Software

Once you are done with these steps, a locally hosted site will open up where you will upload your document in the dropbox and can proceed with querying it.


