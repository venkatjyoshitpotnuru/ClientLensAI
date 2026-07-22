import streamlit as st
from analyzer import analyze_conversation
from utils import read_docx
from save_results import save_analysis, save_review

st.set_page_config(page_title="ClientLens AI", page_icon="🧠", layout="wide")
st.title("🧠 ClientLens AI")
st.caption("AI-powered health coaching conversation analyzer")

uploaded_file=st.file_uploader("Upload Conversation (.docx)",type=["docx"])

if uploaded_file:
    conversation=read_docx(uploaded_file)
    st.subheader("📄 Conversation Preview")
    st.text_area("",conversation,height=350,disabled=True)

    if st.button("Analyze Conversation",use_container_width=True):
        try:
            with st.spinner("Analyzing conversation..."):
                analysis=analyze_conversation(conversation)
            
            # --- NEW ERROR HANDLING LOGIC ---
            if "error" in analysis:
                st.error(f"Analysis failed: {analysis['error']}")
            else:
                # --- ORIGINAL UI RENDERING LOGIC ---
                analysis_path=save_analysis(analysis)
                st.success("Analysis completed successfully.")
                st.caption(f"Saved analysis: {analysis_path}")

                st.subheader("📋 Weekly Summary")
                for item in analysis.get("weekly_summary",[]):
                    st.write(f"• {item}")

                st.subheader("📊 Health Metrics")
                metrics=[("🥗 Nutrition","nutrition"),("😴 Sleep","sleep"),("🏃 Exercise","exercise"),("💧 Water","water"),("😟 Stress","stress")]
                c1,c2=st.columns(2)
                for i,(title,key) in enumerate(metrics):
                    with (c1 if i%2==0 else c2):
                        with st.container(border=True):
                            d=analysis.get(key,{})
                            st.markdown(f"### {title}")
                            st.write("**Status:**",d.get("status","Not Available"))
                            st.write("**Details:**",d.get("details","Not Available"))
                            st.caption("Classification: "+d.get("classification","Not Available"))

                st.subheader("⚠ Symptoms")
                for s in analysis.get("symptoms",[]):
                    with st.container(border=True):
                        st.markdown(f"### {s.get('name','Unknown')}")
                        st.write(s.get("evidence",""))
                        st.caption(s.get("classification",""))

                st.subheader("🚩 Risk Flags")
                rf=analysis.get("risk_flags",[])
                [st.error(x) for x in rf] if rf else st.success("No risk flags.")

                st.subheader("📌 Pending Actions")
                pa=analysis.get("pending_actions",[])
                [st.info(x) for x in pa] if pa else st.success("No pending actions.")

                st.subheader("🤖 Coach Recommendation")
                st.success(analysis.get("coach_recommendation","Not Available"))

                st.subheader("📖 Supporting Evidence")
                for key in ["nutrition","sleep","exercise","water","stress"]:
                    with st.expander(key.title()):
                        ev=analysis.get(key,{}).get("evidence",[])
                        [st.write("•",e) for e in ev] if ev else st.write("No evidence.")

                st.subheader("👨 Human Review")
                status=st.radio("Review Status",["Approve","Needs Edit","Reject"],horizontal=True)
                notes=st.text_area("Reviewer Notes")
                if st.button("Save Review"):
                    review_path=save_review(status,notes)
                    st.success("Review saved.")
                    st.caption(f"Saved review: {review_path}")

                with st.expander("Raw JSON"):
                    st.json(analysis)

        except Exception as e:
            # This now acts as a true fallback for unexpected UI/App errors
            st.error("An unexpected error occurred in the application.")
            st.exception(e)
else:
    st.info("Upload a DOCX conversation to begin.")