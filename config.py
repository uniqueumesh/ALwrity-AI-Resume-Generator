import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# App Configuration
APP_TITLE = "ALwrity AI Resume Generator"
APP_DESCRIPTION = "Generate professional resumes with AI assistance"

# Resume Templates
RESUME_TEMPLATES = {
    "professional_sidebar": "Professional Sidebar Template",
    "executive": "Executive/Leadership Template",
    "technical": "Technical Professional Template",
    "creative": "Creative Professional Template",
    "modern": "Modern Clean Template",
    "professional": "Professional Corporate Template",
    "ats_friendly": "ATS-Optimized Template"
}

# UI Configuration
SIDEBAR_WIDTH = 300
MAIN_AREA_WIDTH = 800
