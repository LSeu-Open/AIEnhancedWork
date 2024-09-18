![header](Header_code.png)

## Table of Contents

* [Introduction](#introduction)
* [Cursor the dedicated IDE for seamless AI integration](#cursor-the-dedicated-ide-for-seamless-ai-integration)
* [Code dedicated providers and models](#code-dedicated-providers-and-models)
* [Generalist Providers and Models](#generalist-providers-and-models)
  * [Prerequisites](#prerequisites)
  * [Install Continue.dev extension](#install-continue-extension)
  * [Setup Ollama as the Local Model Provider](#setup-ollama-as-the-local-model-provider)
  * [Setup Groq as the Cloud-based Model Provider](#setup-groq-as-the-cloud-based-model-provider)
* [Help me pick a model !](#models-for-coding)

<br>

## Introduction

The integration of AI into software development has revolutionized the way we write code, collaborate, and innovate. As AI models become increasingly sophisticated, they're empowering developers to automate repetitive tasks, optimize workflows, and make data-driven decisions. By integrating AI tools into your Integrated Development Environment (IDE), you can unlock a new world of possibilities for accelerated development, improved collaboration, and enhanced decision-making.

### 🟢 The Pros: Boosting Productivity and Innovation

* **Increased productivity** : AI tools can automate repetitive coding tasks, generate code snippets, and provide intelligent code suggestions, allowing developers to focus on more complex problems and accelerate development cycles.
* **Improved code quality** : AI-powered code analysis can detect bugs, security vulnerabilities, and code smells, helping developers write cleaner and more maintainable code.
* **Enhanced learning experience** : AI assistants can provide real-time guidance, explanations, and best practice recommendations, facilitating the learning process for novice developers.
* **Accessibility** : AI tools can make coding more accessible to non-experts by bridging the gap between novice and experienced developers, enabling a broader range of individuals to participate in software development.

### 🔴 The Cons: Challenges and Considerations

* **Potential bias and errors** : AI models can inherit biases from their training data or make mistakes, leading to incorrect code suggestions or flawed analysis.
* **Over-reliance and loss of skills** : Excessive dependence on AI tools may hinder developers' ability to write code independently and erode their problem-solving skills over time.
* **Security and privacy concerns** : AI tools may inadvertently expose sensitive data or introduce security vulnerabilities if not properly secured and maintained.
* **Integration challenges** : Integrating AI tools into existing development workflows and IDEs can be complex, requiring additional configuration and compatibility considerations.
* **Cost and accessibility** : Advanced AI tools may come with significant licensing costs or require specialized hardware, making them less accessible to individual developers or smaller organizations.

> [!CAUTION]
> **AI models for coding aren't here to replace the expertise of a seasoned dev**. They can turbocharge your workflow, helping you crank out code faster and more efficiently. Plus, they can even serve as a mentor, guiding you through learning new programming languages and techniques.

## Cursor the dedicated IDE for seamless AI integration 
<img src="https://cursor.sh/brand/icon.svg" width="30"> ***[Cursor.sh](https://cursor.sh/)*** is an AI-driven code editor designed to assist developers in writing code more efficiently and quickly. It leverages LLM like **GPT-4** to provide a unique set of features and functionalities, making it a prominent competitor in the coding tool market.

Some key features of Cursor.sh include:

* **Code understanding and context** : Cursor.sh can ***understand the context of your entire codebase***, allowing it to provide tailored suggestions, generate unit tests, and even implement new features by modifying the relevant files.
* **Natural language editing** : You can edit code using natural language prompts, such as changing an entire method or class with a single instruction.
* **Code generation** : Cursor.sh can generate code from scratch based on simple instructions provided by the user.
* **Copilot++** : An enhanced version of GitHub Copilot that can suggest mid-line completions and entire diffs, trained to autocomplete based on sequences of edits.
* **Integration with VSCode** : Cursor.sh is ***a fork of VSCode***, allowing users to import all their extensions, themes, and keybindings with a single click.
* **Privacy options** : Cursor.sh ***offers a privacy mode*** where none of your code is stored on their servers or logs, catering to security-critical work.

> [!Note]
> ***Cursor.sh*** has received **positive reviews from developers**, with many praising its ability to save time and increase productivity by reducing the need for manual coding and code navigation.
>
> However, some users have reported **compatibility issues** with certain ***VSCode extensions or versions***, which may impact the support for specific languages or frameworks.

<br>

## Code dedicated providers and models

In addition to **AI-powered IDE**, there are several ***dedicated code suggestion and autocompletion models*** that can further enhance your coding experience.

Models like ***Copilot***, ***Codium***, and ***Replit AI*** offer powerful features such as:

* Intelligent code completion.
* Real-time suggestions based on context and syntax.
* Code refactoring and rewriting.
* Collaboration tools for real-time feedback.
* These models are designed to work seamlessly with your IDE, providing a more efficient and effective coding experience.

> For more information on these models, please refer to the dedicated ***[table](https://github.com/LSeu-Open/AIEnhancedWork/tree/main?tab=readme-ov-file#code-suggestions-and-autocompletion)*** in the main page of this GitHub repository.

<br>

## Generalist Providers and Models

### Prerequisites

* **A code editor or Integrated Development Environment (IDE)** - I'll be using ***VSCode*** in this tutorial.
* **A model provider** - in this tutorial, I'll be working with ***Ollama and Groq***.
* **A reliable model to work with**.
  * As a local provider, I suggest deploying the ***deepseek-coder:33b-instruct*** or ***Codestral:22b*** models through Ollama. **Please note that this may necessitate expensive hardware resources.** However, for those working with smaller computers, ***CodeQwen1.5-7B-Chat*** can also be a very competent alternative.
  * On Groq, I personally prefer the ***Llama3-70b*** model.
 
> [!Note]
> Carefully selecting a model considering **its strengths and weaknesses is key** for optimal code usability, especially when aligned with **your primary language**, such as ***Python*** in my case.

<div align="center">
 
**👉 [Help me pick a model !](#models-for-coding) 👈**
  
</div>

### Install Continue extension

> [Official Continue.dev website](https://www.continue.dev/)

* Click on the Extensions icon in the left sidebar or use the keyboard shortcut: Ctrl + Shift + X (Windows/Linux) or Cmd + Shift + X (macOS).
* In the Extensions marketplace, search for "Continue" to find the extension.
* Click on the "Continue" extension to open its page.
* Click the "Install" button to begin the installation process.
* Wait for the extension to download and install. This might take a few seconds.
* Once the installation is complete, click on the "Reload Required" button to reload VS Code.

### Setup Ollama as the Local Model Provider

For those who prioritize keeping everything local and private, I'll be using ***[Ollama](https://ollama.com/)*** as the provider in this tutorial. If you haven't already, be sure to check out our **[A Practical Tutorial to Run a Local Model](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/run-local-llm-ollama-and-page-assist.md)** to learn how to install Ollama and get started.
  
> [!Note]
> In this tutorial, I am using the ***Codestral:22b*** model. This particular model is specialized for coding and has been meticulously trained on vast datasets by Mistral.ai.
>
> This model stands out for its **exceptional size and capabilities, selected specifically for the hardware I use on my PC.** As with any model, it has its unique strengths and weaknesses. To get the most out of this tool, be sure to **[choose wisely](#models-for-coding)** among the available options.

#### Sidebar chat Model

* Open the **Continue.dev** extension by clicking on its icon in the left sidebar.

* The extension will prompt you for a Model Provider; select the **Local Provider** option.

* If you have set up Ollama correctly, **it should automatically detect your models.**
  
* At the bottom of the window, you will find a list of all your installed models. For this tutorial, I choose ***Codestral:22b***.

#### Inline autocomplete Model

* By default, the extension is set to use **starcoder-2-3b for autocomplete**. If you want to keep using this model, ensure it is installed with your Ollama setup. Otherwise, if you wish to switch to a more capable model, click on the settings icon at the bottom right of the extension window.
  
* This will open the **config.json** file, where you can customize the extension's behavior.
  
* Navigate to the following snippet:

```
 "tabAutocompleteModel": {
    "title": "starcoder-2-3b",
    "provider": "ollama",
    "model": "starcoder-2-3b"
  },
```

* Replace **starcoder-2-3b** with the model you prefer. For example, if you want to use **Codestral:22b**, update the code to:

 ```
 "tabAutocompleteModel": {
    "title": "codestral:22b",
    "provider": "ollama",
    "model": "codestral:22b"
  },
```
* Save your modifications and close the config file.

* You are now **ready to use your chosen model as a programming assistant within Visual Studio Code**, thanks to Ollama and Continue.dev.
  

### Setup Groq as the Cloud-based Model Provider

If you **don't have the necessary hardware to run models locally** or want to tap into more powerful capabilities, this tutorial is for you. I'll be using ***[Groq](https://groq.com/)*** as the provider, leveraging their infrastructure's fast inference capabilities. 

> [!Note]
> In this tutorial, I'll be leveraging **Groq**, but feel free to substitute it with your preferred provider - whether that's OpenAI, Anthropic, or another that suits your needs.
>
>  When choosing your model, Keep in mind that each model has its strengths and weaknesses, so **[choose wisely](#models-for-coding)**.

> Before we get started, make sure you have a Groq account set up - if you haven't already, take a moment to create one.

* Click on the **Continue icon** in the left sidebar to open the Continue panel.
* If it is the first time you open it, The extension will prompt you for a Model Provider; select the **Cloud Provider** option.
* Select **Groq** as your preferred AI provider.
* Head to the **GroqCloud section** of the Groq website (look for the icon at the bottom).
* Create a new **API key** and copy it to your clipboard.
* Return to the window and **paste your API key into the apiKey input field**.
* **Select the AI model** you want to use from the available options. Here on Groq, I'll choose the "Llama-3-70b Model".
* You now have access to a capable model, **ready to be used** as a programming assistant within Visual Studio Code.
  
👏 **That's it for this tutorial ! You now have an AI model integrated into your VSCode setup. For a comprehensive overview of CodeGPT features and capabilities, please refer to the CodeGPT page. Enjoy coding !**

<br>

## Models for Coding

This section is designed to assist those who require **guidance in selecting the ideal model for coding purposes.** To facilitate this process, I have prepared **two tables** for your reference.

The first table highlights **Open-source models**, which you can typically run **locally on your machine**. To ensure a smooth experience running these models locally, I will provide the necessary hardware requirements for optimal performance. Please note that while you may be able to run certain models with lower hardware specifications, you can expect slower output and performance as a result.

The second table features **Proprietary models** that usually operate on **cloud-based providers**.

The models are ranked according to **LiveCodeBench Pass@1** Code Generation scores (with higher scores indicating better performance). ***Pass@1 is the probability of passing a given problem in one attempt***. [LiveCodeBench](https://livecodebench.github.io/leaderboard.html) offers a more comprehensive, up-to-date, and contamination-aware evaluation of code-related capabilities compared to HumanEval.

> [!CAUTION]
> Please note that the hardware requirements provided are only indicative, and the specified VRAM requirements in the tables below apply specifically to the default Ollama Q4_0 quantization version of the models. [Learn more about LLMs Quantization](https://huggingface.co/blog/merve/quantization).

### Open Source Models (10+ Pass@1 score)

***Massive models*** : Challenging for local deployment due to computational requirements. Use them via any of the [listed Cloud-based Providers](https://github.com/LSeu-Open/AIEnhancedWork?tab=readme-ov-file#cloud-based-providers-1) (e.g. Groq / Together / Mistral or OpenRouter).

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Pass@1 score (/100) |  Ollama libraries |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| **DeepSeek**       | [DeepSeek-Coder-V2-Instruct](https://ollama.com/library/deepseek-coder-v2:236b) | 236B  | 130GB+ VRAM GPU (2XH100 or better) | 44.7    | [Yes](https://ollama.com/library/deepseek-coder-v2:236b) | [Deepseek](https://chat.deepseek.com/sign_in?from=coder)  |
| **Meta**           | [Llama-3.1-405b-Instruct](https://ollama.com/library/llama3.1:405bt)  | 405B        | 230+ VRAM GPU (3XH100 or better)  | 41.6   | [Yes](https://ollama.com/library/llama3.1:405b) | [OpenRouter](https://openrouter.ai/chat?models=meta-llama/llama-3.1-405b) |
| **Mistral**        | [Mistral-Large-2-Instruct](https://ollama.com/library/mistral-large)  | 123B        | 70GB+ VRAM GPU (1XH100 or better) | 41.3   | [Yes](https://ollama.com/library/mistral-large) | [Mistral](https://mistral.ai/)  |
| **Meta**           | [Llama-3.1-70b-Instruct](https://ollama.com/library/llama3.1:70b-instruct-q4_0) | 70B | 40GB+ VRAM GPU (2xRTX 4090 or better) | 32.1 | [Yes](https://ollama.com/library/llama3.1:70b) | [Groq](https://groq.com/)     |
| **Meta**           | [Llama3-70B-instruct](https://ollama.com/library/llama3:70b-instruct) | 70B |  40GB+ VRAM GPU (2xRTX 4090 or better) | 27.1   |  [Yes](https://ollama.com/library/llama3:70b-instruct) | [Groq](https://groq.com/)|
| **Mistral**        | [Mixtral-8x22b-Instruct-v0.1](https://ollama.com/library/mixtral:8x22b-instruct) | 141B | 80GB+ VRAM GPU (1xH100 or better) | 25.8   | [Yes](https://ollama.com/library/mixtral:8x22b-instruct) | [Perplexity Labs](https://labs.perplexity.ai/) |
| **Cohere**         | [Command R+](https://ollama.com/library/command-r-plus)               | 104B        | 60GB+ VRAM GPU (3xRTX 4090 or better) | 20 | [Yes](https://ollama.com/library/command-r-plus)   | [Cohere](https://cohere.com/command) |
| **Meta**           | [CodeLlama-70B-Instruct](https://ollama.com/library/codellama:70b-instruct) | 70B |  40GB+ VRAM GPU (2xRTX 4090 or better) | 12.6|  [Yes](https://ollama.com/library/codellama:70b-instruct) | No |


**Mid-sized models** : Suitable for deployment on a high-performance local workstation.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Pass@1 score (/100) |  Ollama libraries |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| **DeepSeek**       | [DeepSeek-Coder-V2-Lite-Instruct](https://ollama.com/library/deepseek-coder-v2)    | 16B  | 10GB+ VRAM GPU (RX 7800 or RTX 4070 or better)| 41.1   | [Yes](https://ollama.com/library/deepseek-coder-v2) | [Deepseek](https://chat.deepseek.com/sign_in?from=coder)  |
| **Mistral**        | [Codestral-22B](https://ollama.com/library/codestral)                 | 22B       | 14GB+ VRAM GPU (RX 7800 or RTX 4070 Ti or better) | 32.9 |  [Yes](https://ollama.com/library/codestral) | [Mistral](https://chat.mistral.ai/) | 
| **DeepSeek**       | [DeepSeek-Coder-33B-instruct](https://ollama.com/library/deepseek-coder:33b-instruct) | 33B  | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 22.3    | [Yes](https://ollama.com/library/deepseek-coder:33b-instruct) | [Deepseek](https://chat.deepseek.com/sign_in?from=coder)  |
| **m-a-p**          | [OpenCodeInterpreter-DS-33B](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-33B) | 33B  | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 18.9 |  [Yes](https://ollama.com/wojtek/opencodeinterpreter)  | No |


***Small models*** : Lightweight and deployable on most local machines.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Pass@1 score (/100) |  Ollama libraries |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| **01.ai**        | [Yi-Coder-9B-Chat](https://huggingface.co/01-ai/Yi-Coder-9B-Chat)  | 9B        | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better) | 31.2   | [Yes](https://ollama.com/library/yi-coder:9b-chat)  | [Hugging Face](https://huggingface.co/01-ai/Yi-Coder-9B-Chat)  |
| **Mistral**        | [Mamba-codestral-7B-v0.1](https://huggingface.co/mistralai/mamba-codestral-7B-v0.1)  | 7B        | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better) | 21.1   | No | [Mistral](https://mistral.ai/)  |
| **Alibaba**        | [CodeQwen1.5-7B-Chat](https://ollama.com/library/codeqwen:v1.5-chat)  | 7B          | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better)   |  19.6 |  [Yes](https://ollama.com/library/codeqwen:v1.5-chat) | No |
| **Meta**           | [Llama3.1-8B-instruct](https://ollama.com/library/llama3.1:8b)        | 8B         | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better)   |   19.2      | [Yes](https://ollama.com/library/llama3.1:8b) | [Groq](https://groq.com/) |
| **DeepSeek**       | [DeepSeek-Coder-6.7B-instruct](https://ollama.com/library/deepseek-coder:6.7b-instruct)    | 7B  | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better)   | 18.9  | [Yes](https://ollama.com/library/deepseek-coder:6.7b-instruct) | [Deepseek](https://chat.deepseek.com/sign_in?from=coder)  |
| **m-a-p**          | [OpenCodeInterpreter-DS-6.7B](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-6.7B) | 6.7B   | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better)   | 18.7 | No | [Hugging Face](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-6.7B) |
| **THUDM**          | [CodeGeeX4-All-9B](https://ollama.com/library/codegeex4:9b-all-q4_0)  | 9B          | 8GB+ VRAM GPU (RX 7600 or RTX 4060 or better)  | 17.8 |  [Yes](https://ollama.com/library/codegeex4:9b-all-q4_0) | [Hugging Face](https://huggingface.co/spaces/vilarin/glm-chat) |

### Proprietary Models (10+ Pass@1 score)

***Proprietary models*** : typically accessible through a paid API or web interface.

| Model             | Provider     | Pass@1 score (/100) | Pricing |
|:-----------------:|:------------:|:----------------------:|:-------:|
| [GPT-o1-preview](https://chat.openai.com/)   | **OpenAI**       | 59.0 | Paid    |
| [Claude-3.5 Sonnet](https://claude.ai//)     | **Anthropic**    | 54.1   | Paid    |
| [GPT-4o](https://chat.openai.com/)           | **OpenAI**       | 48 | Paid    |
| [GPT-4 Turbo](https://chat.openai.com/)      | **OpenAI**       | 43.7 | Paid    |
| [Gemini Pro 1.5](https://gemini.google.com/) | **Google**       | 42.2   | Paid    |
| [GPT-4O-mini](https://chat.openai.com/)      | **OpenAI**       | 40.7 | Paid    |
| [Claude-3 Opus](https://claude.ai/)          | **Anthropic**    | 35.3 | Paid    |
| [GPT-4](https://chat.openai.com/)            | **OpenAI**       | 34.9 | Paid    |
| [Gemini Flash 1.5](https://gemini.google.com/) | **Google**       | 29.6 | Paid    |


