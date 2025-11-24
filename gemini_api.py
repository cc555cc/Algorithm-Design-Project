import google.generativeai as genai


genai.configure(api_key="YOUR_GEMINI_API_KEY")

def ask_gemini(question: str) -> str:
    """
    Sends a question to Gemini API and returns response text.
    """
    try:
        model = genai.GenerativeModel("gemini-1.0-pro")
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Gemini API Error: {str(e)}"
