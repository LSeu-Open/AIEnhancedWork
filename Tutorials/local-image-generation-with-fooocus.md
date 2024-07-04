![Header](Header_Fooocus.png)

## Table of Contents

- [Introduction](#introduction)
- [Hardware Requirement](#hardware-requirement)
- [Download and Setup](#download-and-setup)
- [Usage](#usage)

## Introduction

This **tutorial** will guide you through the process of running **Fooocus**, a local image generation software, on your machine. Fooocus is a tool that allows you to **create custom images** using various styles. 

By running Fooocus locally, you'll have **full control over the output** and can experiment with different settings without relying on cloud services or data connections. 

In this tutorial, we'll cover the **basics of getting started with Fooocus**, including installing and configuring the software, understanding **its key features**, and experimenting with some simple image generation techniques.

<br>

## Hardware Requirement

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

## Download and Setup

### Windows

#### Nvidia GPUs

To get started with Fooocus, follow these steps:

* Download the files from the [official GitHub repository](https://github.com/lllyasviel/Fooocus/releases).
* Extract the downloaded file and run the ```run.bat``` script.
* When you launch Fooocus for the first time, it will download default models to the ```\Fooocus\models\checkpoints``` folder. You can choose to download them in advance if you prefer not to wait.
* You may also see options for ```run_anime.bat``` and ```run_realistic.bat``` , but note that **since version 2.3.0, you can switch presets directly from the browser.**
* By following these steps, you'll be able to access and use Fooocus with ease.

#### AMD GPUs

> [!NOTE]
> The AMD support is in beta.
> In case of trouble check the [troubleshoot page](https://github.com/lllyasviel/Fooocus/blob/main/troubleshoot.md).

Same with Nvidia GPU. Download the software and edit the content of ```run.bat``` as:

    .\python_embeded\python.exe -m pip uninstall torch torchvision torchaudio torchtext functorch xformers -y
    .\python_embeded\python.exe -m pip install torch-directml
    .\python_embeded\python.exe -s Fooocus\entry_with_update.py --directml
    pause

Then run the ```run.bat```.

### MacOS

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

### Linux

#### NVIDIA GPUs

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

#### AMD GPUs

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

## Usage

> [!NOTE]
> The following guide is based on the usage of Fooocus on a windows 11 machine using an Nvidia RTX 4090 GPU.

> [!CAUTION]
> Use AI-generated images responsibly: **Always disclose that they were generated by AI.**
> Be mindful of **intellectual property rights.**

### Before Starting

When using your image generation model, **it's essential to provide detailed and specific prompts to achieve the desired output**. A well-crafted prompt can make all the difference in generating an image that meets your needs.

To get started, try to be as descriptive as possible:

* ***Specify the object or scene you want to see***: "Generate a photo of a sunset on a beach".
* ***Provide context***: "Create an image of a futuristic cityscape with towering skyscrapers and flying cars".
* ***Add style guidance***: "Produce a minimalist illustration of a cat in a bold, comic book-style font".

By being **specific and detailed**, you'll help the model understand your vision and generate an output that aligns with your expectations. 

> [!TIP]
> You Check out this helpful [twitter/X account](https://twitter.com/nickfloats) to learn how to improve your skills. While this account is for Midjourney, its prompting principles can be applied to Fooocus. Take inspiration and adapt them to create compelling prompts.

### Basic Mode

To begin, simply execute the ```run.bat``` file (or use ```python entry_with_update.py``` on other platforms) to load the software and models.

Once loaded, Fooocus will open a tab in your browser, where you can start exploring its features. By default, you'll see an input box for writing prompts, a "Generate" button, and an image window.

**Starting Image Generation**

To generate images, simply type what you want to create into the input box and click the "Generate" button. Fooocus will then produce two images with a 9:7 ratio by default.

As the generation process unfolds, you'll be able to visualize the output in real-time within the image window.

**Saving and Viewing Generated Images**

Once the images are created, you can zoom in on them by clicking directly on the new images. To save your generated creations, use the dedicated button at the top of each image.


### Advanced Mode

For greater control over your image generation, toggle into Advanced Mode by clicking the corresponding button located below the input field. This mode offers a range of additional settings and options to fine-tune your creative output.

#### Settings

In the Settings tab, you can refine your image generation experience by adjusting various options.

 * Preset Selection : Select a preset model optimized for a specific image style, such as Anime. This ensures that the model is tailored to produce images that match the chosen style.

 * Performance Selection : Choose a preset performance setting to focus on specific generation parameters, like Speed or quality. For example, if you need a highly detailed image, select the Quality option.

* Aspect Ratio : Choose from a list of pre-defined aspect ratios to control the shape and proportions of your generated images. Fooocus limits the ratio options to ensure better output results.

* Number of Images : Decide how many images you want the model to generate. It's often helpful to produce multiple iterations, as the output images may vary significantly. This allows you to choose your preferred result.

* Output Format : The default output format is PNG. You can also select JPEG or WebP formats to suit your needs.

* Negative Prompt Box : Use the negative prompt box to fine-tune your image output by removing unwanted objects, colors, or characters from the generated images. This feature enables you to further customize your results.

#### Style

TODO

#### Advanced

TODO

### Input Image

You may need to use image as input for various reasons :

* You need to upscale an Image (Upscale)
* You want to make a variation of an existing image (Variation)
* You want to create a new image using an existing image (Image Prompt)
* You need the model to describe an image (Describe)
* You want to generate only certain part of the image (Inpaint/outpaint)

#### Upscaling

TODO

#### Image Variation

TODO

#### Image Prompt

TODO

#### Describe

TODO
#### Inpaint and Outpaint

TODO

<br>
