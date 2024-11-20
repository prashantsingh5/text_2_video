import torch
from diffusers import DiffusionPipeline
from PIL import Image
import os

# Define device (use GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the pre-trained Stable Diffusion XL model
model_id = "stabilityai/stable-diffusion-xl-base-1.0"  # Free Stable Diffusion XL model
pipe = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to(device)

# Enable slicing for memory optimization (VRAM usage)
pipe.enable_attention_slicing()

# Define the base prompt and variations
base_prompt = "highly detailed sleek sports car in anime style, glossy finish, dramatic lighting, perfect centering, straight view, clean white background, studio lighting, 8k uhd, hyperrealistic"

# Car color variations with consistent styling
background_variations = [
    "highly detailed sleek pure white sports car in anime style, glossy pearl finish, dramatic lighting, perfect centering, straight view, clean white background, studio lighting, 8k uhd, hyperrealistic",
    "highly detailed sleek cherry red sports car in anime style, glossy metallic finish, dramatic lighting, perfect centering, straight view, clean white background, studio lighting, 8k uhd, hyperrealistic",
    "highly detailed sleek electric blue sports car in anime style, glossy metallic finish, dramatic lighting, perfect centering, straight view, clean white background, studio lighting, 8k uhd, hyperrealistic",
    "highly detailed sleek emerald green sports car in anime style, glossy metallic finish, dramatic lighting, perfect centering, straight view, clean white background, studio lighting, 8k uhd, hyperrealistic",
    "highly detailed sleek sunburst orange sports car in anime style, glossy metallic finish, dramatic lighting, perfect centering, straight view, clean white background, studio lighting, 8k uhd, hyperrealistic",
    "highly detailed sleek royal purple sports car in anime style, glossy metallic finish, dramatic lighting, perfect centering, straight view, clean white background, studio lighting, 8k uhd, hyperrealistic",
    "highly detailed sleek silver sports car in anime style, chrome metallic finish, dramatic lighting, perfect centering, straight view, clean white background, studio lighting, 8k uhd, hyperrealistic",
    "highly detailed sleek golden sports car in anime style, glossy metallic finish, dramatic lighting, perfect centering, straight view, clean white background, studio lighting, 8k uhd, hyperrealistic",
    "highly detailed sleek hot pink sports car in anime style, glossy metallic finish, dramatic lighting, perfect centering, straight view, clean white background, studio lighting, 8k uhd, hyperrealistic",
]

# Rest of the code remains unchanged
# Create a folder to save frames
output_dir = "generated_images"
os.makedirs(output_dir, exist_ok=True)

# Number of images to generate
num_frames = len(background_variations)

# Generate images with controlled variations
for i, prompt in enumerate(background_variations):
    seed = 42  # Fixed seed for consistent image generation
    generator = torch.manual_seed(seed)

    # Generate image from modified prompt
    image = pipe(prompt, generator=generator, num_inference_steps=50, guidance_scale=7.5).images[0]
    
    # Save the image
    image_path = os.path.join(output_dir, f"image_{i}.png")
    image.save(image_path)

    print(f"Image {i} saved: {image_path}")

print(f"{num_frames} images generated and saved in {output_dir}")

# Define how many interpolated frames you want between each original pair of images
num_interpolations = 30

# Folder to save interpolated frames
interpolated_output_dir = "interpolated_frames"
os.makedirs(interpolated_output_dir, exist_ok=True)

# Interpolate between consecutive images
def interpolate_images(image1, image2, alpha):
    """Interpolate between two images based on alpha (0.0 to 1.0)."""
    return Image.blend(image1, image2, alpha)

for i in range(num_frames - 1):
    image1_path = os.path.join(output_dir, f"image_{i}.png")
    image2_path = os.path.join(output_dir, f"image_{i + 1}.png")
    
    # Save the original image
    original_image = Image.open(image1_path)
    original_image.save(os.path.join(interpolated_output_dir, f"frame_{i * (num_interpolations + 1)}.png"))
    
    # Create interpolated frames between two images
    for j in range(1, num_interpolations + 1):
        alpha = j / (num_interpolations + 1)
        interpolated_image = interpolate_images(Image.open(image1_path), Image.open(image2_path), alpha)
        interpolated_image.save(os.path.join(interpolated_output_dir, f"frame_{i * (num_interpolations + 1) + j}.png"))

# Save the last image of the sequence
final_image = Image.open(os.path.join(output_dir, f"image_{num_frames - 1}.png"))
final_image.save(os.path.join(interpolated_output_dir, f"frame_{(num_frames - 1) * (num_interpolations + 1)}.png"))

print(f"Interpolated frames saved in {interpolated_output_dir}")

# Create a video from interpolated frames using FFmpeg
os.system("ffmpeg -r 30 -f image2 -s 512x512 -i interpolated_frames/frame_%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p output_video.mp4")