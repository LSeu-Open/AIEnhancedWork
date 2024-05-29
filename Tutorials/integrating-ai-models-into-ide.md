![Header](https://capsule-render.vercel.app/api?type=venom&height=250&color=timeGradient&text=Using%20AI%20Models-nl-into%20Your%20Integrated-nl-Development%20Environment%20(IDE)&fontColor=141414&fontSize=40)

## Table of Contents

* [Introduction](#introduction)
* [Cursor the dedicated IDE for seamless AI integration](#cursor-the-dedicated-ide-for-seamless-ai-integration)
* [Code dedicated providers and models](#code-dedicated-providers-and-models)
* [Generalist Providers and Models](#generalist-providers-and-models)
  * [Prerequisites](#prerequisites)
  * [Install CodeGPT extension](#install-codegpt-extension)
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
 
## Code dedicated providers and models

In addition to **AI-powered IDE**, there are several ***dedicated code suggestion and autocompletion models*** that can further enhance your coding experience.

Models like ***Copilot***, ***Codium***, and ***Replit AI*** offer powerful features such as:

* Intelligent code completion.
* Real-time suggestions based on context and syntax.
* Code refactoring and rewriting.
* Collaboration tools for real-time feedback.
* These models are designed to work seamlessly with your IDE, providing a more efficient and effective coding experience.

> For more information on these models, please refer to the dedicated ***[table](https://github.com/LSeu-Open/AIEnhancedWork/tree/main?tab=readme-ov-file#code-suggestions-and-autocompletion)*** in the main page of this GitHub repository.

## Generalist Providers and Models

### Prerequisites

* **A code editor or Integrated Development Environment (IDE)** - I'll be using ***VSCode*** in this tutorial.
* **A model provider** - in this tutorial, I'll be working with ***Ollama and Groq***.
* **A reliable model to work with**.
  * As a local provider, I suggest deploying the ***deepseek-coder:33b-instruct*** model through Ollama. Please note that this may necessitate expensive hardware resources. However, for those working with smaller computers, ***CodeQwen1.5-7B-Chat*** can also be a very competent alternative.
  * On Groq, I personally prefer the ***Llama3-70b*** model.
 
> [!Note]
> Carefully selecting a model considering **its strengths and weaknesses is key** for optimal code usability, especially when aligned with **your primary language**, such as ***Python*** in my case.

<div align="center">
 
**👉 [Help me pick a model !](#models-for-coding) 👈**
  
</div>



### Install CodeGPT extension

* Click on the Extensions icon in the left sidebar or use the keyboard shortcut: Ctrl + Shift + X (Windows/Linux) or Cmd + Shift + X (macOS).
* In the Extensions marketplace, search for "CodeGPT" to find the extension.
* Click on the "CodeGPT" extension to open its page.
* Click the "Install" button to begin the installation process.
* Wait for the extension to download and install. This might take a few seconds.
* Once the installation is complete, click on the "Reload Required" button to reload VS Code.

### Setup Ollama as the Local Model Provider

For those who prioritize keeping everything local and private, I'll be using ***[Ollama](https://ollama.com/)*** as the provider in this tutorial. If you haven't already, be sure to check out our **[A Practical Tutorial to Run a Local Model](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/run-local-llm-ollama-and-page-assist.md)** to learn how to install Ollama and get started.
  
 * First, We need create a Modelfile by selecting the deepseek-coder model to load it as a custom model in CodeGPT.

* Create a folder named CodeGPT and then create a file inside called Modelfile in VSCode, add the following code:

```
FROM deepseek-coder:33b-instruct

# sets the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1

# sets the context window size to 1500, this controls how many tokens the LLM can use as context to generate the next token
PARAMETER num_ctx 1500

# sets a custom system message to specify the behavior of the chat assistant
SYSTEM You are expert Code Assistant
```
> [!CAUTION]
> Ensure that the ModelFile is saved without file extension; otherwise you won't be able to use it.

> [!Note]
> In this tutorial, I am using the ***deepseek-coder:33b-instruct*** model. This particular model is specialized for coding and has been meticulously trained on vast datasets by DeepSeek.ai.
>
>  Keep in mind that each model has its strengths and weaknesses, so choose carefully.

* Run the following command in your terminal to activate this new configuration. In this case, we will create the configuration model “codegpt-deepseek-coder:33b”

```
ollama create codegpt-deepseek-coder:33b -f ./CodeGPT/Modelfile
```

* If we run ```ollama list```, we’ll be able to see that the new model is already in our list.

* Test this new configuration by using ```ollama run codegpt-deepseek-coder:33b``` with our model set up to be a code assistant.

* Once you have your new model configuration up and running, let’s connect it with Visual Studio Code using the **CodeGPT extension and linking it with Ollama**.

* From the extensions menu, click on the **CodeGPT icon**, then expand the provider selector and choose Ollama.

* Once the provider is selected, in the model selector, type the name of the model we just created, in this case, **codegpt-deepseek-coder:33b**.

* You now have this new model, created by you, **ready to be used** as a programming assistant within Visual Studio Code thanks to Ollama and CodeGPT.

### Setup Groq as the Cloud-based Model Provider

If you **don't have the necessary hardware to run models locally** or want to tap into more powerful capabilities, this tutorial is for you. I'll be using ***[Groq](https://groq.com/)*** as the provider, leveraging their infrastructure's fast inference capabilities. 

> [!Note]
> In this tutorial, I'll be leveraging **Groq**, but feel free to substitute it with your preferred provider - whether that's OpenAI, Anthropic, or another that suits your needs.
>
>  When choosing your model, Keep in mind that each model has its strengths and weaknesses, so choose carefully.

> Before we get started, make sure you have a Groq account set up - if you haven't already, take a moment to create one.

* Click on the **CodeGPT icon** in the left sidebar to open the CodeGPT panel.
* Click on the **"Select AI Menu"** at the top of the panel.
* From the dropdown menu, select "Groq" as your preferred AI provider and Click the **"Connect" button** to proceed.
* Head to the **GroqCloud section** of the Groq website (look for the icon at the bottom).
* Create a new **API key** and copy it to your clipboard.
* Return to the CodeGPT window and **paste your API key into the dedicated input field**.
* **Select the AI model** you want to use from the available options. Here on Groq, I'll choose the "Llama-3-70b Model".
* You now have access to a capable model, **ready to be used** as a programming assistant within Visual Studio Code thanks to Groq and CodeGPT.
  
👏 **That's it for this tutorial ! You now have an AI model integrated into your VSCode setup. For a comprehensive overview of CodeGPT features and capabilities, please refer to the CodeGPT page. Enjoy coding !**

## Models for Coding

This section is designed to assist those who require **guidance in selecting the ideal model for coding purposes.** To facilitate this process, I have prepared **two tables** for your reference.

The first table highlights **Open-source models**, which you can typically run **locally on your machine**. To ensure a smooth experience running these models locally, I will provide the necessary hardware requirements for optimal performance. Please note that while you may be able to run certain models with lower hardware specifications, you can expect slower output and performance as a result.

The second table features **Proprietary models** that usually operate on **cloud-based providers**.

I rank Models according to their **HumanEval scores (Higher is better)** from the [EvalPlus Leaderboard](https://evalplus.github.io/leaderboard.html). HumanEval Scores can change, and I'll try to **keep them up-to-date as frequently as possible**. 

> [!CAUTION]
> The ***HumanEval*** benchmark exhibits a **Python-centric bias**, This inclination means that assessing functional correctness via this benchmark may yield results **more favorable for the models well-versed in Python** compared to other programming languages.
>
> However, it aims at gauging **universally applicable skills** like logical reasoning and problem-solving capabilities that are **valuable across all coding disciplines, not limited by language constraints.**

### Open Source Models (50+ HumanEval score)

| Model                                                                                   | Organisation      | HumanEval score (/100) | Ollama libraries | Cloud-based providers | Hardware requirement  | 
|:---------------------------------------------------------------------------------------:|:-----------------:|:----:|:----:|:----:|:---------------------------------------------------:|
| [CodeQwen1.5-7B-Chat](https://ollama.com/library/codeqwen:v1.5-chat)                    | **Alibaba**       | 78.7 |  Yes  | None | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better)   |
| [DeepSeek-Coder-33B-instruct](https://ollama.com/library/deepseek-coder:33b-instruct)   | **Deepseek**      | 75   |  Yes | [Hugging Face](https://huggingface.co/spaces/deepseek-ai/deepseek-coder-33b-instruct) | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better)   |
| [OpenCodeInterpreter-DS-33B](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-33B)   |**m-a-p**          | 73.8 |  No  | None | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better)   |
| [WizardCoder-33B-V1.1](https://ollama.com/library/wizardcoder:33b-v1.1)                 | **TheBloke**      | 73.2 |  Yes | None | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better    |
| [Llama3-70B-instruct](https://ollama.com/library/llama3:70b-instruct)                   | **Meta**          | 72   |  Yes | [Groq](https://groq.com/) / [Perplexity Labs](https://labs.perplexity.ai/) | 40GB+ VRAM GPU (2xRTX 4090 or better) |
| [Mixtral-8x22B-Instruct-v0.1](https://ollama.com/library/mixtral:8x22b-instruct)        | **Mistral**       | 72   |  Yes | [Perplexity Labs](https://labs.perplexity.ai/) | 80GB+ VRAM GPU (4xRTX 4090 or better) |
| [OpenCodeInterpreter-DS-6.7B](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-6.7B) | **m-a-p**         | 72   |  No  | None | 8GB+ VRAM GPU (RX 7600 or RTX 4060 or better)       |
| [DeepSeek-Coder-6.7B-instruct](https://ollama.com/library/deepseek-coder:6.7b-instruct) | **Deepseek**      | 71.3 | Yes  | [Hugging Face](https://huggingface.co/spaces/deepseek-ai/deepseek-coder-7b-instruct) |  8GB+ VRAM GPU (RX 7600 or RTX 4060 or better)      |
| [dbrx-instruct](https://ollama.com/library/dbrx:instruct)                               | **Databricks**    | 70.1 |  Yes | [Hugging Face](https://huggingface.co/spaces/databricks/dbrx-instruct) | 80GB+ VRAM GPU (4xRTX 4090 or better)               |
| [CodeLlama-70B-Instruct](https://ollama.com/library/codellama:70b-instruct)             | **Meta**          | 65.9 |  Yes | None | 40GB+ VRAM GPU (2xRTX 4090 or better)               |
| [DeepSeek-Coder-1.3B-instruct](https://ollama.com/library/deepseek-coder:1.3b-instruct) | **Deepseek**      | 60.4 |  Yes | [Deepseek](https://chat.deepseek.com/sign_in?from=coder) | 1GB+ VRAM GPU (RX 550 or GT 1030 or better)         |
| [starcoder2-15b-instruct-v0.1](https://ollama.com/library/starcoder2:15b-instruct)      | **BigCode**       | 60.4 |  Yes | None | 10GB+ VRAM GPU (RX 7800 or RTX 4070 or better)      |
| [Phi-3-mini-4k-instruct](https://ollama.com/library/phi3:instruct)                      | **Microsoft**     | 59.1 |  Yes | None | 3GB+ VRAM GPU (RX 6500 or RTX 3050 or better)       |
| [Command-R+](https://ollama.com/library/command-r:35b)                                  | **Cohere**        | 56.7 |  Yes | [Hugging Face](https://huggingface.co/spaces/CohereForAI/c4ai-command-r-v01) | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better)   |
| [Llama3-8B-instruct](https://ollama.com/library/llama3:instruct)                        | **Meta**          | 56.7 |  Yes | [Groq](https://groq.com/) / [Perplexity Labs](https://labs.perplexity.ai/) | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better)       |
| [WizardCoder-15B-V1.0](https://huggingface.co/WizardLMTeam/WizardCoder-15B-V1.0)        | **TheBloke**      | 50.6 |  No  | None | 8GB+ VRAM GPU (RX 7600 or RTX 4060 or better)       |


### Proprietary Models (50+ HumanEval score)

| Model             | Provider     | HumanEval score (/100) | Pricing |
|:-----------------:|:------------:|:----------------------:|:-------:|
| [GPT-4 Turbo](https://chat.openai.com/)      | **OpenAI**       | 86.6 | Paid    |
| [GPT-4](https://chat.openai.com/)            | **OpenAI**       | 79.3 | Paid    |
| [Claude-3 Opus](https://claude.ai/)          | **Anthropic**    | 77.4 | Paid    |
| [GPT-3.5 Turbo](https://chat.openai.com/)    | **OpenAI**       | 70.7 | Free    |
| [Claude-3 Haiku](https://claude.ai/)         | **Anthropic**    | 77.4 | Free    |
| [Claude-3 Sonnet](https://claude.ai/)        | **Anthropic**    | 64   | Free    |
| [Mistral-Large](https://mistral.ai/)         | **Mistral**      | 62.2 | Free    |
| [Gemini Pro 1.5](https://gemini.google.com/) | **Google**       | 61   | Paid    |
| [Gemini Pro 1.0](https://gemini.google.com/) | **Google**       | 55.5 | Paid    |
| [claude-instant-1](https://claude.ai/)       | **Anthropic**    | 50.6 | Free    |

