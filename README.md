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

```bash
python text_to_video.py
```

4. **Output:**

- Generated images will be saved in the generated_images/ directory.
- Interpolated frames will be saved in the interpolated_frames/ directory.
- The final video will be saved as output_video.mp4.

### Sample Output:


https://github.com/user-attachments/assets/b0c15564-ff8a-45cd-9086-fc65706aea63



## Project Workflow

1. **Image Generation:**

- Generate a series of images using Stable Diffusion XL based on text prompts.

- Example prompt:

```bash
"highly detailed sleek sports car in anime style, glossy finish, dramatic lighting, 8k uhd, hyperrealistic"
```

2. **Interpolation:**

- Interpolate between consecutive images to create smooth transitions.
- Adjust the number of interpolations using num_interpolations.

3. **Video Creation:**

- Combine interpolated frames into a video using FFmpeg.
- The video runs at 30 frames per second.

## Customization

- **Modify Prompts:** Edit the background_variations list in the script to define new prompts for different visual styles.

- **Change Output Directories:** Update output_dir and interpolated_output_dir to save outputs in custom locations.

- **Adjust Video Settings:** Modify the FFmpeg command for custom frame rates or resolutions:

```bash
os.system("ffmpeg -r <frame_rate> -f image2 -s <width>x<height> -i interpolated_frames/frame_%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p output_video.mp4")
```

## Contribution

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

1. Fork the repository.
  
2.  Create a new branch:
```bash
git checkout -b feature-name
```

3. Commit changes and push:
```bash
git commit -m "Add feature"
git push origin feature-name
```

4. Submit a pull request.

## Acknowledgments
- Stable Diffusion XL: Provided by stability.ai.
- FFmpeg: Used for video generation.
- PyTorch and Diffusers: Libraries for AI and machine learning.

## Author

Prashant singh

Contact: [prashantsingha96@gmail.com]
