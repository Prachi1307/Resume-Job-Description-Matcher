import streamlit as st
from resume_parser import extract_text
from matcher import analyze
from styles import inject_css, badge_row
from gauge import match_gauge

st.set_page_config(page_title="Signal Match — Resume ↔ JD", page_icon="🎯", layout="wide")
inject_css()

SAMPLE_RESUME = (
    "Final year B.Tech Computer Science student skilled in Python, SQL, Pandas, "
    "Scikit-learn, Streamlit and Power BI. Built IoT projects using Arduino. "
    "Strong foundation in data structures, algorithms, and problem solving. "
    "Experience with Git and GitHub, and REST API integration."
)
SAMPLE_JD = (
    "Looking for a Data Analyst Intern with strong Python and SQL skills, hands-on "
    "experience with Pandas and data visualization tools like Power BI or Tableau. "
    "Familiarity with machine learning, AWS, and Docker is a plus. Good communication "
    "and problem solving skills required."
)

st.markdown("<div class='hero-eyebrow'>RESUME · JOB DESCRIPTION · SIGNAL CHECK</div>", unsafe_allow_html=True)
st.markdown("<h1 class='hero-title'>Are you tuned to this job?</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-sub'>Upload your resume, paste the job description, and see exactly where the signal is strong — and where it drops out.</p>", unsafe_allow_html=True)
st.write("")

if "resume_text_input" not in st.session_state:
    st.session_state.resume_text_input = ""
if "jd_text_input" not in st.session_state:
    st.session_state.jd_text_input = ""

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
    st.markdown("**📄 Your Resume**")
    resume_file = st.file_uploader("Upload PDF, DOCX, or TXT", type=["pdf", "docx", "txt"], label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
    st.markdown("**📋 Target Job Description**")
    jd_text = st.text_area("Paste the JD", height=180, key="jd_area",
                            value=st.session_state.jd_text_input, label_visibility="collapsed",
                            placeholder="Paste the full job description here...")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")
btn_col1, btn_col2, btn_col3 = st.columns([2, 1, 2])
with btn_col2:
    if st.button("🎲 Try a sample", use_container_width=True):
        st.session_state.jd_text_input = SAMPLE_JD
        st.session_state.use_sample_resume = True
        st.rerun()

analyze_clicked = st.button("⚡ Check the Signal", type="primary", use_container_width=True)

if analyze_clicked:
    resume_text = None
    if st.session_state.get("use_sample_resume") and not resume_file:
        resume_text = SAMPLE_RESUME
    elif resume_file:
        resume_text = extract_text(resume_file)

    if not resume_text:
        st.error("Upload a resume file, or hit 'Try a sample' above.")
    elif not jd_text.strip():
        st.error("Paste a job description first.")
    else:
        with st.spinner("Scanning resume against job signal..."):
            result = analyze(resume_text, jd_text)

        st.divider()
        score = result["score"]

        gauge_col, verdict_col = st.columns([1, 1])
        with gauge_col:
            st.plotly_chart(match_gauge(score), use_container_width=True)
        with verdict_col:
            st.write("")
            st.write("")
            if score >= 70:
                st.markdown("<p class='verdict-strong'>STRONG SIGNAL</p>", unsafe_allow_html=True)
                st.write("Your resume lines up well with this role. Minor tailoring at most.")
            elif score >= 45:
                st.markdown("<p class='verdict-moderate'>MODERATE SIGNAL</p>", unsafe_allow_html=True)
                st.write("Decent overlap, but a few gaps below are worth closing.")
            else:
                st.markdown("<p class='verdict-low'>WEAK SIGNAL</p>", unsafe_allow_html=True)
                st.write("This resume needs real tailoring before applying to this role.")

            k1, k2 = st.columns(2)
            k1.metric("Skills Matched", len(result["matched_skills"]))
            k2.metric("Skills Missing", len(result["missing_skills"]))

        st.write("")
        tab1, tab2, tab3 = st.tabs(["✅ Matched", "❌ Missing", "➕ Extra (not in JD)"])
        with tab1:
            badge_row(result["matched_skills"], "matched")
        with tab2:
            badge_row(result["missing_skills"], "missing")
            if result["missing_skills"]:
                st.caption("Only add these if you genuinely have them — you need to defend every line in an interview.")
        with tab3:
            badge_row(result["extra_skills"], "extra")
