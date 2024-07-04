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

<br>
