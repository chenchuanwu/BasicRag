# RAG (Retrieval-Augmented Generation) System

A Python-based Retrieval-Augmented Generation system that combines knowledge base retrieval with language model capabilities for intelligent question answering.

## 🚀 Features

- **Knowledge Base Management**: Upload and manage documents with deduplication using MD5 checksums
- **Vector Store**: ChromaDB for efficient vector storage and similarity search
- **Embedding**: DashScope Embeddings for high-quality text embeddings
- **LLM Integration**: DeepSeek Chat model for response generation
- **Streamlit UI**: User-friendly web interface for Q&A and file upload
- **Session Management**: Conversation history tracking with session IDs
- **Document Processing**: Automatic text splitting and chunking

## 📁 Project Structure

```
RAG/
├── rag.py                 # Main RAG system implementation
├── vector_stores.py      # Vector store management
├── knowledge_base.py     # Knowledge base operations
├── app_qa.py            # Streamlit Q&A interface
├── app_file_uploader.py # Streamlit file upload interface
├── config_data.py       # Configuration settings
├── file__history_store.py # Session history management
├── md5.txt              # MD5 checksum storage
├── kb_test*.txt         # Knowledge base test files
├── chroma_db/           # ChromaDB storage directory
└── .env                # Environment variables
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd RAG
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 🔧 Configuration

Create a `.env` file in the project root with the following configuration:

```env
# DashScope Configuration
DASHSCOPE_EMBEDDING_MODEL=text-embedding-v4
DASHSCOPE_API_KEY=your_dashscope_api_key

# DeepSeek Configuration
DEEPSEEK_MODEL=qwen3-max
DEEPSEEK_API_KEY=your_deepseek_api_key
DEEPSEEK_BASE_URL=https://api.deepseek.com

# User Configuration
USER_NAME=your_username
```

## 🚀 Usage

### Web Interface

1. **Q&A Interface**:
```bash
streamlit run app_qa.py
```
- Open your browser and go to `http://localhost:8501`
- Start asking questions based on the uploaded knowledge base
- Chat history is maintained during the session

2. **File Upload Interface**:
```bash
streamlit run app_file_uploader.py
```
- Upload text files (.txt, .pdf, .docx, .md)
- View file information and content
- Upload to knowledge base with deduplication

### Command Line Usage

1. **Direct Python Execution**:
```bash
python rag.py
```
- Runs a simple Q&A session with predefined questions

2. **Knowledge Base Operations**:
```bash
python knowledge_base.py
```
- Test knowledge base upload functionality

3. **Vector Store Operations**:
```bash
python vector_stores.py
```
- Test vector store retriever functionality

## 🔍 How It Works

1. **Document Processing**:
   - Files are read and content is extracted
   - Text is split into chunks using RecursiveCharacterTextSplitter
   - Each chunk gets an MD5 checksum for deduplication
   - Chunks are embedded using DashScope Embeddings

2. **Vector Storage**:
   - Embeddings are stored in ChromaDB
   - Metadata includes filename, MD5, timestamp, and operator
   - Similarity search is performed using configurable threshold

3. **Question Answering**:
   - User question is embedded
   - Similar chunks are retrieved from vector store
   - Context is formatted and sent to LLM with prompt template
   - Response is generated using DeepSeek model

4. **Session Management**:
   - Each chat session has a unique session ID
   - Conversation history is tracked and included in context
   - History is stored using message history store

## ⚙️ Configuration Options

### File: config_data.py
- `chunk_size`: 1000 characters per chunk
- `chunk_overlap`: 100 characters overlap
- `similarity_threshold`: 2 (for retriever)
- `max_split_char_number`: 1000 characters before splitting
- `collection_name`: "rag" (ChromaDB collection name)
- `persist_directory`: "./chroma_db" (storage path)

### Prompt Template
```python
[
    ("system", "你是一个知识库，请根据以下知识库回答问题：{context}"),
    MessagesPlaceholder("history"),
    ("user", "{question}")
]
```

## 📊 Performance Features

- **Deduplication**: MD5 checksums prevent duplicate uploads
- **Text Chunking**: Efficient processing of large documents
- **Vector Search**: Fast similarity search using ChromaDB
- **Session Isolation**: Multiple independent chat sessions
- **Streaming Responses**: Real-time response generation

## 🔐 Security Considerations

- API keys are stored in environment variables
- File uploads are limited to supported formats
- Input validation for text processing
- Secure session management

## 🚨 Troubleshooting

### Common Issues:

1. **Module Not Found**:
   - Ensure all dependencies are installed
   - Check virtual environment activation

2. **API Key Issues**:
   - Verify .env file configuration
   - Check API key validity

3. **ChromaDB Issues**:
   - Ensure persist directory exists
   - Check write permissions

4. **Memory Issues**:
   - Reduce chunk size for large files
   - Monitor memory usage during processing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is for educational and research purposes.

## 📞 Support

For questions or issues, please check the troubleshooting section or create an issue in the repository.

---

## 🇨🇳 中文说明

### 项目概述
这是一个基于Python的检索增强生成(RAG)系统，结合了知识库检索和大语言模型能力，用于智能问答。

### 主要特性
- **知识库管理**：支持文档上传，使用MD5校验和进行去重
- **向量存储**：使用ChromaDB进行高效的向量存储和相似性搜索
- **嵌入模型**：使用DashScope Embeddings生成高质量文本嵌入
- **LLM集成**：集成DeepSeek Chat模型进行响应生成
- **Streamlit界面**：用户友好的网页界面，支持问答和文件上传
- **会话管理**：使用会话ID跟踪对话历史
- **文档处理**：自动文本分割和分块处理

### 安装步骤
1. 克隆仓库
2. 创建并激活虚拟环境
3. 安装依赖包
4. 配置环境变量

### 使用方法
1. **问答界面**：运行`streamlit run app_qa.py`，在浏览器中访问`http://localhost:8501`
2. **文件上传**：运行`streamlit run app_file_uploader.py`上传文档到知识库
3. **命令行**：直接运行Python文件进行测试

### 技术架构
1. 文档处理：读取文件、提取文本、分块、生成嵌入
2. 向量存储：存储嵌入向量，支持相似性搜索
3. 问答系统：检索相关上下文，使用LLM生成回答
4. 会话管理：维护对话历史，支持多会话

### 配置说明
- 文件分块大小：1000字符
- 重叠大小：100字符
- 相似度阈值：2
- 支持的文件格式：.txt, .pdf, .docx, .md

### 性能优化
- MD5去重避免重复存储
- 文本分块提高处理效率
- 向量搜索实现快速检索
- 流式响应提升用户体验
- 会话隔离保证数据安全