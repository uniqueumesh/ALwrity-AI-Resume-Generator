# 📄 ALwrity AI Resume Generator

Generate professional resumes with AI assistance using Streamlit and Gemini 2.5 Flash.

## 🚀 Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get Gemini API Key**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Create a free account and generate an API key

3. **Run the App**
   ```bash
   streamlit run app.py
   ```

4. **Open in Browser**
   - The app will open at `http://localhost:8501`

## ✨ Features

- 🤖 AI-powered resume generation
- 🎨 Multiple professional templates
- 🎯 Job-specific optimization
- 📱 Simple, user-friendly interface
- 💾 Download as HTML
- 🔄 Real-time preview

## 🎨 Templates

- **Modern**: Clean, contemporary design
- **Professional**: Corporate, traditional style
- **Creative**: Design-focused layout
- **ATS-Friendly**: Optimized for applicant tracking systems

## 🔧 Configuration

Copy `env_example.txt` to `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## 📝 Usage

1. Enter your Gemini API key in the sidebar
2. Fill in your personal information
3. Add work experience and education
4. Optionally paste a job description for optimization
5. Choose a template
6. Click "Generate Resume"
7. Preview and download your resume

## 🛠️ Project Structure

```
ALwrity-AI-Resume-Generator/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
├── config.py             # Configuration & API keys
├── env_example.txt       # Environment variables template
├── utils/
│   ├── ai_helper.py      # Gemini AI integration
│   └── resume_generator.py # Resume generation logic
└── README.md
```

## 🤝 Contributing

This is a free and open-source project. Contributions are welcome!

## 📄 License

MIT License - see LICENSE file for details.
