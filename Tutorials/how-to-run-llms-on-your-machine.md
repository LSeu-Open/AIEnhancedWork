<div align="center"> 
 
<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Tutorials/TextGeneration.png">

<br>
<br>

 ***This guide explains how to set up and run language models on your computer, enabling you to maintain full control over your AI tools.***
 
 <br>

***<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20with%20Monocle.png" alt="Face with Monocle" width="25" height="25" /> Reading Time : +15min***

</div> 

## Table of Contents

* [Introduction](#introduction)
* [Find the Model that is right for you](#find-the-model-that-is-right-for-you)
* [LM Studio (Beginner)](#lm-studio)
* [Ollama (Intermediate)](#ollama)
* [Llama.cpp (Expert)](#llama-cpp)

<br>

## Introduction

This tutorial guides **individuals seeking greater control and transparency in their data processing by setting up a local Large Language Model (LLM) environment.*** We'll use Ollama as the backend and the Page Assist extension in your browser for this purpose.

#### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20in%20Clouds.png" alt="Face in Clouds" width="25" height="25" /> Challenges with Cloud-Based AI Services

* **Privacy Concerns** : Your data traverses remote servers, raising questions about who might access it and how it will be handled.
* **Lack of Transparency**: Complex algorithms make it difficult to understand or verify how your data is processed, potentially leading to biased results.
* **Security Risks** : Major AI providers handle vast amounts of user data, making them attractive targets for breaches.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Love-You%20Gesture.png" alt="Love-You Gesture" width="25" height="25" /> Benefits of Running LLMs Locally

* **Data Control** : Keep your information entirely on your machine, ensuring it's not shared with external parties.
* **Instant Performance** : Eliminate internet latency for real-time tasks and continuous interaction.
* **Simplified Compliance** : Maintain complete control over data storage and processing, easing adherence to privacy regulations.

<br>

## Find the Model that is right for you

This section provides you with the **knowledge and resources to select the right model for your specific needs.** The first table showcases open-source models that can be run locally on your machine. 

To help you choose, **I have outlined the estimated hardware requirements for each model.** These estimates generally assume the model is quantized (specifically using a common 4-bit quantization), a process that reduces the model's size and memory footprint, offering a good balance between performance and quality. Keep in mind that actual performance can vary based on the specific software used and your system's configuration.

Learn more about quantization [here](https://huggingface.co/blog/merve/quantization).

> [!IMPORTANT]
> Please note that while it is possible to **run models without a GPU**, doing so will load the model into RAM and perform inference using the CPU.
>
> ***This approach will significantly slow down inference speeds.***

### Open Source Models

***Large-scale models (>70 billion parameters)*** : These require significant amounts of both RAM and GPU memory, often rendering local installation infeasible for most users. Consequently, such models are predominantly deployed on cloud-based platforms designed to provide the essential computational resources needed.

| Organization       | Model                                                                 | Model Size  | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (Alpha v0.3.1) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Hardware requirement (using Q4 quantization)              |
|:------------------:|:---------------------------------------------------------------------|:-----------:|:---------------------------------:|:-----------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)       | [Deepseek-R1](https://huggingface.co/deepseek-ai/DeepSeek-V3)     | 685B        | 79.61 | ✔️ | 404GB+ VRAM GPU (5xH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Perplexity.svg" alt="Perplexity" width="150" height="20" />](https://www.perplexity.ai) | [R1-1776](https://huggingface.co/perplexity-ai/r1-1776) | 685B | 79.51 |✔️ | 404GB+ VRAM GPU (6xH100 or better) |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  | [Llama-3_1-Nemotron-Ultra-253B-v1](https://huggingface.co/nvidia/Llama-3_1-Nemotron-Ultra-253B-v1) | 253B | 76.20 | ✔️ |  133GB+ VRAM GPU (2xH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) | 235B | 75.13 | [Hybrid](https://qwenlm.github.io/blog/qwen3/) |  133GB+ VRAM GPU (2xH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)       | [Deepseek-v3](https://huggingface.co/deepseek-ai/DeepSeek-V3) | 236B | 72.79 | ❌ | 133GB+ VRAM GPU (2xH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/DeepCogito.svg" alt="DeepCogito" width="200" height="20" />](https://www.deepcogito.com/research/cogito-v1-preview) | [Cogito-v1-preview-llama-70B](https://huggingface.co/deepcogito/cogito-v1-preview-llama-70B) | 70B | 68.81 | ✔️ | 47GB+ VRAM GPU (2xRTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Tencent.svg" alt="Tencent" width="200" height="20" />](https://github.com/Tencent/) | [Hunyuan-Large](https://huggingface.co/tencent/Tencent-Hunyuan-Large) | 389B | 67.98 | ❌ | 300GB+ VRAM GPU (5xH100 or better) | 
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/MiniMax.svg" alt="MiniMax" width="200" height="20" />](https://www.minimaxi.com/en) | [MiniMax-Text-01](https://huggingface.co/MiniMaxAI/MiniMax-Text-01) | 456B | 67.73 | ❌ | 404GB+ VRAM GPU (6xH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)        | [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)  | 72.2B | 67.38 | ❌ | 47GB+ VRAM GPU (2xRTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | 402B | 67.14 | ❌ | 230+ VRAM GPU (4xH100 or better)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.3-70b-Instruct](https://ollama.com/library/llama3.3) | 70B | 66.64 | ❌ | 40GB+ VRAM GPU (2xRTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)       | [DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B) | 70.6B | 65.40 | ✔️ | 40GB+ VRAM GPU (2xRTX 4090 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)         | [Command A](https://huggingface.co/CohereForAI/c4ai-command-a-03-2025) | 111B | 64.25 | ❌ | 60GB+ VRAM GPU (3xRTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.1-405b-Instruct](https://ollama.com/library/llama3.1:405bt)  | 405B | 63.49 | ❌ | 60GB+ VRAM GPU (3xRTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | 109B | 63.29 | ❌ | 230+ VRAM GPU (4xH100 or better)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mistral-Large-2-Instruct](https://ollama.com/library/mistral-large)  | 123B | 60.38 | ❌ | 70GB+ VRAM GPU (3xRTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)         | [Command R+](https://ollama.com/library/command-r-plus)               | 104B | 49.01 | ❌ | 60GB+ VRAM GPU (3xRTX 4090 or better) |

<br>

***Mid-sized models (<14B parameters)*** : These are well-suited for local deployment on high-end workstations. However, such deployment demands substantial investment in hardware, including a powerful GPU and other components, with total costs generally falling between $2,000 to $3,400 (or equivalent).

| Organization       | Model                                                                 | Model Size  | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (Alpha v0.3.1) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Hardware requirement (using Q4 quantization)              |
|:------------------:|:---------------------------------------------------------------------|:-----------:|:---------------------------------:|:-----------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | 32B | 72.06 | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) | 30.5B | 71.42 | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  | [Llama-3_3-Nemotron-Super-49B-v1](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1) | 49B | 69.71 | ✔️ | 40GB+ VRAM GPU (2xRTX 4090 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)  | [GLM-Z1-32B-0414](https://huggingface.co/THUDM/GLM-Z1-32B-0414) | 32.3B | 69.51 | ✔️ |  20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/DeepCogito.svg" alt="DeepCogito" width="200" height="20" />](https://www.deepcogito.com/research/cogito-v1-preview) | [Cogito-v1-preview-qwen-32B](https://huggingface.co/deepcogito/cogito-v1-preview-qwen-32B) | 32.3B | 69.36 | ✔️ | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)  | [GLM-4-32B-0414](https://huggingface.co/THUDM/GLM-4-32B-0414) | 32.3B | 68.89 | ❌ | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Reka.svg" alt="Reka" width="150" height="20" />](https://www.reka.ai/) | [Reka Flash 3](https://huggingface.co/RekaAI/reka-flash-3) | 21B | 67.16 | ✔️ | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-Deep-32B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-32B) | 32B | 66.11 | ✔️ | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/ServiceNow.svg" alt="Service Now" width="200" height="20" />](https://www.servicenow.com/) | [Apriel-Nemotron-15b-Thinker](https://huggingface.co/ServiceNow-AI/Apriel-Nemotron-15b-Thinker) | 15B | 65.22 | ✔️ |  16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)  | 32B | 64.27 | ✔️ | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |  [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)| 32B | 62.62 | ✔️ |  20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) | 27B | 62.03 | ❌ |  16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mistral-Small-3](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) | 24B  | 57.84 | ❌ |  16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   | [OLMo-2-0325-32B-Instruct](https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct) | 32B | 57.40  | ❌ |  20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/AntGroup.svg" alt="AntGroup" width="250" height="25" />](https://github.com/inclusionAI)| [Ling-lite](https://huggingface.co/inclusionAI/Ling-lite) | 16.8B | 55.15 | ❌ | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) | [Command R](https://cohere.com/blog/command-r) | 32B | 39.53 | ❌ |  20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 
<br>

***Small models (<7B parameters)*** : These are lightweight and easily deployable on medium machines, offering broader accessibility. They typically require a mid-range consumer configuration, with costs generally between $700 to $1,400 (or equivalent).

| Organization       | Model                                                                 | Model Size  | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (Alpha v0.3.1) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Hardware requirement (using Q4 quantization)              |
|:------------------:|:---------------------------------------------------------------------|:-----------:|:---------------------------------:|:-----------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) | 14B | 69.33 | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/DeepCogito.svg" alt="DeepCogito" width="200" height="20" />](https://www.deepcogito.com/research/cogito-v1-preview) | [Cogito-v1-preview-qwen-14B](https://huggingface.co/deepcogito/cogito-v1-preview-qwen-14B) | 14B | 66.91 | ✔️ | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | 8B | 66.47 | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/) | [Phi-4-reasoning-plus](https://huggingface.co/microsoft/Phi-4-reasoning-plus) | 14B | 65.46 | ✔️ | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/) | [Phi-4-reasoning](https://huggingface.co/microsoft/Phi-4-reasoning) | 14B | 63.78 | ✔️ | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  |  [Llama-3.1-Nemotron-Nano-8B-v1](https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1) | 8B | 62.81 | ✔️ |  8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |  [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) | 14B | 60.91 | ✔️ | 10GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it) | 12B |  59.60  | ❌ | 12GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-Deep-7.8B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-7.8B) | 7.8B | 59.29 | ✔️ | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM) | [Internlm3-8b-instruct](https://huggingface.co/internlm/internlm3-8b-instruct) | 8B | 58.90 | ❌ | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-3.5-7.8B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct) | 7.8B | 58.00 | ❌ | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)  | [GLM-Z1-9B-0414](https://huggingface.co/THUDM/GLM-Z1-9B-0414) | 9B | 57.51 | ✔️ |  12GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/) | [Phi-4](https://huggingface.co/microsoft/phi-4) | 14B | 57.05 | ❌ |  12GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/DeepCogito.svg" alt="DeepCogito" width="200" height="20" />](https://www.deepcogito.com/research/cogito-v1-preview) | [Cogito-v1-preview-llama-8B](https://huggingface.co/deepcogito/cogito-v1-preview-llama-8B) | 8B | 56.24 | ✔️ | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Xiaomi.svg" alt="Xiaomi" width="200" height="20" />](https://www.mi.com/global/) | [MiMo-7B-RL](https://huggingface.co/XiaomiMiMo/MiMo-7B-RL) | 7B | 55.04 | ✔️ | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/IBM.svg" alt="ibm" width="200" height="20" />](https://github.com/ibm-granite/) | [Granite-3.3-8b-instruct](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct) | 8B | 54.91 | ❌ | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) |  [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B) | 7B |  53.59 | ✔️ | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)     | [Ministral-8B-Instruct](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) | 8B  | 51.52 | ❌ | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   |  [OLMo-2-1124-13B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct) | 13B | 51.22  | ❌ |  12GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) | 8B | 50.71 | ✔️ | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)           | [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) | 8B | 49.87 | ❌ |  8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   |  [OLMo-2-1124-7B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct) | 7B | 47.49  | ❌ |  8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 

<br>

***Tiny models*** : The smallest models are designed to run on all types of machines, including the oldest ones. These models can be run on most consumer hardware configurations, provided they have at least 6-8 GB of RAM.

| Organization       | Model                                                                 | Model Size  | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (Alpha v0.3.1) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Hardware requirement (using Q4 quantization)              |
|:------------------:|:---------------------------------------------------------------------|:-----------:|:---------------------------------:|:-----------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) | 4B | 60.87 | [Hybrid](https://qwenlm.github.io/blog/qwen3/) |  6GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/DeepCogito.svg" alt="DeepCogito" width="200" height="20" />](https://www.deepcogito.com/research/cogito-v1-preview) | [Cogito-v1-preview-llama-3B](https://huggingface.co/deepcogito/cogito-v1-preview-llama-3B) | 3B | 56.74 | ✔️ | 6GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | 1.7B | 54.70 | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | 4GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) | 3B | 53.89 | ❌ | 6GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-3.5-2.4B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct) | 2.4B | 51.69 |❌ | 4GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-Deep-2.4B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-2.4B) | 2.4B | 50.90 | ✔️ | 4GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it) | 4B | 50.20 | ❌ | 8GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenBMB.svg" alt="OpenBMB" width="200" height="20" />](https://www.openbmb.cn/) | [MiniCPM3-4B](https://huggingface.co/openbmb/MiniCPM3-4B) | 4B | 49.99  | ❌ | 8GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/ServiceNow.svg" alt="Service Now" width="200" height="20" />](https://www.servicenow.com/)  | [Apriel-5B-Instruct](https://huggingface.co/ServiceNow-AI/Apriel-5B-Instruct) | 5B | 49.53 | ❌ | 8GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/IBM.svg" alt="ibm" width="200" height="20" />](https://github.com/ibm-granite/) | [Granite-3.3-2b-instruct](https://huggingface.co/ibm-granite/granite-3.3-2b-instruct) | 2B | 46.72 | ❌ | 4GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | [Ministral-3B-Instruct](https://mistral.ai/news/ministraux/) | 3B | 46.60 | ❌ | 6GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | 0.6B | 42.12 | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | 4GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) | 1.5B | 36.96 | ✔️ |  4GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) | 1B | 36.32 | ❌ |  4GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   | [OLMo-2-0425-1B-Instruct](https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct) | 1B | 36.43 | ❌ |  4GB+ RAM  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it) | 1B | 31.47 | ❌ | 4GB+ RAM  |

<br>
<br>

## LM Studio 

***(Beginner)*** LM Studio is a powerful yet user-friendly tool for running large language models (LLMs) on your local machine. It's especially well-suited for beginners who want to experiment with AI without needing advanced technical skills or an internet connection.

### Why Use LM Studio?

LM Studio offers several advantages that make it ideal for **newcomers**:

**Ease of Use**: It provides a graphical user interface (GUI), so you don't need to know command-line tools or coding.

**Privacy**: Since models run locally, your data stays on your machine — no uploading required.

**Model Access**: You can easily download and use many popular open-source LLMs.

### System Requirements

Before installing LM Studio, make sure your system meets the following minimum requirements:

**RAM**: At least 8GB (16GB or more is recommended for larger models).

**Storage**: Enough space to store model files (typically between 2GB and 20GB+).

**CPU/GPU**: A modern CPU is sufficient. An NVIDIA or AMD GPU can improve performance, but it's not required. Mac users with M1/M2/M3/M4 chips don't need a separate GPU.

**Operating System**:: Windows (x86/ARM), macOS (M1–M4 recommended), or Linux (x86 with AVX2 support)

### Installation

To get started, follow these simple steps:

1. Go to the official [LM Studio website](https://lmstudio.ai/).
2. Download the installer for your operating system.
3. Run the installer and follow the on-screen instructions.
4. Launch LM Studio after installation is complete.

### Finding and Downloading Models

Once installed, you can use LM Studio to find, download, and run a wide variety of open-source LLMs.

1. Open LM Studio and click the Discover tab (magnifying glass icon) or use Ctrl + 2 (Windows/Linux) / Cmd + 2 (macOS).
2. Browse featured models or search for specific ones like "Llama", "Phi-3", "Mistral", or "Gemma" based on the info you gathered in the [Find the Model that is right for you section](#find-the-model-that-is-right-for-you).
3. Choose a model version: many are available in quantized forms (e.g., Q4_K_M), which are optimized for performance and size. LM Studio will automatically select the most suitable version based on your machine specifications.
4. Click Download to get the model.

### Loading a Model

After downloading, you can load the model into LM Studio.

1. Go to the AI Chat tab (chat bubble icon) or use Ctrl + 3 (Windows/Linux) / Cmd + 3 (macOS).
2. Open the Model Loader by clicking the dropdown at the top center or using Ctrl + L (Windows/Linux) / Cmd + L (macOS).
3. Select the model you downloaded.
4. Click Load — LM Studio will allocate memory to run the model. Default loading settings usually work well for beginners.

### Chatting with the Model

Once a model is loaded, you can start interacting with it:

1. Type your question or prompt in the message box at the bottom of the screen.
2. Press Enter to send.
3. The AI will process and respond locally — no internet connection required.

You'll see the response appear immediately in the chat window.

For more detailed information, please refer to the [official LM Studio documentation](https://lmstudio.ai/docs/app). Read more on [Downloading Models](https://lmstudio.ai/docs/app/basics/download-model) or [Manage chats](https://lmstudio.ai/docs/app/basics/chat).

<br>
<br>

## Ollama 

***(Intermediate)*** Ollama is our top recommendation for running LLMs locally for non beginners users due to its robust integration capabilities and adaptability. 

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

For those who prefer a more user-friendly experience, we'll demonstrate how to interact with your Ollama model through our browser-based interface, which provides a graphical and intuitive way of working with your LLM. We will be using the [Page assist extension](https://github.com/n4ze3m/page-assist).

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

After installation, I suggest the following steps :

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
<br>

## Llama cpp 

***(Expert)*** Llama.cpp is a high-performance C++ library designed to run large language models (LLMs) efficiently on various hardware platforms. It supports both standard CPUs and systems with limited resources, making it ideal for deploying quantized models in the **GGUF** format.

### Prerequisites

Before you begin, make sure the following tools are installed:

1. Git
Git is used to clone the Llama.cpp repository from GitHub.

2. Build Tools (Based on Your OS)

- Linux:
Install essential build tools using `apt`:

```bash
sudo apt update && sudo apt install build-essential cmake git
```

- macOS:
Install Xcode command line tools:

```bash
xcode-select --install
```

- Windows:
Use **MSYS2** or a similar environment that provides C++ compilation tools such as `make`, `g++`, and `clang++`. Git for Windows often includes these tools by default.

---

3. Python (Optional)

Python is optional but required if you plan to use the Python bindings (`llama-cpp-python`). You can install it using:

```bash
sudo apt install python3   # Linux
brew install python     # macOS
```

### Installation and Setup

You have two main options for using Llama.cpp: either via its **C++ executable** or through **Python bindings**.

#### Option 1: Using the Core C++ Executable

This is the most straightforward way to run Llama.cpp on your system.

**Step 1: Clone the Repository**

Open a terminal and run:

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
```

**Step 2: Build the Project**

Compile the source code using `make`:

```bash
make
```

This builds the main executable, `./main`, which is optimized for **CPU inference**. For significantly improved performance on compatible hardware, you can build with GPU acceleration (e.g., using `make LLAMA_CUDA=1` for NVIDIA GPUs). Refer to the official documentation for specific commands for CUDA, Metal (macOS), and other backends.

> 🔧 **Note**: For GPU acceleration (CUDA, Metal), you'll need to use specific build commands. See the [Llama.cpp Build Documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) for more details.


**Step 3: Verify the Build (Optional)**

You can check the available command-line options by running:

```bash
./main -h
```

This will display all the supported flags and usage examples.


#### Option 2: Using Python Bindings (`llama-cpp-python`)

If you want to use Llama.cpp within Python, follow these steps:

**Step 1: Create a Virtual Environment**

It's recommended to create an isolated environment to avoid package conflicts.

Using **Conda**:

```bash
conda create --name llama-cpp-env
conda activate llama-cpp-env
```

Using **Python's built-in `venv`** (Linux/macOS):

```bash
python -m venv llama-cpp-env
source llama-cpp-env/bin/activate  # On Linux/macOS
```

On Windows:

```bash
llama-cpp-env\Scripts\activate
```

**Step 2: Install the Python Bindings**

Install `llama-cpp-python` using pip:

```bash
pip install llama-cpp-python
```

**Step 3: Verify Installation (Optional)**

Run a simple test to confirm it's working:

```bash
python -c "from llama_cpp import Llama; print('llama-cpp-python installed successfully!')"
```

### Getting a Model

Llama.cpp primarily uses models in the **GGUF** format, which are quantized versions of popular large language models. These allow running large models with reduced memory usage.

### Steps to Get a GGUF Model:

1. Visit [Hugging Face Hub](https://huggingface.co/) and search for models compatible with Llama.cpp (e.g., "Llama-3-8B-Instruct-GGUF").
2. Choose the desired **quantization level**:
   - `Q4_K_M`: Low memory usage, good for most users.
   - `Q5_K_M`, `Q8_0`: Higher quality but uses more memory.
3. Download the `.gguf` file and save it in a known location (e.g., `models/`).


### Running Inference

#### Option 1 : Using the Core Executable (`./main`)

Run inference from the command line:

```bash
./main -m <path_to_model.gguf> -p "<your_prompt>" [options]
```

**Example:**

```bash
./main -m ./models/llama-3-8b-instruct.Q4_K_M.gguf \
      -p "Explain the theory of relativity in simple terms." \
      -n 256 \          # Max tokens to generate
      -c 2048 \         # Context size (must be >= prompt length + max tokens)
      --temp 0.7        # Temperature setting for randomness
```

**Flags explained:**

- `-m`: Path to your GGUF model file.
- `-p`: The prompt or input text you want the model to respond to.
- `-n`: Maximum number of tokens (words/subwords) to generate.
- `-c`: Context size — how much text the model considers at once. Should be >= prompt length + max tokens.
- `--temp`: Temperature value for controlling randomness.


#### Option 2 : Using Python Bindings

Here's a simple example script (`inference.py`) that loads and runs a model:

```python
from llama_cpp import Llama

# Load the model (adjust path as needed)
llm = Llama(
    model_path="./models/llama-3-8b-instruct.Q4_K_M.gguf",
    n_ctx=2048,      # Context window size
    n_gpu_layers=-1,   # Use GPU if available
    verbose=True     # Show detailed output
)

# Define the prompt
user_prompt = "What are the main benefits of using Python?"

# Generate text
output = llm(
    user_prompt,
    max_tokens=256,
    temperature=0.7,
    top_p=0.9,
    echo=True,        # Include the prompt in output
    stop=["\n", "User:"]
)

# Process and print the result
if output and 'choices' in output and len(output['choices']) > 0:
    generated_text = output['choices'][0]['text']
    response_only = generated_text.replace(user_prompt, "", 1).strip()
    print("Model Response:\n", response_only)
else:
    print("No output generated.")
```

**To run the script:**

```bash
python inference.py
```

## Next Steps

This tutorial covers the basics of setting up and using Llama.cpp. For more advanced features such as:

- **Multi-GPU support**
- **Grammar-based output control**
- **Quantization tuning**
- **Custom sampling methods**

You can refer to the [official Llama.cpp documentation](https://github.com/ggml-org/llama.cpp).

<br>
<br>
