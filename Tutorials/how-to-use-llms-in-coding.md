<div align="center"> 
 
<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Tutorials/CodingAI.png">

***Welcome! This guide helps you boost your coding workflow with AI, from choosing tools and models to seamless IDE integration.***

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20with%20Monocle.png" alt="Face with Monocle" width="25" height="25" /> Reading Time : 16min

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

VS Code users have access to a variety of powerful AI-driven extensions. Below are some notable options designed to enhance different aspects of the development workflow:

### Cline

<img src="https://avatars.githubusercontent.com/u/184127137?s=48&v=4" width="20" height="20" > ***[Cline](https://cline.bot/)*** is self-described as "The Collaborative AI Coder." It's an open-source VS Code extension designed as an AI partner to enhance engineering team capabilities by deeply integrating into the development workflow and amplifying developer impact.

**Currently Supported Models**:

Upon creating a Cline account, users get instant access to frontier AI models. New users start with free credits (no credit card needed). Models available include:
  - ***Anthropic Claude 3.7 Sonnet*** (recommended for coding)
  - ***Anthropic Claude 3.5 Sonnet***
  - ***DeepSeek Chat*** (a cost-effective alternative)
  - ***Google Gemini 2.0 Flash***

Key highlights of Cline include:
*   **Collaborative AI Partner**: Cline focuses on collaboration by creating a thoughtful plan before acting, explaining its reasoning, asking for user input, and breaking down complex tasks step-by-step.
*   **Deep Workflow Integration**: It's more than a code generator. Cline monitors your development environment (terminals, files, error logs), can integrate with external databases and live documents via MCP Servers, and automatically detects and applies fixes.
*   **Enterprise-Grade Security & Privacy**: Cline is engineered for enterprise-level security. It allows access to top-tier models through AWS Bedrock, GCP Vertex, or Azure endpoints while keeping code secure. The website emphasizes that **Cline never tracks or stores your data**.
*   **Open Source & Community Driven**: With a 100% transparent codebase on GitHub (boasting 44.2k stars), Cline promotes an active community and ensures users retain control over the tool.
*   **Safe & Controlled Development**: It implements a checkpoint system, allowing developers to review every change before it's applied and easily roll back to any previous state.
*   **VS Code Extension**: Cline is integrated directly into Visual Studio Code as an extension. Installation is done via the VS Code Marketplace: search for 'Cline', install, and then add an API key after creating an account.
*   **Significant Adoption**: The tool has a strong user base, with 1.5 million installations reported on its website.

<br>

### Continue

<img src="https://avatars.githubusercontent.com/u/127876214?s=48&v=4" width="20" height="20" > ***[Continue](https://www.continue.dev/)*** provides open-source IDE extensions (for VS Code and JetBrains) and a hub of models, rules, prompts, and docs. It enables developers to create, share, and use custom AI code assistants tailored to their specific environments, tools, and development practices, aiming for an "AI-native development" experience that amplifies developer capabilities.

**Currently Supported Models & Providers**:

Continue is designed to work with a wide range of models and providers. The website highlights compatibility with:
  - Ollama and LM Studio (for local models)
  - OpenAI
  - Together AI
  - Anthropic
  - Mistral
  - Azure OpenAI Service

**Key highlights of Continue include**:
*   **Custom AI Code Assistants**: Build AI assistants tailored to your specific codebase, internal documentation, and development workflows.
*   **IDE Integration**: Available as extensions for both VS Code and JetBrains IDEs.
*   **Core AI Coding Features**:
    *   **Tab to Autocomplete**: Autocompletes single lines or entire sections of code in any programming language.
    *   **Reference and Chat**: Attach code snippets, files, or other context (like documentation, GitLab issues, Confluence pages) to ask questions or get explanations.
    *   **Highlight and Edit/Instruct**: Select code sections and use natural language prompts via a keyboard shortcut to rewrite or modify the code.
*   **Open Source**: The core tooling is open-source, with the code available on GitHub.
*   **Continue Hub**: A central place to discover and share models, rules, prompts, documentation, and other building blocks for creating custom AI assistants.
*   **Flexible Context Integration**: Can leverage various sources of context, including your codebase, Git issues, documentation (Methods, Confluence), and local files.
*   **Modular Building Blocks**: Utilize data blocks, docs blocks, rules blocks, MCP (Model Customization Pack) blocks, and prompts blocks to define and refine your AI assistants.

<br>

### Github Copilot

<img src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" width="20" height="20" > ***[GitHub Copilot](https://github.com/features/copilot)*** is an AI pair programmer that provides contextualized assistance throughout the software development lifecycle. It's designed to help developers write better code faster by offering code completions, chat assistance, code explanations, and more, directly within the IDE and GitHub platform.

**Currently Supported Models & Access**:

GitHub Copilot leverages generative AI models developed by GitHub, OpenAI, and Microsoft. Users can often swap between different models depending on their plan and the task at hand. 

  - OpenAI's GPT (e.g., GPT-4.1, o1, o3, o3-mini, o4-mini), 
  - Anthropic's Claude (e.g., Claude 3.5 Sonnet, Claude 3.7 Sonnet)
  - Google's Gemini (e.g., Gemini 2.0 Flash, Gemini 2.5 Pro).
  - The Pro+ plan offers access to all models, including GPT-4.5.

**Key highlights of GitHub Copilot include**:
*   **Agent Mode (Preview)**: Allows delegation of open issues to Copilot, which can then plan, write, test, and iterate on code, ultimately delivering pull requests. It can connect to MCP servers to use repository and external data.
*   **IDE and Platform Integration**: Natively built into GitHub and available as an extension for major IDEs including Visual Studio Code, Visual Studio, JetBrains suite, Neovim, Xcode, Azure Data Studio, and Eclipse.
*   **Broad Language Support**: Trained on all languages found in public repositories, with performance varying based on the volume of training data for each language.
*   **Code Completions & Chat**: Offers intelligent code suggestions as you type and allows for natural language conversations to generate code, explain snippets, or answer questions.
*   **Next Edit Suggestions**: Helps maintain consistency by showing the potential ripple effects of code changes across a project.
*   **Code Review Capabilities**: Can analyze code, identify potential bugs, suggest fixes, and more, before human review.
*   **Flexible Model Usage**: Depending on the subscription, users can switch between different AI models optimized for speed or depth.
*   **Tiered Plans**: Offers "Free" (limited requests), "Pro" (unlimited completions/chats, more models), and "Pro+" (maximum flexibility, all models, coding agent preview) plans. It's free for verified students, teachers, and maintainers of popular open-source projects.
*   **Security & Privacy Focus**: Includes an optional code referencing filter to detect and suppress suggestions matching public code. GitHub offers IP indemnification for unmodified suggestions when this filter is enabled. It also scans for vulnerable code patterns.
*   **Productivity Enhancement**: Widely adopted, with users reporting significant improvements in job satisfaction and coding productivity.

<br>

### Roo Code

<img src="https://avatars.githubusercontent.com/u/169046090?s=48&v=4" width="20" height="20" > ***[Roo Code](https://github.com/RooCodeInc/Roo-Code)*** (formerly Roo Cline) positions itself as providing "a whole dev team of AI agents in your code editor." It is an open-source project, forked from `cline/cline`, and aims to provide advanced AI-driven development assistance.

**Currently Supported Models & Providers**:

*   Being a fork of Cline, Roo Code likely inherits Cline's capabilities regarding model support. 

**Key highlights of Roo Code include**:
*   **AI Agent Team**: The core premise is to offer multiple AI agents within the IDE, suggesting a focus on diverse and specialized AI assistance for development tasks.
*   **Open Source & Forked from Cline**: Built upon the foundation of the `cline/cline` project, indicating a robust set of initial features related to AI-powered coding, environment monitoring, and potentially MCP server integration.
*   **VS Code Extension**: Primarily distributed as a VS Code extension, integrating directly into the editor.
*   **Community & Development**: The project has a significant number of stars (14.2k) and forks (1.4k) on GitHub, indicating active interest and community involvement. It is licensed under Apache-2.0.
*   **Focus on Autonomous Capabilities**: The tagline "Whether you keep it on a short leash or let it roam autonomously" suggests features that allow for varying degrees of AI control and independent operation.
*   **Active Development**: The repository shows ongoing commits and releases, with the latest release noted as v3.18.0 (as of the information on the GitHub page).
*   **Community Engagement**: Encourages users to join their Reddit community or Discord for questions and feature ideas.

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

### Open Source Models: Estimating Hardware Needs

Here's a general guide to help you estimate VRAM/RAM requirements based on model size when using 4-bit quantization:

| Model Size (Parameters, Approx. Q4 Quantized) | Estimated VRAM/RAM Requirement                 | Typical Hardware Scenario                                         |
|-----------------------------------------------|------------------------------------------------|-------------------------------------------------------------------|
| > 100B - 700B+ (Very Large)                   | 60GB - 400GB+ VRAM                             | Multiple server-grade GPUs (e.g., NVIDIA H100s); Cloud deployment often necessary |
| ~50B - 100B (Large)                           | 30GB - 60GB+ VRAM                              | 1-2 high-end workstation/server GPUs (e.g., RTX 4090, A100)      |
| ~15B - 50B (Medium)                           | 16GB - 40GB VRAM                               | Single high-end consumer GPU (e.g., RTX 4080/4090, RX 7900XT)     |
| ~7B - 15B (Small-Medium)                      | 8GB - 16GB VRAM                                | Mid-to-high range consumer GPU (e.g., RTX 3070/4070/4080, RX 6800/7800XT) |
| < 7B (Small/Tiny)                             | 4GB - 8GB+ VRAM, or 8GB+ System RAM (for CPU) | Entry-level GPU / Most modern CPUs with sufficient system RAM    |

**Important Considerations:**
*   **Quantization:** These VRAM estimates are for 4-bit quantized models. Unquantized models will require significantly more VRAM (roughly double for 8-bit, four times for 16-bit precision).
*   **Model Architecture:** Different model architectures can have slightly different memory footprints even with the same parameter count.
*   **Context Length:** Longer context windows can also increase VRAM usage.
*   **Specific Implementations:** The software used to run the model (e.g., Ollama, vLLM, llama.cpp) can influence actual memory usage.

<br>
<br>

Models are ranked based on an Overall score derived from two leaderboards, [Aider polyglot coding leaderboard](https://aider.chat/docs/leaderboards/) and  [BigCodeBench Leaderboard](https://bigcode-bench.github.io/) with higher scores indicating better performance. If one of the two scores is unavailable, the available score will determine the ranking.

The Aider polyglot benchmark tests LLMs on 225 complex Exercism coding challenges spanning **six programming languages: C++, Go, Java, JavaScript, Python, and Rust.**

BigCodeBench evaluates LLMs with [practical and challenging programming tasks](https://github.com/bigcode-project/bigcodebench).

### Open Source Models

***Large-scale models (>70 billion parameters)*** : These require significant amounts of both RAM and GPU memory, often rendering local installation infeasible for most users. Consequently, such models are predominantly deployed on cloud-based platforms designed to provide the essential computational resources needed.

| Organization       | Model                                                                 | Model Size  |  Overall Score | Aider Score | BigCodeBench Score |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:--------------:|:-----------:|:------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | 685B  | **53.35** | 71.6 | 35.1 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) | 235B | **46.05** | 59.6 | 32.5 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) | 671B  | **44.8** | 55.1 | 34.5 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | 402B | **21.9** | 15.4 | 28.4 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)            | [Llama-3.3-70b-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | 70B |  xx | xx | 28.4 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)            | [Llama-3.1-405b-Instruct](https://ollama.com/library/llama3.1:405bt)  | 405B | xx | xx | 26.4 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mistral-Large-2-Instruct](https://ollama.com/library/mistral-large)  | 123B | xx | xx | 26 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)  | [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)  | 72.2B | xx | xx | 25.4 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mixtral-8x22b-Instruct-v0.1](https://ollama.com/library/mixtral:8x22b-instruct) | 141B | xx | xx | 19.9 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | 109B | xx | xx | 16.9 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)          | [Command R+](https://ollama.com/library/command-r-plus) | 104B | xx | xx | 13.9 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)          | [Command A](https://huggingface.co/CohereForAI/c4ai-command-a-03-2025) | 111B | xx | 12.0 | xx |

<br>

***Mid-sized models (<14B parameters)*** : These are well-suited for local deployment on high-end workstations. However, such deployment demands substantial investment in hardware, including a powerful GPU and other components, with total costs generally falling between $2,000 to $3,400 (or equivalent).

| Organization       | Model                                                                 | Model Size  |  Overall Score | Aider Score | BigCodeBench Score |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:--------------:|:-----------:|:------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | 32B | xx | 40.0 | xx |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)  | 32.8B | **24.95** | 20.9 | 29 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)  | 32.8B | **23.6** | 16.4 | 30.8 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Codestral-22B](https://ollama.com/library/codestral) | 22B | **15.85** | 11.1 | 20.6 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/)      | [Phi-4](https://huggingface.co/microsoft/phi-4) | 14B | xx | xx | 27.4 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-Coder-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct)  | 14.8B | xx | xx | 26.6 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) | 27B | xx | xx | 26 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)  | 32.8B | xx | xx | 24.6 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)        | [DeepSeek-Coder-V2-Lite-Instruct](https://ollama.com/library/deepseek-coder-v2) | 16B | xx | xx | 17.2 |

<br>

***Small models (<7B parameters)*** : These are lightweight and easily deployable on medium machines, offering broader accessibility. They typically require a mid-range consumer configuration, with costs generally between $700 to $1,400 (or equivalent).

| Organization       | Model                                                                 | Model Size  |  Overall Score | Aider Score | BigCodeBench Score |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:--------------:|:-----------:|:------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [CodeQwen1.5-7B-Chat](https://ollama.com/library/codeqwen:v1.5-chat)  | 7B | xx | xx | 17.2 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)          | [CodeGeeX4-All-9B](https://ollama.com/library/codegeex4:9b-all-q4_0)  | 9B | xx | xx | 17.2 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/01AI.svg" alt="01AI" width="200" height="20" />](https://www.01.ai/)          | [Yi-Coder-9B-Chat](https://huggingface.co/01-ai/Yi-Coder-9B-Chat)     | 9B |  xx | xx | 14.6 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)  | 7B | xx | xx | 14.2 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)  | 7.62B | xx | xx | 14.2 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mamba-codestral-7B-v0.1](https://huggingface.co/mistralai/mamba-codestral-7B-v0.1)  | 7B |  xx | xx | 13.9 |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)        | [DeepSeek-Coder-6.7B-instruct](https://ollama.com/library/deepseek-coder:6.7b-instruct) | 7B |  xx | xx | 12.8 |

<br>
<br>

### Proprietary Models

Typically accessible through a paid API or web interface.

| Provider             | Model     | Overall Score | Aider Score | BigCodeBench Score | Pricing |
|:-----------------:|:------------:|:----------------------:|:-------:|:-------:|:-------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [o3](https://chat.openai.com/) | **57.55** | 79.6 | 35.5 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />    |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-4 Opus](https://claude.ai//) | **55.5** | 72.0 | 39 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini Pro 2.5](https://gemini.google.com/) | **55.0** | 76.9 | 33.1 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.7 Sonnet](https://claude.ai//) | **50.35** | 64.9 | 35.8 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-4 Sonnet](https://claude.ai//) | **48.55** | 61.3 | 35.8 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/xAI.svg" alt="xAI" width="220" height="20" />](https://x.ai/) | [Grok-3](https://x.ai/blog/grok-3) | **43.2** | 53.3 | 33.1   | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4.1](https://openai.com/index/gpt-4-1/) | **42.6** | 52.4 | 32.8 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini Flash 2.5](https://gemini.google.com/) | **41.9** | 55.1 | 28.7 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.5 Sonnet](https://claude.ai//) | **41.0** | 51.6 | 30.4 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [GPT-4o](https://chat.openai.com/) | **38.2** | 45.3 | 31.1 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4.1 mini](https://openai.com/index/gpt-4-1/) | **32.1** | 32.4 | 31.8 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.5 Haiku](https://claude.ai//) | **29.05** | 28.00 | 30.1 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen 2.5 Max](https://qwenlm.github.io/blog/qwen2.5-max/) | **27.15** | 21.8 | 32.5 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4.1 nano](https://openai.com/index/gpt-4-1/) | **19.5** | 8.9 | 30.1 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [GPT-4o-mini](https://chat.openai.com/)  | **14.45** | 3.6 | 25.3 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)     |

<br>
<br>
