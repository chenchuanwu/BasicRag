import os
from dotenv import load_dotenv
from vector_stores import VectorStores
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from operator import itemgetter
from file__history_store import get_history
load_dotenv()


def print_prompt(prompt):
    print(prompt.to_string())
    return prompt




class RAG:
    def __init__(self):
        self.vector_service = VectorStores(
            embedding=DashScopeEmbeddings(model=os.getenv("DASHSCOPE_EMBEDDING_MODEL"))
        )
        self.retriever = None
        self.llm = None
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "你是一个知识库，请根据以下知识库回答问题：{context}"),
                MessagesPlaceholder("history"),
                ("user", "{question}")
            ]
        )
        self.chat_model = ChatOpenAI(
            model=os.getenv("DEEPSEEK_MODEL"),
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_BASE_URL")
        )
        self.chain = self._get_chain()
        self.context = None
        self.response = None
        self.history = None

    def _format_docs(self, docs):
        if not docs:
            return "no relevant documents found"
        formatted_str = ""
        for doc in docs:
            formatted_str += f"Document: {doc.page_content}\n"
        return formatted_str

    def _get_chain(self):
        retriever = self.vector_service.get_retriever()

        chain = (
            RunnablePassthrough.assign(
                context=itemgetter("question") | retriever | self._format_docs
            )
            | self.prompt_template
            | print_prompt
            | self.chat_model
            | StrOutputParser()
        )

        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="question",
            history_messages_key="history",
        )
        return conversation_chain


if __name__ == "__main__":
    #session id configuration
    session_config = {
        "configurable": {
            "session_id": "user_001",
        }
    }
    
    res = RAG().chain.invoke(input={"question":"what is the company policy about remote work?"},config=session_config)
    print(res)
