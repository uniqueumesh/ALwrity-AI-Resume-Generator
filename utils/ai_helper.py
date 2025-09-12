import google.generativeai as genai
from config import GEMINI_API_KEY

def setup_gemini():
    """Setup Gemini AI with API key"""
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel('gemini-2.0-flash-exp')

def generate_resume_content(user_info, job_description=None):
    """Generate resume content using Gemini AI"""
    model = setup_gemini()
    
    prompt = f"""
    Create a professional resume based on the following information:
    
    Personal Information: {user_info.get('personal_info', {})}
    Work Experience: {user_info.get('experience', [])}
    Education: {user_info.get('education', [])}
    Skills: {user_info.get('skills', [])}
    
    Job Description (if provided): {job_description}
    
    Please generate:
    1. A compelling professional summary (2-3 sentences)
    2. Enhanced work experience descriptions with action verbs and quantifiable results
    3. Skills section optimized for the target role
    4. Any additional sections that would strengthen the resume
    
    Format the response in a structured way that can be easily parsed.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"

def optimize_for_job(resume_content, job_description):
    """Optimize resume content for specific job"""
    model = setup_gemini()
    
    prompt = f"""
    Optimize this resume content for the following job description:
    
    Job Description: {job_description}
    
    Resume Content: {resume_content}
    
    Please:
    1. Highlight relevant keywords from the job description
    2. Emphasize matching skills and experience
    3. Suggest improvements to better align with the role
    4. Maintain professional tone and formatting
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error optimizing content: {str(e)}"

def extract_summary_from_content(content):
    """Extract professional summary from AI-generated content"""
    try:
        if "Professional Summary:" in content:
            summary = content.split("Professional Summary:")[1].split("Work Experience:")[0].strip()
        elif "Summary:" in content:
            summary = content.split("Summary:")[1].split("Experience:")[0].strip()
        else:
            summary = "Experienced professional with strong skills and proven track record."
        return summary
    except:
        return "Experienced professional with strong skills and proven track record."
