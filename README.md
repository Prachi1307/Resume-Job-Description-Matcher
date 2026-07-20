Resume ↔ Job Description Matcher

A Streamlit app that scores how well a resume matches a job description, and shows exactly which skills are aligned and which are missing — built to help job seekers tailor their resumes before applying, not just guess.

✨ Features
📄 Resume upload — supports PDF, DOCX, and TXT
📋 Job description input — paste any JD as plain text
📊 Match score gauge — TF-IDF + cosine similarity, visualized as a live diagnostic gauge
✅ Skill gap breakdown — matched, missing, and extra skills, checked against a 60+ term technical and soft-skill taxonomy with strict word-boundary matching (no false positives like "R" matching inside "career")
🎲 Try a sample — instant demo with sample resume/JD text, no upload required
🎨 Custom themed UI — dark "signal match" interface, not default Streamlit styling

🖼️ Screenshot
<img width="1716" height="852" alt="image" src="https://github.com/user-attachments/assets/5a556628-56bd-4c62-93f6-d42c543942f8" />
<img width="1855" height="900" alt="image" src="https://github.com/user-attachments/assets/2dbd52f0-ad10-45a3-907c-e033357fe45d" />


🛠️ Tech Stack
Layer	Tools
Frontend	Streamlit
Matching logic	scikit-learn (TF-IDF, cosine similarity)
File parsing	pypdf, python-docx
Visualization	Plotly (gauge chart)
🚀 Getting Started
Prerequisites
Python 3.10+
pip
Installation
bash
git clone https://github.com/<your-username>/resume-jd-matcher.git
cd resume-jd-matcher
pip install -r requirements.txt
Run
bash
streamlit run app.py

Opens at http://localhost:8501. Upload a resume, paste a job description, click ⚡ Check the Signal — or click 🎲 Try a sample to see it work instantly with no files needed.

📁 Project Structure
resume-jd-matcher/
├── app.py              # Main Streamlit app
├── matcher.py           # TF-IDF matching + skill gap detection
├── resume_parser.py     # PDF/DOCX/TXT text extraction
├── styles.py             # Custom theme CSS + skill badge rendering
├── gauge.py               # Plotly match-score gauge
├── requirements.txt
└── README.md
🧠 How the Matching Works

Two techniques working together, no black box:

Overall match score — both texts are vectorized with TF-IDF, then compared using cosine similarity to produce a 0-100% score reflecting overall textual/topical overlap.
Skill gap detection — a fixed vocabulary of ~60 technical and soft skills is checked against both documents using strict word-boundary regex matching, so short/ambiguous tokens (like the language "R") don't false-positive on substrings inside unrelated words.
⚠️ Known Limitations
The skill vocabulary is hardcoded in matcher.py (SKILLS_DB) — it won't catch skills outside that list. A production version would use NER (e.g. spaCy) for dynamic skill extraction.
TF-IDF is bag-of-words — it doesn't understand semantic meaning, only word overlap. A stronger version would use sentence embeddings (sentence-transformers) so that, for example, "led a team" and "team leadership" are recognized as equivalent.
PDF text extraction can misorder text on resumes with complex multi-column layouts, since pypdf reads in document order.
🗺️ Roadmap
 Swap TF-IDF for sentence-transformer embeddings for semantic matching
 Dynamic skill extraction via NER instead of a fixed list
 Support batch-matching one resume against multiple JDs at once
 
📄 License
MIT — free to use, modify, and build on.

🙋 Author

Built by Prachi Shelake
