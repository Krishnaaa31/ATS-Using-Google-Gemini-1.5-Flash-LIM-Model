# ATS Using Google Gemini 1.5 Flash LIM Model

## Overview
This project introduces an advanced Application Tracking System (ATS) that utilizes the Google Gemini 1.5 Flash LIM Model to automate and optimize the recruitment process. The system employs state-of-the-art machine learning and natural language processing (NLP) techniques to efficiently parse, evaluate, and rank resumes, ensuring streamlined candidate screening and improved decision-making for recruiters.

## Features
- **Automated Resume Parsing:** Extracts critical information such as contact details, skills, work experience, and education.
- **Keyword Matching:** Analyzes resumes for specific keywords and phrases relevant to job descriptions.
- **Skill Assessment:** Identifies and evaluates candidates' technical and soft skills.
- **Experience Analysis:** Prioritizes candidates based on the relevance and depth of their experience.
- **Customizable:** Easily adaptable to different industries, job roles, and recruitment workflows.

## Technologies Used
- **Google Gemini 1.5 Flash LIM Model:** Powers the core NLP and machine learning capabilities.
- **Python:** Primary programming language for development.
- **Natural Language Processing (NLP):** Enables parsing and semantic analysis of resumes.
- **Machine Learning:** Implements candidate ranking and skill matching algorithms.
- **Frameworks/Libraries:** TensorFlow, PyTorch, spaCy, and scikit-learn.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/ats-google-gemini.git
   cd ats-google-gemini
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Google Gemini 1.5 Model:**
   Follow the instructions [here](https://gemini.google.com/docs) to access and integrate the Gemini 1.5 Flash LIM Model into your project.

5. **Run the Application:**
   ```bash
   python main.py
   ```

## Usage
1. **Input Resumes:** Upload resumes in supported formats (PDF, DOCX, etc.).
2. **Job Description:** Provide the job description to customize the parsing and evaluation process.
3. **Run Analysis:** The system will parse and rank candidates based on relevance.
4. **Review Results:** Access a detailed report with rankings and recommendations.

## Directory Structure
```
ats-google-gemini/
├── data/                # Sample resumes and job descriptions
├── models/              # Pretrained model and related files
├── src/                 # Source code for the application
│   ├── parsing/         # Modules for resume parsing
│   ├── ranking/         # Candidate ranking algorithms
│   └── utils/           # Utility functions and helpers
├── tests/               # Test cases for the application
├── requirements.txt     # Dependencies
├── main.py              # Entry point for the application
└── README.md            # Project documentation
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Special thanks to the Google team for providing the Gemini 1.5 Flash LIM Model.
- Inspiration from various open-source ATS tools and machine learning resources.

## Contact
For questions, suggestions, or collaboration opportunities, please reach out at [km9833988906@gmail.com].
