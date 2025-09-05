import streamlit as st

st.set_page_config(page_title="Mohamed El Shrbeny Portfolio", layout="wide")

# ---------- CSS for animation and background ----------
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #f0f0f0, #e0e0ff);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Arial', sans-serif;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.project-card {
    border-radius: 15px;
    padding: 20px;
    margin: 10px;
    box-shadow: 3px 3px 10px #aaa;
    transition: transform 0.3s;
    background-color: white;
}
.project-card:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<h1 style='text-align:center; color:#333;'>Mohamed El Shrbeny 👋</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#555;'>Machine Learning & Computer Vision Engineer</h3>", unsafe_allow_html=True)

# ---------- About Me ----------
st.markdown("""
### About Me
I am a Machine Learning Engineer specializing in Python and PyTorch, with expertise in:
- Computer Vision: Classification, Image Processing, Segmentation, Object Detection, OCR
- LLMs: Evaluation, Fine-tuning (SFT, RLHF), RAG, Agents, Vector Databases
- Deployment: FastAPI, Docker, Kubernetes
- Databases: PostgreSQL

📝 Check out my articles: [DeepLearning4ComputerVision](https://deeplearning4computervision.blogspot.com/)
""")

# ---------- Projects ----------
st.markdown("### 💼 Projects")
projects = [
    {
        "name": "Recommender System",
        "desc": "LLM + RAG project for personalized recommendations.",
        "link": "https://github.com/mahmedahmed3355/recommandsystem2",
        "img": "https://media.giphy.com/media/l0HlQ7LRalrMPmO8c/giphy.gif"
    },
    {
        "name": "Medical Imaging Diagnosis Agent",
        "desc": "Analyze medical images using AI agents.",
        "link": "https://github.com/mahmedahmed3355/medical_imaging_agent",
        "img": "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif"
    },
]

for p in projects:
    st.markdown(f"""
    <div class="project-card">
    <h4>{p['name']}</h4>
    <p>{p['desc']}</p>
    <img src="{p['img']}" width="300">
    <br><a href="{p['link']}" target="_blank">View on GitHub</a>
    </div>
    """, unsafe_allow_html=True)

# ---------- Skills ----------
st.markdown("### 🛠 Skills & Tools")
skills = [
    "Python", "PyTorch", "OpenCV", "TensorFlow", "Scikit-Learn",
    "LangChain", "LangGraph", "LangSmith", "FastAPI",
    "Docker", "Kubernetes", "PostgreSQL", "Git", "Flask", "Streamlit"
]
st.markdown(", ".join(skills))

# ---------- Contact ----------
st.markdown("### 📫 Connect with Me")
st.markdown("""
- [GitHub](https://github.com/mahmedahmed3355)
- [LinkedIn](https://www.linkedin.com/in/mohamed-ahmed-700019a5/)
- Email: mohamed_ahmed_335588@hotmail.com
- Email: engmohamedelshrbeny@gmail.com
""")
