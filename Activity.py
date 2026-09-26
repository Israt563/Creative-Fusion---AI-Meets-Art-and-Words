#!/usr/bin/env python3
# Single Image AI Captions - Clean Hub Version
import os
from PIL import Image
from huggingface_hub import InferenceClient

# ==========================================
# PASTE YOUR HUGGING FACE API KEY HERE:
HF_API_KEY = "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"
# ==========================================

MODEL = "Salesforce/blip-image-captioning-base"

def main():
    path = input("Enter image filename (default: test.jpg): ").strip()
    if not path:
        path = "test.jpg"
        
    if not os.path.isfile(path):
        print(f"\n--- Caption Failed ---")
        print(f"Image   : {path}")
        print(f"Error   : File not found in this folder.")
        print("-" * 22)
        return
        
    try:
        print("⏳ Connecting to Hugging Face AI...")
        
        # Initialize client explicitly pointing to the free hf-inference provider
        client = InferenceClient(token=HF_API_KEY, provider="hf-inference")
        
        with Image.open(path) as img:
            caption = client.image_to_text(image=img, model=MODEL)
            
        print("\n--- AI Caption Success ---")
        print(f"Image   : {path}")
        print(f"Caption : {caption}")
        print("-" * 26)
        
    except Exception as e:
        print(f"\n--- Caption Failed ---")
        print(f"Image   : {path}")
        print(f"Error   : {str(e)}")
        print("-" * 22)

if __name__ == "__main__":
    main()