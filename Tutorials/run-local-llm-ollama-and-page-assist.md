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
