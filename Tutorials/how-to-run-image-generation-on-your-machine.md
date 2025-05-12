<div align="center"> 
 
<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Tutorials/ImageGeneration.png">

<br>
<br>

 ***This guide explains how to set up and run Image Generation models on your computer, enabling you to maintain full control over your AI Image workflows.***

 ***<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20with%20Monocle.png" alt="Face with Monocle" width="25" height="25" /> Reading Time : 12min***
 
 <br>

</div> 

## Table of Contents

- [Introduction](#introduction)
- [Hardware Requirement](#hardware-requirement)
- [Find the Model that is right for you](#find-the-model-that-is-right-for-you)
- [Fooocus (Beginner)](#fooocus)
- [AUTOMATIC1111 Stable Diffusion web UI (Intermediate)](#automatic1111-stable-diffusion-web-ui)
- [ComfyUI (Expert)](#comfyui)

<br>

## Introduction

Fooocus provides **stable diffusion image generation capabilities on local hardware**, offering creative control and privacy-focused artwork creation. This offline implementation **enables unrestricted experimentation with styles, prompts, and generation parameters.**

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Backhand%20Index%20Pointing%20Right.png" alt="Backhand Index Pointing Right" width="25" height="25" /> **Key Benefit: Generate AI art independently without cloud services or usage limitations.**

## Hardware Requirement

To run Image generation on your machine, Your hardware configuration **must meet these specifications for optimal performance.** Lower specifications may impact generation speed and quality.

| Operating System  | GPU                          | Minimal GPU Memory           | Minimal System Memory     | [System Swap](https://github.com/lllyasviel/Fooocus/blob/main/troubleshoot.md) | Note                                                                       |
|:-----------------:|:----------------------------:|:----------------------------:|:-------------------------:|:------------------------------:|:---------------------------------------------------------------------------|
| Windows/Linux     | Nvidia RTX 4XXX              | 4GB                          | 8GB                       | Required                       | fastest                                                                    |
| Windows/Linux     | Nvidia RTX 3XXX              | 4GB                          | 8GB                       | Required                       | usually faster than RTX 2XXX                                               |
| Windows/Linux     | Nvidia RTX 2XXX              | 4GB                          | 8GB                       | Required                       | usually faster than GTX 1XXX                                               |
| Windows/Linux     | Nvidia GTX 1XXX              | 8GB (6GB uncertain)          | 8GB                       | Required                       | only marginally faster than CPU                                            |
| Windows/Linux     | Nvidia GTX 9XX               | 8GB                          | 8GB                       | Required                       | faster or slower than CPU                                                  |
| Windows/Linux     | Nvidia GTX < 9XX             | Not supported                | /                         | /                              | /                                                                          |
| Windows           | AMD GPU                      | 8GB    (updated 2023 Dec 30) | 8GB                       | Required                       | via DirectML (&ast; ROCm is on hold), about 3x slower than Nvidia RTX 3XXX |
| Linux             | AMD GPU                      | 8GB                          | 8GB                       | Required                       | via ROCm, about 1.5x slower than Nvidia RTX 3XXX                           |
| Mac               | M1/M2 MPS                    | Shared                       | Shared                    | Shared                         | about 9x slower than Nvidia RTX 3XXX                                       |
| Windows/Linux/Mac | **only use CPU**             | 0GB                          | 32GB                      | Required                       | **about 17x slower than Nvidia RTX 3XXX**                                      |

<br>

## Find the Model that is right for you

:TODO: List of best Open source text to image models

<br>

## Fooocus (Beginner)

Fooocus is an open-source AI image generation tool that simplifies the use of Stable Diffusion, making it accessible for users to create high-quality visuals. It requires minimal setup and can run on systems with a GPU (Nvidia) with 4GB of memory and 8GB of RAM.

### Installation
1.  Download the Fooocus files from its [official GitHub repository](https://github.com/lllyasviel/Fooocus).
2.  Extract the downloaded files to your desired location on your computer (e.g., your desktop).
3.  Locate and run the `run.bat` file (for Windows). This will initiate the download and installation of necessary files, including the default Stable Diffusion XL model (e.g., Juggernaut XL). The first time you run it, it will download a checkpoint file which contains the image data. This might take some time.
4.  Once the setup is complete, a web page (usually `http://127.0.0.1:7865/`) will automatically open in your default web browser. This is the Fooocus interface where you can begin generating images.

Alternatively, you can use online platforms that host Fooocus (like Google Colab notebooks, or services like MimicPC) to run it without a local installation, though local installation gives you more control.

### Basic Image Generation
1.  Once Fooocus is running and the web interface is open, you'll see a prominent prompt input field at the bottom of the page.
2.  Type a detailed description of the image you want to create into this prompt box. For example: "a photorealistic portrait of an astronaut cat exploring a vibrant alien jungle, detailed fur, glowing plants".
3.  Click the "Generate" button. Fooocus will then process your prompt and generate images based on it. By default, it usually generates two images per prompt.

### Advanced Options

To access more granular controls and fine-tune your image generation, click the "Advanced" checkbox, typically located at the bottom of the interface, near the prompt input.

#### Key Advanced Settings:

*   **Performance Settings**:
    *   Located under the "Speed" tab (or similar).
    *   Adjust the trade-off between generation speed and image quality.
    *   Options typically include:
        *   **Speed**: Faster generation with a moderate number of steps (e.g., 30 steps). Good for quick iterations.
        *   **Quality**: Slower generation with more steps (e.g., 60 steps), often resulting in higher detail.
        *   **Extreme Speed**: Very fast generation with fewer steps (e.g., 8 steps), useful for rapid prototyping but may sacrifice quality.

*   **Aspect Ratios**:
    *   Found under the "Advanced" tab or near the prompt.
    *   Choose the desired dimensions and orientation for your output images (e.g., 1:1 square, 16:9 widescreen, 9:16 portrait). The same prompt can produce significantly different compositions based on this setting.

*   **Number of Images**:
    *   Also under the "Advanced" tab.
    *   Specify how many images you want Fooocus to generate at once for a single prompt (e.g., 1, 2, 4).

*   **Negative Prompt**:
    *   A separate input field within the "Advanced" options.
    *   Input terms for elements, styles, or artifacts you want to *exclude* from your image. For instance, you can add "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, blurry, bad anatomy, blurred, watermark, grainy, signature, cut off, draft, low quality, noise, text, words" to improve results.

*   **Style**:
    *   Found under the "Style" tab.
    *   Fooocus offers a wide range of predefined styles. You can select multiple styles to combine their effects.
    *   Examples: "Fooocus V2", "Fooocus Enhance", "Fooocus Sharp", "Photorealistic", "Cinematic", "Anime", "Impressionism", etc. Experiment with these to drastically change the look and feel of your images.

*   **Model Selection**:
    *   Under the "Model" tab.
    *   **Base Model**: Choose the primary Stable Diffusion model Fooocus will use (e.g., JuggernautXL, SDXL Base). You can download additional models and place them in the `Fooocus\models\checkpoints` folder.
    *   **Refiner Model**: Optionally, select a refiner model that can enhance the details of the generated image. This is often used in a second pass.
    *   **LoRAs (Low-Rank Adaptations)**: Select up to five LoRAs. LoRAs are smaller, fine-tuned models that can add specific styles, characters, or concepts. You can adjust the weight (influence) of each LoRA. Place LoRA files in `Fooocus\models\loras`.

*   **Advanced Tab (Fine-tuning)**:
    *   **Guidance Scale (CFG Scale)**: Controls how strictly the AI adheres to your prompt. Lower values (e.g., 4-7) give the AI more creative freedom, while higher values (e.g., 7-12) make it follow the prompt more closely. Default is often around 7.
    *   **Image Sharpness**: Adjusts the clarity and detail of edges in the image. Lower settings produce softer, potentially blurrier edges, while higher settings create sharper images. Often a subtle effect.
    *   **Sampler & Scheduler**: These are more technical settings that determine how the noise is iteratively removed to form an image. For most users, the defaults work well. Common samplers include `dpmpp_2m_sde_gpu` and schedulers like `karras`.

### Image-to-Image Generation (Input Image)

Fooocus allows you to use existing images as a basis for new creations. Click the "Input Image" checkbox (usually below the prompt area) to reveal these features. This will open up several tabs: "Upscale or Variation", "Image Prompt", and "Inpaint or Outpaint".

#### Input Image Features:

*   **Upscale or Variation**:
    *   Upload an image to this section.
    *   **Vary (Subtle/Strong)**: Generate new versions of an uploaded image. "Subtle" makes minor changes, while "Strong" introduces more significant alterations while trying to retain the core subject.
    *   **Upscale (e.g., 1.5x, 2x, Fast 2x)**: Increase the resolution of an uploaded image. For example, the "Upscale (Fast 2x)" option is optimized for enlarging images like 2k to 4k. Select an option and click "Generate".

*   **Image Prompt**:
    *   Upload up to four reference images. These images, along with your text prompt, will guide the generation of new images.
    *   You can control the influence of each image prompt using options like "PyraCanny" (edge detection), "CPDS" (detail preservation), or "FaceSwap" (if you have a face in the image prompt and want to apply it).
    *   Adjust the "Stop At" and "Weight" parameters to control how much each image prompt influences the final result.

*   **Inpaint or Outpaint**:
    *   Upload an image. The interface will allow you to draw a mask over the image.
    *   **Inpainting**: Modify or add details *within* the selected (masked) area of an image. Provide a prompt describing what you want in the masked area (e.g., "add a red hat").
    *   **Outpainting**: Extend the image beyond its original borders. Mask the area *outside* the part you want to keep, or use the "Outpaint Direction" buttons. The AI will predict and generate the new areas based on your prompt and the existing image.
    *   You can choose the method (e.g., "Inpaint" or "Improve Detail").
    *   After setting up your image, mask, and prompt, click "Generate".

### Tips for Better Results

*   **Be Specific in Prompts**: The more detail you provide, the better Fooocus can understand your vision. Think about subject, action, environment, lighting, style, and composition.
*   **Iterate**: Don't expect the perfect image on the first try. Generate multiple images, pick the ones you like, and refine your prompts or use image-to-image features.
*   **Experiment with Styles**: The "Style" tab is very powerful. Combining a few well-chosen styles can dramatically improve your output.
*   **Use Negative Prompts**: This is crucial for avoiding common AI artifacts and unwanted elements.
*   **Check the Console**: If `run.bat` is still open in a command prompt window, it often shows progress and any errors, which can be helpful for troubleshooting.
*   **Update Fooocus**: The software is actively developed. Pull the latest updates from GitHub regularly to get new features and bug fixes by running `update.bat` or `git pull` if you cloned the repository.

<br>

## AUTOMATIC1111 Stable Diffusion web UI (Intermediate)

AUTOMATIC1111 Stable Diffusion Web UI (often abbreviated as A1111) is a popular browser-based interface for Stable Diffusion, a powerful AI model that generates images from text descriptions or modifies existing images based on prompts. It is known for its extensive features and is a go-to tool for users who want more control over their AI image generation. While packed with options, this guide will help you understand its core functionalities.

### Installation

Before using AUTOMATIC1111, you need to set it up on your system. The process generally involves installing Python, Git, and then downloading the Web UI files. For users with Nvidia GPUs, installing CUDA and cuDNN is highly recommended for faster image generation, though the Web UI can run on CPU as well (much slower).

**Steps for Installation (Windows Example):**
1.  **Set Up Python**: Install a compatible version of Python (check the A1111 GitHub page for recommended versions, typically Python 3.10.x). Ensure you add Python to your system's PATH during installation.
2.  **Install Git**: Download and install Git for Windows from [git-scm.com](https://git-scm.com/download/win).
3.  **Download AUTOMATIC1111**:
    *   Open Command Prompt (cmd).
    *   Navigate to your desired installation directory. For example, to install in your user profile: `cd %userprofile%` and press Enter.
    *   Clone the repository by typing `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git` and pressing Enter. This will create a `stable-diffusion-webui` folder in your chosen directory.
4.  **Add a Model File (Checkpoint)**:
    *   Navigate to the `stable-diffusion-webui\models\Stable-diffusion` folder within your installation directory.
    *   Download a Stable Diffusion model checkpoint file (e.g., `v1-5-pruned-emaonly.safetensors` for Stable Diffusion 1.5, or an SDXL base model like `sd_xl_base_1.0.safetensors`). You can find models on sites like Hugging Face or Civitai. Place the `.ckpt` or `.safetensors` file in this folder.
5.  **Run AUTOMATIC1111**:
    *   In File Explorer, go to the `stable-diffusion-webui` folder.
    *   Double-click the `webui-user.bat` file.
    *   A command prompt window will open and start the setup process, downloading necessary dependencies. This might take a while on the first run.
    *   Once it's ready, you'll see a message similar to: `Running on local URL: http://127.0.0.1:7860`.
    *   Open this URL in your web browser to access the AUTOMATIC1111 interface.

### Interface Overview

The AUTOMATIC1111 Web UI is organized into several key areas:

*   **Top Row**:
    *   **Stable Diffusion checkpoint**: Dropdown to select your primary model.
    *   **Tabs**: `txt2img`, `img2img`, `Extras`, `PNG Info`, `Checkpoint Merger`, `Train`, `Settings`, `Extensions`.

*   **Main Generation Area (e.g., `txt2img` tab)**:
    *   **Prompt Input**: Fields for your "Prompt" (what you want to see) and "Negative prompt" (what you want to avoid).
    *   **Generation Parameters**: Sliders and input boxes for settings like:
        *   Sampling method
        *   Sampling steps
        *   Width & Height
        *   Batch count & Batch size
        *   CFG Scale
        *   Seed
    *   **Generate Button**: The large orange button to start image generation.
    *   **Output Area**: Where generated images appear, along with options to save them or send them to other tabs.

You can change the default white theme to a dark theme by appending `?__theme=dark` to the URL (e.g., `http://127.0.0.1:7860/?__theme=dark`). This can also be set permanently in the Settings tab.

### Text-to-Image (`txt2img`) Tab

The `txt2img` tab is where you'll typically start, turning text prompts into images.

#### Basic Usage:
1.  **Select Checkpoint**: Choose your desired Stable Diffusion model from the "Stable Diffusion checkpoint" dropdown at the top left. If you've added new models to the `models\Stable-diffusion` folder, click the small blue refresh button next to the dropdown to update the list.
2.  **Enter Prompt**: In the "Prompt" text box, describe the image you want to create. Be specific.
    *   Example: `masterpiece, best quality, a majestic lion king sitting on a throne in a futuristic neon city, cinematic lighting`
    *   **Emphasis**: Use parentheses to increase or decrease a word's influence:
        *   `(word)`: increases attention by a factor of 1.1
        *   `((word))`: increases attention by a factor of 1.21 (1.1 * 1.1)
        *   `[word]`: decreases attention
        *   `(word:1.5)`: increases attention by a factor of 1.5
3.  **Enter Negative Prompt**: In the "Negative prompt" text box, list elements you want to exclude.
    *   Example: `(worst quality, low quality:1.4), ugly, blurry, deformed, watermark, text, signature, extra limbs, disfigured face`
4.  **Set Dimensions**:
    *   **Width** and **Height**: Set the dimensions for your output image. For SD 1.5 models, common sizes are 512x512, 512x768, or 768x512. For SDXL models, 1024x1024 or similar resolutions are standard.
5.  **Configure Batch Options**:
    *   **Batch count**: How many times to run the generation process sequentially. If set to 4, it will generate images four times.
    *   **Batch size**: How many images to generate in parallel during each run. If set to 2, and Batch count is 1, it will generate 2 images.
    *   Total images = Batch count * Batch size.
6.  Click the orange **Generate** button. Your images will appear in the output area on the right (or below).

#### Key Generation Parameters:

*   **Sampling method**: Algorithm used for denoising. Popular choices:
    *   `Euler a` (ancestral): Good for creative results, changes a lot with step count.
    *   `DPM++ 2M Karras`: High quality, often recommended.
    *   `DPM++ SDE Karras`: Similar to 2M Karras, can be good for photorealism.
    *   `UniPC`: Fast and good quality.
    Experiment to find what works best for your style and model.
*   **Sampling steps**: Number of iterations.
    *   For `Euler a`: 20-40 steps.
    *   For `DPM++` samplers: 20-30 steps are often sufficient.
    *   More steps generally mean more detail but longer generation time. Diminishing returns after a certain point.
*   **CFG Scale (Classifier Free Guidance Scale)**: How strictly the AI should follow your prompt.
    *   Low values (e.g., 3-6): More creative, less adherence to prompt.
    *   Medium values (e.g., 7-10): Balanced. Default is often 7.
    *   High values (e.g., 11-15+): Strong adherence, but can lead to overly saturated or "burnt" images if too high.
*   **Seed**: The initial noise pattern.
    *   Value of `-1` (default): Uses a random seed for each generation, producing different images.
    *   Specific number: Using the same seed, prompt, and all other settings will reproduce the *exact* same image.
    *   **Dice icon (🎲️)**: Sets the seed to -1 (random).
    *   **Recycle icon (♻️)**: Reuses the seed from the *last generated image in the current batch*.

#### Other Useful `txt2img` Features:

*   **Hires. fix**: Generates a higher-resolution image. It first creates a smaller image based on your main Width/Height, then upscales it in a second pass using a selected upscaler (e.g., `Latent`, `R-ESRGAN 4x+`).
    *   **Upscaler**: Choose the algorithm for upscaling.
    *   **Hires steps**: Steps for the upscaling pass.
    *   **Denoising strength**: How much the upscaler should change the initial low-res image. Lower values preserve more of the original structure. (0.3-0.7 is a common range).
*   **Refiner (primarily for SDXL models)**: Uses a secondary "refiner" model to add details to an image generated by the base SDXL model.
    *   **Refiner Checkpoint**: Select your SDXL refiner model.
    *   **Switch at**: Determines at what percentage of the sampling steps the process switches from the base model to the refiner (e.g., 0.8 means 80% base, 20% refiner).
*   **Restore faces**: Applies face correction algorithms (like GFPGAN or CodeFormer) to improve faces in the generated image. Check the box to enable.
*   **Tiling**: Creates images that can be seamlessly tiled, useful for patterns and textures.

### Image-to-Image (`img2img`) Tab

This tab allows you to upload an existing image and transform it using a text prompt.

#### Sub-tabs within `img2img`:

*   **img2img (default)**:
    1.  Upload your source image.
    2.  Write a prompt describing the desired changes or the new scene.
    3.  Adjust **Denoising strength**: This is crucial. It controls how much the original image is altered.
        *   `0.0 - 0.3`: Minor changes, preserves original image structure well.
        *   `0.4 - 0.7`: Moderate changes, good balance for style transfer or significant alterations.
        *   `0.7 - 1.0`: Major changes, original image may become unrecognizable.
*   **Sketch**: Upload an image and draw a simple color sketch on top of it to guide the generation.
*   **Inpaint**: Modify specific parts of an image.
    1.  Upload your image. A mask brush will appear.
    2.  Paint over the area you want to change.
    3.  Write a prompt describing what you want *in the masked area*.
    4.  Configure settings:
        *   **Mask blur**: How much to blur the edges of the mask.
        *   **Mask mode**:
            *   `Inpaint masked`: Changes the masked area.
            *   `Inpaint not masked`: Changes everything *except* the masked area.
        *   **Masked content**:
            *   `fill`: Fills with average color of the image (good for removing objects).
            *   `original`: Starts from the original pixels in the masked area.
            *   `latent noise/nothing`: Fills with noise/black (good for generating something new).
        *   **Inpaint area**:
            *   `Whole picture`: Processes the entire image, considering the masked area.
            *   `Only masked`: Processes only the masked region, potentially faster but less context-aware. Set padding for better blending.
    5.  Adjust **Denoising strength** as in `img2img`.
*   **Inpaint sketch**: Similar to Inpaint, but you draw your changes directly with colors.
*   **Inpaint upload**: Upload an image and a separate black-and-white mask image.
*   **Batch**: Process multiple images from an input directory.

### Other Important Tabs & Features

*   **Extras Tab**:
    *   **Upscaling**: Contains tools to upscale single or multiple images. Select an upscaler (e.g., `R-ESRGAN 4x+`, `SwinIR`, `LDSR`) and scale factor.
    *   **GFPGAN/CodeFormer**: Dedicated tools for face restoration on uploaded images.
*   **PNG Info Tab**:
    *   Drag and drop a PNG image generated by A1111 into this tab.
    *   It will display all the generation parameters (prompt, negative prompt, seed, steps, model, etc.) embedded in the image.
    *   Buttons allow you to send these parameters directly to `txt2img` or `img2img`, making it easy to recreate or iterate on past work.
*   **Checkpoint Merger Tab**:
    *   Allows you to combine up to three different checkpoint models to create new, custom models.
    *   Select Primary (A), Secondary (B), and Tertiary (C) models.
    *   Adjust the **Multiplier (M)** to control the weighting of model B (and C if used).
    *   Choose an **Interpolation Method** (e.g., "Weighted sum", "Add difference").
*   **Train Tab (Advanced)**:
    *   For creating your own embeddings (textual inversions), Hypernetworks, or training LoRAs/Dreambooth models. This is an advanced topic requiring more in-depth study.
*   **Settings Tab**:
    *   Contains a vast number of options to customize the Web UI's behavior, defaults, and optimizations.
    *   Useful settings:
        *   `User interface > Theme`: Set to dark or light.
        *   `Saving images/grids`: Configure how images are saved, filename patterns, quality.
        *   `Stable Diffusion > Apply color correction...`: Can help with image color consistency.
        *   `Optimizations`: Settings for performance, like `Cross-attention optimization method` (e.g., xFormers, sdp-no-mem, Doggettx). xFormers is highly recommended for Nvidia GPUs if available.
*   **Extensions Tab**:
    *   **Installed**: Shows your current extensions.
    *   **Available**: Lets you load a list of community-created extensions. Click "Load from:" to fetch the index.
    *   **Install from URL**: Install extensions directly from their Git repository URL.
    *   Popular extensions include ControlNet (for precise control over image composition), Regional Prompter, Deforum (for animations), etc. Remember to click "Apply and restart UI" after installing/uninstalling extensions.

### Tips for Better Results

*   **Start Simple**: Don't use too many complex keywords or settings at once.
*   **Iterate**: Generate, observe, refine your prompt, adjust settings, and generate again.
*   **Study Prompts**: Look at prompts from images you like (e.g., on Civitai or other image sharing sites) to learn how others structure them.
*   **Use Negative Prompts Actively**: This is crucial for cleaning up common AI artifacts.
*   **Experiment with Samplers and Steps**: Different combinations yield different results.
*   **Master Denoising Strength (in img2img)**: This is key to controlling how much an input image is changed.
*   **Save Your Best Seeds**: If you get a great result, note down the seed and other parameters.
*   **Explore LoRAs and Embeddings**: These can add specific styles, characters, or concepts to your generations. Place LoRAs in `stable-diffusion-webui\models\Lora` and embeddings in `stable-diffusion-webui\embeddings`. Use them in your prompt by typing `<lora:filename:weight>` or the embedding's trigger word.


<br>

## ComfyUI (Expert)

<br>
