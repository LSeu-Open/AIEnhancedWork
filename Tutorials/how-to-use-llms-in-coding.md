<div align="center"> 
 
<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Tutorials/CodingAI.png">

***Welcome! This guide helps you boost your coding workflow with AI, from choosing tools and models to seamless IDE integration.***

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20with%20Monocle.png" alt="Face with Monocle" width="25" height="25" /> Reading Time : 16min

***TODO: Complete Empty sections and update the models score***

</div> 

## Table of Contents

* [Introduction](#introduction)
* [Implementing AI Assistance](#implementing-ai-assistance)
  * [AI-powered integrated development environment (IDE)](#ai-powered-integrated-development-environment-ide)
    * [Cursor](#cursor)
    * [Void](#void)
    * [Windsurf](#windsurf)
    * [Zed](#zed)
  * [AI-powered Extensions for VScode](#ai-powered-extensions-for-vscode)
    * [Cline](#cline)
    * [Continue](#continue)
    * [Github Copilot](#github-copilot)
    * [Roo Code](#roo-code)
* [Find the Model that is right for you](#find-the-model-that-is-right-for-you)
  * [Open Source Models](#open-source-models)
  * [Proprietary Models](#proprietary-models)

<br>

# Introduction

Modern development environments now **leverage AI capabilities to enhance code synthesis, automate routine operations, and optimize development workflows.** IDE integration of language models enables contextual code assistance, automated testing, and intelligent refactoring while maintaining established development practices.

***The Pros: Boosting Productivity and Innovation***

* **Increased productivity** : AI tools can automate repetitive coding tasks, generate code snippets, and provide intelligent code suggestions, allowing developers to focus on more complex problems and accelerate development cycles.
* **Improved code quality** : AI-powered code analysis can detect bugs, security vulnerabilities, and code smells, helping developers write cleaner and more maintainable code.
* **Enhanced learning experience** : AI assistants can provide real-time guidance, explanations, and best practice recommendations, facilitating the learning process for novice developers.
* **Accessibility** : AI tools can make coding more accessible to non-experts by bridging the gap between novice and experienced developers, enabling a broader range of individuals to participate in software development.

<br>

***The Cons: Challenges and Considerations***

* **Potential bias and errors** : AI models can inherit biases from their training data or make mistakes, leading to incorrect code suggestions or flawed analysis.
* **Over-reliance and loss of skills** : Excessive dependence on AI tools may hinder developers' ability to write code independently and erode their problem-solving skills over time.
* **Security and privacy concerns** : AI tools may inadvertently expose sensitive data or introduce security vulnerabilities if not properly secured and maintained.
* **Integration challenges** : Integrating AI tools into existing development workflows and IDEs can be complex, requiring additional configuration and compatibility considerations.
* **Cost and accessibility** : Advanced AI tools may come with significant licensing costs or require specialized hardware, making them less accessible to individual developers or smaller organizations.

<br>

> [!CAUTION]
> Code assistance models **complement developer expertise by augmenting development workflows through contextual suggestions and documentation integration.** These systems enhance implementation speed and technical learning while relying on established programming principles and human oversight.
>
> **Always validate AI-generated code against official documentation and established development standards. Implement thorough code review practices when using automated suggestions.** 

<br>
<br>

# Implementing AI Assistance

##  AI-powered integrated development environment (IDE)

### Cursor

<img src="https://cursor.sh/brand/icon.svg" width="20" height="20" > ***[Cursor](https://cursor.sh/)*** integrates language models into a VS Code-based editor, **providing contextual code completion, codebase analysis, and natural language editing capabilities.** The platform supports both cloud-based and local AI models.

**Currently Supported Models** :

Cursor provides access to **Premium large models** such as :

  - ***Claude 3.7 Sonnet and Claude 3.5 Sonnet*** by Anthropic
  - ***o3 / o4-mini and gpt-4.1*** by OpenAI
  - ***Gemini 2.5 Flash and Gemini 2.5 Pro*** by Google
  - ***Deepseek-R1 and Deepseek-V3*** by Deepseek
  - ***Grok 3 and Grok 3-mini*** by xAI

Key highlights of Cursor include:

* **Code understanding and context** : Cursor.sh can ***understand the context of your entire codebase***, allowing it to provide tailored suggestions, generate unit tests, and even implement new features by modifying the relevant files.
* **Natural language editing** : You can edit code using natural language prompts, such as changing an entire method or class with a single instruction.
* **Code generation** : Cursor.sh can generate code from scratch based on simple instructions provided by the user.
* **Integration with VSCode** : Cursor.sh is ***a fork of VSCode***, allowing users to import all their extensions, themes, and keybindings with a single click.
* **Privacy options** : Cursor.sh ***offers a privacy mode*** where none of your code is stored on their servers or logs, catering to security-critical work.

<br>

### Void

<img src="https://voideditor.com/void/logo_cube_noshadow.png" width="20" height="20" > ***[Void](https://voideditor.com/)*** is an open-source AI code editor built as a fork of VS Code, emphasizing user flexibility and data privacy. It enables direct connections to virtually any LLM, bypassing private backends.

**Currently Supported Models** :

- ***Claude 3.7 Sonnet and Claude 3.5 Sonnet*** by Anthropic
- ***o3 / o4-mini and gpt-4.1*** by OpenAI
- ***Gemini 2.5 Flash and Gemini 2.5 Pro*** by Google
- ***Deepseek-R1 and Deepseek-V3*** by Deepseek
- ***All models from your favorite cloud-provider***
- ***Local models via Ollama/vLLM***

Key highlights of Void include:

*   **VS Code Foundation**: Easily transfer existing themes, keybinds, and settings.
*   **Universal & Direct LLM Access**: Connect to any preferred LLM without intermediaries, ensuring data control.
*   **Core AI Coding Features**: Includes Tab Autocomplete, Quick Edit, and versatile Chat modes (Agent, Gather, Normal).
*   **Developer-Focused Tools**: Offers checkpoints for LLM changes, lint error detection, native tool use, and efficient application of edits, even on large files.

<br>

### Windsurf

<img src="https://windsurf.com/favicon.ico" width="20" height="20" > ***[Windsurf](https://windsurf.com/editor)*** is an agentic IDE and VS Code fork, designed for a "flow state" by blending developer and AI workflows. It employs "Flows," where AI acts as both Copilot and Agent, powered by its core engine, **Cascade**, for deep codebase understanding, command execution, and multi-file editing.

**Currently Supported Models** :

Windsurf provides access to **Premium large models** such as :

- ***Claude 3.7 Sonnet and Claude 3.5 Sonnet*** by Anthropic
- ***o3 / o4-mini and gpt-4.1*** by OpenAI
- ***Gemini 2.5 Flash and Gemini 2.5 Pro*** by Google
- ***Deepseek-R1 and Deepseek-V3*** by Deepseek

and also in-house models such as :

- ***SWE-1*** and ***SWE-1-lite*** by Windsurf

Key highlights of Windsurf include:

*   **Agentic AI (Flows & Cascade)**: AI seamlessly collaborates and performs autonomous tasks, deeply integrated into the editing experience.
*   **Windsurf Previews**: Live preview web applications, use AI to reshape elements, and deploy directly from the IDE.
*   **VS Code Foundation**: Builds upon the familiar and extensible VS Code environment.
*   **Smart Coding Tools**: Features include linter integration, "Tab to Jump" predictive navigation, "Supercomplete" for anticipating next actions, natural language commands (in-line & terminal via Cmd+I), Codelenses for quick actions, and @mentions for contextual AI guidance.

<br>

### Zed

<img src="https://zed.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo_icon.d67dc948.webp&w=48&q=100" width="20" height="20" > ***[Zed](https://zed.dev/)*** is a high-performance code editor built in Rust, prioritizing speed, human-AI collaboration, and advanced AI features. It supports macOS, Linux, and is coming to Windows. It features native AI capabilities like **Agentic Editing** and **Edit Prediction** (powered by its open-source ***Zeta*** model) and supports integration with various leading LLMs.

**Currently Supported Models** :
- Integrates with its native open-source model: ***Zeta***
- Supports external LLMs such as:
    - ***Claude 3.7 Sonnet*** and ***Claude 3.5 Sonnet*** by Anthropic

Key highlights of Zed include:

*   **Exceptional Performance**: Built in Rust for efficient multi-core CPU and GPU usage, ensuring speed.
*   **Intelligent & Collaborative AI**: Native support for agentic editing and AI-driven code assistance, plus built-in tools for team collaboration.
*   **Modern Development Tools**: Includes native Git support, remote development capabilities, multibuffer editing, and interactive programming (Jupyter).
*   **Extensible & Customizable**: Supports multiple languages (Tree-sitter, LSP), a fast integrated terminal, Vim-friendly modal editing, and a growing extensions ecosystem.

<br>
<br>

##  AI-powered Extensions for VScode

### Cline

#### Install Cline

* **Using VS Code Marketplace** :

* **using VSIX File** :

#### Create Your account

#### How Cline works

<br>

### Continue

For those who prioritize keeping everything local and private, I'll be using ***[Ollama](https://ollama.com/)*** as the provider in this tutorial. If you haven't already, be sure to check out our **[A Practical Tutorial to Run a Local Model](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/run-local-llm-ollama-and-page-assist.md)** to learn how to install Ollama and get started.
  
> [!Note]
> In this tutorial, I am using the ***Codestral:22b*** model. This particular model is specialized for coding and has been meticulously trained on vast datasets by Mistral.ai.
>
> This model stands out for its **exceptional size and capabilities, selected specifically for the hardware I use on my PC.** As with any model, it has its unique strengths and weaknesses. To get the most out of this tool, be sure to **[choose wisely](#models-for-coding)** among the available options.

#### Install Continue extension

> [Official Continue.dev website](https://www.continue.dev/)

* Click on the Extensions icon in the left sidebar or use the keyboard shortcut: Ctrl + Shift + X (Windows/Linux) or Cmd + Shift + X (macOS).
* In the Extensions marketplace, search for "Continue" to find the extension.
* Click on the "Continue" extension to open its page.
* Click the "Install" button to begin the installation process.
* Wait for the extension to download and install. This might take a few seconds.
* Once the installation is complete, click on the "Reload Required" button to reload VS Code.


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

* Replace **starcoder-2-3b** with the model you prefer. For example, if you want to use **Qwen2.5-Coder-32B-Instruct**, update the code to:

 ```
 "tabAutocompleteModel": {
    "title": "Qwen2.5-Coder-32B-Instruct",
    "provider": "ollama",
    "model": "Qwen2.5-Coder-32B-Instruct"
  },
```
or by **Qwen2.5-Coder-7B-Instruct** for less powerfull computers : 

 ```
 "tabAutocompleteModel": {
    "title": "qwen2.5-coder:7b-instruct",
    "provider": "ollama",
    "model": "qwen2.5-coder:7b-instruct"
  },
```

* Save your modifications and close the config file.

<br>

### Github Copilot

#### Install Github Copilot

* **Using VS Code Marketplace** :

* **using VSIX File** :

#### Create Your account

#### How Github Copilot works

<br>

### Roo Code

#### Install Roo Code

* **Using VS Code Marketplace** :

* **using VSIX File** :

#### Connect your AI Provider

#### How Roo Code works

<br>
<br>

# Find the Provider that is right for you

Choosing the right AI provider is a foundational step in leveraging Large Language Models (LLMs) effectively for your coding tasks. In this context, a "provider" refers to any entity or platform that grants you access to these powerful models. This could be the original developers of an LLM, a third-party service hosting various models, or even software that enables you to run models directly on your own local machine.

The decision is more than just picking a name; it significantly influences crucial aspects of your AI-assisted development experience. Your choice will determine the range and type of models available to you, the associated costs and licensing terms, the features and overall performance you can expect, and, critically, the level of data privacy and security for your code. Furthermore, it impacts how easily the AI capabilities can be integrated into your existing workflows.

Therefore, before diving into specific providers, it's vital to consider several key factors. Think about your preferred **deployment model**: are you comfortable with cloud-based solutions, or is a local, self-hosted setup a priority for data control and offline access? Evaluate the **model access and variety** offered—do you need cutting-edge proprietary models, a broad selection of open-source options, or models specifically fine-tuned for coding?

Naturally, **pricing and licensing** are practical concerns, so understanding the cost structures and usage rights is essential. The **integration and developer experience**, including the quality of APIs and documentation, will affect your productivity. Given the sensitivity of code, **security and data usage policies** demand careful review. Finally, assess the provider's **performance, reliability, and scalability** to ensure they meet your current and future needs for speed and consistent availability.

## Major Cloud AI Providers

These are typically large tech companies that develop and offer access to their own flagship LLMs. Access is usually via APIs, and they manage all the underlying infrastructure.

| Tool             | Description                                                                                                                 | Models      | Pricing     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [AI21 Labs](https://www.ai21.com/) |  Known for their language models like Jurassic-1 Jumbo focused on quality, safety, and controllability. |  [Jamba Large 1.6 ](https://huggingface.co/ai21labs/AI21-Jamba-Large-1.6) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Anthropic](https://www.anthropic.com/claude) | Known for their constitutional AI model Claude, focused on being helpful, harmless, and honest. | Claude 3.7 Sonnet  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [Cohere](https://cohere.com/) | Provides an enterprise AI platform with models like Cohere Generate for custom content creation. | [Command A](https://cohere.com/blog/command-A) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Databricks](https://www.databricks.com/) | A unified, open analytics platform that provides tools and services for data processing, analytics, and artificial intelligence at scale. | [Dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct) | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Deepseek](https://chat.deepseek.com/) | An AI company that has developed several notable AI models and technologies | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Google](https://gemini.google.com/) |  Provides models like LaMBDA, PaLM, and Bard for language understanding, generation, and multimodal AI tasks. | all Gemini Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [Microsoft Azure](https://azure.microsoft.com/) | A comprehensive suite of AI services and tools designed to help developers and organizations build, deploy, and manage AI applications at scale. | Large Panel of Open source and Proprietary Models | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Mistral AI](https://mistral.ai/) | A French artificial intelligence company that specializes in developing large language models (LLMs) and AI products. | [Mistral Large 2](https://huggingface.co/mistralai/Mistral-Large-Instruct-2411) and more| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [OpenAI](https://chatgpt.com/) | Offers models like GPT-4, DALL-E, and Whisper for natural language processing, image generation, and speech recognition. | [o1](https://openai.com/o1/) and more | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Reka](https://chat.reka.ai/) | An AI company that develops advanced multimodal AI models and technologies. | [Reka Flash 3](https://huggingface.co/RekaAI/reka-flash-3) and more | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |

<br>

## Aggregator & Specialized Cloud Platforms

These platforms offer access to a variety of models from different developers, including many popular open-source models and sometimes proprietary ones, often through a single API or interface. Some may offer specialized hardware or value-added services like fine-tuning.

| Tool             | Description                                                                                                                 | Models      | Pricing     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [Amazon Web Services (AWS)](https://aws.amazon.com/bedrock/) | Offers models like Amazon CodeWhisperer for code generation and understanding through their SageMaker platform. | Large Panel of Open source and Proprietary Models | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Cerebras](https://inference.cerebras.ai/) | An AI company that has developed innovative hardware and software solutions for AI computing. | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) and more | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [DeepInfra](https://deepinfra.com/chat) | A platform that provides scalable and cost-effective infrastructure for deploying machine learning models. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Fireworks](https://fireworks.ai/) | A comprehensive solution for companies looking to deploy AI into production, focusing on performance, cost-effectiveness, and developer experience. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Groq](https://groq.com/) | Specializes in high-performance AI inference with custom LPU (Language Processing Unit) hardware, offering models like Meta's Llama 3. | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) and more  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [Hyperbolic](https://app.hyperbolic.xyz/models) | an open-access AI cloud platform designed to democratize AIe by making high-performance compute resources—especially GPUs—affordable and accessible to everyone. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [LeptonAI](https://www.lepton.ai/) | A platform that provides cloud-based infrastructure and tools for deploying and running AI applications efficiently. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Nebius](https://studio.nebius.com/) | A high-performance, cost-effective Inference-as-a-Service platform designed to make advanced AI generation accessible | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Novita](https://novita.ai/models) | A high-performance, cost-effective Inference-as-a-Service platform designed to make advanced AI generation accessible | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [OctoAI](https://octoai.cloud/) | A full-stack inference platform designed specifically for generative AI applications. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [OpenRouter](https://openrouter.ai/) |  A versatile platform designed to provide access to a wide range of large language models (LLMs) from both proprietary and open-source sources. |  Large Panel of Open source and Proprietary Models | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Poe](https://poe.com) | An AI chatbot aggregator platform developed by Quora that provides users access to multiple advanced language models and chatbots within a single interface. | Large Panel of Open source and Proprietary Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [SambaNova](https://sambanova.ai/) | An artificial intelligence company that provides a comprehensive AI platform for enterprises. | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) and more | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Together](https://www.together.ai/) | A cloud platform designed for building and running generative AI applications. | Large Panel of Open source Models | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> | 

<br>

## Local Model Execution Solutions (Self-Hosting)

These tools allow you to download, configure, and run LLMs directly on your own computer hardware. You become your own "provider." We already covered this in the [How to run LLMs on your machine](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/how-to-run-llms-on-your-machine.md) tutorial.

<br>

## Which Provider Type Suits Your Needs?

To determine which category of AI provider best fits your situation, it's helpful to reflect on your specific needs and priorities. 

* **Consider your primary goal**: are you aiming for the highest possible accuracy in code generation, prioritizing absolute data privacy, seeking the most cost-effective solution, or are you in an experimental phase? 
* **Your budget** constraints will naturally play a role, as will the criticality of data privacy for your projects. 
* Also, **take stock of your local hardware capabilities**—can your machine handle running models locally? 
* Think about **whether you need access to one specific model or the flexibility to switch between many, and how much technical effort you're willing to invest in setup and ongoing maintenance.**

> These reflections can guide you toward a suitable provider type. 

* For instance, if maintaining absolute data privacy is paramount and you have capable hardware, **Local Model Execution Solutions** are likely your best bet.
* If your work demands the most powerful, cutting-edge proprietary models for critical tasks, then exploring **Major Cloud AI Providers** would be the logical step
* For those who desire easy access to a variety of open-source models via the cloud, or require specialized performance benefits like high-speed inference, **Aggregator & Specialized Cloud Platforms** offer compelling advantages.
* And if you're an individual developer or working with a limited budget, investigating free tiers from various cloud providers or starting with a local setup (hardware permitting) can be excellent entry points.

Once you've identified a provider type—or perhaps even a specific provider—that aligns with your priorities, the next crucial step is to explore the actual Large Language Models they offer. Your choice of provider will significantly influence the range and type of models available to you. This brings us to the next important decision: selecting the right model for your coding endeavors.

<br>
<br>

# Find the Model that is right for you

Now that you've chosen your provider, let's find the right model for your coding needs.

To help you choose, **I have outlined the estimated hardware requirements for each model.** These estimates generally assume the model is quantized (specifically using a common 4-bit quantization), a process that reduces the model's size and memory footprint, offering a good balance between performance and quality. Keep in mind that actual performance can vary based on the specific software used and your system's configuration.

Learn more about quantization [here](https://huggingface.co/blog/merve/quantization).

> [!IMPORTANT]
> Please note that while it is possible to **run models without a GPU**, doing so will load the model into RAM and perform inference using the CPU.
>
> ***This approach will significantly slow down inference speeds.***

The models are ranked according to **[Aider polyglot coding leaderboard](https://aider.chat/docs/leaderboards/)** scores (with higher scores indicating better performance). Its benchmarking system automates the assessment of an LLM's ability to **follow instructions and execute code edits independently**, eliminating the need for human oversight. 

The Aider polyglot benchmark tests LLMs on 225 complex Exercism coding challenges spanning **six programming languages: C++, Go, Java, JavaScript, Python, and Rust.**

### Open Source Models

***Large-scale models (>70 billion parameters)*** : These require significant amounts of both RAM and GPU memory, often rendering local installation infeasible for most users. Consequently, such models are predominantly deployed on cloud-based platforms designed to provide the essential computational resources needed.

| Organization       | Model                                                                 | Model Size  | Percent correct | Hardware requirement (using Q4 quantization) |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) | 235B | 59.6 | 133GB+ VRAM GPU (2xH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | 685B  | 56.9 | 404GB+ VRAM GPU (5xH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)        | [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) | 671B  | 55.1 | 404GB+ VRAM GPU (5xH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)            | [Llama-3.3-70b-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | 70B |  28.4 | 47GB+ VRAM GPU (2xRTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)            | [Llama-3.1-405b-Instruct](https://ollama.com/library/llama3.1:405bt)  | 405B | 26.4 | 230+ VRAM GPU (3XH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mistral-Large-2-Instruct](https://ollama.com/library/mistral-large)  | 123B | 26 | 70GB+ VRAM GPU (1XH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)  | 72.2B | 25.4 | 47GB+ VRAM GPU (2xRTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) | [Command A](https://huggingface.co/CohereForAI/c4ai-command-a-03-2025) | 111B | 20.3 | 60GB+ VRAM GPU (3xRTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mixtral-8x22b-Instruct-v0.1](https://ollama.com/library/mixtral:8x22b-instruct) | 141B | 19.9 | 80GB+ VRAM GPU (1xH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | 402B | 15.6 | 230+ VRAM GPU (4xH100 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)          | [Command R+](https://ollama.com/library/command-r-plus) | 104B | 13.8 | 60GB+ VRAM GPU (3xRTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | 109B | 12.0 | 230+ VRAM GPU (4xH100 or better) |

<br>

***Mid-sized models (<14B parameters)*** : These are well-suited for local deployment on high-end workstations. However, such deployment demands substantial investment in hardware, including a powerful GPU and other components, with total costs generally falling between $2,000 to $3,400 (or equivalent).

| Organization       | Model                                                                 | Model Size  | Percent correct | Hardware requirement (using Q4 quantization) |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | 32B | 40.0 | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)  | 32.8B | 30.8 | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)  | 32.8B | 29 | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/)      | [Phi-4](https://huggingface.co/microsoft/phi-4) | 14B | 27.4 | 10GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-Coder-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct)  | 14.8B | 26.6 |  10GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)  | 32.8B | 24.6 |  20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Codestral-22B](https://ollama.com/library/codestral) | 22B | 20.6 | 14GB+ VRAM GPU (RX 7800 or RTX 4070 Ti or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)        | [DeepSeek-Coder-V2-Lite-Instruct](https://ollama.com/library/deepseek-coder-v2) | 16B | 17.2 |  10GB+ VRAM GPU (RX 7800 or RTX 4070 or better)|

<br>

***Small models (<7B parameters)*** : These are lightweight and easily deployable on medium machines, offering broader accessibility. They typically require a mid-range consumer configuration, with costs generally between $700 to $1,400 (or equivalent).

| Organization       | Model                                                                 | Model Size  | Percent correct | Hardware requirement (using Q4 quantization) |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)  | 7B | 20.3 | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [CodeQwen1.5-7B-Chat](https://ollama.com/library/codeqwen:v1.5-chat)  | 7B | 17.2 |  8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)          | [CodeGeeX4-All-9B](https://ollama.com/library/codegeex4:9b-all-q4_0)  | 9B | 17.2 | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/01AI.svg" alt="01AI" width="200" height="20" />](https://www.01.ai/)          | [Yi-Coder-9B-Chat](https://huggingface.co/01-ai/Yi-Coder-9B-Chat)     | 9B          | 14.6 | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)  | 7.62B | 14.2 | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mamba-codestral-7B-v0.1](https://huggingface.co/mistralai/mamba-codestral-7B-v0.1)  | 7B | 13.9 | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)        | [DeepSeek-Coder-6.7B-instruct](https://ollama.com/library/deepseek-coder:6.7b-instruct) | 7B | 12.8 | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) | 14B | **Incoming** | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | 8B | **Incoming** | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/) | [Phi-4-reasoning-plus](https://huggingface.co/microsoft/Phi-4-reasoning-plus) | 14B | **Incoming** |  16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it) | 12B | **Incoming** | 16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)  | [GLM-Z1-9B-0414](https://huggingface.co/THUDM/GLM-Z1-9B-0414) | 9B | **Incoming** | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/) | [Phi-4](https://huggingface.co/microsoft/phi-4) | 14B | **Incoming** |  16GB+ VRAM GPU (RX 7800 or RTX 4080 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Xiaomi.svg" alt="Xiaomi" width="200" height="20" />](https://www.mi.com/global/) | [MiMo-7B-RL](https://huggingface.co/XiaomiMiMo/MiMo-7B-RL) | 7B | **Incoming** | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/IBM.svg" alt="ibm" width="200" height="20" />](https://github.com/ibm-granite/) | [Granite-3.3-8b-instruct](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct) | 8B | **Incoming** | 8GB+ VRAM GPU (rx 7700 or RTX 4070 or better) |

<br>
<br>

### Proprietary Models

Typically accessible through a paid API or web interface.

| Provider             | Model     | Percent correct | Pricing |
|:-----------------:|:------------:|:----------------------:|:-------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [o3](https://chat.openai.com/) | 79.6 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />    |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini Pro 2.5](https://gemini.google.com/) | 76.9| <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.7 Sonnet](https://claude.ai//) | 64.9 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [o1](https://chat.openai.com/) | 61.7 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />    |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/xAI.svg" alt="xAI" width="220" height="20" />](https://x.ai/) | [Grok-3](https://x.ai/blog/grok-3) | 53.3 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4.1](https://openai.com/index/gpt-4-1/) | 52.4 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.5 Sonnet](https://claude.ai//) | 51.6 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini Flash 2.5](https://gemini.google.com/) | 47.1 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [GPT-4o](https://chat.openai.com/) | 45.3 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4.1 mini](https://openai.com/index/gpt-4-1/) | 32.4 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.5 Haiku](https://claude.ai//) | 28.0 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen 2.5 Max](https://qwenlm.github.io/blog/qwen2.5-max/) | 21.8 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4.1 nano](https://openai.com/index/gpt-4-1/) | 8.9 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [GPT-4o-mini](https://chat.openai.com/)  | 3.6 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)     |

<br>
<br>
