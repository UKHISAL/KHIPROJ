from diffusers import StableDiffusionPipeline
import torch
import os
from datetime import datetime

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    use_safetensors=True
).to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt, output_dir="generated_images"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Generating image for: '{prompt}'...")
    image = pipe(prompt).images[0]

    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    filepath = os.path.join(output_dir, filename)
    image.save(filepath)
    print(f"Image saved at: {filepath}")

# Example usage
if __name__ == "__main__":
    prompt = input("Enter a text prompt: ")
    generate_image(prompt)
