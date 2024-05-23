# LLM, Just for You: A Practical Tutorial to Run a Local Model

## Introduction (***Sorry for the long intro***)

This tutorial is designed for ***individuals seeking greater control and transparency*** in their data processing, regardless of their background or expertise. I will provide a step-by-step guide on how to set up a local LLM environment using Ollama as the backend and Page Assist extension in your browser.

### 🔴 The Privacy and security issue of Cloud based LLM services

Using Large Language Model (LLM) services online raises significant privacy concerns. One major issue is that your data is stored and processed by third-party providers, which can lead to unintended consequences. For example, your input data may be shared with other users or used for purposes beyond what you initially intended.

The complexity of the algorithms used to train these models also poses a problem. These algorithms are often opaque, making it difficult to understand how your data is being processed and potentially leading to biased or discriminatory outcomes.

Finally, the sheer scale of cloud-based LLMs means that even minor issues can result in massive data breaches, compromising the privacy and security of countless users

### 🟢 Control in Your Hands: Advantage sof Running LLM Models Locally

Running Large Language Model (LLM) models locally offers several benefits. One major advantage is that it allows you to maintain complete control over your input data and ensure its confidentiality - no sensitive information will be shared with third-party providers.

This approach also enables faster processing times and reduced latency, making it well-suited for applications where real-time feedback is crucial. By keeping your data and model on-premises, you can avoid potential issues related to data sovereignty, such as data localization requirements and regulatory compliance.

Ultimately, running LLM models locally provides a high degree of privacy and control, allowing you to tailor the model's training and deployment to meet your specific goals and objectives

## Step 1 : Install and Setup Ollama

### Installation

| Platform          | Installation Method |
|:-----------------:|:--------------------:|
| **macOS**         | [Download](https://ollama.com/download/Ollama-darwin.zip) |
| **Windows** | [Download](https://ollama.com/download/OllamaSetup.exe)  |
| **Linux**          | [Manual install instructions](https://github.com/ollama/ollama/blob/main/docs/linux.md) |
| **Docker**         | [Ollama Docker image](https://hub.docker.com/r/ollama/ollama) is available on Docker Hub.  |

### Quickstart

> [!Note]
> You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.
> Depending on your hardware specifications The model might take a long time to generate text or process requests.

<div align="center">
 
**👉 [Help me pick a model !](#find-the-llm-model-that-is-right-for-you) 👈**
  
</div>


To run and chat with [Llama 3](https://ollama.com/library/llama3) write the following input in a terminal:

```
ollama run llama3
```
This will allow you to chat with the **llama3:8B model** within the command-line interface (CLI). See the list of models available on [ollama.com/library](https://ollama.com/library 'ollama model library'). 

To download a model without launching it, simply enter the following command:

```
ollama pull llama3
```
To view the list of models you've downloaded, simply use the following command:

```
ollama list
```

## Step 2 : Use Ollama in your browser using Page assist extension.

It is not comfortable working directly in the command-line interface (CLI) for most, so i will show you how to interact with your Ollama model using a browser-based interface. We will be using the [Page assist extension](https://github.com/n4ze3m/page-assist).

Page Assist is an open-source Chrome Extension that provides a Sidebar and Web UI for your Local AI model. It allows you to interact with your model from any webpage.

### Installation and setup 

You can install the extension from the [Chrome Web Store](https://chromewebstore.google.com/detail/page-assist-a-web-ui-for/jfgfiigpkhlkbnfnbobbkinehhfdhndo)

#### Browser Support

| Browser  | Sidebar | Chat With Webpage | Web UI |
| -------- | ------- | ----------------- | ------ |
| Chrome   | ✅      | ✅                | ✅     |
| Brave    | ✅      | ✅                | ✅     |
| Edge     | ✅      | ❌                | ✅     |
| Opera GX | ❌      | ❌                | ✅     |
| Arc      | ❌      | ❌                | ✅     |
| Firefox  | ❌      | ❌                | ❌     |

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

## Find the LLM model that is right for you

This section is designed to assist you with the knowledge and resources needed **to make informed decisions about the right model for your specific requirements.** To support your search, To facilitate this process, I have prepared **two tables** for your reference.

* The first table highlights **Open-source models**, which you can typically run **locally on your machine**. To ensure a smooth experience running these models locally, I will provide the necessary hardware requirements for optimal performance. Please note that while you may be able to run certain models with lower hardware specifications, you can expect slower output and performance as a result. 

For **users with limited system resources or older hardware** configurations, **I'll provide additional insights on cloud-based providers that can efficiently run these models.**

* The second table features **Proprietary models** that usually operate on **cloud-based providers**.

I rank Models according to their **Elo scores (Higher is better)** from the [LMSys Chatbot Arena Leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard). Elo Scores update constantly based on user votes, and I'll try to **keep them up-to-date as frequently as possible**.

### Open Source Models (1100+ Elo score)

| Model                                         | Organization | Elo score  |  Hardware requirement | Ollama libraries | Cloud-based providers |
|:----------------------------------------------|:-------------|:----------:|:---------------------:|:----------------:|:---------------------:|
| [Llama-3-70b-Instruct](https://ollama.com/library/llama3:70b-instruct) | Meta | 1203 |40GB+ VRAM GPU (2xRTX 4090 or better) | Yes | [Groq](https://groq.com/)/[Perplexity Labs](https://labs.perplexity.ai/)  |
| [Command R+](https://ollama.com/library/command-r-plus) | Cohere | 1188 |  60GB+ VRAM GPU (3xRTX 4090 or better) | Yes | [Cohere](https://cohere.com/command) |
| [Qwen1.5-110B-Chat](https://ollama.com/library/qwen:110b-chat) | Alibaba | 1169 | 70GB+ VRAM GPU (4xRTX 4090 or better) | Yes | None |
| [Llama-3-8b-Instruct](https://ollama.com/library/llama3:instruct)  | Meta | 1154 | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better) | Yes |[Groq](https://groq.com/)/[Perplexity Labs](https://labs.perplexity.ai/) |
| [Qwen1.5-72B-Chat](https://ollama.com/library/qwen:72b-chat) | Alibaba | 1153 | 40GB+ VRAM GPU (2xRTX 4090 or better) | Yes | None |
| [Command R](https://ollama.com/library/command-r) | Cohere | 1149 | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | Yes | [Cohere](https://cohere.com/command) |
| [Mixtral-8x22b-Instruct-v0.1](https://ollama.com/library/mixtral:8x22b-instruct) | Mistral | 1144 | 80GB+ VRAM GPU (4xRTX 4090 or better) | Yes | [Perplexity Labs](https://labs.perplexity.ai/) |
| [Qwen1.5-32B-Chat](https://ollama.com/library/qwen:32b-chat) | Alibaba | 1134 | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | Yes | None |
| [Zephyr-ORPO-141b-A35b-v0.1](https://huggingface.co/HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1) | Hugging Face | 1129 | 80GB+ VRAM GPU (4xRTX 4090 or better) | No | [Hugging Face](https://huggingface.co/HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1) |
| [Starling-LM-7B-beta](https://ollama.com/library/starling-lm:beta) | AI feedback | 1118 | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better) | Yes | [Hugging Face](https://huggingface.co/Nexusflow/Starling-LM-7B-beta)                  |
| [Qwen1.5-14B-Chat](https://ollama.com/library/qwen:14b-chat) | Alibaba | 1116 | 10GB+ VRAM GPU (RX 7800 or RTX 4070 or better) | Yes | None |

### Proprietary Model (1100+ Elo score)

| Model                                         | Provider     | Elo score  | Pricing |
|:----------------------------------------------|:-------------|:----------:|:-------:|
| [GPT-4o](https://chat.openai.com/)            | OpenAI       | 1287       | Paid    |
| [GPT-4 Turbo](https://chat.openai.com/)       | OpenAI       | 1252       | Paid    |
| [GPT-4](https://chat.openai.com/)             | OpenAI       | 1250       | Paid    |
| [Gemini Pro 1.5](https://gemini.google.com/)  | Google       | 1248       | Paid    |
| [Claude-3 Opus](https://claude.ai/)           | Anthropic    | 1246       | Paid    |
| [Yi-Large](https://www.01.ai/)                | 01.ai        | 1236       | Preview |
| [Claude-3 Sonnet](https://claude.ai/)         | Anthropic    | 1199       | Paid    |
| [Gemini Pro (Bard)](https://gemini.google.com/) | Google     | 1199       | Paid    |
| [Reka-Core](https://www.reka.ai/)             | Reka         | 1195       | Freemium |
| [Qwen-Max](https://help.aliyun.com/zh/dashscope/developer-reference/api-details) | Alibaba | 1186 | Preview |
| [Claude-3 Haiku](https://claude.ai/)          | Anthropic    | 1181       | Paid    |
| [Reka-Flash](https://www.reka.ai/)            | Reka         | 1155       | Freemium |
| [Mistral-Large](https://mistral.ai/)          | Mistral      | 1153       | Free    |
| [claude-1](https://claude.ai/)                | Anthropic    | 1151       | Paid    |
| [Mistral-Medium](https://mistral.ai/)         | Mistral      | 1146       | Free    |
| [claude-2](https://claude.ai/)                | Anthropic    | 1133       | Paid    |
| [Mistral-Next](https://mistral.ai/)           | Mistral      | 1127       | Free    |
| [claude-instant-1](https://claude.ai/)        | Anthropic    | 1112       | Paid    |
| [GPT-3.5 Turbo](https://chat.openai.com/)     | OpenAI       | 1110       | Free    |
