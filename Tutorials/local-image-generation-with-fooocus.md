![Header](Header_Fooocus.png)

## Table of Contents

- [Introduction](#introduction)
- [Hardware Requirement](#hardware-requirement)
- [Download and Setup](#download-and-setup)
  - [Windows](#windows)
  - [MacOS](#macos)
  - [Linux](#linux)
- [Usage](#usage)
    - [Before Starting](#before-starting)
    - [Basic Mode](#basic-mode)
    - [Advanced Mode](#advanced-mode)
        - [Settings](#settings)
        - [Style](#style)
        - [Model](#model)
        - [Advanced](#advanced)     
    - [Input Image](#input-image)
        - [Upscaling](#upscaling)
        - [Variation](#variation)
        - [Image Prompting](#image-prompting)
        - [Describe Image](#describe-image)
        - [Inpainting and Outpainting](#inpainting-and-outpainting)

<br>

# Introduction

This **tutorial** will guide you through the process of running **Fooocus**, a local image generation software, on your machine. Fooocus is a tool that allows you to **create custom images** using various styles. 

By running Fooocus locally, you'll have **full control over the output** and can experiment with different settings without relying on cloud services or data connections. 

In this tutorial, we'll cover the **basics of getting started with Fooocus**, including installing and configuring the software, understanding **its key features**, and experimenting with some simple image generation techniques.

<br>

# Hardware Requirement

To run Fooocus locally, ensure your device meets the following minimum requirements. Meeting these specs ensures a smooth setup and use experience. If your device falls short, you may not be able to use Fooocus locally.

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

# Download and Setup

## Windows

### Nvidia GPUs

To get started with Fooocus, follow these steps:

* Download the files from the [official GitHub repository](https://github.com/lllyasviel/Fooocus/releases).
* Extract the downloaded file and run the ```run.bat``` script.
* When you launch Fooocus for the first time, it will download default models to the ```\Fooocus\models\checkpoints``` folder. You can choose to download them in advance if you prefer not to wait.
* You may also see options for ```run_anime.bat``` and ```run_realistic.bat``` , but note that **since version 2.3.0, you can switch presets directly from the browser.**
* By following these steps, you'll be able to access and use Fooocus with ease.

### AMD GPUs

> [!NOTE]
> The AMD support is in beta.
> In case of trouble check the [troubleshoot page](https://github.com/lllyasviel/Fooocus/blob/main/troubleshoot.md).

Same with Nvidia GPU. Download the software and edit the content of ```run.bat``` as:

    .\python_embeded\python.exe -m pip uninstall torch torchvision torchaudio torchtext functorch xformers -y
    .\python_embeded\python.exe -m pip install torch-directml
    .\python_embeded\python.exe -s Fooocus\entry_with_update.py --directml
    pause

Then run the ```run.bat```.

## MacOS

> [!NOTE]
> Mac is not intensively tested. The following is an unofficial guide to help you get started.
> In case of trouble check the [troubleshoot page](https://github.com/lllyasviel/Fooocus/blob/main/troubleshoot.md).

Installing Fooocus is possible on Apple M1 or M2-based Macs running macOS Catalina or later. It's essential to note that M1 and M2 computers rely on integrated graphics processing, which may result in longer image processing times compared to machines with dedicated graphics cards.

* Install the conda package manager and pytorch nightly. Read the Accelerated PyTorch training on Mac Apple Developer guide for instructions. Make sure pytorch recognizes your MPS device.
* Open the macOS Terminal app and clone this repository with ```git clone https://github.com/lllyasviel/Fooocus.git```.
* Change to the new Fooocus directory, ```cd Fooocus```.
* Create a new conda environment, ```conda env create -f environment.yaml```.
* Activate your new conda environment, ```conda activate fooocus```.
* Install the packages required by Fooocus, ```pip install -r requirements_versions.txt```.
* Launch Fooocus by running ```python entry_with_update.py```. (Some Mac M2 users may need python entry_with_update.py --disable-offload-from-vram to speed up model loading/unloading.)
* The first time you run Fooocus, it will automatically download the Stable Diffusion SDXL models and will take a significant amount of time, depending on your internet connection.
* Use ```python entry_with_update.py --preset anime``` or ```python entry_with_update.py --preset realistic``` for Fooocus Anime/Realistic Edition.

## Linux

### NVIDIA GPUs

If you want to use Anaconda/Miniconda, you can

```
git clone https://github.com/lllyasviel/Fooocus.git
cd Fooocus
conda env create -f environment.yaml
conda activate fooocus
pip install -r requirements_versions.txt
```

Then download the models: download default models to the folder "Fooocus\models\checkpoints". Or let Fooocus automatically download the models using the launcher:

```
conda activate fooocus
python entry_with_update.py
```

Or, if you want to open a remote port, use

```
conda activate fooocus
python entry_with_update.py --listen
```

Use ```python entry_with_update.py --preset anime``` or ```python entry_with_update.py --preset realistic``` for Fooocus Anime/Realistic Edition.

### AMD GPUs

> [!NOTE]
> The AMD support is in beta.
> In case of trouble check the [troubleshoot page](https://github.com/lllyasviel/Fooocus/blob/main/troubleshoot.md).

Same with the above instructions. You need to change torch to the AMD version.

```
pip uninstall torch torchvision torchaudio torchtext functorch xformers 
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.6
```

Use ```python entry_with_update.py --preset anime``` or ```python entry_with_update.py --preset realistic``` for Fooocus Anime/Realistic Edition.

<br>

# Usage

> [!NOTE]
> The following guide is based on the usage of Fooocus on a windows 11 machine using an Nvidia RTX 4090 GPU.

> [!CAUTION]
> Use AI-generated images responsibly: **Always disclose that they were generated by AI.**
> Be mindful of **intellectual property rights.**

## Before Starting

When using your image generation model, **it's essential to provide detailed and specific prompts to achieve the desired output**. A well-crafted prompt can make all the difference in generating an image that meets your needs.

To get started, try to be as descriptive as possible:

* ***Specify the object or scene you want to see***: "Generate a photo of a sunset on a beach".
* ***Provide context***: "Create an image of a futuristic cityscape with towering skyscrapers and flying cars".
* ***Add style guidance***: "Produce a minimalist illustration of a cat in a bold, comic book-style font".

By being **specific and detailed**, you'll help the model understand your vision and generate an output that aligns with your expectations. 

> [!TIP]
> You Check out this helpful [twitter/X account](https://twitter.com/nickfloats) to learn how to improve your skills. While this account is for Midjourney, its prompting principles can be applied to Fooocus. Take inspiration and adapt them to create compelling prompts.

## Basic Mode

To begin, simply execute the ```run.bat``` file (or use ```python entry_with_update.py``` on other platforms) to load the software and models.

Once loaded, Fooocus will open a tab in your browser, where you can start exploring its features. By default, you'll see an input box for writing prompts, a "Generate" button, and an image window.

**Starting Image Generation**

To generate images, simply type what you want to create into the input box and click the "Generate" button. Fooocus will then produce two images with a 9:7 ratio by default.

As the generation process unfolds, you'll be able to visualize the output in real-time within the image window.

**Saving and Viewing Generated Images**

Once the images are created, you can zoom in on them by clicking directly on the new images. To save your generated creations, use the dedicated button at the top of each image.


## Advanced Mode

For greater control over your image generation, toggle into Advanced Mode by clicking the corresponding button located below the input field. This mode offers a range of additional settings and options to fine-tune your creative output.

### Settings

In the Settings tab, you can refine your image generation experience by adjusting various options.

 * Preset Selection : Select a preset model optimized for a specific image style, such as Anime. This ensures that the model is tailored to produce images that match the chosen style.

 * Performance Selection : Choose a preset performance setting to focus on specific generation parameters, like Speed or quality. For example, if you need a highly detailed image, select the Quality option.

* Aspect Ratio : Choose from a list of pre-defined aspect ratios to control the shape and proportions of your generated images. Fooocus limits the ratio options to ensure better output results.

* Number of Images : Decide how many images you want the model to generate. It's often helpful to produce multiple iterations, as the output images may vary significantly. This allows you to choose your preferred result.

* Output Format : The default output format is PNG. You can also select JPEG or WebP formats to suit your needs.

* Negative Prompt Box : Use the negative prompt box to fine-tune your image output by removing unwanted objects, colors, or characters from the generated images. This feature enables you to further customize your results.

### Style

The Style tab allows you to modify the aesthetic of your generated images. To explore different styles, use the search box to find a specific style that suits your needs.

Use the search box to quickly locate a specific style that resonates with your creative vision. Once you've found the desired style, adjust the settings as needed to refine the look of your generated images.

Some examples of available styles include:

* Minimalism: A sleek and simple design
* Rococo: A ornate and decorative style inspired by 18th-century French art
* Watercolor: A soft and whimsical aesthetic reminiscent of watercolor paintings
* Art Deco: A glamorous and geometric style popularized in the Roaring Twenties

Fooocus offers a wide range of styles, each one carefully crafted to evoke a unique mood, atmosphere, or visual identity. Take some time to browse through the library and get familiar with what's available.

### Model

The Model tab provides advanced users with the ability to fine-tune the underlying model and weights used by Fooocus. While this level of customization can be powerful, it is essential to carefully consider any changes before making them.

Before modifying the model or weights, we strongly recommend that you have a solid understanding of the concepts involved. This includes familiarity with machine learning, neural networks, and the specific algorithms used by Fooocus. 

<div align="center"> 
 
<strong> If you are unsure about what you are doing, it is best to leave these settings unchanged. </strong>

</div>

### Advanced

The Advanced tab offers two settings, carefully developed by the Fooocus team, which provide additional control over your image generation process.

**Sharpness**

Fooocus introduces Image Sharpness, a feature designed to address the common issue of overly smooth images generated by SDXL. This setting allows you to control the level of detail and sharpness in your final image.

By adjusting the Image Sharpness value, you can achieve a range of effects:
* Higher values will result in less smoothed images with more defined edges.
* Lower values will produce smoother, more subtle images.
  
To get the most out of this feature, try experimenting with different settings to find the sweet spot that suits your creative vision. The default value is set to 2, providing a good balance between sharpness and smoothness.

**Guidance Scale**

The Guidance Scale, also known as the Classifier-Free Guidance (CFG) scale, is a critical parameter that controls how closely the image generation process follows your text prompt.

As you increase the value of the CFG scale:

* The generated images will become more aligned with the original text prompt.
* However, be cautious not to set it too high, as this can limit diversity and quality in your output.
  
On the other hand, a lower CFG scale value:

* Allows for greater creative freedom and produces higher-quality images.
* May result in output that deviates from the original text prompt, but still maintains a strong connection to its essence.

To get the most out of the Guidance Scale:

* Experiment with different values to find the sweet spot that suits your creative vision.
* Consider the trade-off between prompt adherence and creative freedom when setting this parameter.
* Don't be afraid to adjust the CFG scale value to achieve the perfect balance for your project.

## Input Image

The Input Image option allows you to leverage images as input for your generation process, offering a powerful way to guide and refine your creative output.

There are several scenarios where using images as input can be particularly useful.

### Upscaling 

If you need to enlarge an image while maintaining its quality, the input image option can help you achieve this.

To upscale your desired image, follow these easy steps:

Step 1: Upload Your Image
Begin by uploading your target image into the designated box.

Step 2: Choose the Upscale Option
Select the "Upscale" option from the right-hand menu. You can choose from various upscaling options, such as 1.5x or 2x.

Step 3: Set the Image Number
In the Settings tab, make sure the image number is set to 1.

Step 4: Generate Your Enlarged Image
Once you've completed these steps, click the "Generate" button to create your enlarged image.

When you choose the upscale option (2x), your generated image will have x2 more pixels than the original. This means that if your original image has 1000x1000 pixels, the upscaled image will have 2000x2000 pixels.

### Variation

Want to create a variation of an existing image? This feature allows you to build upon a starting point and generate new and interesting variations. Here's how to do it:

Step 1: Upload Your Starting Image
Begin by uploading your existing image into the designated box.

Step 2: Choose the Variation Option
Select the "Variation" option from the right-hand menu.  You can choose from various Vary options, such as Subtle variation or Strong variation.

Step 3: Generate Your Variations
Once you've completed these steps, click the "Generate" button to create your variations. You'll receive a new set of images that are inspired by your starting image but with unique twists and features.

When you generate variations, you can expect to see changes in aspects such as:

* Color palette
* Composition
* Texture
* Object placement
  
These changes will be applied in various ways, resulting in a set of new images that are distinct from the original but still share similarities with it.

### Image Prompting 

Want to use an existing image as inspiration for a new creation ? Image prompting is a powerful feature that allows you to generate a new image based on an existing one. Here's how to do it:

Step 1: Upload Your Prompt Image
Begin by uploading the image (or multiple images) you want to use as a prompt(s) into the designated box.

Step 2: Set the Generation Parameters
In the Settings tab, you can adjust various parameters to control the style and direction of the generated image.

Step 3: Generate Your Prompted Image
Once you've completed these steps, click the "Generate" button to create your prompted image. You'll receive a new set of images that are inspired by your starting image but with unique characteristics and features.

When you generate an image prompt, you can expect to see a new image that is influenced by the original. The generated image may:

* Share similar colors or textures
* Feature similar objects or compositions
* Have a similar mood or atmosphere
  
These elements will be combined in unique ways to create a new and creative image that's inspired by your starting prompt.

### Describe Image

Want to know more about what's in an image? The Image Description feature allows you to upload an image and receive a detailed description of its contents. Here's how to do it:

Step 1: Upload Your Image
Begin by uploading the image you want to have described into the designated box.

Step 2: Choose which type of content you want the model to describe.

Step 3: Review Your Description
Once you've completed these steps, click the "Generate" button to receive your image description. You'll be provided with a detailed and accurate summary of the image's contents, including:

* Objects and their positions
* Colors and textures
* Compositions and layouts
* Any notable features or details

This feature can also inspire new prompt ideas by revealing what makes an image compelling.

### Inpainting and Outpainting 

Inpainting

Inpainting is a process that allows you to modify or replace specific parts of an existing image. 

Outpainting

Outpainting is a technique that allows you to extend an image beyond its original borders

TODO : Finish the tutorial 

<br>
