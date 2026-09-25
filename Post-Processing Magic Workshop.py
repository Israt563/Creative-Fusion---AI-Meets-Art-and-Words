import os
from io import BytesIO
from PIL import Image, ImageEnhance, ImageFilter
from huggingface_hub import InferenceClient

# ⚠️ PASTE YOUR ACTUAL FINE-GRAINED HUGGING FACE TOKEN HERE
HF_API_KEY = "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"

# Initialize InferenceClient cleanly without forcing broken raw routing URLs
client = InferenceClient(api_key=HF_API_KEY)
MODEL = "black-forest-labs/FLUX.1-schnell"


def generate_image_from_text(prompt):
  """Generates image using InferenceClient and returns a PIL.Image."""
  try:
    # Let the client handle communication with the provider backend
    image = client.text_to_image(prompt, model=MODEL)
    return image.convert("RGB")
  except Exception as e:
    raise Exception(f"Generation failed: {e}")


def post_process_image(image):
  """Applies brightness, contrast, and subtle blur effects."""
  image = ImageEnhance.Brightness(image).enhance(1.2)
  image = ImageEnhance.Contrast(image).enhance(1.3)
  return image.filter(ImageFilter.GaussianBlur(radius=1))


def main():
  print("Welcome to the Post-Processing Magic Workshop!")
  print(
      "This program generates an image from text and applies post-processing"
      " effects."
  )
  print("Type 'exit' to quit.\n")

  while True:
    user_input = input(
        "Enter a description for the image (or 'exit' to quit):\n"
    ).strip()
    if user_input.lower() == "exit":
      print("Goodbye!")
      break
    if not user_input:
      continue

    try:
      print("\nGenerating image (takes ~10 seconds)...")
      image = generate_image_from_text(user_input)

      print("Applying post-processing effects...\n")
      processed_image = post_process_image(image)
      processed_image.show()

      save_option = (
          input("Do you want to save the processed image? (yes/no): ")
          .strip()
          .lower()
      )
      if save_option == "yes":
        file_name = input(
            "Enter a name for the image file (without extension): "
        ).strip()
        filename_full = f"{file_name}.png"
        processed_image.save(filename_full)
        print(f"Image saved as {filename_full}\n")

      print("-" * 80 + "\n")
    except Exception as e:
      print(f"❌ An error occurred: {e}\n")


if __name__ == "__main__":
  main()