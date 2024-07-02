# Local Image Generation with Fooocus: A Comprehensive Tutorial

## Table of Contents

- [Introduction](#introduction)
- [Hardware Requirement](#hardware-requirement)
- [Download](#download)
- [Default Models](#default-models)
- [Usage](#usage)

## Introduction

This tutorial will guide you through the process of running **Fooocus**, a local image generation software, on your machine. Fooocus is a tool that allows you to create custom images using various styles. 

By running Fooocus locally, you'll have full control over the output and can experiment with different settings without relying on cloud services or data connections. 

In this tutorial, we'll cover the basics of getting started with Focal, including installing and configuring the software, understanding its key features, and experimenting with some simple image generation techniques.

<br>

## Hardware Requirement

To run Fooocus locally, ensure your device meets the following minimum requirements. Meeting these specs ensures a smooth setup and use experience. If your device falls short, you may not be able to use Fooocus locally.

| Operating System  | GPU                          | Minimal GPU Memory           | Minimal System Memory     | [System Swap](troubleshoot.md) | Note                                                                       |
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

#### Nvidia GPU

To get started with Fooocus, follow these steps:

* Download the files from the [official GitHub repository](https://github.com/lllyasviel/Fooocus/releases).
* Extract the downloaded file and run the ```run.bat``` script.
* When you launch Fooocus for the first time, it will download default models to the ```\Fooocus\models\checkpoints``` folder. You can choose to download them in advance if you prefer not to wait.
* You may also see options for ```run_anime.bat``` and ```run_realistic.bat``` , but note that since version 2.3.0, you can switch presets directly from the browser.
* By following these steps, you'll be able to access and use Fooocus with ease.

#### AMD GPU

Same with Nvidia GPU. Download the software and edit the content of `run.bat` as:

    .\python_embeded\python.exe -m pip uninstall torch torchvision torchaudio torchtext functorch xformers -y
    .\python_embeded\python.exe -m pip install torch-directml
    .\python_embeded\python.exe -s Fooocus\entry_with_update.py --directml
    pause

Then run the `run.bat`.

> [!NOTE]
> The AMD support is in beta.
> In case of trouble check the [troubleshoot page](https://github.com/lllyasviel/Fooocus/blob/main/troubleshoot.md).

### MacOS

### Linux

#### Using Anaconda

#### Using Python Venv
### Docker

<br>

## Default Models

<br>

## Usage

<br>
