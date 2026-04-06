import re
import os

def extract_email(text):
    """Extracts email addresses from text using regex."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    matches = re.findall(email_pattern, text)
    return matches[0] if matches else None

def extract_name(text):
    """
    Extracts name using a simple heuristic:
    Assumes the name is on the first non-empty line.
    """
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if lines:
        return lines[0]
    return None

def extract_skills(text, skills_list):
    """
    Matches skills from the text against a provided list.
    Case-insensitive matching.
    """
    found_skills = []
    text_lower = text.lower()
    for skill in skills_list:
        if skill.lower() in text_lower:
            found_skills.append(skill)
    return found_skills

def parse_resume(file_path, skills_db):
    """
    Parses a resume file and extracts information.
    Currently supports .txt files.
    """
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    try:
        text = ""
        if file_path.lower().endswith('.pdf'):
            try:
                from pypdf import PdfReader
                reader = PdfReader(file_path)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            except ImportError:
                return {"error": "pypdf library not found. Please install it using 'pip install pypdf'"}
        else:
            # Assume text file
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            
        return {
            "name": extract_name(text),
            "email": extract_email(text),
            "skills": extract_skills(text, skills_db)
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Sample Skills Database
    SKILLS_DB = ["Python", "Java", "C++", "SQL", "Machine Learning", "Data Analysis", "Communication", "Project Management"]
    
    # Create a dummy resume for testing if it doesn't exist
    sample_file = "sample_resume.txt"
    if not os.path.exists(sample_file):
        with open(sample_file, "w", encoding="utf-8") as f:
            f.write("John Doe\n")
            f.write("Software Engineer\n")
            f.write("john.doe@example.com\n\n")
            f.write("Experience:\n")
            f.write("Worked on various Python projects using SQL and Machine Learning.\n")
            f.write("Good communication skills.\n")
        print(f"Created {sample_file} for testing.")

    # Test the parser
    result = parse_resume(sample_file, SKILLS_DB)
    print("Parsed Data:")
    print(result)
