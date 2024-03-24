import threading
import time
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Emirhan Metin"
PAGE_ICON = ":wave:"
NAME = "Emirhan Metin"
DESCRIPTION = """
DevOps Engineer
"""
EMAIL = "metinemirhan6@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/emirhan-metin-171856234/",
    "GitHub": "https://github.com/ArgoFox1",
    "CVwebsite": "https://emirhanmetincv.onrender.com/",
}
PROJECTS = {
    "🏆 Docker-K8S-JavaApp": "https://github.com/ArgoFox1/Docker-K8S-JavaApp",
    "🏆 Docker-K8S-NativeMonitoring-App": "https://github.com/ArgoFox1/Docker-K8S-NativeMonitoring-App",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 1 year interested in DevOps Engineering
- ✔️ Strong Knowledge on Docker, Kubernetes, Shell & Bash Scripting, AWS
- ✔️ Strong Knowledge on configuring and troubleshooting of server applications on Kubernetes and Docker
- ✔️ Good understanding of CI/CD principles with Jenkins
- ✔️ Knowledge of SQL
- ✔️ Knowledge of Logging, Monitoring, Tracing tools such as Grafana, Prometheus, EKS, Kibana, Docker Metrics
- ✔️ Excellent team-player and displaying a strong sense of initiative on tasks
- ✔️ Excellent Troubleshooting
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 💪Docker
- 💪Kubernetes
- 💪BashScripting & ShellScripting
- 💪AWS
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Transcriptionist | FutveTechnology**")
st.write("06/2020 - 12/2020")

# --- CERTS ---
st.write('\n')
st.subheader("Certificates")
st.write(
    """
- **DOCKER**  - [Certificate Link](https://www.udemy.com/certificate/UC-436e05a0-76ac-4b34-88fd-add42fb6dcf9/)
- **KUBERNETES** - [Certificate Link](https://www.udemy.com/certificate/UC-8cdb6290-6a7e-4a83-bfae-7f846c31c81c/)
- **AWS** - [Certificate Link](https://www.udemy.com/certificate/UC-31ac714c-3fd3-4f66-8f50-88a065bdaeb2/)
- **Linux101** - [Certificate Link](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fgelecegiyazanlar.turkcell.com.tr%2Fcertificate%2FdWlkMjk5OTY4Y2lkMzUycWlkOTdlbmQ)
- **Linux201** - [Certificate Link](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fgelecegiyazanlar.turkcell.com.tr%2Fcertificate%2FdWlkMjk5OTY4Y2lkMzUzcWlkOThlbmQ)
- **Linux301** - [Certificate Link](https://www.linkedin.com/sharing/share-offsite/?url=https://gelecegiyazanlar.turkcell.com.tr/certificate/dWlkMjk5OTY4Y2lkMzU0cWlkOTllbmQ)
- **Linux401** - [Certificate Link](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fgelecegiyazanlar.turkcell.com.tr%2Fcertificate%2FdWlkMjk5OTY4Y2lkMzU1cWlkMTAwZW5k)
- **SQL** - [Certificate Link](https://drive.google.com/file/d/1Yvbxj4wfQTy2rF_4zydIhXLXVRJvEkNN/view)
- **TSQL** - [Certificate Link](https://drive.google.com/file/d/1kD-gIU1Vt3lfB9bXXE3Qd6V_XLBD5yQr/view)
- **Database Security** - [Certificate Link](https://drive.google.com/file/d/1-zvQiAtknRbe7YTGmvKTCYuZbARjpWy_/view)

"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Background Thread to Keep Application Active ---
def keep_alive():
    while True:
        print("Uygulama aktif tutuluyor...")
        time.sleep(840)  # 14 dakika bekleyin (14 dakika = 840 saniye)

# Arka planda keep_alive fonksiyonunu çalıştır
thread = threading.Thread(target=keep_alive)
thread.start()
