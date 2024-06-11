![header](https://capsule-render.vercel.app/api?type=venom&height=300&color=timeGradient&text=AI%20Enhanced%20Work&textBg=false&fontColor=141414&fontAlign=50&desc=Empower%20Your%20Workflow%20with%20AI-Driven%20Solutions&descAlignY=65&section=header)

🤖 **Welcome to our repository** , carefully curated to enhance productivity, automate tasks, and simplify daily workflows.

Please note that while we try to provide a comprehensive selection of resources, **this repository may not be exhaustive**, and omission does not imply exclusion. Inclusion in this collection does not constitute an endorsement of any particular tool or service.

If you'd like **to suggest new tools or improvements, please submit a pull request (PR)** to enhance the repository's contents. Your contributions are valued and appreciated!

Liked it? Please give a ⭐️ to **AIEnhancedWork**.

 ## Table of Contents
* [Academic and Scientific Research](#academic-and-scientific-research)
  
* [AI Agents](#ai-agents)
  - [Autonomous Agents](#autonomous-agents)
  - [Language Models for Function Calling](#language-models-for-function-calling)
    
* [Automation](#automation)
  
* [Chatbots and conversational AI](#chatbots-and-conversational-ai)
  - [Chatbots Providers](#chatbots-providers)
     - [Cloud-based Providers](#cloud-based-providers)
     - [Local Providers](#local-providers)
       
* [Code Suggestions and Autocompletion](#code-suggestions-and-autocompletion)
  
* [Data Analysis](#data-analysis)
  
* [Image Generation and Editing](#image-generation-and-editing)
  - [Image Generation](#image-generation)
  - [Image Editing](#image-editing)
  - [Video Generation](#video-generation)
    
* [Language learning](#language-learning)
  
* [Music and Audio Generation](#music-and-audio-generation)
  - [Music Generation](#music-generation)
  - [Text to speech](#text-to-speech)
    
* [Productivity](#productivity)
  - [Versatile Productivity tools](#versatile-productivity-tools)
  - [Meeting transcription and summaries](#meeting-transcription-and-summaries)
  - [Presentation slides](#presentation-slides)
  - [Audio and Video transcription and summaries](#audio-and-video-transcription-and-summaries)
  - [Website building](#website-building)
    
<br>

## Introduction

🟢 ***Employing AI-powered tools can yield significant benefits for your work tasks, including***:

* **Automating repetitive and mundane tasks**: By delegating routine chores to AI systems, you gain valuable time to focus on more strategic initiatives.
* **Delivering data-driven insights**: Utilize analytics provided by AI tools to make informed decisions and drive optimal results.
* **Optimizing workflows and processes**: Enhance productivity and efficiency with streamlined operations powered by AI technologies.
* **Creating an engaging and intuitive workspace**: Foster a more personalized, enjoyable, and intellectually stimulating environment through AI implementations.

🔴 ***However, potential downsides should be considered***:

* **Dependence on AI may undermine human skills**: Overreliance on AI systems could lead to diminished problem-solving abilities, critical thinking, and creativity.
* **Potential errors or biased outcomes**: AI systems can occasionally produce inaccuracies or generate prejudiced results, which might negatively impact decision-making processes and outcomes.
* **Risks to privacy and security**: AI usage may introduce vulnerabilities related to the processing, storage, and sharing of sensitive data, potentially resulting in breaches or unauthorized access.

> [!CAUTION]
> **Balancing the benefits of AI with an awareness of these potential drawbacks is crucial. Taking appropriate measures to mitigate risks is essential for successful integration into workflows.**
>
> To effectively mitigate risks associated with generative AI technologies, it's essential to have a solid understanding of their fundamentals. By educating yourself, you'll be better equipped to identify and correct errors and biases, ensuring more accurate and reliable results.
> Microsoft offers [helpful lessons](https://microsoft.github.io/generative-ai-for-beginners/#/) on this subject that can provide you with valuable knowledge.

> [!IMPORTANT]
> **This repository now features a new section dedicated solely to **tutorials**. In this section, I will provide detailed guides aimed at enhancing specific uses of these AI tools.**
>
> * Learn to set up a local LLM chatbot with our first tutorial, "[A Practical Tutorial to Run a Local Model](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/run-local-llm-ollama-and-page-assist.md)", and address privacy concerns of cloud-based AI tools.
> * Learn to set up your IDE to integrate your preferred AI provider with this second tutorial, "[Integrating AI Models into Your Integrated Development Environment (IDE)](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/integrating-ai-models-into-ide.md), and enhance your overall coding experience.

<br>

## Academic and Scientific Research

AI-powered tools designed specifically for academic and research endeavors, enhancing your workflow and insights in the pursuit of knowledge.

> [!CAUTION]
> **Please exercise caution when using AI tools in scientific research. While these tools can greatly enhance your workflow and insights, they are not a replacement for human judgment, critical thinking, and rigorous methodology.**
>
> **Always critically evaluate the results and consider potential biases, limitations, and uncertainties when interpreting AI-generated outputs.**

| Tool             | Description                                                                                                                 | Licence     | Pricing     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [ResearchRabbit](https://www.researchrabbit.ai/) | AI-powered platform that aims to streamline the literature review process for researchers and academics by providing intelligent discovery, recommendation, and visualization capabilities | Proprietary | Free    |
| [Semantic Scholar](https://www.semanticscholar.org/) | A free, AI-powered research tool for scientific literature , with now Semantic Reader, an augmented reader with the potential to revolutionize scientific reading by making it more accessible and richly contextual| Open | Free    |
| [Scispace](https://typeset.io/) | AI-powered platform that aims to simplify and enhance the research and literature review process for academics and researchers | Proprietary | Freemium    |

<br>

## AI Agents

AI agents are intelligent software entities that can perform tasks autonomously or semi-autonomously on behalf of a user or system. These agents can learn from experience, adapt to new situations, and communicate with other agents or systems to achieve their goals.

### Autonomous Agents

| Tool             | Description                                                                                                                 | Licence     | Pricing     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [AgentGPT](https://agentgpt.reworkd.ai/) | A generative artificial intelligence tool that allows users to create autonomous AI agents capable of performing various tasks autonomously. | Open | Freemium    |
| [Godmode](https://godmode.space/) |  A web platform that provides access to innovative AI agents like autoGPT and babyAGI, allowing users to harness the power of autonomous AI agents. | Open | Free    |
| [GPT-Engineer](https://github.com/gpt-engineer-org/gpt-engineer) |  An open-source AI-powered application builder that generates codebases from natural language project descriptions. | Open | Free    |
| [Super AGI](https://superagi.com/) | An open-source autonomous AI agent framework that enables developers to build, manage, and run useful autonomous agents efficiently and reliably. | Open | Free    |

### Language Models for Function Calling

Function Calling allows language models to interact with external functions or APIs within conversations. It generates JSON objects with function names and arguments, enabling actions like querying databases, sending emails, or making API calls based on conversation context. This expands capabilities beyond text responses, allowing dynamic and reactive interactions.

| Tool                                              | Description                                                                                                                                                            | Licence       | Pricing    |
|:--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------:|:----------:|
| [Octopus-V2](https://huggingface.co/NexaAIDev/Octopus-v2) | An open-source language model with 2B parameters, developed by Nexa AI for Android API function calling, representing a research breakthrough in LLM application | Open        | Free |
| [GPT-3.5-turbo, GPT-4 and GPT-4](https://chat.openai.com/) |   OpenAI now feature the capability of "Function Calling", which allows developers to define functions and guide the model to generate arguments for those functions. | Proprietary | Freemium |

> [!Note]
> Do not confond Function Calling with Retrieval-Augmented Generation (RAG) which is a technique that retrieves relevant information from a database and injects it into the language model's context, allowing the model to focus on what is most relevant for a given query.
> 
> RAG augments the model's knowledge, while function calling augments its capabilities and actions.


<br>

## Automation

Automate repetitive, rule-based tasks to improve efficiency and accuracy in processes.

| Tool             | Description                                                                                                                   | Licence       | Pricing       |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-------------:|:-------------:|
| [Bardeen](https://www.bardeen.ai/) | An AI-powered automation platform that enables users to automate repetitive tasks across various applications without writing code. It offers pre-built integrations with popular tools and allows users to create custom workflows. | Proprietary | Paid |
| [N8N](https://n8n.io/) | A free and open-source fair-code licensed workflow automation tool. It allows users to create workflows using a visual editor and connect various services to automate tasks. N8N can be self-hosted, providing users with more control over their data. | Open | Free |
| [ProFlow](https://useproflow.com/) | an AI-powered workflow automation and optimization platform that helps businesses streamline their sales, marketing, and operations processes. | Proprietary | Freemium |
| [Taskade](https://www.taskade.com/) | An all-in-one collaboration platform that combines project management, task tracking, and team communication features. It offers real-time syncing, customizable templates, and integrations with popular tools. Taskade also has AI-powered features like smart due dates and natural language processing for better task management. | Proprietary | Paid |
| [Zapier](https://zapier.com/) | A popular web-based automation platform that connects various apps and services to automate workflows. It offers a wide range of pre-built integrations and allows users to create custom automation rules called "Zaps" without needing to write code. Zapier's AI capabilities include filtering, formatting, and transforming data between apps. | Proprietary | Paid |

<br>

## Chatbots and conversational AI

Generalist conversational AI tools (or chatbots) optimize daily work tasks by offering valuable information, automating repetitive processes, aiding content creation, and fostering collaboration, leading to improved productivity and efficiency.

> [!TIP]
> *Optimizing your interactions with chatbots through prompt engineering can significantly enhance their performance. Here's a useful [prompt engineering cheat sheet](https://medium.com/@mdsatriaalamshah/chatgpt-prompt-engineering-cheat-sheet-8ee73a81d2bc) to help you improve your LLM skills. For those who strive for more , this [awesome Course](https://learn.codesignal.com/preview/course-paths/16/prompt-engineering-for-everyone) form CodeSignal will make you a lot better at prompting.*
>
> To make it easy for you to get an **overview of this market**, we're providing a ***[thorough and regularly updated directory of all chatbot models](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/List-of-all-Models.md)***.
>
> If you're ready to dive deeper into these models, we'd be happy **to walk you through the process of selecting a model**. You can find our ***[detailed guide](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/run-local-llm-ollama-and-page-assist.md#find-the-llm-model-that-is-right-for-you)***.

| Model Familly                                       | Best Model                                                                       | Best Model Licensing | Organization   | Knowledge Cutoff | Pricing model |
|:----------------------------------------------------|:---------------------------------------------------------------------------------|:-------------:|:--------------:|:------------:|:-----------:|
| [ChatGPT](https://chat.openai.com/)                 | [GPT-4o](https://openai.com/index/hello-gpt-4o/)                                 | Proprietary   | OpenAI         | 2023-12      | Freemium |
| [Claude](https://claude.ai/)                        | [Claude 3 Opus](https://claude.ai/)                                              | Proprietary   | Anthropic      | 2023-08      | Freemium |
| [Gemini](https://gemini.google.com/)                | [Gemini 1.5 Pro](https://gemini.google.com/?hl=en)                               | Proprietary   | Google         | 2023-11      | Freemium |
| [Grok](https://github.com/xai-org/grok-1)           | [Grok-1](https://github.com/xai-org/grok-1)                                      | Proprietary   | 𝕏              | Online       | Freemium |
| [Mistral](https://mistral.ai/)                      | [Mistral Large](https://chat.mistral.ai/chat)                                    | Proprietary   | Mistral AI     | 2023-04      | Freemium |
| [MPT](https://huggingface.co/mosaicml)              | [MPT-30B-chat](https://huggingface.co/mosaicml/mpt-30b-chat)                     | Proprietary   | Perplexity AI  | Online       | Freemium |
| [Reka](https://www.reka.ai/)                        | [Reka Core](https://chat.reka.ai/auth/login)                                     | Proprietary   | Reka           | Online       | Free |
| [Yi](https://www.01.ai/)                            | [Yi-Large](https://www.01.ai/)                                                   | Proprietary   | 01.ai          | 2023-06      | Free |
|                                                     |                                                                                  |               |                |              |      |
| [Command-R](https://cohere.com/)                    | [Command R+](https://txt.cohere.com/command-r-plus-microsoft-azure/)             | Open          | Cohere         | 2023-03      | Free |
| [DBRX](https://www.databricks.com/)                 | [dbrx-instruct ](https://huggingface.co/databricks/dbrx-instruct)                | Open          | Databricks     | 2023-12      | Free |
| [DeepSeek](https://www.deepseek.com/)               | [DeepSeek-LLM-67B-Chat](https://huggingface.co/deepseek-ai/deepseek-llm-67b-chat)| Open          | Deepseek       | 2023-11      | Free     |
| [Dolphin](https://erichartford.com/dolphin)         | [dolphin-2.9.1-llama-3-70b](https://huggingface.co/cognitivecomputations/dolphin-2.9.1-llama-3-70b) | Open | Cognitive Computations | 2023-10 | Free |
| [Llama](https://github.com/facebookresearch/llama)  | [Llama-3-70b-Instruct](https://llama.meta.com/llama3/)                           | Open          | Meta           | 2023-12      | Free |
| [OLMo](https://huggingface.co/allenai/OLMo-7B)      | [Tulu-2-DP0-70B](https://huggingface.co/allenai/tulu-2-dpo-70b)                  | Open          | Allen AI       | 2023-02      | Free |
| [Openchat](https://github.com/imoneoi/openchat)     | [OpenChat-3.5-0106](https://huggingface.co/openchat/openchat-3.5-0106)           | Open          | Community      | 2024-01      | Free |
| [Phi](https://huggingface.co/microsoft)             | [Phi-3-medium-128k-instruct](https://huggingface.co/microsoft/Phi-3-medium-128k-instruct) | Open | Microsoft      | 2024-03      | Free |
| [Qwen](https://qwenlm.github.io/)                   | [Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct)             | Open          | Alibaba        | 2023-08      | Free |
| [Vicuna](https://huggingface.co/lmsys)              | [vicuna-33b-v1.3](https://huggingface.co/lmsys/vicuna-33b-v1.3)                  | Open          | LMSYS          | 2023-08      | Free |


### Chatbots Providers

> [!IMPORTANT]
> If you're concerned about **privacy issues related to cloud based LLM** tools or you want to experiment with chatbots check out this [practical guide](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/run-local-llm-ollama-and-page-assist.md) on **how to set up and run your own model on your local machine.**

#### Cloud-based Providers

| Tool             | Description                                                                                                                 | Pricing     | Models     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [AI21 Labs](https://www.ai21.com/) |  Known for their language models like Jurassic-1 Jumbo focused on quality, safety, and controllability. | Freemium | Jurassic-2 / Jamba |
| [Amazon Web Services (AWS)](https://aws.amazon.com/what-is/large-language-model/) | Offers models like Amazon CodeWhisperer for code generation and understanding through their SageMaker platform. | Paid |  CodeWhisperer |
| [Anthropic](https://www.anthropic.com/claude) | Known for their constitutional AI model Claude, focused on being helpful, harmless, and honest. | Freemium | Claude 3 (opus, sonnet..)    |
| [Cohere](https://cohere.com/) | Provides an enterprise AI platform with models like Cohere Generate for custom content creation. | Freemium | Command R and R+    |
| [Google Cloud](https://gemini.google.com/) |  Provides models like LaMBDA, PaLM, and Bard for language understanding, generation, and multimodal AI tasks. | Freemium | Gemini / PaLM |
| [Groq](https://groq.com/) | Specializes in high-performance AI inference with custom LPU (Language Processing Unit) hardware, offering models like Meta's Llama 3. | Freemium | Llama 3 / Mixtral / Gemma |
| [Hugging Face](https://huggingface.co/models) | The AI dedicated github, Offers a platform with many open-source models like BERT, GPT-Neo, and Llama for various AI tasks. | Free | Public (limited)|
| [OpenAI](chat.openai.com) | Offers models like GPT-3, GPT-4, DALL-E, and Whisper for natural language processing, image generation, and speech recognition. | Freemium | GPT3.5 / GPT4    |
| [Perplexity Labs](https://labs.perplexity.ai/) | An online platform that provides free access to various powerful open-source large language models (LLMs) for experimentation and use in a wide range of applications. | Free | Llama 3 / Mixtral / Gemma |

#### Local Providers

| Tool             | Description                                                                                                                 | OS     | Models     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [Enchanted](https://github.com/AugustDev/enchanted) | iOS and macOS app for chatting with private self hosted language models.| MacOS/IOS | Open sources Models |
| [Jan](https://jan.ai/) | Clean UI with useful features like system monitoring and LLM library.| All | Open sources Models. |
| [LM Studio](https://superagi.com/) |  Elegant UI with the ability to run every Hugging Face repository. | All | Open sources Models |
| [Ollama](https://ollama.com/) | Fastest when used on the terminal, and any model can be downloaded with a single command. | All | Open sources Models |

> [!IMPORTANT]
> **Having trouble choosing a model ?** I'm here to help you make an informed decision. [This dedicated section](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/run-local-llm-ollama-and-page-assist.md#find-the-llm-model-that-is-right-for-you) provides a comprehensive overview of **the best open-source and Proprietary models**, along with ***estimated performance metric.***

<br>


## Code Suggestions and Autocompletion

AI-powered code suggestion and autocompletion tools enhance developer productivity by offering real-time, context-aware code recommendations, minimizing errors, and streamlining the coding process.

| Tool       | Description                                                                                                           | Licence     | Pricing model |
|:-----------|-----------------------------------------------------------------------------------------------------------------------|:-----------:|:-------------:|
| [AskCodi](https://www.askcodi.com/)    | An AI-powered coding assistant that offers code suggestions, debugging help, and explanations for code snippets. | Proprietary |Freemium |
| [Blackbox](https://www.blackbox.ai/)   | An AI platform that helps businesses automate processes, make predictions, and optimize decision-making. | Proprietary |Free |
| [Boxy](https://codesandbox.io/blog/meet-boxy-ai-coding-assistant)       | An AI coding assistant by CodeSandbox providing real-time code suggestions and completions. | Proprietary |Freemium |
| [Codeium](https://codeium.com/)    | An AI-powered code completion tool that helps developers write code faster and more accurately. | Proprietary |Free |
| [CodeWhisperer](https://aws.amazon.com/codewhisperer/)    | Developed by Amazon, provide real-time code suggestions and completions. | Proprietary |Freemium |
| [Codium](https://www.codium.ai/)     | An AI-powered tool that analyze your code, docstring, and comments and suggests tests as you code. | Proprietary |Freemium |
| [Copilot](https://github.com/features/copilot) | Developed by GitHub and OpenAI, provide real-time code suggestions and completions. | Proprietary |Paid |
| [Continue](https://www.continue.dev/)     | An open-source autopilot for software development that enables developers to create their own AI code assistant within their integrated development environment (IDE) like VS Code or JetBrains IDEs. | Open |Free |
| [JetBrains AI](https://www.jetbrains.com/ai/) | JetBrains is working on integrating AI capabilities into their development tools. | Proprietary |Paid        |
| [Replit AI](https://replit.com/ai)  | A coding assistant and tutorial platform developed by Replit, offering code suggestions and explanations. | Proprietary |Freemium |
| [Tabnine](https://www.tabnine.com/)    | An AI-powered code completion tool that helps developers write code faster and more accurately. | Proprietary |Freemium |

> [!IMPORTANT]
> Concerned about **privacy issues** related to cloud based LLM tools or you want to **experiment with chatbots when coding** ? We've got you covered !
> 
> check out our **[tutorial](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/integrating-ai-models-into-ide.md)** to integrate Cloud-based AI providers like OpenAI, Anthropic, or Groq, or local model providers such as ollama, **directly into your coding environment**.
>
> **Having trouble choosing a model ?** I'm here to help you make an informed decision. [This dedicated section](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/integrating-ai-models-into-ide.md#models-for-coding) provides a comprehensive overview of **the best open-source and Proprietary models** for coding, along with ***estimated performance metric.***


<br>

## Data Analysis 

AI tools for data analysis automate routine tasks, identify patterns and trends, and provide intuitive visualizations, enabling analysts to extract valuable insights from complex data sets with ease and efficiency.

> [!CAUTION]
> **Exercise caution with fully automated analysis results, as errors and biases may occur. Use AI tools as a complement to human judgment for more reliable insights.**

| Tool             | Description                                                                                                                 | Licence     | Pricing     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [AskCSV](https://askcsv.com/) | An AI-powered tool that allows users to ask questions about CSV data files in natural language and receive answers. | Proprietary | Freemium    |
| [DataSquirrel](https://datasquirrel.ai/) | An AI-powered data extraction and analysis tool.                                                    | Proprietary | Freemium    |
| [Grapha AI](https://grapha.ai/) | An AI-powered platform for automating data analysis and generating insights.                                 | Proprietary | Freemium    |
| [Hal9](https://hal9.com/) | Data analytics leveraging generative AI to get insights from databases.                                            | Proprietary | Freemium    |
| [Julius](https://julius.ai/) | An AI-powered tool for automating data entry and document processing tasks.                                     | Proprietary | Freemium    |
| [Monitr](https://www.monitr.space/) | An AI-powered data extraction and analysis tool.                                                         | Proprietary | Freemium    |
| [Pi Exchange](https://www.pi.exchange/) | A platform for building and deploying AI models.                                                     | Proprietary | Paid        |
| [Research Studio](https://researchstudio.ai/)  | An AI-powered research assistant that helps users find, analyze, and summarize information.   | Proprietary | Paid        |
| [Rows AI](https://www.rows.com/) | An AI-powered spreadsheet tool that helps users automate data analysis and manipulation tasks.              | Proprietary | Freemium    |
| [Vizly](https://vizly.fyi/)  | A tool for creating interactive data visualizations.                                                            | Proprietary | Free        |

If you are using **Excel** or **Google Sheets**, you can benefit from AI tools that help you write formulas.  👇

| Tool                                             | Description                                                                                                                 | Licence     | Pricing     |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------|-------------|
| [Formulabot](https://formulabot.com/)           | A virtual assistant designed to streamline the process of creating Excel formulas by understanding natural language instructions. | Proprietary | Paid        |
| [GPTExcel](https://gptexcel.uk/)                | An AI tool designed to generate and explain Microsoft Excel and Google Sheets formulas efficiently.                            | Proprietary | Freemium    |
| [Sheety](https://sheety.ai/formula-generator)   | A tool designed to streamline the process of creating Google Sheets formulas using artificial intelligence.                  | Proprietary | Free        |

<br>

## Image Generation and Editing

AI tools for image generation, editing, and enhancement, offering text-to-image creation, filters, quality improvement, and multimedia capabilities for creative and professional projects.

> [!CAUTION]
> Use AI-generated images responsibly: **Always disclose that they were generated by AI.**
> Be mindful of **intellectual property rights.**

> [!TIP]
> *To get the most out of image generative AI models, it's important to refine your prompts and inputs. Check out this helpful [twitter/X account](https://twitter.com/nickfloats) to learn how to improve your skills and create more impressive results. By optimizing your prompts, you can unlock new levels of creativity and achieve your desired outcomes more effectively.*

### Image Generation

| Tool              | Description                                                                                                         | Licence     | Pricing     |
|:------------------|---------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [Craiyon](https://www.craiyon.com/) | An AI-powered platform for generating artistic images and animations.                             | Proprietary | Paid        |
| [Dall-E](https://openai.com/research/dall-e) | An AI model developed by OpenAI that generates images from textual descriptions.         | Proprietary | Paid|
| [Firefly](https://www.adobe.com/fr/products/firefly.html) | A creative AI tool for generating images, animations, and other visual content. | Proprietary | Paid |
| [Imagen 3](https://deepmind.google/technologies/imagen-3/) |  A high quality text-to-image model capable of producing images in various formats and styles. | Proprietary |  None (Preview) |
| [Lexica](https://lexica.art/) | An AI art platform that generates images from textual descriptions.                                     | Proprietary | Free |
| [Leonardo](https://leonardo.ai/) | An open-source AI model for generating images from textual descriptions.                             | Open        | Free |
| [Midjourney](https://www.midjourney.com/home) | A world-famous AI platform that generates images and visual content based on user input. | Proprietary| Paid |
| [Nightcafe](https://creator.nightcafe.studio/) | An open-source AI art platform that generates images from textual descriptions using deep learning models. | Open | Free |
| [Picasso](https://www.nvidia.com/en-us/gpu-cloud/picasso/) | An AI-powered platform for generating images and animations, developed by NVIDIA. | Proprietary | Paid |
| [Removebg](https://www.remove.bg/) | An online tool that allows users to automatically remove backgrounds from images.                  | Proprietary | Freemium    |
| [Stable diffusion](https://stability.ai/stable-image) | An open-source AI model for generating images from textual descriptions using diffusion-based generative models. | Open | Free |

> [!TIP]
> A convenient **local option for using image generation models** is now available. Please check out **[Fooocus](https://github.com/lllyasviel/Fooocus)** for more information.
### Image Editing

| Tool              | Description                                                                                                         | Licence     | Pricing     |
|:------------------|---------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [BRIA AI](https://huggingface.co/spaces/briaai/BRIA-RMBG-1.4) | An AI-powered model to automatically remove backgrounds from images.    | Open        | Free        |
| [Clarity AI](https://github.com/philz1337x/clarity-upscaler)  |AI Image Upscaler & Enhancer - free and open-source Magnific Alternative | Open        | Free        |
| [ImageFX](https://aitestkitchen.withgoogle.com/tools/image-fx) | An AI-powered tool for applying various image effects and filters.     | Proprietary | Paid |
| [Lensa](https://prisma-ai.com/lensa) | An AI-powered mobile app for editing and enhancing photos, particularly for portrait editing.    | Proprietary | Paid |
| [Luminar Neo](https://skylum.com/fr/luminar) | An AI-powered photo editing software developed by Skylum.                                | Proprietary | Paid |
| [Magnific AI](https://magnific.ai/) | an AI-powered image upscaler and enhancer designed for professionals and enthusiasts in photography, graphic design, digital art, and illustration. | Proprietary | Paid |
| [Pixlr](https://pixlr.com/) | An AI-powered online photo editing tool.                                                                  | Proprietary | Freemium |
| [Removebg](https://www.remove.bg/) | An online tool that allows users to automatically remove backgrounds from images.                  | Proprietary | Freemium    |

### Video Generation

| Tool              | Description                                                                                                         | Licence     | Pricing     |
|:------------------|---------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [Elai](https://elai.io/) | A video creation platform that enables users to produce  videos by inputting text that is then narrated by AI-generated avatars. | Proprietary | Paid |
| [Heygen](https://www.heygen.com/) | An innovative video platform that harnesses the power of generative AI to streamline the video creation process. | Proprietary | Paid |
| [Higgsfield](https://higgsfield.ai/) | A pioneering foundational model company that specializes in democratizing social media content creation through AI-powered video generation and editing tools. | Proprietary | None (Preview) |
| [Runway](https://runwayml.com/) | An AI-powered platform for creatives to use machine learning models in their workflows.               | Proprietary | Paid |
| [Sora](https://openai.com/sora) | An AI model developed by OpenAI for generating videos from textual descriptions.                      | Proprietary | Paid |
| [Synthesia](https://www.synthesia.io/) | A synthetic media generation AI tool to create AI-generated video content efficiently.         | Proprietary | Paid |
| [Veo](https://deepmind.google/technologies/veo/) | A generative video model developed by Google, capable of producing high-quality 1080p videos. | Proprietary | None (Preview) |
| [Vlogger](https://enriccorona.github.io/vlogger/) | A method for text and audio-driven talking human video generation from a single input image of a person. | Proprietary | None (Preview) |
| [Wombo](https://www.w.ai/) | An AI-powered mobile app for creating lip-syncing videos and other creative content.                       | Proprietary | Freemium |

<br>

## Language learning

AI-powered tools for language learning, providing personalized guidance and feedback.

| Tool                                              | Description                                                                                                                                                            | Licence       | Pricing    |
|:--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------:|:----------:|
| [Conversly](https://www.conversly.ai/)            | A language learning app that allows users to practice conversing and improve their speaking and listening skills in a new language.                                    | Proprietary   | Freemium   |
| [Duolingo max](https://blog.duolingo.com/duolingo-max/) |  New premium subscription tier from Duolingo that incorporates advanced AI technology, specifically OpenAI's GPT-4, to provide enhanced language learning features and exercises. | Proprietary   | Paid   |
| [Langotalk](https://www.langotalk.org/)           | An AI-powered language learning tool that helps users learn languages like Spanish, English, French, German, Dutch, or Italian.                                        | Proprietary   | Paid       |
| [Lingolette](https://lingolette.com/en)           | An AI-powered language learning tool that focuses on improving spoken and written fluency through interactive conversations and personalized lessons.                  | Proprietary   | Free       |
| [Proseable](https://www.proseable.com/)           | An AI-powered language learning tool designed to help users improve their conversational skills and fluency in a new language through interactive practice and personalized feedback.  | Proprietary | Freemium   |

<br>

## Music and Audio Generation

### Music Generation

AI tools for music generation use machine learning to create original compositions in various styles, aiding musicians and generating customizable background music.

| Tool                                              | Description                                                                                                                                                            | Licence       | Pricing    |
|:--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------:|:----------:|
| [Jukebox](https://jukebox.openai.com/)            | A generative AI model developed by OpenAI that can create original music, including rudimentary singing, in a variety of genres and artist styles.                     | Proprietary   | None (Research)   |
| [Magenta](https://magenta.tensorflow.org/)        |  AI  project developed by Google that explores the use of machine learning as a tool for creative applications, particularly in music and art.                         | Open          | Free       |
| [Mubert](https://mubert.com/)                     |  A generative AI platform that allows users to create and stream original, AI-generated music and audio.                                                               | Proprietary   | Freemium   |
| [MuseNet](https://openai.com/research/musenet)    |  An AI model developed by OpenAI that can generate original 4-minute musical compositions with up to 10 different instruments.                                         | Proprietary   | None (Research)   |
| [Stable Audio](https://stability.ai/stable-audio) |  A generative AI system developed by Stability AI for creating high-quality audio and music.                                                                           | Proprietary   | Freemium   |
| [Suno](https://suno.com/)                         |  A cutting-edge AI-powered music generator that lets users create custom songs in various genres using text prompts.                                                   | Proprietary   | Free       |


### Text to speech

Text-to-speech AI tools convert written text into natural-sounding speech, improving accessibility and creating engaging experiences. They use deep learning algorithms to synthesize speech with customizable features such as voice, accent, and speaking style.

| Tool                                                       | Description                                                                                                 | Licence     | Pricing   |
|:-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|:-----------:|:---------:|
| [Audioread](https://audioread.com/)                        | A transformative tool that converts text into lifelike speech.                                              | Proprietary | Paid      |
| [Bark](https://github.com/suno-ai/bark)                    | A groundbreaking text-to-audio model developed by Suno, leveraging GPT-style models.                        | Open        | Free      |
| [Coqui](https://github.com/coqui-ai/TTS)                   | A pioneering project that focused on advancing generative voice technology.                                 | Open        | Free      |
| [Eleven Labs](https://elevenlabs.io/)                      | Industry leader proprietary tool for generating speech from text using deep learning.                       | Proprietary | Freemium  |
| [Listnr](https://listnr.ai/)                               | A cutting-edge AI voice generator that seamlessly converts text into natural-sounding speech.               | Proprietary | Freemium  |
| [MeloTTS](https://github.com/myshell-ai/MeloTTS)           | An open-source text-to-speech tool that uses deep learning to generate high-quality speech synthesis.       | Open        | Free      |
| [Metavoice](https://github.com/metavoiceio/metavoice-src)  | A groundbreaking model that has been developed to create human-like speech with emotional nuances.          | Proprietary | Free      |
| [Murf](https://murf.ai/)                                   | A n innovative voice generator tool that revolutionizes the process of creating voiceovers.                 | Proprietary | Freemium  |
| [SpeechT5](https://github.com/microsoft/SpeechT5/)         | A cutting-edge model in speech synthesis and natural language processing that offers a unified approach to various speech-related tasks. | Proprietary | Free |
| [Speechki](https://speechki.org/)                          | An advanced AI Realistic Voice Generator that offers over 1100 voices in more than 80 languages.            | Proprietary | Freemium  |
| [Unrealspeech](https://unrealspeech.com/)                  | A text-to-speech software that stands out for its human-like audio output, providing a superior listening experience. | Proprietary | Freemium |
| [VoiceCraft](https://jasonppy.github.io/VoiceCraft_web/)   | A state-of-the-art text-to-speech (TTS) model that can perform zero-shot speech editing and TTS on diverse audio data. | Open | Free |

<br>

## Productivity

### Versatile Productivity tools

Enhance productivity and accuracy across domains with these versatile AI tools. (yes, These tools could fit into multiple categories.)
   
| Tool                                                       | Description                                                                                                 | Licence     | Pricing   |
|:-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|:-----------:|:---------:|
| [BeeyondAI](https://www.beeyondai.com/)                    | AI digital assistant that offers a wide range of tools to enhance productivity and creativity across various aspects of life. | Proprietary | Paid      |
| [Copilot](https://www.microsoft.com/fr-fr/microsoft-copilot) |  An AI assistant developed by Microsoft, designed to enhance productivity and creativity for users.       | Proprietary | Freemium  |
| [Hyperis](https://hyperis.com/welcome)                     | AI-driven assistant app designed to help users prioritize tasks, focus on important work, and boost creativity. | Proprietary | Freemium  |
| [KPU](https://maisa.ai/)                                   | A revolutionary Knowledge Processing Unit by Maisa AI that enhances the reasoning capabilities of large language models. | Proprietary | None (Preview) |
| [Odyssey](https://odysseyapp.io/)                          |a macOS application that allows users to visually connect and run various AI models and other tools without coding, making it a versatile platform for creative and automation tasks.| Proprietary | Paid |
| [Ultra-Attention](https://ultra-attention.com/)            |  AI-powered software solution designed specifically for freelancers and remote workers to help them conquer distractions, boost focus, and enhance productivity. | Proprietary | Freemium  |

### Meeting transcription and summaries

AI meeting transcription and summarization tools automatically transcribe and summarize meetings, helping teams stay organized and informed. They use NLP and machine learning to identify key topics and action items, saving time and reducing errors.

| Tool                                                       | Description                                                                                                                                             | Licence     | Pricing  |
|:-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------:|:--------:|
| [Airgram](https://www.airgram.io/)                         | Industry leader proprietary tool for generating speech from text using deep learning.                                                                   | Proprietary | Freemium |
| [Fireflies](https://fireflies.ai/)                         | An AI Meeting Assistant tool that offers a range of features to enhance meeting productivity.                                                           | Proprietary | Freemium |
| [Otter](https://otter.ai/)                                 | AI Meeting Assistant tool that transcribes meetings in real-time, records audio, captures slides, extracts action items, and generates AI meeting summaries | Proprietary | Freemium |
| [Tactiq](https://tactiq.io/)                               | A powerful tool that provides live transcriptions and insightful AI summaries for meetings conducted on platforms like Google Meet, Zoom, and MS Teams. | Proprietary | Freemium |
| [Tldv](https://tldv.io/)                                   | A powerful tool designed to record, transcribe, and share online meetings on platforms like Google Meet and Zoom.                                       | Proprietary | Freemium |

### Presentation slides

AI presentation tools enable users to create professional slides with ease, offering automatic layout, design, and content suggestions for impactful presentations.

| Tool                                              | Description                                                                                                                                                            | Licence       | Pricing    |
|:--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------:|:----------:|
| [Gamma](https://gamma.app/)                       | An innovative tool that harnesses artificial intelligence to create professional presentations, documents, and webpages swiftly and efficiently.                       | Proprietary   | Freemium   |
| [MagicSlides](https://www.magicslides.app/)       | A powerful tool that leverages artificial intelligence to create professional presentations quickly and effortlessly.                                                  | Proprietary   | Freemium   |
| [PlusAI](https://www.plusdocs.com/)               |  An advanced AI tool that integrates with Google Slides and Google Docs to assist users in creating professional presentations and well-written documents efficiently. | Proprietary   | Paid       |
| [SlidesPilot](https://www.slidespilot.com/)       | An innovative tool designed to streamline the creation of professional and visually appealing presentation slides.                                                     | Proprietary   | Freemium   |

### Audio and Video transcription and summaries

AI audio and video transcription and summarization tools use NLP and computer vision to quickly and accurately extract insights from video content. They automate the transcription and summary process, saving time and reducing errors, so users can focus on analysis and interpretation.

| Tool                                                       | Description                                                                                                 | Licence     | Pricing   |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|:-----------:|:---------:|
| [Eightify](https://eightify.app/)                          | A powerful tool that utilizes YouTube AI technology to summarize videos quickly, providing users with key ideas in seconds. | Proprietary | Free      |
| [Exemplary AI](https://exemplary.ai/)                      | A cloud-based tool that harnesses Artificial Intelligence (AI) and LLMs to offer transcription solutions.                   | Proprietary | Freemium  |
| [Riverside](https://riverside.fm/)                         | An online studio that specializes in high-quality podcast and video recording and editing.                                  | Proprietary | Freemium  |
| [SolidPoint](https://solidpoint.ai/)                       | A range of tools that leverage AI technology to enhance productivity and efficiency in various tasks. One of its key features is the Summarize tool. | Proprietary | Free |
| [Summarize.tech](https://www.summarize.tech/)              | An AI-powered tool that automatically generates summaries of long videos from YouTube.                                      | Proprietary | Freemium  |
| [Summify](https://summify.io/)                             | A powerful tool that efficiently condenses lengthy videos into concise and informative summaries.                           | Proprietary | Freemium  |
| [Voxweave](https://voxweave.xyz/)                          | An innovative AI-powered tool that revolutionizes the interaction with YouTube videos by transforming them into concise summaries. | Proprietary | Freemium  |
| [WavoAI](https://wavoai.com/)                              | An AI-powered tool that provides accurate transcriptions and insights from audio recordings.                                | Proprietary | Freemium  |


### Website building

AI-powered website builders leverage machine learning and natural language processing to simplify website creation and deployment. They automate the design, development, and deployment process, enabling users to quickly build and launch custom websites without extensive coding knowledge, and focus on content creation


| Tool                                                       | Description                                                                                                 | Licence     | Pricing   |
|:-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------|-----------|
| [10web](https://10web.io/ai-website-builder/)              | An AI-powered website building platform that allows users to create websites quickly and easily using artificial intelligence. | Proprietary | Paid      |
| [B12](https://www.b12.io/)                                 | An AI-powered website builder platform designed specifically for professional service providers and businesses. | Proprietary | Paid      |
| [Framer](https://www.framer.com/features/ai/)              | A comprehensive web design and prototyping tool that combines visual design, interactive prototyping, CMS capabilities, AI-powered tools, and collaboration features into a single platform. | Proprietary | Freemium  |
| [Hostinger](https://www.hostinger.com/website-builder)     | A powerful tool that allows users to create a fully functional website using artificial intelligence in just a few simple steps. | Proprietary | Paid      |
| [Limecube](https://www.limecube.co/)                       | An AI-driven, code-free solution for small businesses to quickly build a professional, on-brand website .   | Proprietary | Paid      |
| [Odoo](https://www.odoo.com/app/website)                   | Odoo's AI Website Builder aims to empower businesses of all sizes to easily build a professional, feature-rich online presence leveraging advanced AI capabilities, without any coding or design expertise required. | Proprietary | Free      |
| [Relume](https://www.relume.io/)                           | An AI-powered website building platform that aims to streamline and accelerate the design process for marketing websites. | Proprietary | Freemium  |
| [Studio.design](https://studio.design/)                    | An AI-powered web design tool that aims to revolutionize the website building process for designers and creatives. | Proprietary | Freemium  |
| [Uimagic](https://www.uimagic.io/)                         | A powerful AI-driven web design solution that aims to streamline the website creation process by generating tailored designs, content, and visuals using advanced AI capabilities. | Proprietary | Freemium  |
| [Webflow](https://webflow.com/)                            | A powerful visual web development platform that allows users to design, build, and launch responsive websites without writing code.| Proprietary | Freemium  |
| [Wix](https://www.wix.com/ai-website-builder)              | Wix AI Website Builder utilizes advanced artificial intelligence and natural language processing to automatically generate a complete, professional website tailored to the user's specific business needs and preferences. | Proprietary | Freemium  |

<br>

<h3 align="center">  Any kind of positive contribution to AIEnhancedWork is welcome ! </h3>
<h4 align="center">  A ⭐️ to AIEnhancedWork is must as a motivation booster. </h4>
