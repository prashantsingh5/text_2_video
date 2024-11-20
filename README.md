# Text-to-Video Generator

This project is a **Text-to-Video Generator** that creates videos from text prompts using Stable Diffusion XL. The process involves generating images from text, interpolating between the images to create smooth transitions, and combining the frames into a video.

## Features

- **Text-to-Image Generation**: Uses Stable Diffusion XL to generate high-quality images from text prompts.
- **Frame Interpolation**: Smooth transitions between images by interpolating frames.
- **Video Creation**: Combines frames into a video using FFmpeg.
- **Customizable Prompts**: Easily modify prompts for unique outputs.
- **GPU Support**: Leverages GPU for faster processing if available.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.8+**
- **PyTorch**: Install it from [PyTorch.org](https://pytorch.org/).
- **diffusers library**: For Stable Diffusion XL.
- **Pillow**: For image processing.
- **FFmpeg**: For video generation.

1. To install the required Python libraries:

```bash
pip install torch torchvision diffusers pillow
```

2. Install FFmpeg based on your system:

- On Windows: Download from FFmpeg.org[https://ffmpeg.org/].

## How to Run

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/text-to-video-generator.git
   cd text-to-video-generator
  ```

2. **Set Up the Environment:** Ensure the prerequisites are installed as mentioned above.

3. **Run the Script:** Execute the script to generate images, interpolate frames, and create a video:
