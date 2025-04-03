<div align="center"> 
 
[![SVG Banners](https://svg-banners.vercel.app/api?type=luminance&text1=Integrating%20AI%20Models%20into%20your%20IDE%20👨‍💻&width=1100&height=550)](https://github.com/Akshay090/svg-banners)

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand.png" alt="Waving Hand" width="30" height="30" /> ***Welcome to your guide for enhancing your development workflow with AI assistance! Whether you're new to AI-powered coding or looking to optimize your setup, this tutorial will walk you through seamless IDE integration.*** <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand.png" alt="Waving Hand" width="30" height="30" />

***<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Orange%20Square.png" alt="Orange Square" width="15" height="15" /> Level : Intermediate***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20with%20Monocle.png" alt="Face with Monocle" width="25" height="25" /> Reading Time : 16min***


</div> 

## Table of Contents

* [Introduction](#introduction)
* [Cursor the dedicated IDE for seamless AI integration](#cursor-the-dedicated-ide-for-seamless-ai-integration)
* [Implementing AI Assistance](#implementing-ai-assistance)
  * [Model providers](#model-providers)
    * [Code dedicated providers](#code-dedicated-providers)
    * [Generalist Models Providers](#generalist-models-providers)
  * [LLMs Models](#llms-models)
    * [Open Source Models](#open-source-models)
    * [Proprietary Models](#proprietary-models)
* [Hands-on implementation guide using Ollama and Continue](#hands-on-implementation-guide-using-ollama-and-continue)  
  * [Setup Ollama as the Local Model Provider](#setup-ollama-as-the-local-model-provider)
  * [Installation and usage of Continue.dev extension](#install-continue-extension)

<br>

# Introduction

Modern development environments now **leverage AI capabilities to enhance code synthesis, automate routine operations, and optimize development workflows.** IDE integration of language models enables contextual code assistance, automated testing, and intelligent refactoring while maintaining established development practices.

<img src="https://github.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/blob/master/Emojis/Symbols/Green%20Circle.png" width="15" height="15" /> ***The Pros: Boosting Productivity and Innovation***

* **Increased productivity** : AI tools can automate repetitive coding tasks, generate code snippets, and provide intelligent code suggestions, allowing developers to focus on more complex problems and accelerate development cycles.
* **Improved code quality** : AI-powered code analysis can detect bugs, security vulnerabilities, and code smells, helping developers write cleaner and more maintainable code.
* **Enhanced learning experience** : AI assistants can provide real-time guidance, explanations, and best practice recommendations, facilitating the learning process for novice developers.
* **Accessibility** : AI tools can make coding more accessible to non-experts by bridging the gap between novice and experienced developers, enabling a broader range of individuals to participate in software development.

<br>

<img src="https://github.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/blob/master/Emojis/Symbols/Red%20Circle.png" width="15" height="15" /> ***The Cons: Challenges and Considerations***

* **Potential bias and errors** : AI models can inherit biases from their training data or make mistakes, leading to incorrect code suggestions or flawed analysis.
* **Over-reliance and loss of skills** : Excessive dependence on AI tools may hinder developers' ability to write code independently and erode their problem-solving skills over time.
* **Security and privacy concerns** : AI tools may inadvertently expose sensitive data or introduce security vulnerabilities if not properly secured and maintained.
* **Integration challenges** : Integrating AI tools into existing development workflows and IDEs can be complex, requiring additional configuration and compatibility considerations.
* **Cost and accessibility** : Advanced AI tools may come with significant licensing costs or require specialized hardware, making them less accessible to individual developers or smaller organizations.

<br>

> [!CAUTION]
> Code assistance models **complement developer expertise by augmenting development workflows through contextual suggestions and documentation integration.** These systems enhance implementation speed and technical learning while relying on established programming principles and human oversight.
>
> <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" /> **Always validate AI-generated code against official documentation and established development standards. Implement thorough code review practices when using automated suggestions.** <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" />

<br>

# Cursor the dedicated IDE for seamless AI integration 

<img src="https://cursor.sh/brand/icon.svg" width="20" height="20" > ***[Cursor](https://cursor.sh/)*** integrates language models into a VS Code-based editor, **providing contextual code completion, codebase analysis, and natural language editing capabilities.** The platform supports both cloud-based and local AI models.

**Currently Supported Models** :

- ***Claude 3.7 Sonnet and Claude 3.5 Sonnet*** by Anthropic
- ***o1 / o3-mini and gpt-4.5*** by OpenAI
- ***Gemini 2.0 Flash and Gemini 2.0 Pro*** by Google
- ***Deepseek-R1 and Deepseek-V3*** by Deepseek
- ***Cursor-fast and Cursor-small*** by Cursor

Some key features of Cursor include:

* **Code understanding and context** : Cursor.sh can ***understand the context of your entire codebase***, allowing it to provide tailored suggestions, generate unit tests, and even implement new features by modifying the relevant files.
* **Natural language editing** : You can edit code using natural language prompts, such as changing an entire method or class with a single instruction.
* **Code generation** : Cursor.sh can generate code from scratch based on simple instructions provided by the user.
* **Integration with VSCode** : Cursor.sh is ***a fork of VSCode***, allowing users to import all their extensions, themes, and keybindings with a single click.
* **Privacy options** : Cursor.sh ***offers a privacy mode*** where none of your code is stored on their servers or logs, catering to security-critical work.

<br>
<br>

# Implementing AI Assistance

## Model providers

**First Let's pick the right AI provider** for your coding needs! Consider What features you'll use most, Where your code will live (local or cloud), Your privacy preferences, and How it fits with your favorite IDE.

> [!TIP]
> **Take a moment to explore different options - finding the right fit makes all the difference!**
> 
> Reference the [Artificial Analysis Leaderboard](https://artificialanalysis.ai/leaderboards/providers) for **comparative analysis of LLM providers across key performance metrics**: pricing, token generation speed, response latency, and context window capabilities.

> [!CAUTION]
> <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" /> **Security Consideration** : Cloud-based code assistance services process codebase data through remote infrastructure, potentially exposing sensitive information to third-party systems. Consider data privacy implications and compliance requirements when implementing proprietary code processing services.
>
> Proprietary code assistance services **may utilize submitted code for model training and refinement.** Review provider terms of service regarding data collection and model training practices. <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" />

### Code dedicated providers

***Cloud-based Proprietary Providers*** 

| Tool       | Description                                                                                                           | Licence     | Pricing |
|:-----------|-----------------------------------------------------------------------------------------------------------------------|:-----------:|:-------------:|
| [AskCodi](https://www.askcodi.com/)    | An AI-powered coding assistant that offers code suggestions, debugging help, and explanations for code snippets. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) |[<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Blackbox](https://www.blackbox.ai/)   | An AI platform that helps businesses automate processes, make predictions, and optimize decision-making. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Boxy](https://codesandbox.io/blog/meet-boxy-ai-coding-assistant)       | An AI coding assistant by CodeSandbox providing real-time code suggestions and completions. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Codeium](https://codeium.com/)    | An AI-powered code completion tool that helps developers write code faster and more accurately. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [CodeWhisperer](https://aws.amazon.com/codewhisperer/)    | Developed by Amazon, provide real-time code suggestions and completions. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Codium](https://www.codium.ai/)     | An AI-powered tool that analyze your code, docstring, and comments and suggests tests as you code. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Copilot](https://github.com/features/copilot) | Developed by GitHub and OpenAI, provide real-time code suggestions and completions. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [JetBrains AI](https://www.jetbrains.com/ai/) | JetBrains is working on integrating AI capabilities into their development tools. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) |<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />        |
| [Replit AI](https://replit.com/ai)  | A coding assistant and tutorial platform developed by Replit, offering code suggestions and explanations. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Tabnine](https://www.tabnine.com/)    | An AI-powered code completion tool that helps developers write code faster and more accurately. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |

<br>

***Open-Source Providers*** 

| Tool       | Description                                                                                                           | Licence     | Pricing |
|:-----------|-----------------------------------------------------------------------------------------------------------------------|:-----------:|:-------------:|
| [Aider](https://aider.chat/)    | an AI-powered pair programming tool designed to assist developers in writing and editing code directly from the command line.  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/free.svg" alt="Free" width="80" height="20" /> |
| [Continue](https://www.continue.dev/)     | An open-source autopilot for software development that enables developers to create their own AI code assistant within their integrated development environment (IDE) like VS Code or JetBrains IDEs. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/free.svg" alt="Free" width="80" height="20" /> |
| [Llamacoder](https://llamacoder.together.ai/) | An open source Claude Artifacts – generate small apps with one prompt. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source)  | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/free.svg" alt="Free" width="80" height="20" /> |
| [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) | Open Interpreter is an innovative open-source project that allows language models to execute code on a user's computer to complete various tasks. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source)  | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/free.svg" alt="Free" width="80" height="20" /> |

<br>

### Generalist Models Providers

***Cloud-based Providers***

| Tool             | Description                                                                                                                 | Pricing     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/AI21.svg" alt="ai21" width="200" height="20" />](https://www.ai21.com) |  Known for their language models like Jurassic-1 Jumbo focused on quality, safety, and controllability. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/amazon.svg" alt="Amazon" width="200" height="20" />](https://aws.amazon.com/ai/) | Offers models like Amazon CodeWhisperer for code generation and understanding through their SageMaker platform. | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |  
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | Known for their constitutional AI model Claude, focused on being helpful, harmless, and honest. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) | 
| [Cerebras](https://inference.cerebras.ai/) | An AI company that has developed innovative hardware and software solutions for AI computing. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) | Provides an enterprise AI platform with models like Cohere Generate for custom content creation. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/databricks.svg" alt="databricks" width="200" height="20" />](https://www.databricks.com) | A unified, open analytics platform that provides tools and services for data processing, analytics, and artificial intelligence at scale. | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [DeepInfra](https://deepinfra.com/chat) | A platform that provides scalable and cost-effective infrastructure for deploying machine learning models. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://chat.deepseek.com/) | An AI company that has developed several notable AI models and technologies | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Fireworks.svg" alt="Fireworks" width="200" height="20" />](https://fireworks.ai/) | A comprehensive solution for companies looking to deploy AI into production, focusing on performance, cost-effectiveness, and developer experience. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)  |  Provides models like LaMBDA, PaLM, and Bard for language understanding, generation, and multimodal AI tasks. |[<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) | 
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Groq.svg" alt="Groq" width="220" height="20" />](https://groq.com/) | Specializes in high-performance AI inference with custom LPU (Language Processing Unit) hardware, offering models like Meta's Llama 3. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/spaces) | The AI dedicated github, Offers a platform with most open-source models like BERT, GPT-Neo, and Llama for various AI tasks. | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/free.svg" alt="Free" width="80" height="20" /> | 
| [LeptonAI](https://www.lepton.ai/) | A platform that provides cloud-based infrastructure and tools for deploying and running AI applications efficiently. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://azure.microsoft.com/) | A comprehensive suite of AI services and tools designed to help developers and organizations build, deploy, and manage AI applications at scale. | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | A French artificial intelligence company that specializes in developing large language models (LLMs) and AI products. |[<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [OctoAI](https://octoai.cloud/) | A full-stack inference platform designed specifically for generative AI applications. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | Offers models like GPT-4, DALL-E, and Whisper for natural language processing, image generation, and speech recognition. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenRouter.svg" alt="OpenRouter" width="200" height="20" />](https://openrouter.ai/) |  A versatile platform designed to provide access to a wide range of large language models (LLMs) from both proprietary and open-source sources. | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Perplexity.svg" alt="Perplexity" width="200" height="20" />](https://labs.perplexity.ai/) | An online platform that provides free access to various powerful open-source large language models (LLMs) for experimentation and use in a wide range of applications. | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/free.svg" alt="Free" width="80" height="20" /> | 
| [Poe](https://poe.com) | An AI chatbot aggregator platform developed by Quora that provides users access to multiple advanced language models and chatbots within a single interface. |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Reka.svg" alt="Reka" width="150" height="20" />](https://www.reka.ai/)| An AI company that develops advanced multimodal AI models and technologies. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Replicate](https://replicate.com/home) | A cloud platform that allows developers to easily run and deploy open-source machine learning models. | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [SambaNova](https://sambanova.ai/) | An artificial intelligence company that provides a comprehensive AI platform for enterprises. | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Together](https://www.together.ai/) | A cloud platform designed for building and running generative AI applications. | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> | 
| [Vercel](https://sdk.vercel.ai/) | A powerful tool for developers looking to explore and integrate various AI models into their applications efficiently. | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |

<br>

***Local Providers***

> [!IMPORTANT]
> **Deploy LLMs locally** with our [implementation guide](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/run-llms-locally-on-your-machine.md) for privacy-focused language processing and model experimentation on your hardware.

| Tool             | Description                                                                                                                 | OS     | Models     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [AnythingLLM](https://anythingllm.com/) | an open-source, full-stack application that allows users to chat with their documents in a private and enterprise-friendly environment. | All | Open source Models and Proprietary models via API |
| [Enchanted](https://github.com/AugustDev/enchanted) | iOS and macOS app for chatting with private self hosted language models.| MacOS/IOS | Open source Models |
| [GPT4ALL](https://www.nomic.ai/gpt4all) | An open-source software ecosystem developed by Nomic AI that enables users to run powerful large language models (LLMs) locally on their personal computers. | All | Open source Models |
| [Jan](https://jan.ai/) | Clean UI with useful features like system monitoring and LLM library.| All | Open source Models. |
| [LM Studio](https://superagi.com/) |  Elegant UI with the ability to run every Hugging Face repository. | All | Open source Models |
| [Msty](https://msty.app/) |  an AI chat application that offers a user-friendly interface for interacting with both local and online AI language models. | All | Open source Models and Proprietary models via API |
| [Ollama](https://ollama.com/) | Fastest when used on the terminal, and any model can be downloaded with a single command. | All | Open sources Models |

<br>
<br>

## LLMs Models

Now that you've chosen your provider, let's find the right model for your coding needs.

We designed **two tables** to assist those who require **guidance in selecting the ideal model for coding purposes.**

The first table highlights **Open-source models**, which you can typically run **locally on your machine** (Probably not hte Massive Models). To ensure a smooth experience running these models locally, I will provide the necessary hardware requirements for optimal performance. Please note that while you may be able to run certain models with lower hardware specifications, you can expect slower output and performance as a result.

The second table features **Proprietary models** that usually operate on **cloud-based providers**.

The models are ranked according to **[BigCodeBench Pass@1](https://bigcode-bench.github.io/)** scores (with higher scores indicating better performance). ***Pass@1 is the probability of passing a given problem in one attempt***.

> [!CAUTION]
> <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" /> Please note that the hardware requirements provided are only indicative, and the specified VRAM requirements in the tables below apply specifically to the default Ollama Q4_0 quantization version of the models. [Learn more about LLMs Quantization](https://huggingface.co/blog/merve/quantization). <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" />

> [!TIP]
> **You can always try different models to find your perfect match. Many developers mix and match based on different tasks!**
>
> <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" /> **Badges provide direct links to model downloads, provider services, and official documentation.** <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Triangular%20Flag.png" alt="Triangular Flag" width="25" height="25" />

### Open Source Models

***Massive models*** : Challenging for local deployment due to computational requirements. Use them via any of the [listed Cloud-based Providers](https://github.com/LSeu-Open/AIEnhancedWork?tab=readme-ov-file#cloud-based-providers-1) (e.g. Groq / Together / Mistral or OpenRouter).

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Pass@1 score (/100) |  Ollama libraries |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)        | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | 685B  | 405GB+ VRAM GPU (5XH100 or better) | 35.1 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-r1:671b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/deepseek-ai/DeepSeek-R1) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)        | [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) | 671B  |  405GB+ VRAM GPU (5XH100 or better)  | 34.1   | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-v3) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://chat.deepseek.com/sign_in?from=coder)  |
| [NexuFlow](https://nexusflow.ai/)         | [Athene-v2](https://huggingface.co/Nexusflow/Athene-V2-Chat)  | 72.2B         | 47GB+ VRAM GPU (2xRTX 4090 or better) | 32.1 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/athene-v2) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)        | [DeepSeek-Coder-V2-Instruct](https://ollama.com/library/deepseek-coder-v2:236b) | 236B  | 130GB+ VRAM GPU (2XH100 or better) | 29.4  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-coder-v2:236b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://chat.deepseek.com/sign_in?from=coder)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)            | [Llama-3.3-70b-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | 70B | 40GB+ VRAM GPU (2xRTX 4090 or better) | 28.4 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.3) |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Groq.svg" alt="Groq" width="220" height="20" />](https://groq.com/)     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)            | [Llama-3.1-405b-Instruct](https://ollama.com/library/llama3.1:405bt)  | 405B        | 230+ VRAM GPU (3XH100 or better)  | 26.4   | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/llama3.1:405b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenRouter.svg" alt="OpenRouter" width="200" height="20" />](https://openrouter.ai/chat?models=meta-llama/llama-3.1-405b) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mistral-Large-2-Instruct](https://ollama.com/library/mistral-large)  | 123B        | 70GB+ VRAM GPU (1XH100 or better) | 26   | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/mistral-large) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)  | 72.2B         | 47GB+ VRAM GPU (2xRTX 4090 or better) | 25.4 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:72b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct)  | 72.7B         | 47GB+ VRAM GPU (2xRTX 4090 or better) | 20.6 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2:72b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2-72B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mixtral-8x22b-Instruct-v0.1](https://ollama.com/library/mixtral:8x22b-instruct) | 141B | 80GB+ VRAM GPU (1xH100 or better) | 19.9   | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/mixtral:8x22b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/)          | [Command R+](https://ollama.com/library/command-r-plus)               | 104B        | 60GB+ VRAM GPU (3xRTX 4090 or better) | 13.8 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/command-r-plus)   | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/command) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)            | [CodeLlama-70B-Instruct](https://ollama.com/library/codellama:70b-instruct) | 70B |  40GB+ VRAM GPU (2xRTX 4090 or better) | 13.5 |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/codellama:70b-instruct) | None |


**Mid-sized models** : Suitable for deployment on a high-performance local workstation.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Pass@1 score (/100) |  Ollama libraries |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)  | 32.8B         | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 30.8 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5-coder:32b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)  | 32.8B         | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 29 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwq) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://chat.qwen.ai/)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/)      | [Phi-4](https://huggingface.co/microsoft/phi-4) | 14B | 10GB+ VRAM GPU (rx 7700 or RTX 4070 or better) | 27.4 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/phi4) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-Coder-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct)  | 14.8B         | 10GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 26.6 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5-coder:14b) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)  | 32.8B         | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 24.6 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:32b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Codestral-22B](https://ollama.com/library/codestral)                 | 22B       | 14GB+ VRAM GPU (RX 7800 or RTX 4070 Ti or better) | 20.6 |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/codestral) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://chat.mistral.ai/) | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)        | [DeepSeek-Coder-V2-Lite-Instruct](https://ollama.com/library/deepseek-coder-v2)    | 16B  | 10GB+ VRAM GPU (RX 7800 or RTX 4070 or better)| 17.2   | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-coder-v2) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://chat.deepseek.com/sign_in?from=coder)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Map.svg" alt="Map" width="200" height="20" />](https://m-a-p.ai/)          | [OpenCodeInterpreter-DS-33B](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-33B) | 33B  | 20GB+ VRAM GPU (RX 7900 XT or RTX 4090 or better) | 15.2 |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/wojtek/opencodeinterpreter)  | None |

***Small models*** : Lightweight and deployable on most local machines.

| Organization       | Model                                                                 | Model Size  | Hardware requirement              | Pass@1 score (/100) |  Ollama libraries |  Cloud-based providers |
|:------------------:|:---------------------------------------------------------------------:|:-----------:|:---------------------------------:|:-----------:|:-----------------:|:----------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)  | 7B | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better) | 20.3 |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5-coder:7b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [CodeQwen1.5-7B-Chat](https://ollama.com/library/codeqwen:v1.5-chat)  | 7B | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better) | 17.2 |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/codeqwen:v1.5-chat) | None |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)          | [CodeGeeX4-All-9B](https://ollama.com/library/codegeex4:9b-all-q4_0)  | 9B | 8GB+ VRAM GPU (RX 7600 or RTX 4060 or better) | 17.2 |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/codegeex4:9b-all-q4_0) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/spaces/vilarin/glm-chat) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/01AI.svg" alt="01AI" width="200" height="20" />](https://www.01.ai/)          | [Yi-Coder-9B-Chat](https://huggingface.co/01-ai/Yi-Coder-9B-Chat)     | 9B          | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better) | 14.6 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/yi-coder:9b-chat)  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/01-ai/Yi-Coder-9B-Chat)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)         | [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)  | 7.62B     | 6GB+ VRAM GPU (RX 7600 or RTX 4060 or better) | 14.2 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/qwen2.5:7b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="Hugging Face" width="200" height="20" />](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)        | [Mamba-codestral-7B-v0.1](https://huggingface.co/mistralai/mamba-codestral-7B-v0.1)  | 7B | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better) | 13.9 | No | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)        | [DeepSeek-Coder-6.7B-instruct](https://ollama.com/library/deepseek-coder:6.7b-instruct) | 7B | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better) | 12.8 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Ollama.svg" alt="Ollama" width="230" height="30" />](https://ollama.com/library/deepseek-coder:6.7b-instruct) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://chat.deepseek.com/sign_in?from=coder)  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Map.svg" alt="Map" width="200" height="20" />](https://m-a-p.ai/)          | [OpenCodeInterpreter-DS-6.7B](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-6.7B) | 6.7B | 5GB+ VRAM GPU (RX 6500 or RTX 3050 or better) | 13.2 | No | [<img src="https://github.com/LSeu-

### Proprietary Models

Typically accessible through a paid API or web interface.

| Provider             | Model     | Pass@1 score (/100) | Pricing |
|:-----------------:|:------------:|:----------------------:|:-------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.7 Sonnet](https://claude.ai//) | 35.8 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [o1](https://chat.openai.com/) | 35.5 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />    |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [o3-Mini](https://chat.openai.com/) | 35.5 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />    |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini Pro 2.5](https://gemini.google.com/) | 33.1 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [GPT-4 Turbo](https://chat.openai.com/)  | 32.1| <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini Pro 2.0](https://gemini.google.com/) | 31.8 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [GPT-4o](https://chat.openai.com/) | 31.1 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.5 Sonnet](https://claude.ai//) | 30.4 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini Flash 2.0](https://gemini.google.com/) | 28.7 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini Pro 1.5](https://gemini.google.com/) | 27.4 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3 Opus](https://claude.ai/)  | 26 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [GPT-4o-mini](https://chat.openai.com/)  | 25.3 | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)     |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini Flash 1.5](https://gemini.google.com/) | 23.6 | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />     |

<br>
<br>

## Hands-on implementation guide using Ollama and Continue

***Step-by-step guide for privacy-preserving code assistance using open-source solutions.***

### Setup Ollama as the Local Model Provider

For those who prioritize keeping everything local and private, I'll be using ***[Ollama](https://ollama.com/)*** as the provider in this tutorial. If you haven't already, be sure to check out our **[A Practical Tutorial to Run a Local Model](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/run-local-llm-ollama-and-page-assist.md)** to learn how to install Ollama and get started.
  
> [!Note]
> In this tutorial, I am using the ***Codestral:22b*** model. This particular model is specialized for coding and has been meticulously trained on vast datasets by Mistral.ai.
>
> This model stands out for its **exceptional size and capabilities, selected specifically for the hardware I use on my PC.** As with any model, it has its unique strengths and weaknesses. To get the most out of this tool, be sure to **[choose wisely](#models-for-coding)** among the available options.

### Install Continue extension

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

* Replace **starcoder-2-3b** with the model you prefer. For example, if you want to use **Codestral:22b**, update the code to:

 ```
 "tabAutocompleteModel": {
    "title": "codestral:22b",
    "provider": "ollama",
    "model": "codestral:22b"
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

<div align="center"> 
 
 <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Clapping%20Hands.png" alt="Clapping Hands" width="25" height="25" />   **That's it for this tutorial ! You now have an AI model integrated into your VSCode setup.** <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Clapping%20Hands.png" alt="Clapping Hands" width="25" height="25" />

</div>
  
<br>

## (Bonus) Setup Groq as the Cloud-based Model Provider

If you **don't have the necessary hardware to run models locally** or want to tap into more powerful capabilities, this tutorial is for you. I'll be using ***[Groq](https://groq.com/)*** as the provider, leveraging their infrastructure's fast inference capabilities. 

> [!Note]
> In this tutorial, I'll be leveraging **Groq**, but feel free to substitute it with your preferred provider - whether that's OpenAI, Anthropic, or another that suits your needs.
>
>  When choosing your model, Keep in mind that each model has its strengths and weaknesses.

> Before we get started, make sure you have a Groq account set up - if you haven't already, take a moment to create one.

* Click on the **Continue icon** in the left sidebar to open the Continue panel.
* If it is the first time you open it, The extension will prompt you for a Model Provider; select the **Cloud Provider** option.
* Select **Groq** as your preferred AI provider.
* Head to the **GroqCloud section** of the Groq website (look for the icon at the bottom).
* Create a new **API key** and copy it to your clipboard.
* Return to the window and **paste your API key into the apiKey input field**.
* **Select the AI model** you want to use from the available options. Here on Groq, I'll choose the "Llama-3-70b Model".
* You now have access to a capable model, **ready to be used** as a programming assistant within Visual Studio Code.
  

<br>

