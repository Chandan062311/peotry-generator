import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    model_name = "EleutherAI/gpt-neo-125M"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    
    prompt = "Once upon a time"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=50)
    
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Generated Text:", generated_text)

if __name__ == "__main__":
    main()