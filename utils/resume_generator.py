from jinja2 import Template
import streamlit as st

def load_resume_template(template_name):
    """Load resume template based on selection"""
    templates = {
        "modern": """
        <div style="font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px;">
            <div style="text-align: center; border-bottom: 3px solid #2E86AB; padding-bottom: 20px; margin-bottom: 30px;">
                <h1 style="color: #2E86AB; margin: 0; font-size: 2.5em;">{{personal_info.name}}</h1>
                <p style="color: #666; margin: 5px 0;">{{personal_info.email}} | {{personal_info.phone}} | {{personal_info.location}}</p>
            </div>
            
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; border-bottom: 2px solid #2E86AB; padding-bottom: 5px;">Professional Summary</h2>
                <p>{{summary}}</p>
            </div>
            
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; border-bottom: 2px solid #2E86AB; padding-bottom: 5px;">Work Experience</h2>
                {% for exp in experience %}
                <div style="margin-bottom: 20px;">
                    <h3 style="margin: 0; color: #333;">{{exp.title}} - {{exp.company}}</h3>
                    <p style="color: #666; margin: 5px 0; font-style: italic;">{{exp.duration}}</p>
                    <p>{{exp.description}}</p>
                </div>
                {% endfor %}
            </div>
            
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; border-bottom: 2px solid #2E86AB; padding-bottom: 5px;">Education</h2>
                {% for edu in education %}
                <div style="margin-bottom: 15px;">
                    <h3 style="margin: 0; color: #333;">{{edu.degree}} - {{edu.institution}}</h3>
                    <p style="color: #666; margin: 5px 0;">{{edu.year}}</p>
                </div>
                {% endfor %}
            </div>
            
            <div>
                <h2 style="color: #2E86AB; border-bottom: 2px solid #2E86AB; padding-bottom: 5px;">Skills</h2>
                <p>{{skills}}</p>
            </div>
        </div>
        """,
        
        "professional": """
        <div style="font-family: 'Times New Roman', serif; max-width: 800px; margin: 0 auto; padding: 20px;">
            <div style="text-align: center; margin-bottom: 30px;">
                <h1 style="color: #000; margin: 0; font-size: 2.2em; text-transform: uppercase;">{{personal_info.name}}</h1>
                <p style="color: #333; margin: 5px 0;">{{personal_info.email}} | {{personal_info.phone}} | {{personal_info.location}}</p>
            </div>
            
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; text-transform: uppercase; letter-spacing: 1px;">Professional Summary</h2>
                <hr style="border: 1px solid #000;">
                <p>{{summary}}</p>
            </div>
            
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; text-transform: uppercase; letter-spacing: 1px;">Professional Experience</h2>
                <hr style="border: 1px solid #000;">
                {% for exp in experience %}
                <div style="margin-bottom: 20px;">
                    <h3 style="margin: 0; color: #000;">{{exp.title}}</h3>
                    <p style="color: #333; margin: 5px 0; font-weight: bold;">{{exp.company}} | {{exp.duration}}</p>
                    <p>{{exp.description}}</p>
                </div>
                {% endfor %}
            </div>
            
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; text-transform: uppercase; letter-spacing: 1px;">Education</h2>
                <hr style="border: 1px solid #000;">
                {% for edu in education %}
                <div style="margin-bottom: 15px;">
                    <h3 style="margin: 0; color: #000;">{{edu.degree}}</h3>
                    <p style="color: #333; margin: 5px 0;">{{edu.institution}} | {{edu.year}}</p>
                </div>
                {% endfor %}
            </div>
            
            <div>
                <h2 style="color: #000; text-transform: uppercase; letter-spacing: 1px;">Technical Skills</h2>
                <hr style="border: 1px solid #000;">
                <p>{{skills}}</p>
            </div>
        </div>
        """,
        
        "creative": """
        <div style="font-family: 'Helvetica Neue', Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
            <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; backdrop-filter: blur(10px);">
                <div style="text-align: center; margin-bottom: 30px;">
                    <h1 style="margin: 0; font-size: 2.8em; font-weight: 300; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">{{personal_info.name}}</h1>
                    <p style="margin: 10px 0; font-size: 1.1em; opacity: 0.9;">{{personal_info.email}} | {{personal_info.phone}} | {{personal_info.location}}</p>
                </div>
                
                <div style="margin-bottom: 25px;">
                    <h2 style="border-left: 4px solid #fff; padding-left: 15px; margin-bottom: 15px;">Professional Summary</h2>
                    <p style="line-height: 1.6;">{{summary}}</p>
                </div>
                
                <div style="margin-bottom: 25px;">
                    <h2 style="border-left: 4px solid #fff; padding-left: 15px; margin-bottom: 15px;">Work Experience</h2>
                    {% for exp in experience %}
                    <div style="margin-bottom: 20px; background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px;">
                        <h3 style="margin: 0; font-size: 1.2em;">{{exp.title}} - {{exp.company}}</h3>
                        <p style="margin: 5px 0; opacity: 0.8; font-style: italic;">{{exp.duration}}</p>
                        <p style="line-height: 1.5;">{{exp.description}}</p>
                    </div>
                    {% endfor %}
                </div>
                
                <div style="margin-bottom: 25px;">
                    <h2 style="border-left: 4px solid #fff; padding-left: 15px; margin-bottom: 15px;">Education</h2>
                    {% for edu in education %}
                    <div style="margin-bottom: 15px;">
                        <h3 style="margin: 0;">{{edu.degree}} - {{edu.institution}}</h3>
                        <p style="margin: 5px 0; opacity: 0.8;">{{edu.year}}</p>
                    </div>
                    {% endfor %}
                </div>
                
                <div>
                    <h2 style="border-left: 4px solid #fff; padding-left: 15px; margin-bottom: 15px;">Skills</h2>
                    <p style="line-height: 1.6;">{{skills}}</p>
                </div>
            </div>
        </div>
        """,
        
        "ats_friendly": """
        <div style="font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.4;">
            <div style="text-align: center; margin-bottom: 30px;">
                <h1 style="color: #000; margin: 0; font-size: 2.2em; font-weight: bold;">{{personal_info.name}}</h1>
                <p style="color: #000; margin: 5px 0; font-size: 1.1em;">{{personal_info.email}} | {{personal_info.phone}} | {{personal_info.location}}</p>
            </div>
            
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; font-size: 1.3em; font-weight: bold; margin-bottom: 10px;">PROFESSIONAL SUMMARY</h2>
                <p>{{summary}}</p>
            </div>
            
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; font-size: 1.3em; font-weight: bold; margin-bottom: 10px;">PROFESSIONAL EXPERIENCE</h2>
                {% for exp in experience %}
                <div style="margin-bottom: 20px;">
                    <h3 style="margin: 0; color: #000; font-size: 1.1em; font-weight: bold;">{{exp.title}}</h3>
                    <p style="color: #000; margin: 5px 0; font-weight: bold;">{{exp.company}} | {{exp.duration}}</p>
                    <p>{{exp.description}}</p>
                </div>
                {% endfor %}
            </div>
            
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; font-size: 1.3em; font-weight: bold; margin-bottom: 10px;">EDUCATION</h2>
                {% for edu in education %}
                <div style="margin-bottom: 15px;">
                    <h3 style="margin: 0; color: #000; font-size: 1.1em; font-weight: bold;">{{edu.degree}}</h3>
                    <p style="color: #000; margin: 5px 0;">{{edu.institution}} | {{edu.year}}</p>
                </div>
                {% endfor %}
            </div>
            
            <div>
                <h2 style="color: #000; font-size: 1.3em; font-weight: bold; margin-bottom: 10px;">TECHNICAL SKILLS</h2>
                <p>{{skills}}</p>
            </div>
        </div>
        """
    }
    
    return templates.get(template_name, templates["modern"])

def generate_resume_html(resume_data, template_name="modern"):
    """Generate HTML resume from data"""
    template_str = load_resume_template(template_name)
    template = Template(template_str)
    return template.render(**resume_data)

def create_download_link(html_content, filename="resume.html"):
    """Create download link for HTML resume"""
    import base64
    
    b64 = base64.b64encode(html_content.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="{filename}" style="background-color: #2E86AB; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 10px 0;">📄 Download Resume</a>'
    return href
