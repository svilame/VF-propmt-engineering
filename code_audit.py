import os
import sys
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def audit_code(code: str):
    prompt = f"""
You are a senior software auditor. Analyze the code below for the following aspects:

1. **Bugs** – Logical or runtime errors
2. **Security Issues** – Input sanitization, insecure function usage, OWASP Top 10 risks
3. **Code Style Violations** – PEP8 compliance, naming conventions
4. **Performance Problems** – Inefficiencies, unnecessary loops, API/memory optimizations
5. **Code Complexity** – Nested loops, long functions, cyclomatic complexity
6. **Test Coverage** – Identify missing unit tests and critical logic not covered
7. **Documentation Quality** – Missing or unclear comments/docstrings

---
Code to Audit:
{code}
---

Return a detailed report with:
- Detected issues (section-wise)
- Suggested improvements
- Corrected code version (if applicable)
"""
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    filepath = sys.argv[1]
    with open(filepath, "r") as file:
        code = file.read()
    report = audit_code(code)
    print(report)
