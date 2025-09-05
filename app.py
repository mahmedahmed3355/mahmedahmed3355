import streamlit as st

# ---------- الصفحة الرئيسية ----------
st.set_page_config(page_title="Mohamed El Shrbeny Portfolio", layout="wide")

# ---------- Header ----------
st.title("Mohamed El Shrbeny 👋")
st.subheader("Machine Learning & Computer Vision Engineer")

# ---------- About Me ----------
st.markdown("""
🔭 **About Me**  
مهندس تعلم آلي ومطور رؤية حاسوبية متخصص في Python و PyTorch، عندي خبرة في:  
- Computer Vision: Classification, Image Processing, Segmentation, Object Detection, OCR  
- LLMs: Evaluation, Fine-tuning (SFT, RLHF), RAG, Agents, Vector Databases  
- Deployment: FastAPI, Docker, Kubernetes  
- Databases: PostgreSQL  

📝 I write articles on [DeepLearning4ComputerVision](https://deeplearning4computervision.blogspot.com/)
""")

# ---------- Projects ----------
st.header("💼 Projects")
projects = [
    {
        "name": "Recommender System",
        "desc": "LLM + RAG project for personalized recommendations.",
        "link": "https://github.com/mahmedahmed3355/recommandsystem2"
    },
    {
        "name": "Medical Imaging Diagnosis Agent",
        "desc": "Analyze medical images using AI agents.",
        "link": "https://github.com/mahmedahmed3355/medical_imaging_agent"
    },
    {
        "name": "PDF Scanner & OCR App",
        "desc": "Scan PDFs & IDs, extract text offline using Tesseract OCR.",
        "link": "https://github.com/mahmedahmed3355/pdf_scanner_ocr"
    },
    {
        "name": "AI Teaching Agent Team",
        "desc": "Multi-agent system for educational content creation in Google Docs.",
        "link": "https://github.com/mahmedahmed3355/ai_teaching_agent_team"
    },
    {
        "name": "AI Image Restoration Web App",
        "desc": "Denoising and restoring images using advanced CV models.",
        "link": "https://github.com/mahmedahmed3355/ai_image_restoration_app"
    },
]

for p in projects:
    st.markdown(f"**[{p['name']}]({p['link']})** - {p['desc']}")

# ---------- Skills ----------
st.header("🛠 Skills & Tools")
skills = [
    "Python", "PyTorch", "OpenCV", "TensorFlow", "Scikit-Learn",
    "LangChain", "LangGraph", "LangSmith", "FastAPI",
    "Docker", "Kubernetes", "PostgreSQL", "Git", "Flask", "Streamlit"
]
st.write(", ".join(skills))

# ---------- Contact ----------
st.header("📫 Connect with Me")
st.markdown("""
- [GitHub](https://github.com/mahmedahmed3355)
- [LinkedIn](https://www.linkedin.com/in/mohamed-ahmed-700019a5/)
- Email: mohamed_ahmed_335588@hotmail.com
- Email: engmohamedelshrbeny@gmail.com
""")
