from jinja2 import Template
import streamlit as st

def load_resume_template(template_name):
    """Load resume template based on selection"""
    templates = {
        "professional_sidebar": """
        <div style="font-family: 'Inter', Arial, sans-serif; width: 8.5in; margin: 0 auto; line-height: 1.45; color: #2C3E50; display: grid; grid-template-columns: 2.7in 1fr;">
            <!-- Sidebar -->
            <aside style="background:#183447; color:#fff; padding: 0.6in 0.4in; min-height: 11in;">
                <!-- Photo -->
                {% if personal_info.photo_url %}
                <div style="display:flex; justify-content:center; margin-bottom: 18px;">
                    <img src="{{personal_info.photo_url}}" alt="photo" style="width:130px; height:130px; border-radius:50%; object-fit:cover; border:4px solid #0f2733;"/>
                </div>
                {% endif %}

                <!-- Contact -->
                <h3 style="font-size:14pt; letter-spacing:1px; margin: 18px 0 8px;">CONTACT</h3>
                <hr style="border:0; border-top:1px solid #315164; margin: 0 0 10px 0;">
                <div style="font-size:10.5pt;">
                    {% if personal_info.phone %}<div style="margin:6px 0;">{{personal_info.phone}}</div>{% endif %}
                    {% if personal_info.email %}<div style="margin:6px 0;">{{personal_info.email}}</div>{% endif %}
                    {% if personal_info.location %}<div style="margin:6px 0;">{{personal_info.location}}</div>{% endif %}
                    {% if personal_info.website %}<div style="margin:6px 0;">{{personal_info.website}}</div>{% endif %}
                    {% if personal_info.linkedin %}<div style="margin:6px 0;">{{personal_info.linkedin}}</div>{% endif %}
                </div>

                <!-- Education -->
                <h3 style="font-size:14pt; letter-spacing:1px; margin: 18px 0 8px;">EDUCATION</h3>
                <hr style="border:0; border-top:1px solid #315164; margin: 0 0 10px 0;">
                <div style="font-size:10.5pt;">
                    {% for edu in education %}
                    <div style="margin:10px 0;">
                        {% if edu.start_year or edu.end_year %}
                        <div style="opacity:0.9;">{{edu.start_year or ''}}{% if edu.end_year %} - {{edu.end_year}}{% endif %}</div>
                        {% endif %}
                        <div style="font-weight:700;">{{edu.institution}}</div>
                        {% if edu.degree %}<div>{{edu.degree}}</div>{% endif %}
                        {% if edu.details %}
                        <ul style="margin:6px 0 0 16px; padding:0;">
                            {% for d in edu.details %}<li style="margin:2px 0;">{{d}}</li>{% endfor %}
                        </ul>
                        {% endif %}
                    </div>
                    {% endfor %}
                </div>

                <!-- Skills -->
                <h3 style="font-size:14pt; letter-spacing:1px; margin: 18px 0 8px;">SKILLS</h3>
                <hr style="border:0; border-top:1px solid #315164; margin: 0 0 10px 0;">
                <ul style="font-size:10.5pt; margin:0; padding-left:16px;">
                    {% for s in skills_list %}<li style="margin:4px 0;">{{s}}</li>{% endfor %}
                </ul>

                <!-- Languages -->
                {% if languages %}
                <h3 style="font-size:14pt; letter-spacing:1px; margin: 18px 0 8px;">LANGUAGES</h3>
                <hr style="border:0; border-top:1px solid #315164; margin: 0 0 10px 0;">
                <ul style="font-size:10.5pt; margin:0; padding-left:16px;">
                    {% for lang in languages %}
                    <li style="margin:4px 0;">{{lang.name}} {% if lang.level %}({{lang.level}}){% endif %}</li>
                    {% endfor %}
                </ul>
                {% endif %}
            </aside>

            <!-- Main Content -->
            <main style="background:#fff; padding: 0.6in 0.6in;">
                <!-- Name / Title -->
                <div style="margin-bottom: 18px;">
                    <h1 style="margin:0; font-size:28pt; color:#183447; font-weight:800; letter-spacing:0.5px;">{{personal_info.name}}</h1>
                    <div style="margin-top:6px; font-size:12pt; color:#6A7D8F; font-weight:600;">{{personal_info.title}}</div>
                    <div style="width:80px; height:4px; background:#183447; margin-top:10px;"></div>
                </div>

                <!-- Profile -->
                <section style="margin-bottom: 18px;">
                    <h2 style="font-size:13pt; color:#183447; letter-spacing:1px; font-weight:800; margin:0 0 6px;">PROFILE</h2>
                    <hr style="border:0; border-top:2px solid #D9DFE5; margin: 0 0 10px 0;">
                    <p style="font-size:11pt; margin:0; text-align:justify;">{{summary}}</p>
                </section>

                <!-- Work Experience -->
                <section>
                    <h2 style="font-size:13pt; color:#183447; letter-spacing:1px; font-weight:800; margin:0 0 6px;">WORK EXPERIENCE</h2>
                    <hr style="border:0; border-top:2px solid #D9DFE5; margin: 0 0 10px 0;">
                    {% for exp in experience %}
                    <div style="display:flex; justify-content:space-between; gap:16px; margin-bottom:14px;">
                        <div style="flex:1;">
                            <div style="font-weight:800; color:#2C3E50;">{{exp.company}}</div>
                            <div style="color:#2C3E50;">{{exp.title}}</div>
                            {% if exp.points %}
                            <ul style="margin:6px 0 0 18px; padding:0;">
                                {% for p in exp.points %}<li style="margin:4px 0;">{{p}}</li>{% endfor %}
                            </ul>
                            {% else %}
                            <p style="margin:6px 0 0;">{{exp.description}}</p>
                            {% endif %}
                        </div>
                        <div style="min-width:120px; text-align:right; color:#6A7D8F;">{{exp.duration}}</div>
                    </div>
                    {% endfor %}
                </section>

                <!-- References -->
                {% if references %}
                <section style="margin-top:18px;">
                    <h2 style="font-size:13pt; color:#183447; letter-spacing:1px; font-weight:800; margin:0 0 6px;">REFERENCE</h2>
                    <hr style="border:0; border-top:2px solid #D9DFE5; margin: 0 0 10px 0;">
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; font-size:10.5pt;">
                        {% for ref in references %}
                        <div>
                            <div style="font-weight:700;">{{ref.name}}</div>
                            <div>{{ref.company}} / {{ref.title}}</div>
                            <div style="margin-top:4px;">Phone: {{ref.phone}}</div>
                            <div>Email: {{ref.email}}</div>
                        </div>
                        {% endfor %}
                    </div>
                </section>
                {% endif %}
            </main>
        </div>
        """,
        "executive": """
        <div style="font-family: 'Times New Roman', serif; max-width: 8.5in; margin: 0 auto; padding: 0.75in; line-height: 1.4; color: #2C3E50;">
            <!-- Header Section -->
            <div style="text-align: center; margin-bottom: 30px; border-bottom: 3px solid #2C3E50; padding-bottom: 20px;">
                <h1 style="color: #2C3E50; margin: 0; font-size: 24pt; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">{{personal_info.name}}</h1>
                <p style="color: #2C3E50; margin: 8px 0; font-size: 11pt; font-weight: bold;">{{personal_info.title or 'Executive Professional'}}</p>
                <p style="color: #666; margin: 5px 0; font-size: 10pt;">{{personal_info.email}} | {{personal_info.phone}} | {{personal_info.location}}</p>
                {% if personal_info.linkedin %}<p style="color: #666; margin: 5px 0; font-size: 10pt;">LinkedIn: {{personal_info.linkedin}}</p>{% endif %}
            </div>
            
            <!-- Executive Summary -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2C3E50; font-size: 16pt; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; border-bottom: 2px solid #E74C3C; padding-bottom: 3px;">Executive Summary</h2>
                <p style="font-size: 11pt; margin: 0; text-align: justify;">{{summary}}</p>
            </div>
            
            <!-- Core Competencies -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2C3E50; font-size: 16pt; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; border-bottom: 2px solid #E74C3C; padding-bottom: 3px;">Core Competencies</h2>
                <p style="font-size: 11pt; margin: 0;">{{skills}}</p>
            </div>
            
            <!-- Professional Experience -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2C3E50; font-size: 16pt; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; border-bottom: 2px solid #E74C3C; padding-bottom: 3px;">Professional Experience</h2>
                {% for exp in experience %}
                <div style="margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                        <h3 style="margin: 0; color: #2C3E50; font-size: 14pt; font-weight: bold;">{{exp.title}}</h3>
                        <span style="color: #666; font-size: 10pt; font-style: italic;">{{exp.duration}}</span>
                    </div>
                    <p style="margin: 0 0 8px 0; color: #2C3E50; font-size: 12pt; font-weight: bold;">{{exp.company}}</p>
                    <p style="font-size: 11pt; margin: 0; line-height: 1.5;">{{exp.description}}</p>
                </div>
                {% endfor %}
            </div>
            
            <!-- Education -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2C3E50; font-size: 16pt; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; border-bottom: 2px solid #E74C3C; padding-bottom: 3px;">Education</h2>
                {% for edu in education %}
                <div style="margin-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h3 style="margin: 0; color: #2C3E50; font-size: 12pt; font-weight: bold;">{{edu.degree}}</h3>
                        <span style="color: #666; font-size: 10pt;">{{edu.year}}</span>
                    </div>
                    <p style="margin: 5px 0; color: #2C3E50; font-size: 11pt; font-weight: bold;">{{edu.institution}}</p>
                </div>
                {% endfor %}
            </div>
            
            <!-- Additional Sections -->
            {% if certifications %}
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2C3E50; font-size: 16pt; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; border-bottom: 2px solid #E74C3C; padding-bottom: 3px;">Certifications</h2>
                <p style="font-size: 11pt; margin: 0;">{{certifications}}</p>
            </div>
            {% endif %}
        </div>
        """,
        
        "technical": """
        <div style="font-family: 'Arial', sans-serif; max-width: 8.5in; margin: 0 auto; padding: 0.75in; line-height: 1.4; color: #333;">
            <!-- Header Section -->
            <div style="text-align: center; margin-bottom: 30px; border-bottom: 3px solid #2E86AB; padding-bottom: 20px;">
                <h1 style="color: #2E86AB; margin: 0; font-size: 24pt; font-weight: bold;">{{personal_info.name}}</h1>
                <p style="color: #2E86AB; margin: 8px 0; font-size: 12pt; font-weight: bold;">{{personal_info.title or 'Technical Professional'}}</p>
                <p style="color: #666; margin: 5px 0; font-size: 10pt;">{{personal_info.email}} | {{personal_info.phone}} | {{personal_info.location}}</p>
                {% if personal_info.github %}<p style="color: #666; margin: 5px 0; font-size: 10pt;">GitHub: {{personal_info.github}}</p>{% endif %}
                {% if personal_info.linkedin %}<p style="color: #666; margin: 5px 0; font-size: 10pt;">LinkedIn: {{personal_info.linkedin}}</p>{% endif %}
            </div>
            
            <!-- Professional Summary -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Professional Summary</h2>
                <p style="font-size: 11pt; margin: 0; text-align: justify;">{{summary}}</p>
            </div>
            
            <!-- Technical Skills -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Technical Skills</h2>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                    <div>
                        <h3 style="color: #333; font-size: 12pt; font-weight: bold; margin: 0 0 8px 0;">Programming Languages</h3>
                        <p style="font-size: 10pt; margin: 0;">{{technical_skills.languages or 'Python, JavaScript, Java, C++'}}</p>
                    </div>
                    <div>
                        <h3 style="color: #333; font-size: 12pt; font-weight: bold; margin: 0 0 8px 0;">Frameworks & Tools</h3>
                        <p style="font-size: 10pt; margin: 0;">{{technical_skills.frameworks or 'React, Node.js, Django, Docker'}}</p>
                    </div>
                    <div>
                        <h3 style="color: #333; font-size: 12pt; font-weight: bold; margin: 0 0 8px 0;">Databases</h3>
                        <p style="font-size: 10pt; margin: 0;">{{technical_skills.databases or 'MySQL, PostgreSQL, MongoDB'}}</p>
                    </div>
                    <div>
                        <h3 style="color: #333; font-size: 12pt; font-weight: bold; margin: 0 0 8px 0;">Cloud & DevOps</h3>
                        <p style="font-size: 10pt; margin: 0;">{{technical_skills.cloud or 'AWS, Azure, Kubernetes, CI/CD'}}</p>
                    </div>
                </div>
            </div>
            
            <!-- Professional Experience -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Professional Experience</h2>
                {% for exp in experience %}
                <div style="margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                        <h3 style="margin: 0; color: #333; font-size: 14pt; font-weight: bold;">{{exp.title}}</h3>
                        <span style="color: #666; font-size: 10pt; font-style: italic;">{{exp.duration}}</span>
                    </div>
                    <p style="margin: 0 0 8px 0; color: #2E86AB; font-size: 12pt; font-weight: bold;">{{exp.company}}</p>
                    <p style="font-size: 11pt; margin: 0; line-height: 1.5;">{{exp.description}}</p>
                </div>
                {% endfor %}
            </div>
            
            <!-- Projects -->
            {% if projects %}
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Key Projects</h2>
                {% for project in projects %}
                <div style="margin-bottom: 15px;">
                    <h3 style="margin: 0; color: #333; font-size: 12pt; font-weight: bold;">{{project.name}}</h3>
                    <p style="margin: 5px 0; font-size: 11pt;">{{project.description}}</p>
                    <p style="margin: 0; color: #666; font-size: 10pt;">Technologies: {{project.technologies}}</p>
                </div>
                {% endfor %}
            </div>
            {% endif %}
            
            <!-- Education -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Education</h2>
                {% for edu in education %}
                <div style="margin-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h3 style="margin: 0; color: #333; font-size: 12pt; font-weight: bold;">{{edu.degree}}</h3>
                        <span style="color: #666; font-size: 10pt;">{{edu.year}}</span>
                    </div>
                    <p style="margin: 5px 0; color: #2E86AB; font-size: 11pt; font-weight: bold;">{{edu.institution}}</p>
                </div>
                {% endfor %}
            </div>
            
            <!-- Certifications -->
            {% if certifications %}
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Certifications</h2>
                <p style="font-size: 11pt; margin: 0;">{{certifications}}</p>
            </div>
            {% endif %}
        </div>
        """,
        
        "creative": """
        <div style="font-family: 'Helvetica Neue', Arial, sans-serif; max-width: 8.5in; margin: 0 auto; padding: 0.75in; line-height: 1.4; color: #2C3E50;">
            <!-- Header Section -->
            <div style="text-align: center; margin-bottom: 30px; background: linear-gradient(135deg, #8E44AD 0%, #F39C12 100%); color: white; padding: 30px; border-radius: 15px;">
                <h1 style="margin: 0; font-size: 28pt; font-weight: 300; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">{{personal_info.name}}</h1>
                <p style="margin: 10px 0; font-size: 14pt; opacity: 0.9;">{{personal_info.title or 'Creative Professional'}}</p>
                <p style="margin: 5px 0; font-size: 11pt; opacity: 0.8;">{{personal_info.email}} | {{personal_info.phone}} | {{personal_info.location}}</p>
                {% if personal_info.portfolio %}<p style="margin: 5px 0; font-size: 11pt; opacity: 0.8;">Portfolio: {{personal_info.portfolio}}</p>{% endif %}
                {% if personal_info.linkedin %}<p style="margin: 5px 0; font-size: 11pt; opacity: 0.8;">LinkedIn: {{personal_info.linkedin}}</p>{% endif %}
            </div>
            
            <!-- Professional Summary -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #8E44AD; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-left: 4px solid #8E44AD; padding-left: 15px;">Professional Summary</h2>
                <p style="font-size: 11pt; margin: 0; text-align: justify; line-height: 1.6;">{{summary}}</p>
            </div>
            
            <!-- Creative Skills -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #8E44AD; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-left: 4px solid #8E44AD; padding-left: 15px;">Creative Skills</h2>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    <div>
                        <h3 style="color: #2C3E50; font-size: 12pt; font-weight: bold; margin: 0 0 8px 0;">Design Tools</h3>
                        <p style="font-size: 10pt; margin: 0;">{{creative_skills.design or 'Adobe Creative Suite, Figma, Sketch'}}</p>
                    </div>
                    <div>
                        <h3 style="color: #2C3E50; font-size: 12pt; font-weight: bold; margin: 0 0 8px 0;">Digital Marketing</h3>
                        <p style="font-size: 10pt; margin: 0;">{{creative_skills.marketing or 'Google Analytics, Social Media, SEO'}}</p>
                    </div>
                    <div>
                        <h3 style="color: #2C3E50; font-size: 12pt; font-weight: bold; margin: 0 0 8px 0;">Content Creation</h3>
                        <p style="font-size: 10pt; margin: 0;">{{creative_skills.content or 'Copywriting, Video Production, Photography'}}</p>
                    </div>
                    <div>
                        <h3 style="color: #2C3E50; font-size: 12pt; font-weight: bold; margin: 0 0 8px 0;">Web Development</h3>
                        <p style="font-size: 10pt; margin: 0;">{{creative_skills.web or 'HTML/CSS, WordPress, Shopify'}}</p>
                    </div>
                </div>
            </div>
            
            <!-- Professional Experience -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #8E44AD; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-left: 4px solid #8E44AD; padding-left: 15px;">Professional Experience</h2>
                {% for exp in experience %}
                <div style="margin-bottom: 20px; background: rgba(142, 68, 173, 0.1); padding: 15px; border-radius: 8px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                        <h3 style="margin: 0; color: #2C3E50; font-size: 14pt; font-weight: bold;">{{exp.title}}</h3>
                        <span style="color: #666; font-size: 10pt; font-style: italic;">{{exp.duration}}</span>
                    </div>
                    <p style="margin: 0 0 8px 0; color: #8E44AD; font-size: 12pt; font-weight: bold;">{{exp.company}}</p>
                    <p style="font-size: 11pt; margin: 0; line-height: 1.5;">{{exp.description}}</p>
                </div>
                {% endfor %}
            </div>
            
            <!-- Creative Projects -->
            {% if projects %}
            <div style="margin-bottom: 25px;">
                <h2 style="color: #8E44AD; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-left: 4px solid #8E44AD; padding-left: 15px;">Creative Projects</h2>
                {% for project in projects %}
                <div style="margin-bottom: 15px; background: rgba(243, 156, 18, 0.1); padding: 15px; border-radius: 8px;">
                    <h3 style="margin: 0; color: #2C3E50; font-size: 12pt; font-weight: bold;">{{project.name}}</h3>
                    <p style="margin: 5px 0; font-size: 11pt;">{{project.description}}</p>
                    <p style="margin: 0; color: #666; font-size: 10pt;">Tools: {{project.tools}}</p>
                </div>
                {% endfor %}
            </div>
            {% endif %}
            
            <!-- Education -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #8E44AD; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-left: 4px solid #8E44AD; padding-left: 15px;">Education</h2>
                {% for edu in education %}
                <div style="margin-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h3 style="margin: 0; color: #2C3E50; font-size: 12pt; font-weight: bold;">{{edu.degree}}</h3>
                        <span style="color: #666; font-size: 10pt;">{{edu.year}}</span>
                    </div>
                    <p style="margin: 5px 0; color: #8E44AD; font-size: 11pt; font-weight: bold;">{{edu.institution}}</p>
                </div>
                {% endfor %}
            </div>
            
            <!-- Awards & Recognition -->
            {% if awards %}
            <div style="margin-bottom: 25px;">
                <h2 style="color: #8E44AD; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-left: 4px solid #8E44AD; padding-left: 15px;">Awards & Recognition</h2>
                <p style="font-size: 11pt; margin: 0;">{{awards}}</p>
            </div>
            {% endif %}
        </div>
        """,
        
        "modern": """
        <div style="font-family: Arial, sans-serif; max-width: 8.5in; margin: 0 auto; padding: 0.75in; line-height: 1.4; color: #333;">
            <!-- Header Section -->
            <div style="text-align: center; border-bottom: 3px solid #2E86AB; padding-bottom: 20px; margin-bottom: 30px;">
                <h1 style="color: #2E86AB; margin: 0; font-size: 24pt; font-weight: bold;">{{personal_info.name}}</h1>
                <p style="color: #2E86AB; margin: 8px 0; font-size: 12pt; font-weight: bold;">{{personal_info.title or 'Professional'}}</p>
                <p style="color: #666; margin: 5px 0; font-size: 10pt;">{{personal_info.email}} | {{personal_info.phone}} | {{personal_info.location}}</p>
                {% if personal_info.linkedin %}<p style="color: #666; margin: 5px 0; font-size: 10pt;">LinkedIn: {{personal_info.linkedin}}</p>{% endif %}
            </div>
            
            <!-- Professional Summary -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Professional Summary</h2>
                <p style="font-size: 11pt; margin: 0; text-align: justify;">{{summary}}</p>
            </div>
            
            <!-- Core Competencies -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Core Competencies</h2>
                <p style="font-size: 11pt; margin: 0;">{{skills}}</p>
            </div>
            
            <!-- Professional Experience -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Professional Experience</h2>
                {% for exp in experience %}
                <div style="margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                        <h3 style="margin: 0; color: #333; font-size: 14pt; font-weight: bold;">{{exp.title}}</h3>
                        <span style="color: #666; font-size: 10pt; font-style: italic;">{{exp.duration}}</span>
                    </div>
                    <p style="margin: 0 0 8px 0; color: #2E86AB; font-size: 12pt; font-weight: bold;">{{exp.company}}</p>
                    <p style="font-size: 11pt; margin: 0; line-height: 1.5;">{{exp.description}}</p>
                </div>
                {% endfor %}
            </div>
            
            <!-- Education -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Education</h2>
                {% for edu in education %}
                <div style="margin-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h3 style="margin: 0; color: #333; font-size: 12pt; font-weight: bold;">{{edu.degree}}</h3>
                        <span style="color: #666; font-size: 10pt;">{{edu.year}}</span>
                    </div>
                    <p style="margin: 5px 0; color: #2E86AB; font-size: 11pt; font-weight: bold;">{{edu.institution}}</p>
                </div>
                {% endfor %}
            </div>
            
            <!-- Additional Sections -->
            {% if certifications %}
            <div style="margin-bottom: 25px;">
                <h2 style="color: #2E86AB; font-size: 16pt; font-weight: bold; margin-bottom: 10px; border-bottom: 2px solid #2E86AB; padding-bottom: 3px;">Certifications</h2>
                <p style="font-size: 11pt; margin: 0;">{{certifications}}</p>
            </div>
            {% endif %}
        </div>
        """,
        
        "ats_friendly": """
        <div style="font-family: Arial, sans-serif; max-width: 8.5in; margin: 0 auto; padding: 0.75in; line-height: 1.4; color: #000;">
            <!-- Header Section -->
            <div style="text-align: center; margin-bottom: 30px;">
                <h1 style="color: #000; margin: 0; font-size: 24pt; font-weight: bold; text-transform: uppercase;">{{personal_info.name}}</h1>
                <p style="color: #000; margin: 8px 0; font-size: 12pt; font-weight: bold;">{{personal_info.title or 'Professional'}}</p>
                <p style="color: #000; margin: 5px 0; font-size: 11pt;">{{personal_info.email}} | {{personal_info.phone}} | {{personal_info.location}}</p>
                {% if personal_info.linkedin %}<p style="color: #000; margin: 5px 0; font-size: 11pt;">LinkedIn: {{personal_info.linkedin}}</p>{% endif %}
            </div>
            
            <!-- Professional Summary -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; font-size: 16pt; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">PROFESSIONAL SUMMARY</h2>
                <hr style="border: 1px solid #000; margin-bottom: 10px;">
                <p style="font-size: 11pt; margin: 0; text-align: justify;">{{summary}}</p>
            </div>
            
            <!-- Core Competencies -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; font-size: 16pt; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">CORE COMPETENCIES</h2>
                <hr style="border: 1px solid #000; margin-bottom: 10px;">
                <p style="font-size: 11pt; margin: 0;">{{skills}}</p>
            </div>
            
            <!-- Professional Experience -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; font-size: 16pt; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">PROFESSIONAL EXPERIENCE</h2>
                <hr style="border: 1px solid #000; margin-bottom: 10px;">
                {% for exp in experience %}
                <div style="margin-bottom: 20px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                        <h3 style="margin: 0; color: #000; font-size: 14pt; font-weight: bold;">{{exp.title}}</h3>
                        <span style="color: #000; font-size: 11pt; font-weight: bold;">{{exp.duration}}</span>
                    </div>
                    <p style="margin: 0 0 8px 0; color: #000; font-size: 12pt; font-weight: bold;">{{exp.company}}</p>
                    <p style="font-size: 11pt; margin: 0; line-height: 1.5;">{{exp.description}}</p>
                </div>
                {% endfor %}
            </div>
            
            <!-- Education -->
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; font-size: 16pt; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">EDUCATION</h2>
                <hr style="border: 1px solid #000; margin-bottom: 10px;">
                {% for edu in education %}
                <div style="margin-bottom: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h3 style="margin: 0; color: #000; font-size: 12pt; font-weight: bold;">{{edu.degree}}</h3>
                        <span style="color: #000; font-size: 11pt; font-weight: bold;">{{edu.year}}</span>
                    </div>
                    <p style="margin: 5px 0; color: #000; font-size: 11pt; font-weight: bold;">{{edu.institution}}</p>
                </div>
                {% endfor %}
            </div>
            
            <!-- Additional Sections -->
            {% if certifications %}
            <div style="margin-bottom: 25px;">
                <h2 style="color: #000; font-size: 16pt; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">CERTIFICATIONS</h2>
                <hr style="border: 1px solid #000; margin-bottom: 10px;">
                <p style="font-size: 11pt; margin: 0;">{{certifications}}</p>
            </div>
            {% endif %}
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
