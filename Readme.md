# Portfolio: Enterprise AI/ML/DL Systems & Modern Architecture

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Author](https://img.shields.io/badge/Author-Muhammad%20Ibrahim-orange.svg)](https://github.com/ibrahimuk111)

Welcome to the central repository for **Muhammad Ibrahim's** Data Science, Machine Learning ,Deep Learning, AI Engineering, and Systems Architecture portfolio. This repository serves as a comprehensive showcase of end-to-end production systems, spanning Generative AI, Large Language Models (LLMs), Agentic Systems, Full-Stack & Mobile AI Applications, AI Safety & Guardrails, MLOps Pipelines, Edge Computer Vision, and Privacy-Preserving Artificial Intelligence.

---

## 📂 Complete Repository Architecture

```
Ibrahim-s-Portfolio/
│
├── 📱 AI Mobile & FullStack Web Apps/
│   ├── AI_Powered_Flutter_Mobile_App/         # ExecuTorch/MediaPipe + Flutter + FastAPI
│   ├── Edge_Vision_Mobile_Scanner_App/        # ONNX Mobile Runtime offline scanner
│   ├── Enterprise_AI_SaaS_Dashboard/          # Multi-tenant auth, token metering, subscription API
│   └── FullStack_MultiModal_Agent_Web_App/    # Next.js React + Tailwind CSS + FastAPI
│
├── 🤖 AI Agents & Multi-Agent Systems/
│   ├── Autonomous_Code_Refactor_Agent/         # AST analysis + LLM-based refactoring
│   ├── Customer_Support_Swarm_Agents/          # Multi-agent domain router & swarm
│   ├── Multi_Agent_Research_Engine/           # LangGraph + Tavily + Streamlit
│   └── Multi_Modal_Assistant_Agent/            # Voice/Image + LangChain agent
│
├── 🛡️ AI Safety & Guardrails/
│   ├── Adversarial_Attack_Defense_CV/          # FGSM/PGD robustness benchmarks
│   ├── Enterprise_LLM_Guardrails_API/          # PII masking + Toxicity FastAPI
│   ├── RAG_Hallucination_Detector/             # Faithfulness & Answer Relevancy eval
│   └── XAI_Model_Interpretability_Dashboard/   # SHAP + LIME interpretability UI
│
├── ⚡ MLOps & LLMOps Pipelines/
│   ├── Automated_Data_Model_Drift_Monitor/      # KS-statistical drift monitoring
│   ├── End_To_End_CI_CD_ML_Pipeline/           # GitHub Actions + Docker + PyTest
│   ├── LLM_FineTuning_Quantization_Pipeline/  # QLoRA + GGUF quantization simulator
│   └── Vector_Database_Benchmarking_Engine/    # FAISS vs ChromaDB vs Pinecone QPS
│
├── 👁️ Edge AI & Vision Optimization/
│   ├── Edge_Video_Analytics_Pipeline/          # Action recognition & counting engine
│   ├── RealTime_LowLatency_YOLOv10_Tracker/     # Sub-10ms ONNX / TensorRT tracking
│   ├── Underwater_Visual_Enhancement_Detector/ # Dehazing & domain adaptation
│   └── Vision_Language_Model_Video_Summarizer/ # Qwen2-VL / LLaVA video log summary
│
├── 🔒 Privacy Preserving AI/
│   ├── Differential_Privacy_ML_Classifier/      # Opacus PyTorch private training
│   ├── Federated_Learning_Intrusion_Detection/  # Flower framework CAN bus security
│   ├── Homomorphic_Encryption_Inference_Engine/ # TenSEAL encrypted neural net infer
│   └── Secure_MultiParty_Computation_Analytics/# Secret sharing analytics
│
├── 🧠 LLM Projects/
│   ├── Chain-of-Thought & Self-Consistency/     # Reasoning chain prompting
│   ├── Code Generation with Llama/            # Code synthesis pipelines
│   ├── Conversational Memory with Summarization/ # Dynamic context summarization
│   ├── Fine-tune FLAN-T5 on Instruction Data/  # PEFT instruction tuning
│   ├── FineTuned_Medical_Legal_Specialist_LLM/ # Unsloth + QLoRA + GGUF export
│   ├── Function Calling Tool Use with Llama 3.1/# Tool execution & JSON output
│   ├── GraphRAG_KnowledgeGraph_Engine/        # Neo4j + LangChain Knowledge Graph RAG
│   ├── LLM as a Judge - Automated Evaluation/  # Automated LLM response scoring
│   ├── Local_vLLM_Inference_Server/            # vLLM PagedAttention streaming server
│   ├── ReAct Agent (Reasoning + Acting)/        # Autonomous tool agent loops
│   ├── Self-Ask with Web Search/               # Search augmented reasoning
│   ├── Semantic Search & Re-ranking/           # Cross-encoder dense search
│   ├── Structured Output Extraction/           # JSON schema enforcement
│   └── Text-to-SQL with Llama/                 # Text-to-SQL translation engine
│
├── 🎯 RAG Projects/
│   ├── Agentic RAG with LangGraph/             # Self-corrective agent RAG
│   ├── Enterprise_MultiDoc_Copilot/            # PDF/Excel parent-child citation copilot
│   ├── Multi-Modal RAG - Text + Image/          # Multimodal vision vector retrieval
│   ├── Multi_RAG_Router_Agent/                 # LlamaIndex multi-index query router
│   ├── RAG Evaluation Pipeline with RAGAS/     # Metrics score evaluation
│   ├── The Core Memory Bank (PDF Document Q&A)/ # Vector doc memory bank
│   ├── The Financial Analyst - NL to SQL/      # Financial RAG & SQL generation
│   └── The YouTube Summarizer & Study Buddy/   # Video transcript Q&A assistant
│
├── 👁️ Computer Vision Projects/
│   ├── AI Super-Resolution and Image Restoration/# ESRGAN image restoration
│   ├── Anomaly Detection in Industrial Inspection/# Unsupervised anomaly detection
│   ├── Automatic Number Plate Recognition/     # ANPR YOLOv8 + OCR pipeline
│   ├── Blinking and Drowsiness Detection/      # Eye aspect ratio safety detection
│   ├── Blood Cell Cancer Detection/            # Medical microscopic image classification
│   ├── Brain Tumor Detection/                  # MRI segmentation & classification
│   ├── Car Detection using Drone/              # Aerial object detection
│   ├── Deep Fake Video Detection/              # Spatial-temporal deepfake detection
│   ├── Digital Image Tampering Detection/      # Error Level Analysis forensics
│   ├── Eye Diseases Detection/                 # Retinal pathology classification
│   ├── Face Liveness Detection System/         # Anti-spoofing liveness verification
│   ├── Facial Emotion Recognition/             # Expression classification CNN
│   ├── Fire Detection YOLOv8/                  # Real-time hazard detection
│   ├── Image Captioning/                       # Encoder-Decoder caption generator
│   ├── Lung Cancer Detection/                  # Chest CT scan classifier
│   ├── Multi_Camera_Object_Counting_App/       # YOLOv8 + DeepSORT virtual line counter
│   ├── Self Driving Car/                       # Lane detection & steering control
│   └── VLM_Video_QA_Summarizer/                # Qwen2-VL video scene QA
│
├── 🔤 Advanced NLP Projects/
│   ├── Advanced_Human_vs_AI_Text_Classifier/    # BERT AI text detection
│   ├── Advanced_Mental_Health_Sentiment/       # Deep text sentiment profiling
│   ├── Advanced_Resume_Screening_System/        # Resume NER & skill matching
│   ├── Advanced_Text_Origin_Classifier_NLP/    # Stylometric text origin classifier
│   ├── Custom_NER_Relation_Extraction_Pipeline/# spaCy / PyTorch entity relation extraction
│   ├── Fact vs. Fabrication - Disinformation/  # Fake news detection pipeline
│   ├── Financial_News_Sentiment_Classification/ # Financial BERT sentiment model
│   ├── Identity Shield - Threat Moderator/     # Multilingual toxic comment filter
│   ├── Instruction Hierarchy Classifier/        # Prompt injection classifier
│   ├── Jigsaw Toxic Comment Classifier/        # Multi-label toxicity classification
│   ├── Multilingual_Translation_Summarization/ # Hugging Face translation pipeline
│   ├── Named Entity Recognition with BERT/     # BERT Token Classification
│   └── PubMedQA - Biomedical Question Answering/# Medical NLP QA engine
│
├── 📊 Data Analysis Projects/
│   ├── Airbnb Price Analysis (NYC 2019)/       # Spatial price regression & EDA
│   ├── AutoML_Feature_Engineering_Engine/     # Optuna + LightGBM AutoML pipeline
│   ├── Bank Marketing Campaign Analysis/        # Classification & deposit prediction
│   ├── COVID-19 Global Trends Analysis/        # Geospatial & time-series analysis
│   ├── Customer Churn Prediction & Analysis/    # SMOTE imbalance modeling & SHAP
│   ├── Customer Shopping Trends & Basket/      # Apriori market basket analysis
│   ├── E-commerce Sales Analysis (RFM)/        # Customer lifetime value & RFM segmentation
│   ├── Global Superstore Sales Analysis/       # Enterprise revenue profiling
│   ├── HR Analytics - Employee Attrition/      # Employee retention modeling
│   ├── Movie Industry Analysis (TMDB 5000)/    # Revenue & rating regression
│   ├── Time_Series_Predictive_Analytics_Dashboard/# Prophet forecasting Streamlit UI
│   ├── US Accidents Analysis (2016-2023)/      # Big data traffic accident profiling
│   └── Wine Quality Prediction/                # Physicochemical property classification
│
├── 🔗 LangChain Projects/
│   ├── Audio To Text Transcription/            # Whisper audio transcription chain
│   ├── Basic PDF QA/                           # Document loader QA chain
│   ├── Blog Generation/                        # Automated blog writing agent
│   ├── Calories Health Advisor/                # Multimodal food calorie estimation
│   ├── Chat With Multiple Documents/           # Multi-file retrieval chain
│   ├── Codebasics FAQ Chatbot/                 # Domain FAQ retrieval bot
│   ├── Conversational Q&A Chatbot/             # Buffer memory chatbot
│   ├── Invoice Data Extractor/                 # Structured document extraction
│   ├── LLM Generic App/                        # Flexible prompt pipeline
│   ├── News Research Tool/                     # Article search & Q&A
│   ├── Q&A Chatbot Using LLM/                  # Basic LLM QA chain
│   ├── SQL Database QA/                        # Text-to-SQL LangChain agent
│   ├── Text Summarization/                     # Map-Reduce summarization
│   ├── Web Page Summarization/                 # URL content summarizer
│   └── WordPress Code Assistant/              # Code generation assistant
│
└── ⚙️ Machine Learning Projects/
    ├── Bank Customer Churn Prediction/         # Churn classification model
    ├── Credit Card Fraud Detection/            # Highly imbalanced anomaly detection
    ├── House Price Prediction (Regression)/    # XGBoost regression engine
    └── Predictive Maintenance Classification/  # Machine failure sensor classification
```

---

## 📂 Domain Overview and Project Directory

### 1. AI Mobile & FullStack Web Apps
Cross-platform mobile applications, full-stack AI SaaS dashboards, and multi-modal web clients powered by ExecuTorch, ONNX Mobile, Flutter, and Next.js/FastAPI.
* [AI_Powered_Flutter_Mobile_App](./AI%20Mobile%20%26%20FullStack%20Web%20Apps/AI_Powered_Flutter_Mobile_App)
* [Edge_Vision_Mobile_Scanner_App](./AI%20Mobile%20%26%20FullStack%20Web%20Apps/Edge_Vision_Mobile_Scanner_App)
* [Enterprise_AI_SaaS_Dashboard](./AI%20Mobile%20%26%20FullStack%20Web%20Apps/Enterprise_AI_SaaS_Dashboard)
* [FullStack_MultiModal_Agent_Web_App](./AI%20Mobile%20%26%20FullStack%20Web%20Apps/FullStack_MultiModal_Agent_Web_App)

### 2. AI Agents & Multi-Agent Systems
Multi-agent orchestration, swarm intelligence routers, autonomous code refactoring tools, and multi-modal assistants using LangGraph, Tavily, and LangChain.
* [Autonomous_Code_Refactor_Agent](./AI%20Agents%20%26%20Multi-Agent%20Systems/Autonomous_Code_Refactor_Agent)
* [Customer_Support_Swarm_Agents](./AI%20Agents%20%26%20Multi-Agent%20Systems/Customer_Support_Swarm_Agents)
* [Multi_Agent_Research_Engine](./AI%20Agents%20%26%20Multi-Agent%20Systems/Multi_Agent_Research_Engine)
* [Multi_Modal_Assistant_Agent](./AI%20Agents%20%26%20Multi-Agent%20Systems/Multi_Modal_Assistant_Agent)

### 3. AI Safety & Guardrails
Enterprise safety mechanisms, toxicity and PII masking APIs, RAG hallucination detectors, computer vision adversarial defense, and XAI interpretability dashboards.
* [Adversarial_Attack_Defense_CV](./AI%20Safety%20%26%20Guardrails/Adversarial_Attack_Defense_CV)
* [Enterprise_LLM_Guardrails_API](./AI%20Safety%20%26%20Guardrails/Enterprise_LLM_Guardrails_API)
* [RAG_Hallucination_Detector](./AI%20Safety%20%26%20Guardrails/RAG_Hallucination_Detector)
* [XAI_Model_Interpretability_Dashboard](./AI%20Safety%20%26%20Guardrails/XAI_Model_Interpretability_Dashboard)

### 4. MLOps & LLMOps Pipelines
Continuous delivery and monitoring infrastructure for ML models, automated data/model drift detection, fine-tuning/quantization pipelines, and vector database benchmarking.
* [Automated_Data_Model_Drift_Monitor](./MLOps%20%26%20LLMOps%20Pipelines/Automated_Data_Model_Drift_Monitor)
* [End_To_End_CI_CD_ML_Pipeline](./MLOps%20%26%20LLMOps%20Pipelines/End_To_End_CI_CD_ML_Pipeline)
* [LLM_FineTuning_Quantization_Pipeline](./MLOps%20%26%20LLMOps%20Pipelines/LLM_FineTuning_Quantization_Pipeline)
* [Vector_Database_Benchmarking_Engine](./MLOps%20%26%20LLMOps%20Pipelines/Vector_Database_Benchmarking_Engine)

### 5. Edge AI & Vision Optimization
Low-latency edge vision analytics, sub-10ms real-time object tracking with ONNX/TensorRT, underwater video enhancement, and VLM video summarization.
* [Edge_Video_Analytics_Pipeline](./Edge%20AI%20%26%20Vision%20Optimization/Edge_Video_Analytics_Pipeline)
* [RealTime_LowLatency_YOLOv10_Tracker](./Edge%20AI%20%26%20Vision%20Optimization/RealTime_LowLatency_YOLOv10_Tracker)
* [Underwater_Visual_Enhancement_Detector](./Edge%20AI%20%26%20Vision%20Optimization/Underwater_Visual_Enhancement_Detector)
* [Vision_Language_Model_Video_Summarizer](./Edge%20AI%20%26%20Vision%20Optimization/Vision_Language_Model_Video_Summarizer)

### 6. Privacy Preserving AI
Privacy-enhancing machine learning algorithms including differential privacy with Opacus, federated learning with Flower, homomorphic encryption via TenSEAL, and secure multi-party computation.
* [Differential_Privacy_ML_Classifier](./Privacy%20Preserving%20AI/Differential_Privacy_ML_Classifier)
* [Federated_Learning_Intrusion_Detection](./Privacy%20Preserving%20AI/Federated_Learning_Intrusion_Detection)
* [Homomorphic_Encryption_Inference_Engine](./Privacy%20Preserving%20AI/Homomorphic_Encryption_Inference_Engine)
* [Secure_MultiParty_Computation_Analytics](./Privacy%20Preserving%20AI/Secure_MultiParty_Computation_Analytics)

### 7. LLM Projects
Advanced Large Language Model applications covering prompt engineering, fine-tuning (PEFT/QLoRA), vLLM inference hosting, GraphRAG knowledge graphs, code generation, and automated evaluation.
* [Chain-of-Thought & Self-Consistency](./LLM%20Projects/Chain-of-Thought%20%26%20Self-Consistency)
* [Code Generation with Llama](./LLM%20Projects/Code%20Generation%20with%20Llama)
* [Conversational Memory with Summarization](./LLM%20Projects/Conversational%20Memory%20with%20Summarization)
* [Fine-tune FLAN-T5 on Instruction Data](./LLM%20Projects/Fine-tune%20FLAN-T5%20on%20Instruction%20Data)
* [FineTuned_Medical_Legal_Specialist_LLM](./LLM%20Projects/FineTuned_Medical_Legal_Specialist_LLM)
* [Function Calling  Tool Use with Llama 3.1](./LLM%20Projects/Function%20Calling%20%20Tool%20Use%20with%20Llama%203.1)
* [GraphRAG_KnowledgeGraph_Engine](./LLM%20Projects/GraphRAG_KnowledgeGraph_Engine)
* [LLM as a Judge - Automated Evaluation of Responses](./LLM%20Projects/LLM%20as%20a%20Judge%20-%20Automated%20Evaluation%20of%20Responses)
* [Local_vLLM_Inference_Server](./LLM%20Projects/Local_vLLM_Inference_Server)
* [ReAct Agent (Reasoning + Acting)](./LLM%20Projects/ReAct%20Agent%20%28Reasoning%20%2B%20Acting%29)
* [Self-Ask with Web Search](./LLM%20Projects/Self-Ask%20with%20Web%20Search)
* [Semantic Search & Re-ranking with Embeddings](./LLM%20Projects/Semantic%20Search%20%26%20Re-ranking%20with%20Embeddings)
* [Structured Output Extraction](./LLM%20Projects/Structured%20Output%20Extraction)
* [Text-to-SQL with Llama](./LLM%20Projects/Text-to-SQL%20with%20Llama)

### 8. RAG Projects
Retrieval-Augmented Generation architectures including agentic RAG, multi-document enterprise copilot, multimodal retrieval, multi-index query routing, and RAGAS evaluation framework.
* [Agentic RAG with LangGraph](./RAG%20Projects/Agentic%20RAG%20with%20LangGraph)
* [Enterprise_MultiDoc_Copilot](./RAG%20Projects/Enterprise_MultiDoc_Copilot)
* [Multi-Modal RAG - Text + Image Understanding](./RAG%20Projects/Multi-Modal%20RAG%20-%20Text%20%2B%20Image%20Understanding)
* [Multi_RAG_Router_Agent](./RAG%20Projects/Multi_RAG_Router_Agent)
* [RAG Evaluation Pipeline with RAGAS](./RAG%20Projects/RAG%20Evaluation%20Pipeline%20with%20RAGAS)
* [The Core Memory Bank (PDF Document Q&A)](./RAG%20Projects/The%20Core%20Memory%20Bank%20%28PDF%20Document%20Q%26A%29)
* [The Financial Analyst - Natural Language to SQL with LLM](./RAG%20Projects/The%20Financial%20Analyst%20-%20Natural%20Language%20to%20SQL%20with%20LLM)
* [The YouTube Summarizer & Study Buddy](./RAG%20Projects/The%20YouTube%20Summarizer%20%26%20Study%20Buddy)

### 9. Computer Vision Projects
Deep learning models for spatial analysis, object detection (YOLOv8/v10), medical imaging diagnostics, face liveness verification, super-resolution, and visual inspection.
* [AI Super-Resolution and Image Restoration](./Computer%20Vision%20Projects/AI%20Super-Resolution%20and%20Image%20Restoration)
* [Anomaly Detection in Industrial Inspection](./Computer%20Vision%20Projects/Anomaly%20Detection%20in%20Industrial%20Inspection)
* [Automatic Number Plate Recognition](./Computer%20Vision%20Projects/Automatic%20Number%20Plate%20Recognition)
* [Blinking and Drowsiness Detection](./Computer%20Vision%20Projects/Blinking%20and%20Drowsiness%20Detection)
* [Blood Cell Cancer Detection](./Computer%20Vision%20Projects/Blood%20Cell%20Cancer%20Detection)
* [Brain Tumor Detection](./Computer%20Vision%20Projects/Brain%20Tumor%20Detection)
* [Car Detection using Drone](./Computer%20Vision%20Projects/Car%20Detection%20using%20Drone)
* [Deep Fake Video Detection](./Computer%20Vision%20Projects/Deep%20Fake%20Video%20Detection)
* [Digital Image Tampering Detection](./Computer%20Vision%20Projects/Digital%20Image%20Tampering%20Detection)
* [Eye Diseases Detection](./Computer%20Vision%20Projects/Eye%20Diseases%20Detection)
* [Face Liveness Detection System](./Computer%20Vision%20Projects/Face%20Liveness%20Detection%20System)
* [Facial Emotion Recognition](./Computer%20Vision%20Projects/Facial%20Emotion%20Recognition)
* [Fire Detection YOLOv8](./Computer%20Vision%20Projects/Fire%20Detection%20YOLOv8)
* [Image Captioning](./Computer%20Vision%20Projects/Image%20Captioning)
* [Lung Cancer Detection](./Computer%20Vision%20Projects/Lung%20Cancer%20Detection)
* [Multi_Camera_Object_Counting_App](./Computer%20Vision%20Projects/Multi_Camera_Object_Counting_App)
* [Self Driving Car](./Computer%20Vision%20Projects/Self%20Driving%20Car)
* [VLM_Video_QA_Summarizer](./Computer%20Vision%20Projects/VLM_Video_QA_Summarizer)

### 10. Advanced NLP Projects
Natural Language Processing pipelines including transformer-based NER, text classification, sentiment analysis, toxic comment moderation, and disinformation detection.
* [Advanced_Human_vs_AI_Text_Classifier_using_NLP_and_BERT](./Advanced%20NLP%20Projects/Advanced_Human_vs_AI_Text_Classifier_using_NLP_and_BERT)
* [Advanced_Mental_Health_Sentiment_Analysis_NLP_Project](./Advanced%20NLP%20Projects/Advanced_Mental_Health_Sentiment_Analysis_NLP_Project)
* [Advanced_Resume_Screening_System_using_NLP_and_ML](./Advanced%20NLP%20Projects/Advanced_Resume_Screening_System_using_NLP_and_ML)
* [Advanced_Text_Origin_Classifier_NLP](./Advanced%20NLP%20Projects/Advanced_Text_Origin_Classifier_NLP)
* [Custom_NER_Relation_Extraction_Pipeline](./Advanced%20NLP%20Projects/Custom_NER_Relation_Extraction_Pipeline)
* [Fact vs. Fabrication - Multi-Genre Disinformation Detector](./Advanced%20NLP%20Projects/Fact%20vs.%20Fabrication%20-%20Multi-Genre%20Disinformation%20Detector)
* [Financial_News_Sentiment_Classification_using_NLP_and_ML](./Advanced%20NLP%20Projects/Financial_News_Sentiment_Classification_using_NLP_and_ML)
* [Identity Shield - Multilingual Hate Speech & Threat Moderator](./Advanced%20NLP%20Projects/Identity%20Shield%20-%20Multilingual%20Hate%20Speech%20%26%20Threat%20Moderator)
* [Instruction Hierarchy (Prompt Injection) Classifier](./Advanced%20NLP%20Projects/Instruction%20Hierarchy%20%28Prompt%20Injection%29%20Classifier)
* [Jigsaw Toxic Comment Classifier](./Advanced%20NLP%20Projects/Jigsaw%20Toxic%20Comment%20Classifier)
* [Multilingual_Translation_Summarization_Engine](./Advanced%20NLP%20Projects/Multilingual_Translation_Summarization_Engine)
* [Named Entity Recognition (NER) with Transformer (BERT)](./Advanced%20NLP%20Projects/Named%20Entity%20Recognition%20%28NER%29%20with%20Transformer%20%28BERT%29)
* [PubMedQA - Biomedical Question Answering](./Advanced%20NLP%20Projects/PubMedQA%20-%20Biomedical%20Question%20Answering)

### 11. Data Analysis Projects
Exploratory data analysis, statistical modeling, RFM customer segmentation, time-series forecasting, and AutoML feature engineering pipelines.
* [Airbnb Price Analysis (NYC 2019)](./Data%20Analysis%20Projects/Airbnb%20Price%20Analysis%20%28NYC%202019%29)
* [AutoML_Feature_Engineering_Engine](./Data%20Analysis%20Projects/AutoML_Feature_Engineering_Engine)
* [Bank Marketing Campaign Analysis - Predicting Term Deposit Subscription](./Data%20Analysis%20Projects/Bank%20Marketing%20Campaign%20Analysis%20-%20Predicting%20Term%20Deposit%20Subscription)
* [COVID-19 Global Trends Analysis (Time Series & Geospatial)](./Data%20Analysis%20Projects/COVID-19%20Global%20Trends%20Analysis%20%28Time%20Series%20%26%20Geospatial%29)
* [Customer Churn Prediction & Exploratory Analysis](./Data%20Analysis%20Projects/Customer%20Churn%20Prediction%20%26%20Exploratory%20Analysis)
* [Customer Shopping Trends & Basket Analysis](./Data%20Analysis%20Projects/Customer%20Shopping%20Trends%20%26%20Basket%20Analysis)
* [E-commerce Sales Analysis (RFM Segmentation & CLV)](./Data%20Analysis%20Projects/E-commerce%20Sales%20Analysis%20%28RFM%20Segmentation%20%26%20CLV%29)
* [Global Superstore Sales Analysis](./Data%20Analysis%20Projects/Global%20Superstore%20Sales%20Analysis)
* [HR Analytics - Employee Attrition & Performance](./Data%20Analysis%20Projects/HR%20Analytics%20-%20Employee%20Attrition%20%26%20Performance)
* [Movie Industry Analysis (TMDB 5000 Movie Dataset)](./Data%20Analysis%20Projects/Movie%20Industry%20Analysis%20%28TMDB%205000%20Movie%20Dataset%29)
* [Time_Series_Predictive_Analytics_Dashboard](./Data%20Analysis%20Projects/Time_Series_Predictive_Analytics_Dashboard)
* [US Accidents Analysis (2016-2023)](./Data%20Analysis%20Projects/US%20Accidents%20Analysis%20%282016-2023%29)
* [Wine Quality Prediction - EDA & Classification](./Data%20Analysis%20Projects/Wine%20Quality%20Prediction%20-%20EDA%20%26%20Classification)

### 12. LangChain Projects
Modular LLM workflows and chain orchestration for document Q&A, audio transcription, automated content generation, database querying, and code assistance.
* [Audio To Text Transcription](./LangChain%20Projects/Audio%20To%20Text%20Transcription)
* [Basic PDF QA](./LangChain%20Projects/Basic%20PDF%20QA)
* [Blog Generation](./LangChain%20Projects/Blog%20Generation)
* [Calories Health Advisor](./LangChain%20Projects/Calories%20Health%20Advisor)
* [Chat With Multiple Documents](./LangChain%20Projects/Chat%20With%20Multiple%20Documents)
* [Codebasics FAQ Chatbot](./LangChain%20Projects/Codebasics%20FAQ%20Chatbot)
* [Conversational Q&A Chatbot](./LangChain%20Projects/Conversational%20Q%26A%20Chatbot)
* [Invoice Data Extractor](./LangChain%20Projects/Invoice%20Data%20Extractor)
* [LLM Generic App](./LangChain%20Projects/LLM%20Generic%20App)
* [News Research Tool](./LangChain%20Projects/News%20Research%20Tool)
* [Q&A Chatbot Using LLM](./LangChain%20Projects/Q%26A%20Chatbot%20Using%20LLM)
* [SQL Database QA](./LangChain%20Projects/SQL%20Database%20QA)
* [Text Summarization](./LangChain%20Projects/Text%20Summarization)
* [Web Page Summarization](./LangChain%20Projects/Web%20Page%20Summarization)
* [WordPress Code Assistant](./LangChain%20Projects/WordPress%20Code%20Assistant)

### 13. Machine Learning Projects
Predictive modeling, anomaly detection, regression, and classification algorithms for enterprise business applications.
* [Bank Customer Churn Prediction](./Machine%20Learning%20Projects/Bank%20Customer%20Churn%20Prediction)
* [Credit Card Fraud Detection](./Machine%20Learning%20Projects/Credit%20Card%20Fraud%20Detection)
* [House Price Prediction (Regression)](./Machine%20Learning%20Projects/House%20Price%20Prediction%20%28Regression%29)
* [Predictive Maintenance - Machine Failure Classification](./Machine%20Learning%20Projects/Predictive%20Maintenance%20-%20Machine%20Failure%20Classification)

---

## 🛠️ Global Tech Stack

- **Frontend & Mobile:** Flutter (Dart), Next.js, React, Tailwind CSS, Streamlit
- **Backend & Web APIs:** FastAPI, Pydantic, Uvicorn, Python (3.11+)
- **Generative AI & LLMs:** LangChain, LangGraph, LlamaIndex, Unsloth, QLoRA, vLLM, Neo4j GraphRAG, OpenAI API, Ollama
- **Computer Vision & VLM:** OpenCV, YOLOv8 / YOLOv10, ONNX Runtime, TensorRT, DeepSORT, Qwen2-VL, LLaVA
- **AI Safety & MLOps:** NeMo Guardrails, RAGAS, SHAP, LIME, Optuna, Docker, GitHub Actions, PyTest, MLflow, Evidently AI
- **Privacy & Security:** Flower (Federated Learning), Opacus (Differential Privacy), TenSEAL (Homomorphic Encryption)

---

## 📬 Author & Licensing

**Author:** Muhammad Ibrahim  
💼 **LinkedIn:** [linkedin.com/in/muhammadibrahimds](https://www.linkedin.com/in/muhammadibrahimds)  
🧑‍💻 **GitHub:** [github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
📧 **Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  

**License:** Copyright (c) 2026 Muhammad Ibrahim. All code and documentation in this repository are distributed under the MIT License.
