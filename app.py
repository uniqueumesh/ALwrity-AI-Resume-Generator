import streamlit as st
import os
from utils.ai_helper import generate_resume_content, optimize_for_job, extract_summary_from_content
from utils.resume_generator import generate_resume_html, create_download_link
from config import APP_TITLE, APP_DESCRIPTION, RESUME_TEMPLATES

# Page Configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.title("📄 " + APP_TITLE)
st.markdown(f"*{APP_DESCRIPTION}*")
st.divider()

# Sidebar for API Key and Settings
with st.sidebar:
    st.header("🔧 Setup")
    api_key = st.text_input(
        "Enter your Gemini API Key",
        type="password",
        help="Get your free API key from Google AI Studio"
    )
    
    if api_key:
        os.environ["GEMINI_API_KEY"] = api_key
        st.success("✅ API Key configured!")
    else:
        st.warning("⚠️ Please enter your Gemini API Key to continue")
    
    st.divider()
    
    # Template Selection
    st.header("🎨 Choose Template")
    selected_template = st.selectbox(
        "Resume Template",
        options=list(RESUME_TEMPLATES.keys()),
        format_func=lambda x: RESUME_TEMPLATES[x],
        help="Select a template that matches your industry and style preference"
    )
    
    st.divider()
    
    # Help Section
    st.header("❓ Help")
    st.markdown("""
    **How to use:**
    1. Enter your Gemini API key
    2. Fill in your information
    3. Choose a template
    4. Generate your resume
    5. Download as HTML
    
    **Get API Key:**
    Visit [Google AI Studio](https://aistudio.google.com/) to get your free API key.
    """)

# Main Content
if not api_key:
    st.info("👆 Please enter your Gemini API Key in the sidebar to start generating resumes.")
    
    # Show example of what the app can do
    st.subheader("🎯 What This App Can Do")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🤖 AI-Powered**
        - Generate professional content
        - Optimize for specific jobs
        - Enhance descriptions
        """)
    
    with col2:
        st.markdown("""
        **🎨 Multiple Templates**
        - Modern design
        - Professional style
        - Creative layout
        - ATS-friendly
        """)
    
    with col3:
        st.markdown("""
        **⚡ Easy to Use**
        - Simple forms
        - Real-time preview
        - One-click download
        """)
    
    st.stop()

# Input Form
st.header("📝 Enter Your Information")

with st.form("resume_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👤 Personal Information")
        name = st.text_input("Full Name", placeholder="John Doe", help="Enter your full name as it should appear on your resume")
        email = st.text_input("Email", placeholder="john@email.com", help="Your professional email address")
        phone = st.text_input("Phone", placeholder="+1 (555) 123-4567", help="Your contact number")
        location = st.text_input("Location", placeholder="New York, NY", help="City, State or City, Country")
        
        # Additional fields for different templates
        if selected_template in ["executive", "technical", "creative", "modern"]:
            title = st.text_input("Professional Title", placeholder="Software Engineer", help="Your current or desired job title")
            linkedin = st.text_input("LinkedIn Profile", placeholder="linkedin.com/in/yourname", help="Your LinkedIn profile URL")
            
        if selected_template == "technical":
            github = st.text_input("GitHub Profile", placeholder="github.com/yourname", help="Your GitHub profile URL")
            
        if selected_template == "creative":
            portfolio = st.text_input("Portfolio Website", placeholder="yourname.com", help="Your portfolio or personal website")

        if selected_template == "professional_sidebar":
            website = st.text_input("Website", placeholder="yourname.com", help="Personal site or portfolio")
            photo_url = st.text_input("Photo URL (optional)", placeholder="https://.../photo.jpg", help="Used in sidebar; keep under 500x500px for best print")
        
        st.subheader("🎓 Education")
        degree = st.text_input("Degree", placeholder="Bachelor of Science in Computer Science", help="Your degree or qualification")
        institution = st.text_input("Institution", placeholder="University Name", help="Name of your school or university")
        grad_year = st.text_input("Graduation Year", placeholder="2020", help="Year you graduated")
    
    with col2:
        st.subheader("💼 Work Experience")
        job_title = st.text_input("Current/Recent Job Title", placeholder="Software Developer", help="Your most recent or current job title")
        company = st.text_input("Company", placeholder="Tech Company Inc.", help="Name of your company")
        duration = st.text_input("Duration", placeholder="2020 - Present", help="Start date - End date (or Present)")
        job_description = st.text_area("Job Description", placeholder="Describe your main responsibilities and achievements...", help="Include key accomplishments, responsibilities, and results")
        
        st.subheader("🛠️ Skills")
        skills = st.text_area("Skills (comma-separated)", placeholder="Python, JavaScript, React, SQL, Project Management", help="List your skills separated by commas")

        if selected_template == "professional_sidebar":
            st.subheader("🌐 Languages")
            languages_text = st.text_area("Languages (name:level, comma-separated)", placeholder="English:Fluent, French:Intermediate")
    
    # Optional: Job Description for Optimization
    st.subheader("🎯 Target Job (Optional)")
    target_job = st.text_area(
        "Paste job description to optimize your resume",
        placeholder="Paste the job description you're applying for...",
        help="This helps AI optimize your resume for the specific role",
        height=100
    )
    
    submitted = st.form_submit_button("🚀 Generate Resume", type="primary", use_container_width=True)

# Process Form Submission
if submitted:
    if not name or not email:
        st.error("❌ Please fill in at least your name and email.")
    else:
        with st.spinner("🤖 AI is generating your professional resume..."):
            # Prepare user data
            personal_info = {
                "name": name,
                "email": email,
                "phone": phone,
                "location": location
            }
            
            # Add template-specific fields
            if selected_template in ["executive", "technical", "creative", "modern"]:
                personal_info["title"] = title if 'title' in locals() else ""
                personal_info["linkedin"] = linkedin if 'linkedin' in locals() else ""
            
            if selected_template == "technical" and 'github' in locals():
                personal_info["github"] = github
                
            if selected_template == "creative" and 'portfolio' in locals():
                personal_info["portfolio"] = portfolio
            
            # Languages parsing for professional_sidebar
            languages = []
            if selected_template == "professional_sidebar" and 'languages_text' in locals() and languages_text:
                try:
                    for item in languages_text.split(','):
                        name_level = item.strip().split(':')
                        if len(name_level) == 2:
                            languages.append({"name": name_level[0].strip(), "level": name_level[1].strip()})
                        elif name_level[0].strip():
                            languages.append({"name": name_level[0].strip(), "level": ""})
                except Exception:
                    languages = []

            # Attach website/photo for professional_sidebar
            if selected_template == "professional_sidebar":
                if 'website' in locals():
                    personal_info["website"] = website
                if 'photo_url' in locals():
                    personal_info["photo_url"] = photo_url

            user_data = {
                "personal_info": personal_info,
                "experience": [{
                    "title": job_title,
                    "company": company,
                    "duration": duration,
                    "description": job_description
                }] if job_title else [],
                "education": [{
                    "degree": degree,
                    "institution": institution,
                    "year": grad_year
                }] if degree else [],
                "skills": skills.split(",") if skills else [],
                "languages": languages
            }
            
            # Generate AI content
            ai_content = generate_resume_content(user_data, target_job)
            
            # If target job provided, optimize further
            if target_job:
                ai_content = optimize_for_job(ai_content, target_job)
            
            # Extract summary from AI content
            summary = extract_summary_from_content(ai_content)
            
            # Prepare resume data for template
            # For sidebar template we pass additional structured fields
            resume_data = {
                "personal_info": user_data["personal_info"],
                "summary": summary,
                "experience": user_data["experience"],
                "education": user_data["education"],
                "skills": ", ".join(user_data["skills"]),
                "skills_list": [s.strip() for s in user_data["skills"]] if user_data["skills"] else [],
                "languages": user_data.get("languages", []),
                "references": []
            }
            
            # Generate HTML resume
            html_resume = generate_resume_html(resume_data, selected_template)
            
            # Display results
            st.success("✅ Resume generated successfully!")
            
            # Show preview
            st.subheader("👀 Resume Preview")
            st.components.v1.html(html_resume, height=800, scrolling=True)
            
            # Download option
            st.subheader("💾 Download Resume")
            download_link = create_download_link(html_resume, f"{name.replace(' ', '_')}_resume.html")
            st.markdown(download_link, unsafe_allow_html=True)
            
            # Show AI suggestions
            st.subheader("🤖 AI Suggestions & Generated Content")
            with st.expander("View AI-generated content and suggestions"):
                st.text_area("AI Content", ai_content, height=300, disabled=True)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>Made with ❤️ using Streamlit & Gemini AI | Free & Open Source</p>
    <p><a href="https://github.com/your-repo" target="_blank">GitHub</a> | <a href="https://aistudio.google.com/" target="_blank">Get Gemini API Key</a></p>
</div>
""", unsafe_allow_html=True)
