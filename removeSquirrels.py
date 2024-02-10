# -*- coding: utf-8 -*-
"""removeSquirrels.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14KtGUc0TdkZBziTvIu1TSc4B-i1wvPWE
"""

!pip install diffusers
!pip install transformers

import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from diffusers import StableDiffusionInpaintPipeline
import torch

def initialize_inpaint_pipeline():
    """
    Initialize the inpainting pipeline using StableDiffusionInpaintPipeline.
    Returns:
        inpaint_pipeline (StableDiffusionInpaintPipeline): Initialized inpainting pipeline.
    """
    inpaint_pipeline = StableDiffusionInpaintPipeline.from_pretrained(
        "runwayml/stable-diffusion-inpainting",
        torch_dtype=torch.float32
    )
    inpaint_pipeline = inpaint_pipeline.to("cpu")
    return inpaint_pipeline

def remove_squirrels(input_images, input_masks, inpaint_pipeline):
    """
    Remove squirrels from input images using image inpainting.

    Args:
        input_images (list): List of paths to input image files.
        input_masks (list): List of paths to mask image files corresponding to the input images.
        inpaint_pipeline (StableDiffusionInpaintPipeline): Inpainting pipeline for performing image inpainting.
    """
    for i in range(len(input_images)):
        image_path = input_images[i]
        mask_path = input_masks[i]

        # Load the input image and mask from file paths
        input_image = PIL.Image.open(image_path).convert("RGB").resize((512, 512))
        input_mask = PIL.Image.open(mask_path).convert("RGB").resize((512, 512))

        # Perform image inpainting to remove squirrels
        output_image = inpaint_pipeline(prompt="", image=input_image, mask_image=input_mask).images[0]

        # Save the output image with "squirrelsRemoved" appended to the filename
        output_filename = image_path.replace(".jpg", "-squirrelsRemoved.jpg")
        output_image.save(output_filename)

def main():
    # Initialize the inpainting pipeline
    inpaint_pipeline = initialize_inpaint_pipeline()

    # Example input image and mask files
    input_image_files = [
    "squirrel1.jpg",
    "squirrel2.jpg",
    "squirrel3.jpg",
    "squirrel4.jpg",
    "squirrel5.jpg",
]

    input_mask_files =[
    "squirrel1_mask.jpg",
    "squirrel2_mask.jpg",
    "squirrel3_mask.jpg",
    "squirrel4_mask.jpg",
    "squirrel5_mask.jpg",
]

    # Remove squirrels from images using inpainting
    remove_squirrels(input_image_files, input_mask_files, inpaint_pipeline)

# Call the main function
if __name__ == "__main__":
    main()

