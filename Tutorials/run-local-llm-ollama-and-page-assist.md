![header](Header_local_llms.png)

## Table of Contents

* [Introduction](#introduction)
  + [The Privacy and security issue of Cloud based Providers](#the-privacy-and-security-issue-of-cloud-based-providers)
  + [Benefits of Running LLM Models Locally](#benefits-of-running-llm-locally) 
* [Step 1 Install and Setup Ollama](#step-1-install-and-setup-ollama)
  + [Installation](#installation)
  + [Quickstart](#quickstart)
* [Step 2 Use Ollama in your browser using Page assist extension](#step-2-use-ollama-in-your-browser-using-page-assist-extension)
  + [Installation and setup](#installation-and-setup)
  + [Browser Support](#browser-support)
  + [Usage](#usage)
 * [Find the Model that is right for you](#find-the-model-that-is-right-for-you)

<br>

## Introduction

This tutorial is designed for ***individuals seeking greater control and transparency*** in their data processing, regardless of their background or expertise. I will provide a step-by-step guide on how to set up a local LLM environment using Ollama as the backend and Page Assist extension in your browser.

### The Privacy and security issue of Cloud based Providers

Using Large Language Model (LLM) services online raises significant privacy concerns. One major issue is that your data is stored and processed by third-party providers, which can lead to unintended consequences. For example, your input data may be shared with other users or used for purposes beyond what you initially intended.

The complexity of the algorithms used to train these models also poses a problem. These algorithms are often opaque, making it difficult to understand how your data is being processed and potentially leading to biased or discriminatory outcomes.

Finally, the sheer scale of cloud-based LLMs means that even minor issues can result in massive data breaches, compromising the privacy and security of countless users

### Benefits of Running LLM Locally

Running Large Language Model (LLM) models locally offers several benefits. One major advantage is that it allows you to maintain complete control over your input data and ensure its confidentiality - no sensitive information will be shared with third-party providers.

This approach also enables faster processing times and reduced latency, making it well-suited for applications where real-time feedback is crucial. By keeping your data and model on-premises, you can avoid potential issues related to data sovereignty, such as data localization requirements and regulatory compliance.

Ultimately, running LLM models locally provides a high degree of privacy and control, allowing you to tailor the model's training and deployment to meet your specific goals and objectives.

<br>

## Step 1 Install and Setup Ollama

### Installation

| Platform          | Installation Method |
|:-----------------:|:--------------------:|
| **macOS**         | [Download](https://ollama.com/download/Ollama-darwin.zip) |
| **Windows** | [Download](https://ollama.com/download/OllamaSetup.exe)  |
| **Linux**          | [Manual install instructions](https://github.com/ollama/ollama/blob/main/docs/linux.md) |
| **Docker**         | [Ollama Docker image](https://hub.docker.com/r/ollama/ollama) is available on Docker Hub.  |

### Quickstart

> [!Note]
> You should have at least 6 GB of VRAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.
> Depending on your hardware specifications The model might take a long time to generate text or process requests.

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

## Step 2 Use Ollama in your browser using Page assist extension

It is not comfortable working directly in the command-line interface (CLI) for most, so i will show you how to interact with your Ollama model using a browser-based interface. We will be using the [Page assist extension](https://github.com/n4ze3m/page-assist).

Page Assist is an open-source Chrome Extension that provides a Sidebar and Web UI for your Local AI model. It allows you to interact with your model from any webpage.

Want to explore other possibilities? Take a look at the alternative solutions available in our [Local Providers section](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/README.md#local-providers-1).

### Installation and setup 

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

## Usage

### Sidebar

Once the extension is installed, you can **open the sidebar via context menu or keyboard shortcut**.  By exploiting this sidebar functionality, you can engage in seamless conversations with your model while **leveraging the current web page as contextual reference (website, documentation, PDF...).**

▶️ in order to use `chat with the current page` option you need to set a Embedding Model in the `RAG Settings`.

> Default Keyboard Shortcut: `Ctrl+Shift+P`

### Web UI

You can open the Web UI by clicking on the extension icon which will open a new tab with the Web UI.

> Default Keyboard Shortcut: `Ctrl+Shift+L`

> [!Note]
> You can change the keyboard shortcuts from the extension settings on the Chrome Extension Management page.

<br>

## Find the Model that is right for you

This section is designed to provide you with the **necessary knowledge and resources to make informed decisions about selecting the right model for your specific needs**. To facilitate this process, I have prepared **two reference tables to support your search**.

> The first table showcases **open-source models**, which can be **run locally on your machine.** To ensure optimal performance, I have outlined the **recommended hardware requirements for each model**. Please note that while it may be possible to run certain models with lower hardware specifications, this may result in slower output and performance. 

> For **users with limited system resources** or older hardware configurations, I will also provide guidance on **cloud-based providers that can efficiently run these models**.

> The second table features **proprietary models**, which typically operate on cloud-based providers.

> [!NOTE]
> The models are ranked according to their **Elo scores (with higher scores indicating better performance)** from the [LMSys Chatbot Arena Leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard). Please note that **Elo scores are subject to change** based on user votes and will be updated regularly to reflect the latest rankings.


### Open Source Models (1100+ Elo score)

***Massive models*** : Challenging for local deployment due to computational requirements.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              |  Elo score  |  Ollama libraries |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| **Meta**           | [Llama-3.1-405b-Instruct](https://ollama.com/library/llama3.1:405bt)  | 405B        | 230+ VRAM GPU (4xH100 or better)  |  1262       | [Yes](https://ollama.com/library/llama3.1:405b) | [OpenRouter](https://openrouter.ai/chat?models=meta-llama/llama-3.1-405b) |          
| **Mistral**        | [Mistral-Large-2-Instruct](https://ollama.com/library/mistral-large)  | 123B        | 70GB+ VRAM GPU (3xRTX 4090 or better) | 1248    | [Yes](https://ollama.com/library/mistral-large) | [Mistral](https://mistral.ai/)  |
| **NexusFlow**      | [Athene-70B](https://huggingface.co/Nexusflow/Athene-70B)             | 70B         | 40GB+ VRAM GPU (2xRTX 4090 or better) | 1248    | No                                              | [Hugging Face](https://huggingface.co/Nexusflow/Athene-70B) |
| **Meta**           | [Llama-3.1-70b-Instruct](https://ollama.com/library/llama3.1:70b-instruct-q4_0) | 70B | 40GB+ VRAM GPU (2xRTX 4090 or better) | 1240  | [Yes](https://ollama.com/library/llama3.1:70b)  | [Groq](https://groq.com/) |
| **Nvidia**         | [Nemotron-4-340B-Instruct](https://huggingface.co/nvidia/Nemotron-4-340B-Instruct) | 340B | 160GB+ VRAM GPU ( 2xH100 or better) |  1206 | No                                            | [Nvidia](https://build.nvidia.com/nvidia/nemotron-4-340b-instruct) |
| **Meta**           | [Llama-3-70b-Instruct](https://ollama.com/library/llama3:70b-instruct) | 70B        | 40GB+ VRAM GPU (2xRTX 4090 or better) | 1190    | [Yes](https://ollama.com/library/llama3:70b-instruct) | [Groq](https://groq.com/) |
| **Cohere**         | [Command R+](https://ollama.com/library/command-r-plus)               | 104B        | 60GB+ VRAM GPU (3xRTX 4090 or better) | 1187 | [Yes](https://ollama.com/library/command-r-plus)   | [Cohere](https://cohere.com/command) |
| **Alibaba**        | [Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct)  | 72B         | 40GB+ VRAM GPU (2xRTX 4090 or better) |  1162 | [Yes](https://ollama.com/library/qwen2:72b-instruct) | [Hugging Face](https://huggingface.co/spaces/Qwen/Qwen2-72B-Instruct) |
| **Alibaba**        | [Qwen1.5-110B-Chat](https://ollama.com/library/qwen:110b-chat)        | 110B        | 70GB+ VRAM GPU (4xRTX 4090 or better) |  1159 | [Yes](https://ollama.com/library/qwen:110b-chat) | [Hugging Face](https://huggingface.co/spaces/Qwen/Qwen1.5-110B-Chat-demo)  |
| **Alibaba**        | [Qwen1.5-72B-Chat](https://ollama.com/library/qwen:72b-chat)          | 72B         | 40GB+ VRAM GPU (2xRTX 4090 or better) |  1149 | [Yes](https://ollama.com/library/qwen:72b-chat) | [Hugging Face](https://huggingface.co/spaces/Qwen/Qwen1.5-72B-Chat)   |
| **Mistral**        | [Mixtral-8x22b-Instruct-v0.1](https://ollama.com/library/mixtral:8x22b-instruct) | 141B | 80GB+ VRAM GPU (1xH100 or better) | 1246    | [Yes](https://ollama.com/library/mixtral:8x22b-instruct) | [Perplexity Labs](https://labs.perplexity.ai/) |
| **Databricks**     | [DBRX-Instruct](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm) | 132B | 80GB+ VRAM GPU (1xH100 or better) | 1103    | [Yes](https://ollama.com/library/dbrx:instruct) | No | 
 
**Mid-sized models** : Suitable for deployment on a high-performance local workstation.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              |  Elo score  |  Ollama libraries |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| **Google**         | [Gemma-2-27b-it](https://huggingface.co/google/gemma-2-27b-it)        | 27B         | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) | 1218 | [Yes](https://ollama.com/library/gemma2:27b-instruct-q4_0) | [Hugging Face](https://huggingface.co/google/gemma-2-27b-it) |
| **Cohere**         | [Command R](https://ollama.com/library/command-r)                     | 35B         | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 1149 | [Yes](https://ollama.com/library/command-r)   | [Cohere](https://cohere.com/command) |
| **Mistral**        | [Mixtral-8x7b-Instruct-v0.1](https://mistral.ai/news/mixtral-of-experts/) | 46.7B   | 26GB+ VRAM GPU (1xH100 or better) | 1114    | [Yes](https://ollama.com/library/mixtral:instruct) | [Perplexity Labs](https://labs.perplexity.ai/) |

***Small models*** : Lightweight and deployable on most local machines.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              |  Elo score  |  Ollama libraries |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| **Google**         | [Gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it)          | 9B          | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 1187 | [Yes](https://ollama.com/library/gemma2:9b-instruct-q4_0) | [Hugging Face](https://huggingface.co/spaces/huggingface-projects/gemma-2-9b-it) |
| **Meta**           | [Llama-3.1-8b-Instruct](https://ollama.com/library/llama3.1:8b)       | 8B          | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 1161 | [Yes](https://ollama.com/library/llama3.1:8b) | [Groq](https://groq.com/) |
| **Meta**           | [Llama-3-8b-Instruct](https://ollama.com/library/llama3:instruct)     | 8B          | 6GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 1152 | [Yes](https://ollama.com/library/llama3:instruct) | [Perplexity Labs](https://labs.perplexity.ai/) |
| **Google**         | [Gemma-2-2b-it](https://ollama.com/library/gemma2:2b-instruct-q4_0)   | 2B          | 2GB+ VRAM GPU (rx 6500 or RTX 3050 or better) | 1127 | [Yes](https://ollama.com/library/gemma2:2b-instruct-q4_0) | [Hugging Face](https://huggingface.co/google/gemma-2-2b-it) |
| **Microsoft**      | [Phi-3-medium-128k-instruct](https://huggingface.co/microsoft/Phi-3-medium-128k-instruct) | 14B | 8GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 1123 | [Yes](https://ollama.com/library/phi3:14b-instruct) | No |
| **Microsoft**      | [Phi-3-small-8k-instruct](https://huggingface.co/microsoft/Phi-3-small-8k-instruct) | 7B | 8GB+ VRAM GPU (rx 7600 or RTX 4060 or better) | 1101 | No | No |

### Proprietary Model (1100+ Elo score)

| Model                                         | Provider     | Elo score  | Pricing |
|:----------------------------------------------|:------------:|:----------:|:-------:|
| [Gemini 1.5 Pro Exp](https://gemini.google.com/advanced?hl=en) | **Google** | 1299 | Paid    |
| [GPT-4o](https://chat.openai.com/)            | **OpenAI**       | 1287       | Paid    |
| [GPT-4o-mini](https://chat.openai.com/)       | **OpenAI**       | 1280       | Freemium    |
| [Claude-3.5 Sonnet](https://claude.ai//)      | **Anthropic**    | 1271       | Paid    |
| [Gemini Advanced](https://gemini.google.com/advanced?hl=en) | **Google** | 1267 | Paid    |
| [Gemini 1.5 Pro](https://gemini.google.com/)  | **Google**       | 1262       | Paid    |
| [GPT-4 Turbo](https://chat.openai.com/)       | **OpenAI**       | 1257       | Paid    |
| [GPT-4](https://chat.openai.com/)             | **OpenAI**       | 1251       | Paid    |
| [Claude-3 Opus](https://claude.ai/)           | **Anthropic**    | 1248       | Paid    |
| [Yi-Large](https://www.01.ai/)                | **01.ai**        | 1240       | Freemium |
| [Gemini 1.5 Flash](https://deepmind.google/technologies/gemini/flash/)  | **Google** | 1228 | Paid |
| [Deepseek-v2-API-0628](https://platform.deepseek.com/sign_in)  | **Deepseek** | 1222 | Paid(API) |
| [Gemini Pro (Bard)](https://gemini.google.com/) | **Google**     | 1208       | Paid    |
| [Claude-3 Sonnet](https://claude.ai/)         | **Anthropic**    | 1200       | Freemium    |
| [Reka-Core](https://www.reka.ai/)             | **Reka**         | 1199       | Freemium |
| [Qwen-Max](https://help.aliyun.com/zh/dashscope/developer-reference/api-details) | **Alibaba** | 1182 | Preview |
| [Claude-3 Haiku](https://claude.ai/)          | **Anthropic**    | 1179       | Freemium    |
| [Mistral-Large](https://mistral.ai/)          | **Mistral**      | 1157       | Free    |
| [Reka-Flash](https://www.reka.ai/)            | **Reka**         | 1155       | Freemium |
| [claude-1](https://claude.ai/)                | **Anthropic**    | 1151       | Free    |
| [Mistral-Medium](https://mistral.ai/)         | **Mistral**      | 1148       | Free    |
| [claude-2](https://claude.ai/)                | **Anthropic**    | 1131       | Free    |
| [Mistral-Next](https://mistral.ai/)           | **Mistral**      | 1124       | Free    |
| [GPT-3.5 Turbo](https://chat.openai.com/)     | **OpenAI**       | 1117       | Free    |
| [claude-instant-1](https://claude.ai/)        | **Anthropic**    | 1111       | Free    |

