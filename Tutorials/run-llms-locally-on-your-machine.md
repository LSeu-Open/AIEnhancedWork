<div align="center"> 
 
[![SVG Banners](https://svg-banners.vercel.app/api?type=luminance&text1=How%20to%20run%20LLMs%20locally%20on%20your%20Machine%20🖥️&width=1100&height=550)](https://github.com/Akshay090/svg-banners)

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand.png" alt="Waving Hand" width="30" height="30" /> ***Ready to explore the world of local AI? This guide will help you set up and run language models right on your computer, giving you full control over your AI tools.*** <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand.png" alt="Waving Hand" width="30" height="30" />

***<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Green%20Square.png" alt="Green Square" width="15" height="15" /> Level : Beginner***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20with%20Monocle.png" alt="Face with Monocle" width="25" height="25" /> Reading Time : 9min***


</div> 

## Table of Contents

* [Introduction](#introduction)
* [Find the Provider that is right for you](#find-the-provider-that-is-right-for-you)
* [Find the Model that is right for you](#find-the-model-that-is-right-for-you)
* [Ollama](#ollama)
  + [Installation](#installation)
  + [Quickstart](#quickstart)
  + [User Friendly Ollama Models Interaction](#user-friendly-ollama-models-interaction)
    + [Installation and setup](#installation-and-setup)
    + [Browser Support](#browser-support)
    + [Usage](#usage)


<br>

## Introduction

This tutorial is designed for ***individuals seeking greater control and transparency*** in their data processing, regardless of their background or expertise. We will provide a step-by-step guide on how to set up a local LLM environment using Ollama as the backend and the Page Assist extension in your browser.

#### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20in%20Clouds.png" alt="Face in Clouds" width="25" height="25" /> The Cloud Privacy Challenge

When using online AI services, **your data travels through remote servers, creating several concerns.** Imagine sending your private documents through a public mail system - you can't be certain who might view them or how they'll be handled. Cloud providers may share your inputs with others or use them in ways you didn't expect.

#### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Bust%20in%20Silhouette.png" alt="Bust in Silhouette" width="25" height="25" /> The Transparency Problem

**Cloud-based AI systems operate like black boxes.** Their complex algorithms process your data in ways that are difficult to understand or verify. This lack of transparency can lead to unexpected results and potential biases in their responses.

#### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Man%20Technologist.png" alt="Man Technologist" width="25" height="25" /> Security at Scale

**Major AI providers handle millions of users' data.** While this enables powerful capabilities, it also **creates attractive targets for data breaches.** One security incident could expose vast amounts of sensitive information.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Love-You%20Gesture.png" alt="Love-You Gesture" width="25" height="25" /> Benefits of Local AI

#### Control Your Data

**Running AI locally keeps your information entirely on your machine.** Think of it as having your own personal assistant who works exclusively for you, without sharing your conversations with anyone else.

#### Real-Time Performance

Local processing **eliminates internet latency. Your AI responds instantly, making it perfect for real-time tasks and continuous interaction.** It's like having the AI right at your fingertips rather than across the internet.

#### Compliance Made Simple

**With local AI, you maintain complete control over data storage and processing.** This simplifies compliance with privacy regulations and data protection requirements. **Your data stays within your boundaries, both physically and legally.**

<br>

## Find the Provider that is right for you

To get started, **select a local model provider** that streamlines the process of hosting and deploying a LLM.

This section is designed to provide you with the **necessary knowledge and resources to make informed decisions about selecting the right provider for your specific needs**.


| Provider        | User Interface      | Ease of use               | Model customization      | Built-in chat interface  | Model discovery/download | Multi-platform support        | Open-source   | Integration with other tools |
|:----------------|:-------------------:|:-------------------------:|:------------------------:|:------------------------:|:------------------------:|:---------------------------:|:-------------:|:-------------------------:|
| [Ollama](https://ollama.com/) | Command-line & API  | Simple      | Yes                      | No (requires client)     | Limited                  | Windows, macOS, Linux       | Yes           | Extensive                |
| [LM Studio](https://lmstudio.ai/) | GUI | User-friendly           | Yes                      | Yes                      | Extensive                | Windows, macOS, Linux       | No            | Limited                  |
| [Jan](https://jan.ai/) | GUI          | User-friendly             | Limited                  | Yes                      | Limited                  | Windows, macOS, Linux       | Yes           | Limited                  |
| [MSTY](https://msty.app/) | GUI       | User-friendly             | Limited                  | Yes                      | Limited                  |macOS                        | No            | Limited                  |
| [Enchanted](https://github.com/AugustDev/enchanted) | GUI | User-friendly |  Limited         | Yes                      | Limited                  | macOS                       | No            | Yes (macOS)              |
| [AnythingLLM](https://anythingllm.com/) | Web-based | User-friendly | Yes                    | Yes                      | Limited                  |Cross-platform (web-based)   | Yes           | Yes                      |

<br>

## Find the Model that is right for you

Once you have selected your local model provider, you'll need to **decide which Model** to run. For **users with limited system resources** or older hardware configurations, I will also provide **cloud-based providers that can efficiently run these models**.

This section is designed to provide you with the **necessary knowledge and resources to make informed decisions about selecting the right model for your specific needs**. To facilitate this process, I have prepared **two reference tables to support your search**.

* **The first table showcases open-source models**, which can be **run locally on your machine.** To ensure optimal performance, I have outlined the **recommended hardware requirements for each model**.
* **The second table features proprietary models**, which typically operate on cloud-based providers.

> [!IMPORTANT]
> The VRAM requirements listed in the tables are indicative estimates, calculated for a **Q4_0 quantization** that represents a **balance between model precision and inference speed** as recommended by the **default Ollama configuration.**
>
> Please note that while it may be **possible to run certain models with lower hardware specifications**, this may result in **slower inference speed**. If the model does not fit entirely within the VRAM, it will need to transfer some data to system memory, which is significantly slower. This can greatly impact the inference speed.

> [!NOTE]
> The models are ranked according to their **Quality Index (with higher scores indicating better performance)** from the [Artificial Analysis LLM Leaderboard](https://artificialanalysis.ai/models/o1?models_selected=o1%2Co1-mini%2Cgpt-4o-2024-08-06%2Cgpt-4o-mini%2Cgemini-1-5-pro%2Cgemini-1-5-flash%2Cclaude-35-sonnet%2Cclaude-3-opus%2Cclaude-3-haiku%2Creka-core%2Cdeepseek-v2-5%2Cyi-large%2Cclaude-3-sonnet). Please note that **Quality Index is subject to change** based on daily test-run and will be updated regularly to reflect the latest rankings.
>
> We consider this **benchmarking methodology to be less biased** than the Elo score method employed by LMSys. Furthermore, the **LMSys leaderboard does not address datasets contamination , model quantization and model overfitting issues.**

> [!TIP]
> <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" /> **Badges provide direct links to model downloads, provider services, and official documentation.** <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" />

### Open Source Models

***Massive models*** : Local deployment can be challenging due to high computational requirements. These models are commonly used on cloud-based provider platforms.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Quality Index |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)       | [Deepseek-R1](https://huggingface.co/deepseek-ai/DeepSeek-V3)     | 685B        | 404GB+ VRAM GPU (5xH100 or better) |  60 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-r1:671b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)       | [Deepseek-v3](https://huggingface.co/deepseek-ai/DeepSeek-V3)     | 236B        | 133GB+ VRAM GPU (2xH100 or better) |  52 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-v3) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.3-70b-Instruct](https://ollama.com/library/llama3.3) | 70B | 40GB+ VRAM GPU (2xRTX 4090 or better) | 41  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.3) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Groq.svg" alt="Groq" width="220" height="20" />](https://groq.com) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.1-405b-Instruct](https://ollama.com/library/llama3.1:405bt)  | 405B        | 230+ VRAM GPU (4xH100 or better)  |  40       | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.1:405b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenRouter.svg" alt="OpenRouter" width="200" height="20" />](https://openrouter.ai/chat?models=meta-llama/llama-3.1-405b) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)        | [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)  | 72.2B         | 47GB+ VRAM GPU (2xRTX 4090 or better) |  40 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:72b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)         | [Command A](https://huggingface.co/CohereForAI/c4ai-command-a-03-2025)               | 111B        | 60GB+ VRAM GPU (3xRTX 4090 or better) | 40 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/command-r-plus) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mistral-Large-2-Instruct](https://ollama.com/library/mistral-large)  | 123B        | 70GB+ VRAM GPU (3xRTX 4090 or better) | 38    | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/mistral-large) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.2-90B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct)  | 88.6B        | 40GB+ VRAM GPU (2xRTX 4090 or better)   |  33    | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.2-vision:90b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Fireworks.svg" alt="Fireworks" width="200" height="20" />](https://fireworks.ai/) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)         | [Command R+](https://ollama.com/library/command-r-plus)               | 104B        | 60GB+ VRAM GPU (3xRTX 4090 or better) | 21 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/command-r-plus) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) |


**Mid-sized models** : Suitable for deployment on a high-performance local workstation. These models require high-end consumer configurations with a powerful GPU, which can range from 2,000 to 3,400 ($/£/€ equivalent)

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Quality Index |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)       | [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)  | 32B         | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |  58 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwq) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/QwQ-32B) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Reka.svg" alt="Reka" width="150" height="20" />](https://www.reka.ai/) | [Reka Flash 3](https://huggingface.co/RekaAI/reka-flash-3) | 21B         | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) | 47 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/omercelik/reka-flash-3) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Reka.svg" alt="Reka" width="150" height="20" />](https://space.reka.ai/sign-in?redirect_url=https%3A%2F%2Fspace.reka.ai%2F) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/)      | [Phi-4](https://huggingface.co/microsoft/phi-4) | 14B | 10GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 40 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/phi4) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)       | [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)  | 32.8B         | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 37 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:32b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mistral-Small-3](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) | 24B  | 14GB+ VRAM GPU (RX 7800 or RTX 4080 or better | 35 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/mistral-small) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)         | [Aya-expanse-32b](https://huggingface.co/CohereForAI/aya-expanse-32b)                     | 32B         | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 20 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/aya-expanse:32b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)         | [Gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it)        | 27B         | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) | **Incoming** | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/gemma3:27b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/google/gemma-2-27b-it) |


***Small models*** : Lightweight and easily deployable on most local machines. These models require mid-range consumer configurations with a GPU, ranging from 600 to 1,200 ($/£/€ equivalent). 

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Quality Index |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)       | [Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)  | 14.8B         | 9GB+ VRAM GPU (rx 7800 or RTX 4070 or better) |  25 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:14b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)     | [Ministral-8B-Instruct](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) | 8B  | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better)       | 22   | No | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.2-11b-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct)       | 10.7B          | 8GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 22 | No | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)        | [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)  | 7.62B         | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) |  16 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:7b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)         | [Gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it)          | 9B          | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 15 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/gemma2:9b-instruct-q4_0) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/spaces/huggingface-projects/gemma-2-9b-it) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)         | [Gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it)          | 12B          | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | **Incoming** | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/https://ollama.com/library/gemma3:12b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/google/gemma-3-12b-it) |

***Tiny models*** : The smallest models are designed to run on all types of machines, including the oldest ones. These models can be run on most consumer hardware configurations, provided they have at least 6-8 GB of RAM.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Quality Index |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------:|:-----------:|:-----------------:|:----------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)     | [Ministral-3B-Instruct](https://huggingface.co/ministral/Ministral-3b-instruct) | 3B  | 6GB+ RAM        | 20  | No | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/spaces/gloignon/ministral-3b-test) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.2-3b-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) | 3B | 6GB+ RAM   | 20 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.2:3b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Groq.svg" alt="Groq" width="220" height="20" />](https://groq.com) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)        | [Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)  | 3B        | 6GB+ RAM |  10 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:3b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)          | [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) | 1B | 2GB+ RAM | 10 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.2:1b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Groq.svg" alt="Groq" width="220" height="20" />](https://groq.com) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)        | [Gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it)            | 2B | 2GB+ RAM | 9 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/gemma2:2b) |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/google/gemma-2-2b-it) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)         | [Gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it)          | 4B          | 4GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | **Incoming** | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/gemma3:4b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/google/gemma-3-4b-it) |
<br>

### Proprietary Model

| Provider                                         | Model     | Quality Index | Pricing |
|:----------------------------------------------|:------------:|:----------:|:-------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [o1](https://chat.openai.com/) | 62      | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Eight-Pointed Star" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [o3-mini](https://chat.openai.com/) | 62       | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Eight-Pointed Star" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.7 Sonnet](https://claude.ai//) | 57 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Eight-Pointed Star" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [o1-mini](https://chat.openai.com/) | 54       | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Eight-Pointed Star" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/xAI.svg" alt="xAI" width="220" height="20" />](https://x.ai/) | [Grok-3](https://x.ai/blog/grok-3) | 53  |  <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini 2.0 Pro](https://gemini.google.com/advanced?hl=en) | 49 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Eight-Pointed Star" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini 2.0 Flash](https://deepmind.google/technologies/gemini/flash/)   | 48 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Eight-Pointed Star" width="80" height="20" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/xAI.svg" alt="xAI" width="220" height="20" />](https://x.ai/) | [Grok-3-mini](https://x.ai/blog/grok-3) | 47  |  <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)  | [Qwen-Max](https://qwenlm.github.io/) | 45 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.5 Sonnet](https://claude.ai//) | 44 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Eight-Pointed Star" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [GPT-4o-latest](https://chat.openai.com/) | 41      | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Eight-Pointed Star" width="80" height="20" />     |

<br>

## Ollama

Ollama is our top recommendation for running LLMs locally due to its robust integration capabilities and adaptability. 

As an example, you will find below a step-by-step guide on setting up Ollama as a local model provider through an accessible and user-friendly interface. 

Please follow  official documentations if you wish to use other providers, or open an issue on this repository if you want a dedicated section for your preferred provider in this file.

### Installation

| Platform          | Installation Method |
|:-----------------:|:--------------------:|
| **macOS**         | [Download](https://ollama.com/download/Ollama-darwin.zip) |
| **Windows**       | [Download](https://ollama.com/download/OllamaSetup.exe)  |
| **Linux**         | [Manual install instructions](https://github.com/ollama/ollama/blob/main/docs/linux.md) |
| **Docker**        | [Ollama Docker image](https://hub.docker.com/r/ollama/ollama) is available on Docker Hub.  |

### Quickstart

<br>

To run and chat with [Llama 3.1](https://ollama.com/library/llama3.1) write the following input in a terminal:

```
ollama run llama3.1
```
This will allow you to chat with the **llama3.1:8B model** within the command-line interface (CLI). See the list of models available on [ollama.com/library](https://ollama.com/library 'ollama model library'). 

To download a model without launching it, simply enter the following command:

```
ollama pull llama3.1
```
To view the list of models you've downloaded, simply use the following command:

```
ollama list
```

<br>

### User Friendly Ollama Models Interaction

For those who prefer a more user-friendly experience, We'll demonstrate how to interact with your Ollama model through our browser-based interface, which provides a graphical and intuitive way of working with your LLM. We will be using the [Page assist extension](https://github.com/n4ze3m/page-assist).

Page Assist is an open-source Chrome Extension that provides a Sidebar and Web UI for your Local AI model. It allows you to interact with your model from any webpage.

Want to explore other possibilities? Take a look at the alternative solutions available in our [Local Providers section](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/README.md#local-providers-1).

#### Installation and setup 

You can install the extension from the [Chrome Web Store](https://chromewebstore.google.com/detail/page-assist-a-web-ui-for/jfgfiigpkhlkbnfnbobbkinehhfdhndo)

#### Browser Support

| Browser  | Sidebar | Chat With Webpage | Web UI |
| -------- | ------- | ----------------- | ------ |
| Chrome   | ✅      | ✅                | ✅     |
| Brave    | ✅      | ✅                | ✅     |
| Firefox  | ✅      | ✅                | ✅     |
| Vivaldi  | ✅      | ✅                | ✅     |
| Edge     | ✅      | ❌                | ✅     |
| Opera    | ❌      | ❌                | ✅     |
| Arc      | ❌      | ❌                | ✅     |


If needed, see the [Manual Installation](https://github.com/n4ze3m/page-assist) instructions on their github repository.

Once the extension is installed Just click on the extension icon and it'll take you straight to the chatGPT-like UI.

To verify after installation process, I would suggest the following steps :

- A center message **must letting you know that Ollama is running in the background**, ready to handle your requests.
- To the top left corner, a **dropdown menu** awaits, listing all models you've installed and are currently available for interaction. Simply **select the model with which you wish to engage.**
- In the **top left icon**, click to open a sidebar that enables Conversation Management. This feature allows you to **manage and organize your conversations**.

> [!Note]
> When you first interact with your model, there might be a brief delay as it loads into memory. But once you're chatting away, responses should come quickly !
> Just remember that processing time can vary depending on your computer's specs.

#### Usage

##### Sidebar

Once the extension is installed, you can **open the sidebar via context menu or keyboard shortcut**.  By exploiting this sidebar functionality, you can engage in seamless conversations with your model while **leveraging the current web page as contextual reference (website, documentation, PDF...).**

▶️ in order to use `chat with the current page` option you need to set a Embedding Model in the `RAG Settings`.

> Default Keyboard Shortcut: `Ctrl+Shift+P`

##### Web UI

You can open the Web UI by clicking on the extension icon which will open a new tab with the Web UI.

> Default Keyboard Shortcut: `Ctrl+Shift+L`

> [!Note]
> You can change the keyboard shortcuts from the extension settings on the Chrome Extension Management page.

<br>
