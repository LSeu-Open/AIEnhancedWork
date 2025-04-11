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

This tutorial guides **individuals seeking greater control and transparency in their data processing through setting up a local Large Language Model (LLM) environment.*** We'll use Ollama as the backend and the Page Assist extension in your browser for this purpose.

#### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20in%20Clouds.png" alt="Face in Clouds" width="25" height="25" /> Challenges with Cloud-Based AI Services

* **Privacy Concerns** : Your data traverses remote servers, raising questions about who might access it and how it will be handled.
* **Lack of Transparency**: Complex algorithms make it difficult to understand or verify how your data is processed, potentially leading to biased results.
* **Security Risks** : Major AI providers handle vast amounts of user data, making them attractive targets for breaches.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Love-You%20Gesture.png" alt="Love-You Gesture" width="25" height="25" /> Benefits of Running LLMs Locally

* **Data Control** : Keep your information entirely on your machine, ensuring it's not shared with external parties.
* **Instant Performance** : Eliminate internet latency for real-time tasks and continuous interaction.
* **Simplified Compliance** : Maintain complete control over data storage and processing, easing adherence to privacy regulations.

<br>

## Find the Provider that is right for you

To get started, **choose a local model provider that simplifies hosting and deploying a Large Language Model (LLM).**

This section equips you with the knowledge and resources to make an informed decision tailored to your specific needs.


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

This section provides you with the **knowledge and resources to select the right model for your specific needs.** The first table showcases open-source models that can be run locally on your machine. 

To ensure optimal performance, **I have outlined the recommended hardware requirements for each model.**

For **users with limited system resources** or older hardware configurations, I will also provide **cloud-based providers that can efficiently run these models**.

> [!IMPORTANT]
> Please note that while it is possible to **run models without a GPU**, doing so will load the model into RAM and perform inference using the CPU.
>
> ***This approach will significantly slow down inference speeds.***

### Open Source Models

***Large-scale models (>70 billion parameters)*** : These require significant amounts of both RAM and GPU memory, often rendering local installation infeasible for most users. Consequently, such models are predominantly deployed on cloud-based platforms designed to provide the essential computational resources needed.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | [Score](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Scoring/Models_Scoring_System.md) (Alpha v0.3.1) |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)       | [Deepseek-R1](https://huggingface.co/deepseek-ai/DeepSeek-V3)     | 685B        | 404GB+ VRAM GPU (5xH100 or better) | 79.61 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-r1:671b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Perplexity.svg" alt="Perplexity" width="150" height="20" />](https://www.perplexity.ai) | [R1-1776](https://huggingface.co/perplexity-ai/r1-1776) | 685B | 404GB+ VRAM GPU (5xH100 or better) | 79.51 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/r1-1776:671b) |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Perplexity.svg" alt="Perplexity" width="150" height="20" />](https://www.perplexity.ai) |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  | [Llama-3_1-Nemotron-Ultra-253B-v1](https://huggingface.co/nvidia/Llama-3_1-Nemotron-Ultra-253B-v1) | 253B | 133GB+ VRAM GPU (2xH100 or better) | 76.20 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://huggingface.co/DevQuasar/nvidia.Llama-3_1-Nemotron-Ultra-253B-v1-GGUF) via [GGUF](https://huggingface.co/docs/hub/ollama) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | 402B |  230+ VRAM GPU (4xH100 or better)  | 74.3 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUFF) via [GGUF](https://huggingface.co/docs/hub/ollama) |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://www.meta.ai/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)       | [Deepseek-v3](https://huggingface.co/deepseek-ai/DeepSeek-V3)     | 236B        | 133GB+ VRAM GPU (2xH100 or better) |  72.79 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-v3) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)        | [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)  | 72.2B         | 47GB+ VRAM GPU (2xRTX 4090 or better) |  67.38 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:72b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.3-70b-Instruct](https://ollama.com/library/llama3.3) | 70B | 40GB+ VRAM GPU (2xRTX 4090 or better) | 66.64  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.3) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Groq.svg" alt="Groq" width="220" height="20" />](https://groq.com) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)       | [DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B) | 70.6B | 40GB+ VRAM GPU (2xRTX 4090 or better) |  65.40 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-r1:70b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)         | [Command A](https://huggingface.co/CohereForAI/c4ai-command-a-03-2025)               | 111B        | 60GB+ VRAM GPU (3xRTX 4090 or better) | 64.25 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/command-r-plus) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.1-405b-Instruct](https://ollama.com/library/llama3.1:405bt)  | 405B        | 60GB+ VRAM GPU (3xRTX 4090 or better) | 63.49 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.1:405b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenRouter.svg" alt="OpenRouter" width="200" height="20" />](https://openrouter.ai/chat?models=meta-llama/llama-3.1-405b) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | 109B |  230+ VRAM GPU (4xH100 or better)  | 63.29 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUFF) via [GGUF](https://huggingface.co/docs/hub/ollama) |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://www.meta.ai/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mistral-Large-2-Instruct](https://ollama.com/library/mistral-large)  | 123B        | 70GB+ VRAM GPU (3xRTX 4090 or better) | 60.38 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/mistral-large) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)         | [Command R+](https://ollama.com/library/command-r-plus)               | 104B        | 60GB+ VRAM GPU (3xRTX 4090 or better) | 49.01 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/command-r-plus) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) |

<br>

***Mid-sized models (<14B parameters)*** : These are well-suited for local deployment on high-end workstations. However, such deployment demands substantial investment in hardware, including a powerful GPU and other components, with total costs generally falling between $2,000 to $3,400 (or equivalent).

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | [Score](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Scoring/Models_Scoring_System.md) (Alpha v0.3.1) |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  | [Llama-3_3-Nemotron-Super-49B-v1](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1) | 49B | 40GB+ VRAM GPU (2xRTX 4090 or better) | 69.71 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-v1-GGUF) via [GGUF](https://huggingface.co/docs/hub/ollama) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Reka.svg" alt="Reka" width="150" height="20" />](https://www.reka.ai/) | [Reka Flash 3](https://huggingface.co/RekaAI/reka-flash-3) | 21B | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) | 67.16 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://huggingface.co/bartowski/RekaAI_reka-flash-3-GGUF) via [GGUF](https://huggingface.co/docs/hub/ollama) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Reka.svg" alt="Reka" width="150" height="20" />](https://space.reka.ai/sign-in?redirect_url=https%3A%2F%2Fspace.reka.ai%2F) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-Deep-32B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-32B) | 32B |  20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 66.11 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />]( https://ollama.com/library/exaone-deep:32b) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)  | 32B | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |  64.27 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwq) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/QwQ-32B) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)  | 32.8B | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 62.70 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:32b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |  [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)| 32B | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |  62.62 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-r1:32b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) | 27B | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) | 62.03 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/gemma3:27b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/google/gemma-2-27b-it) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mistral-Small-3](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) | 24B  | 14GB+ VRAM GPU (RX 7800 or RTX 4080 or better | 57.84 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/mistral-small) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   | [OLMo-2-0325-32B-Instruct](https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct) | 32B | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 57.40  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct-GGUF) via [GGUF](https://huggingface.co/docs/hub/ollama) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://playground.allenai.org/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) | [Command R](https://cohere.com/blog/command-r) | 32B | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 39.53 |   [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/command-r) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) |

<br>

***Small models (<7B parameters)*** : These are lightweight and easily deployable on medium machines, offering broader accessibility. They typically require a mid-range consumer configuration, with costs generally between $700 to $1,400 (or equivalent).

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | [Score](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Scoring/Models_Scoring_System.md) (Alpha v0.3.1) |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  |  [Llama-3.1-Nemotron-Nano-8B-v1](https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1) | 8B | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 62.81 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://huggingface.co/bartowski/nvidia_Llama-3.1-Nemotron-Nano-8B-v1-GGUF) via [GGUF](https://huggingface.co/docs/hub/ollama) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |  [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) | 14B |  10GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |  60.91 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-r1:32b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it) | 12B | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 59.60  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/https://ollama.com/library/gemma3:12b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/google/gemma-3-12b-it) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-Deep-7.8B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-7.8B) | 7.8B | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 59.29 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/exaone-deep) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)       | [Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)  | 14.8B | 10GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |  59.52 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:14b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/) | [Phi-4](https://huggingface.co/microsoft/phi-4) | 14B | 10GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 57.05 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/phi4) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)  | 7.62B | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) |  55.85 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:7b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |  [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B) | 7B | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) |  53.59 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-r1) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)     | [Ministral-8B-Instruct](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) | 8B  | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better)       | 51.52 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF) via [GGUF](https://huggingface.co/docs/hub/ollama) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   |  [OLMo-2-1124-13B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct) | 13B | 10GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 51.22  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/olmo2:13b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://playground.allenai.org/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) | 8B | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) |  50.71 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-r1) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) | 8B | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 49.87 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.1) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Groq.svg" alt="Groq" width="220" height="20" />](https://groq.com) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   |  [OLMo-2-1124-7B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct) | 7B | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 47.49  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/olmo2) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://playground.allenai.org/) |

<br>

***Tiny models*** : The smallest models are designed to run on all types of machines, including the oldest ones. These models can be run on most consumer hardware configurations, provided they have at least 6-8 GB of RAM.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | [Score](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Scoring/Models_Scoring_System.md) (Alpha v0.3.1) |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-3.2-3b-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) | 3B | 6GB+ RAM  | 53.89 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.2:3b) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-Deep-2.4B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-2.4B) | 2.4B | 6GB+ RAM  | 51.69 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.2:3b) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)         | [Gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it) | 4B | 8GB+ RAM | 50.20 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/gemma3:4b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/google/gemma-3-4b-it) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenBMB.svg" alt="OpenBMB" width="200" height="20" />](https://www.openbmb.cn/) | [MiniCPM3-4B](https://huggingface.co/openbmb/MiniCPM3-4B) | 4B | 8GB+ RAM | 49.99  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://huggingface.co/openbmb/MiniCPM3-4B-GGUF) via [GGUF](https://huggingface.co/docs/hub/ollama) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | [Ministral-3B-Instruct](https://huggingface.co/ministral/Ministral-3b-instruct) | 3B  | 6GB+ RAM | 46.60  |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://huggingface.co/QuantFactory/Ministral-3b-instruct-GGUF) via [GGUF](https://huggingface.co/docs/hub/ollama) | None | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)        | [Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)  | 3B | 6GB+ RAM | 45.95 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:3b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)        | [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) | 1.5B | 4GB+ RAM | 39.79 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:1.5b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |  [DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) | 1.5B | 4GB+ RAM | 36.96 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-r1:1.5b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)          | [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) | 1B | 4GB+ RAM | 36.32 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.2:1b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Groq.svg" alt="Groq" width="220" height="20" />](https://groq.com) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it) | 1B | 4GB+ RAM | 34.47 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/gemma3:1b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/google/gemma-3-1b-it) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)        | [Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) | 0.5B | 4GB+ RAM | 31.37 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:0.5b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) |

<br>
<br>

### Proprietary Model

| Organization       | Model Name                                                                       | [Score](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Scoring/Models_Scoring_System.md) (Alpha v0.3.1) | [Context Window](https://research.ibm.com/blog/larger-context-window) | Reasoning Model | Pricing  |
|:------------------:|:---------------------------------------------------------------------------------|:--------------:|:---------------:|:---:|:-------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)  | [Gemini 2.5 Pro](https://deepmind.google/technologies/gemini/pro/) | 83.22 | 1M | ✔️ | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [o1](https://openai.com/index/learning-to-reason-with-llms/) | 81.83 | 200K | ✔️ | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [o3-mini](https://openai.com/index/learning-to-reason-with-llms/) | 81.07 | 200K | ✔️ | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)  | [Gemini 2.0 Pro](https://blog.google/technology/google-deepmind/gemini-model-updates-february-2025/) | 77.08 | 2M | ❌ | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [o1-mini](https://openai.com/o1/) | 76.95 | 128K | ✔️ | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/xAI.svg" alt="xAI" width="220" height="20" />](https://x.ai/) | [Grok-3](https://x.ai/blog/grok-3) | 75.4  | 1M | ✔️ | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude 3.7 Sonnet](https://claude.ai/) | 72.92 | 200k | ✔️ | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Doubao.svg" alt="doubao" width="150" height="20" />](https://team.doubao.com/en/) | [Doubao 1.5 Pro](https://team.doubao.com/en/special/doubao_1_5_pro) | 71.60 | 256K | ❌ |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4.5 (Preview)](https://openai.com/index/introducing-gpt-4-5/) | 68.90 | 128k | ❌ | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen 2.5 Max](https://qwenlm.github.io/blog/qwen2.5-max/) | 68.33 | 32K | ❌ | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Perplexity.svg" alt="Perplexity" width="150" height="20" />](https://www.perplexity.ai)  | [Sonar Pro](https://sonar.perplexity.ai/) | 66.87 | 200k | ❌ | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/BigModel.svg" alt="BigModel" width="150" height="20" />](https://bigmodel.cn/) | [GLM-4-Plus](https://bigmodel.cn/dev/howuse/glm-4) | 67.12  | 1M | ❌ | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4o](https://openai.com/index/hello-gpt-4o/) | 66.32 | 128K | ❌ |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/amazon.svg" alt="Amazon" width="200" height="20" />](https://aws.amazon.com/ai/) | [Nova Pro](https://aws.amazon.com/ai/) | 66.20 | 300K | ❌ | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/StepFun.svg" alt="Stepfun" width="150" height="20" />](https://platform.stepfun.com/) | [Step-2-16k-exp](https://platform.stepfun.com/) | 64.69  | 16K | ❌ | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Reka.svg" alt="Reka" width="150" height="20" />](https://www.reka.ai/) | [Reka Core](https://chat.reka.ai) | 60.18  | 128k | ❌ | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/MoonshotAI.svg" alt="moonshot" width="150" height="20" />](https://www.moonshot.cn/) | [Kimi-k1.5](https://github.com/MoonshotAI/Kimi-k1.5) | **Pending** | Unknown | ❌ | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Baidu.svg" alt="baidu" width="150" height="20" />](https://cloud.baidu.com/) | [ERNIE-4.5](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/dm8ag8pbl) | **Pending** | Unknown | ❌ | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Baidu.svg" alt="baidu" width="150" height="20" />](https://cloud.baidu.com/) | [ERNIE-X1](https://yiyan.baidu.com/) | **Pending** | Unknown |✔️ | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |

<br>
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
