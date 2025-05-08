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

Fooocus is designed to be user-friendly, with many optimizations happening automatically "under the hood" to improve image quality. It's an excellent tool for both beginners and experienced users looking for a powerful yet streamlined image generation experience.

<br>

## AUTOMATIC1111 Stable Diffusion web UI (Intermediate)

<br>

## ComfyUI (Expert)

<br>
