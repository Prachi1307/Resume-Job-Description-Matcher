import streamlit as st


def inject_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;700&display=swap');

        :root {
            --bg: #0E1620;
            --panel: #16212E;
            --panel-raised: #1D2C3D;
            --border: rgba(214, 224, 235, 0.08);
            --text: #E7EDF3;
            --muted: #8496A8;
            --amber: #F4A94E;
            --coral: #FF7A6B;
            --teal: #4FD1C5;
        }

        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
        .stApp { background-color: var(--bg); }

        h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; color: var(--text); }
        p, span, div, label { font-family: 'Inter', sans-serif; }

        .hero-eyebrow {
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--teal);
            margin-bottom: 6px;
        }
        .hero-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 40px;
            font-weight: 700;
            color: var(--text);
            margin: 0;
        }
        .hero-sub {
            color: var(--muted);
            font-size: 15px;
            margin-top: 8px;
        }

        .input-card {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 20px;
        }

        div[data-testid="stFileUploader"], .stTextArea textarea {
            background: var(--panel-raised) !important;
            border-radius: 10px !important;
        }
        .stTextArea textarea { color: var(--text) !important; font-family: 'Inter', sans-serif; }

        div.stButton > button {
            background: var(--amber);
            color: #1A1207;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            border: none;
            border-radius: 10px;
            padding: 12px 20px;
        }
        div.stButton > button:hover { filter: brightness(1.08); }

        .verdict-strong { color: var(--teal); font-family: 'Space Grotesk', sans-serif; font-weight: 700; }
        .verdict-moderate { color: var(--amber); font-family: 'Space Grotesk', sans-serif; font-weight: 700; }
        .verdict-low { color: var(--coral); font-family: 'Space Grotesk', sans-serif; font-weight: 700; }

        .badge-row { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px; }
        .badge {
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            padding: 6px 12px;
            border-radius: 999px;
            border: 1px solid var(--border);
        }
        .badge-matched { background: rgba(79, 209, 197, 0.12); color: var(--teal); border-color: rgba(79,209,197,0.3); }
        .badge-missing { background: rgba(255, 122, 107, 0.12); color: var(--coral); border-color: rgba(255,122,107,0.3); }
        .badge-extra { background: rgba(244, 169, 78, 0.12); color: var(--amber); border-color: rgba(244,169,78,0.3); }

        .empty-note { color: var(--muted); font-size: 13px; font-style: italic; }

        div[data-testid="stMetric"] {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px;
        }
        </style>
    """, unsafe_allow_html=True)


def badge_row(skills, kind):
    """kind: 'matched' | 'missing' | 'extra'"""
    if not skills:
        st.markdown("<span class='empty-note'>Nothing here.</span>", unsafe_allow_html=True)
        return
    spans = "".join(f"<span class='badge badge-{kind}'>{s.title()}</span>" for s in skills)
    st.markdown(f"<div class='badge-row'>{spans}</div>", unsafe_allow_html=True)
