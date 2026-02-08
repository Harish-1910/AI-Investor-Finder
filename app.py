from flask import Flask, render_template, request
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def home():
    investors = []
    sector = None   
    country = None

    if request.method == "POST":
        sector = request.form.get("sector")
        country = request.form.get("country")

        prompt = f"""
        Suggest 3 investors who invest in the {sector} sector in {country}.
        Return strictly in this format:
        Investor Name | Reason
        """

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        output = completion.choices[0].message.content

        for line in output.split("\n"):
            if "|" in line:
                name, reason = line.split("|", 1)
                investors.append({
                    "name": name.strip(),
                    "reason": reason.strip()
                })

    return render_template(
        "index.html",
        investors=investors,
        sector=sector
    )
 
 
if __name__ == "__main__":
    app.run()