from flask import Flask, render_template, request
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from config import ProductionConfig, DevelopmentConfig
import os

app = Flask(__name__)
app.config.from_object(ProductionConfig if os.environ.get('FLASK_ENV') == 'production' else DevelopmentConfig)

# Load model and tokenizer once during startup
model_name = "EleutherAI/gpt-neo-125M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.route("/", methods=["GET", "POST"])
def index():
    generated_text = ""
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        inputs = tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=200,
                num_return_sequences=1,
                temperature=0.9,
                top_p=0.9,
                do_sample=True
            )
        # Clean up the generated text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Remove the prompt from the beginning
        generated_text = generated_text.replace(prompt, "", 1).strip()
        
    return render_template("index.html", generated_text=generated_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config['DEBUG'])