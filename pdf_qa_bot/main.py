"""main module for query the PDF"""

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from pdf_qa_bot.embeddings import create_embeddings


class Ask:
    """main class for QA"""

    def __init__(self, query: str) -> None:
        """init method"""

        self.query = query
        self.chain = load_qa_chain(OpenAI(), chain_type="stuff")


    def ask(self, texts: list) -> str:
        """execute the query"""

        docs = create_embeddings(texts).similarity_search(self.query)
        answer = self.chain.run(input_documents=docs, question=self.query)
        return answer
