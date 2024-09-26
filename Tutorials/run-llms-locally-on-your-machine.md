# How to run LLMs locally on your machine

<div align="center">
 
 ⚠️ **OVERALL STRUCTURE IMPROVEMENT IN PROGRESS** ⚠️ 

**We are currently enhancing this page to provide better content. We appreciate your patience as you wait for the finalized version.**

**Please note that this is a work-in-progress tutorial and may contain inaccuracies or incomplete information.**
  
</div>

## Table of Contents

* [Introduction](#introduction)
  + [The Privacy and security issue of Cloud based Providers](#the-privacy-and-security-issue-of-cloud-based-providers)
  + [Benefits of Running LLM Models Locally](#benefits-of-running-llm-locally) 
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

### The Privacy and security issue of Cloud based Providers

The use of Large Language Model (LLM) services online presents significant privacy concerns:

* ***Data Storage and Processing by Third Parties***: Your data is stored and processed by third-party providers, which can result in unintended consequences such as:
  * Sharing your input data with other users.
  * Using your data for purposes beyond your initial intent.

* ***Algorithm Complexity***: The complexity of the algorithms used to train these models poses challenges:
  * **Opacity**: Algorithms are often opaque, making it difficult to understand how your data is being processed.
  * **Bias and Discrimination**: This lack of transparency can lead to biased or discriminatory outcomes.

* ***Scale and Data Breaches***: The large scale of cloud-based LLMs means that even minor issues can result in:
  * Massive data breaches.
  * Compromising the privacy and security of countless users.

### Benefits of Running LLM Locally

Running Large Language Model (LLM) models locally offers several compelling benefits:

* ***Complete Control Over Input Data***: Maintain complete control over your input data and ensure its confidentiality – no sensitive information will be shared with third-party providers.

* ***Faster Processing Times and Reduced Latency***: Enjoy faster processing times and reduced latency, making it well-suited for applications where real-time feedback is crucial.

* ***Avoidance of Data Sovereignty Issues***: Keeping your data and model on-premises helps you avoid potential issues related to:
  * Compliance with data localization requirements.
  * Regulatory standards.
    
Ultimately, running LLM models locally provides a high degree of **privacy and control**, allowing you to tailor the model's training and deployment to meet your specific goals and objectives.

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

### Open Source Models

***Massive models*** : Challenging for local deployment due to computational requirements.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Quality Index |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| **Alibaba**        | [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)  | 72.2B         | 47GB+ VRAM GPU (2xRTX 4090 or better) |  75.25 | [Yes](https://ollama.com/library/qwen2.5:72b-instruct) | No |
| **Mistral**        | [Mistral-Large-2-Instruct](https://ollama.com/library/mistral-large)  | 123B        | 70GB+ VRAM GPU (3xRTX 4090 or better) | 73    | [Yes](https://ollama.com/library/mistral-large) | [Mistral](https://mistral.ai/)  |
| **Meta**           | [Llama-3.1-405b-Instruct](https://ollama.com/library/llama3.1:405bt)  | 405B        | 230+ VRAM GPU (4xH100 or better)  |  71.9       | [Yes](https://ollama.com/library/llama3.1:405b) | [OpenRouter](https://openrouter.ai/chat?models=meta-llama/llama-3.1-405b) |          
| **Alibaba**        | [Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct)  | 72B         | 40GB+ VRAM GPU (2xRTX 4090 or better) |  68.9 | [Yes](https://ollama.com/library/qwen2:72b-instruct) | [Hugging Face](https://huggingface.co/spaces/Qwen/Qwen2-72B-Instruct) |
| **Deepseek**       | [Deepseek-v2.5](https://huggingface.co/deepseek-ai/DeepSeek-V2.5)     | 236B        | 133GB+ VRAM GPU (2xH100 or better) |  65.8 | [Yes](https://ollama.com/library/deepseek-v2.5) | [Deepseek](https://platform.deepseek.com/sign_in) |
| **Meta**           | [Llama-3.1-70b-Instruct](https://ollama.com/library/llama3.1:70b-instruct-q4_0) | 70B | 40GB+ VRAM GPU (2xRTX 4090 or better) | 65.3  | [Yes](https://ollama.com/library/llama3.1:70b)  | [Groq](https://groq.com/) |
| **Meta**           | [Llama-3-70b-Instruct](https://ollama.com/library/llama3:70b-instruct) | 70B        | 40GB+ VRAM GPU (2xRTX 4090 or better) | 61.9    | [Yes](https://ollama.com/library/llama3:70b-instruct) | [Groq](https://groq.com/) |
| **Mistral**        | [Mixtral-8x22b-Instruct-v0.1](https://ollama.com/library/mixtral:8x22b-instruct) | 141B | 80GB+ VRAM GPU (1xH100 or better) | 61.4    | [Yes](https://ollama.com/library/mixtral:8x22b-instruct) | [Perplexity Labs](https://labs.perplexity.ai/) |
| **Cohere**         | [Command R+](https://ollama.com/library/command-r-plus)               | 104B        | 60GB+ VRAM GPU (3xRTX 4090 or better) | 55.9 | [Yes](https://ollama.com/library/command-r-plus)   | [Cohere](https://cohere.com/command) |
| **Databricks**     | [DBRX-Instruct](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm) | 132B | 80GB+ VRAM GPU (1xH100 or better) | 49.6    | [Yes](https://ollama.com/library/dbrx:instruct) | No | 


**Mid-sized models** : Suitable for deployment on a high-performance local workstation.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Quality Index |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| **Mistral**        | [Mistral-Small-Instruct](https://huggingface.co/mistralai/Mistral-Small-Instruct-2409) | 22.2B  | 13GB+ VRAM GPU (RX 7800 or RTX 4080 or better | 60.40    | [Yes](https://ollama.com/library/mistral-small) | [Mistral](https://mistral.ai/)  |
| **Cohere**         | [Command R](https://ollama.com/library/command-r)                     | 35B         | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 51.1 | [Yes](https://ollama.com/library/command-r)   | [Cohere](https://cohere.com/command) |
| **Google**         | [Gemma-2-27b-it](https://huggingface.co/google/gemma-2-27b-it)        | 27B         | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) | 48.55 | [Yes](https://ollama.com/library/gemma2:27b-instruct-q4_0) | [Hugging Face](https://huggingface.co/google/gemma-2-27b-it) |
| **Mistral**        | [Mixtral-8x7b-Instruct-v0.1](https://mistral.ai/news/mixtral-of-experts/) | 46.7B   | 26GB+ VRAM GPU (1xH100 or better) | 41.9    | [Yes](https://ollama.com/library/mixtral:instruct) | [Perplexity Labs](https://labs.perplexity.ai/) |
| **Alibaba**        | [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)  | 32.8B         | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |  Inc | [Yes](https://ollama.com/library/qwen2.5:32b-instruct) | No |

***Small models*** : Lightweight and deployable on most local machines.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Quality Index |  Ollama library |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| **Meta**           | [Llama-3.2-11b-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct)       | 10.7B          | 8GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 53.20 | No | [Hugging Face](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct)|
| **Meta**           | [Llama-3.1-8b-Instruct](https://ollama.com/library/llama3.1:8b)       | 8B          | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 53.15 | [Yes](https://ollama.com/library/llama3.1:8b) | [Groq](https://groq.com/) |
| **Google**         | [Gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it)          | 9B          | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 46.650 | [Yes](https://ollama.com/library/gemma2:9b-instruct-q4_0) | [Hugging Face](https://huggingface.co/spaces/huggingface-projects/gemma-2-9b-it) |
| **Meta**           | [Llama-3-8b-Instruct](https://ollama.com/library/llama3:instruct)     | 8B          | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 46.1 | [Yes](https://ollama.com/library/llama3:instruct) | [Perplexity Labs](https://labs.perplexity.ai/) |
| **Meta**           | [Llama-3.2-3b-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)       | 3B          | 2GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 45.35 | [Yes](https://ollama.com/library/llama3.2:3b-instruct-q4_K_M) | [Groq](https://groq.com/) |
| **Microsoft**      | [Phi-3-medium-128k-instruct](https://huggingface.co/microsoft/Phi-3-medium-128k-instruct) | 14B | 8GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | None | [Yes](https://ollama.com/library/phi3:14b-instruct) | No |
| **Alibaba**        | [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)  | 7.62B         | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) |  Inc | [Yes](https://ollama.com/library/qwen2.5:7b-instruct) | No |


### Proprietary Model

| Model                                         | Provider     | Quality Index | Pricing |
|:----------------------------------------------|:------------:|:----------:|:-------:|
| [GPT-o1-preview](https://chat.openai.com/)    | **OpenAI**   | 84.6       | Paid    |
| [Gemini 1.5 Pro](https://gemini.google.com/advanced?hl=en) | **Google** | 79.7 | Paid    |
| [GPT-4o-latest](https://chat.openai.com/)     | **OpenAI**   | 77.2       | Paid    |
| [GPT-4o-mini](https://chat.openai.com/)       | **OpenAI**    | 71.4       | Freemium    |
| [Claude-3.5 Sonnet](https://claude.ai//)      | **Anthropic** | 76.9       | Paid    |
| [GPT-4 Turbo](https://chat.openai.com/)       | **OpenAI**    | 74.3       | Paid    |
| [Claude-3 Opus](https://claude.ai/)           | **Anthropic** | 70.3       | Paid    |
| [Gemini 1.5 Flash](https://deepmind.google/technologies/gemini/flash/)  | **Google** | 68.0 | Paid |
| [Yi-Large](https://www.01.ai/)                | **01.ai**     | 58.3       | Freemium |
| [Claude-3 Sonnet](https://claude.ai/)         | **Anthropic**  | 57.2       | Freemium    |
| [Reka-Core](https://www.reka.ai/)             | **Reka**       | 56.8       | Freemium |
| [Claude-3 Haiku](https://claude.ai/)          | **Anthropic**  | 54.2       | Freemium    |
| [Reka-Flash](https://www.reka.ai/)            | **Reka**       | 46.2       | Freemium |

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

<div align="center">
 
**👉 [Help me pick a model !](#find-the-model-that-is-right-for-you) 👈**
  
</div>

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
