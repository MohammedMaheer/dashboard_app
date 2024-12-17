import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import logging
import gradio as gr

class StableDiffusionImageGenerator:
    """
    A robust class for generating images using Stable Diffusion with advanced configuration and error handling.
    """
   
    def __init__(self, 
                 model_name="runwayml/stable-diffusion-v1-5", 
                 torch_dtype=torch.float16, 
                 log_level=logging.INFO):
        # Initialization code

    @staticmethod
    def _dummy_safety_checker(images, **kwargs):
        return images, [False] * len(images)
   
    def generate_image(self, prompt: str, num_inference_steps: int = 30, guidance_scale: float = 7.5, seed: int = None) -> Image.Image:
        # Image generation code

    def _sanitize_prompt(self, prompt: str) -> str:
        # Sanitize prompt code

def create_interface():
    generator = StableDiffusionImageGenerator()

    def generate(prompt):
        image = generator.generate_image(prompt)
        return image

    interface = gr.Interface(
        fn=generate,
        inputs="text",
        outputs="image",
        title="Stable Diffusion Image Generator",
        description="Generate images from text prompts using Stable Diffusion.",
        theme="default",
        layout="vertical",
        live=False
    )
    interface.launch(share=True)

if __name__ == "__main__":
    create_interface()
