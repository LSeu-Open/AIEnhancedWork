<div align="center"> 

<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/AIEnhancedWork.png">

<br>
<br>

***A curated index of impactful AI tools and models, that emphasizes technical merit, practical utility and Prioritizing open-source.***

**Effective AI use requires understanding capabilities, limitations, and bias mitigation strategies.**

<br>

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg?style=flat)](./LICENSE.md)

<br>

[⬅️ Back to the Main Page](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/README.md) 

</div>

<br>

# Table of contents

- [Language Only Large Language Models](#language-only-large-language-models)
  - [Advanced Language and Reasoning LLMs](#advanced-language-and-reasoning-llms)
    - [Open source Models](#open-source-models)
    - [Proprietary Models](#proprietary-models)
    - [Finetuned LLMs](#finetuned-llms)
      - [Astrophysics](#astrophysics)
      - [Function calling](#function-calling)
      - [Language Specific](#language-specific)
      - [Math](#math)
      - [Role Play](#role-play)
      - [Uncensored](#uncensored)
    - [LLM Providers](#llm-providers)
      - [Cloud-based LLM Providers](#cloud-based-llm-providers)
      - [Local LLM Providers](#local-llm-providers)
      - [LLM Inference Engines](#llm-inference-engines)
  - [Multimodal Language Models](#multimodal-Language-models) 
    - [Vision Language Models](#vision-language-models)
      - [Open source VLMs](#open-source-vlms)
      - [Proprietary VLMs](#proprietary-vlms)
    - [Omni Large Language Models](#omni-large-language-models)

<br>

# Foundation Models

## Language Only Large Language Models

Large Language Models (LLMs) are **artificial intelligence systems trained on large amounts of text data to recognize patterns and generate human-like language.**

This overview focuses on instruction-tuned models to ensure a fair comparison. Fine-tuned variants are excluded due to their vast number and constant development, but you can find more information in the [Fine-tuned Models](#finetuned-llms) section.

> [!NOTE]
> Whether you're a beginner or an expert, our [tutorial](./Tutorials/how-to-run-llms-on-your-machine.md) provides step-by-step guidance for deploying LLMs on your own machine using tools tailored to your skill level.

> [!IMPORTANT]
> Models are ranked using our [LLM scoring framework](https://github.com/LSeu-Open/LLMScoreEngine), which synthesizes performance benchmarks, human preference evaluations, and technical specifications. A higher score indicates better overall performance.
>
> **Note that scores provide a relative ranking within each model's size category. A higher score does not guarantee superior performance on any specific task or in every language.**
>   
> We have recently added a multilinguality indicator to the tables below, including the number of officially supported languages.
>
> Most models are trained on data encompassing diverse languages, but **you may see varying degrees of performance degradation depending on the language being processed.**

### Advanced Language and Reasoning LLMs

#### Open source Models 

***Large-scale models (70+ billion parameters)*** : These require substantial amounts of RAM and GPU memory, making local installation impractical for most users. As a result, these models are typically deployed on cloud-based platforms that provide the necessary computational resources.

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (v0.5.2) | [Context Window](https://research.ibm.com/blog/larger-context-window) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Multilinguality |
|:------------------:|:---------------------------------------------------------------------------------|:--------------:|:------------:|:------------------:|:----:|:-------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | **[DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528)** | **685B** | **75.96** | **128K** | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Perplexity.svg" alt="Perplexity" width="200" height="20" />](https://www.perplexity.ai) | [R1-1776](https://huggingface.co/perplexity-ai/r1-1776) | 685B | 74.35 | 128K | ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) | 235B | 73.83 | 131K | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | **[119](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen3-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) | 685B | 72.45 | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/MiniMax.svg.svg" alt="MiniMax" width="200" height="20" />](https://www.minimaxi.com/en) | [MiniMax-M1](https://huggingface.co/MiniMaxAI/MiniMax-M1-80k) | 456B | 71.93 | 1M | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Tencent.svg" alt="Tencent" width="200" height="20" />](https://github.com/Tencent/) | [Hunyuan-Large](https://huggingface.co/tencent/Tencent-Hunyuan-Large) | 389B | 70.99 | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Tencent.svg" alt="Tencent" width="200" height="20" />](https://github.com/Tencent/) | [Hunyuan-80B-A13B-Instruct](https://huggingface.co/tencent/Hunyuan-A13B-Instruct) | 80B | 68.56 | 256K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  | [Llama-3_1-Nemotron-Ultra-253B-v1](https://huggingface.co/nvidia/Llama-3_1-Nemotron-Ultra-253B-v1) | 253B | 68.04 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/MiniMax.svg.svg" alt="MiniMax" width="200" height="20" />](https://www.minimaxi.com/en) | [MiniMax-Text-01](https://huggingface.co/MiniMaxAI/MiniMax-Text-01) | 456B | 65.72 | 4M | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | 402B | 62.29 | 1M | ❌ | **[12](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-4)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/DeepCogito.svg" alt="DeepCogito" width="200" height="20" />](https://www.deepcogito.com/research/cogito-v1-preview) | [Cogito-v1-preview-llama-70B](https://huggingface.co/deepcogito/cogito-v1-preview-llama-70B) | 70B | 60.12 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | 70B | 59.06 | 128K | ❌ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | [Mixtral-8x22B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) | 141B | 57.96 | 65k | ❌ | **[5](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#mixtral-8x22b)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B) | 70.6B | 57.84 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) | [Command A](https://huggingface.co/CohereForAI/c4ai-command-a-03-2025) | 111B | 57.10 | 256k | ❌ | **[23](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#command-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Nexusflow.svg" alt="Nexuflow" width="200" height="20" />](https://nexusflow.ai/) |  [Athene-V2-Chat](https://huggingface.co/Nexusflow/Athene-V2-Chat) | 70B |  56.68  | 131K |  ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-3.1-405B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct) | 405B | 56.37 | 128K | ❌ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | 109B | 55.48 | 10M | ❌ | **[12](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-4)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/AntGroup.svg" alt="AntGroup" width="200" height="20" />](https://github.com/inclusionAI)| [Ling-plus](https://huggingface.co/inclusionAI/Ling-plus) | 293B | 55.05 | 64k  | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/rednote.svg" alt="Rednote" width="200" height="18" />](https://github.com/rednote-hilab/dots.llm1) | [Dots.llm1](https://huggingface.co/rednote-hilab/dots.llm1.inst) | 143B | 55.23 | 128k | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/databricks.svg" alt="databricks" width="200" height="20" />](https://www.databricks.com) | [Dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct) | 132B | 52.69 | 33k | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | [Mistral Large 2](https://huggingface.co/mistralai/Mistral-Large-Instruct-2411)  | 123B | 51.71  | 128K | ❌ | **[13](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#mistral-large)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) | [Command R+](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024) | 104B | 44.18 | 128k | ❌ | **[23](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#command-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Baidu.svg" alt="Baidu" width="200" height="20" />](https://ernie.baidu.com/) | [ERNIE-4.5-300B-A47B-PT](https://huggingface.co/baidu/ERNIE-4.5-300B-A47B-PT) | 300B | **Incoming** | 131K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<Intervitens Inc](https://huggingface.co/IntervitensInc) | [Pangu-pro](https://huggingface.co/IntervitensInc/pangu-pro-moe-model) | 72B | **Incoming** | ?K | ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

***Mid-sized models (14+ billion parameters)*** :  These models are suitable for local deployment on high-end workstations. However, such deployments require a significant hardware investment, including a powerful GPU (24–32 GB of VRAM) and related components, typically resulting in total costs exceeding $3,000 (or equivalent).

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (v0.5.2) | [Context Window](https://research.ibm.com/blog/larger-context-window) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Multilinguality |
|:------------------:|:---------------------------------------------------------------------------------|:--------------:|:------------:|:------------------:|:----:|:-------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | **[Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)** | **32B** | **70.84** | **131K** | [Hybrid](https://qwenlm.github.io/blog/qwen3/) |  **[119](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen3-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) | 30.5B | 68.82 | 131K | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | **[119](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen3-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B) | 32B | 65.99 | 131K | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  | [Llama-3_3-Nemotron-Super-49B-v1](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1) | 49B | 65.21 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)  | [GLM-Z1-32B-0414](https://huggingface.co/THUDM/GLM-Z1-32B-0414) | 32.3B | 65.28 | 132K | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/DeepCogito.svg" alt="DeepCogito" width="200" height="20" />](https://www.deepcogito.com/research/cogito-v1-preview) | [Cogito-v1-preview-qwen-32B](https://huggingface.co/deepcogito/cogito-v1-preview-qwen-32B) | 32.3B | 61.79 | 132K | ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon-H1-34B-Instruct](https://huggingface.co/tiiuae/Falcon-H1-34B-Instruct) | 34B | 61.61 | 256k | ❌ | **[18](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#falcon-h1)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | [Magistral-Small-2506](https://huggingface.co/mistralai/Magistral-Small-2506) | 23.9B | 61.31 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#magistral-small-and-medium)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) | 27B | 61.06 | 128k | ❌ | **[140+](https://ai.google.dev/gemma/docs/core#multilingual)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-3.5-32B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-32B-Instruct) | 32B | 59.64 | 32k  | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/kr.svg" alt="korea" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | [Mistral-Small-3.2](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506) | 23.9B | 59.95 | 128K | ❌ | **[11](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#mistral-small)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B) | 32B | 59.35 | 132K | ✔️ | **[29](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen2-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)  | [GLM-4-32B-0414](https://huggingface.co/THUDM/GLM-4-32B-0414) | 32.3B | 58.88 | 132K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | [Mistral-Small-3.1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) | 23.9B | 58.35 | 128K | ❌ | **[11](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#mistral-small)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Reka.svg" alt="Reka" width="200" height="20" />](https://www.reka.ai/) | [Reka Flash 3](https://huggingface.co/RekaAI/reka-flash-3) | 21B | 57.02 | 128K |✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-Deep-32B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-32B) | 32B | 56.23 | 32k  | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/kr.svg" alt="korea" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/ServiceNow.svg" alt="Service Now" width="200" height="20" />](https://www.servicenow.com/) | [Apriel-Nemotron-15b-Thinker](https://huggingface.co/ServiceNow-AI/Apriel-Nemotron-15b-Thinker) | 15B | 55.33 | 32K | ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenThoughts.svg" alt="Open Thoughts" width="200" height="20" />](https://www.open-thoughts.ai/) | [OpenThinker-32B](https://huggingface.co/open-thoughts/OpenThinker-32B) | 32B | 54.94 | 132K | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/AntGroup.svg" alt="AntGroup" width="250" height="25" />](https://github.com/inclusionAI)| [Ling-lite-1.5](https://huggingface.co/inclusionAI/Ling-lite-1.5) | 16.8B | 54.23 | 64k  | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />   |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   | [OLMo-2-0325-32B-Instruct](https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct) | 32B | 52.80 | 32k  | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Cohere.svg" alt="cohere" width="200" height="20" />](https://cohere.com/) | [Command R](https://cohere.com/blog/command-r) | 32.3B | 37.77 | 128K | ❌ | **[23](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#command-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Baidu.svg" alt="Baidu" width="200" height="20" />](https://ernie.baidu.com/) | [ERNIE-4.5-21B-A3B-PT](https://huggingface.co/baidu/ERNIE-4.5-21B-A3B-PT) | 21B | **Incoming** | 131K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

***Small models (7B+ parameters)*** :  These are lightweight and easy to deploy on standard machines, offering wider accessibility. They typically require a mid-range consumer setup, including a GPU (8–16 GB of VRAM) and related components, with costs generally ranging from $1,000 to $2,000 (or equivalent).

##### Small models (10B to <14B parameters)

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (v0.5.2) | [Context Window](https://research.ibm.com/blog/larger-context-window) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Multilinguality |
|:------------------:|:---------------------------------------------------------------------------------|:--------------:|:------------:|:------------------:|:----:|:-------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | **[Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B)** | **14B** | **68.66** | **131K** | [Hybrid](https://qwenlm.github.io/blog/qwen3/) |  **[119](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen3-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/) | [Phi-4-reasoning-plus](https://huggingface.co/microsoft/Phi-4-reasoning-plus) | 14B | 62.91 | 32K | ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/) | [Phi-4](https://huggingface.co/microsoft/phi-4) | 14B | 62.77 | 16k | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/) | [Phi-4-reasoning](https://huggingface.co/microsoft/Phi-4-reasoning) | 14B | 60.10 | 32K | ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it) | 12B | 59.89 | 128k | ❌ | **[140+](https://ai.google.dev/gemma/docs/core#multilingual)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/DeepCogito.svg" alt="DeepCogito" width="200" height="20" />](https://www.deepcogito.com/research/cogito-v1-preview) | [Cogito-v1-preview-qwen-14B](https://huggingface.co/deepcogito/cogito-v1-preview-qwen-14B) | 14B | 59.15 | 132K | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) | 14B | 54.17 | 132K | ✔️ | **[29](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen2-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon3-10B-Instruct](https://huggingface.co/tiiuae/Falcon3-10B-Instruct) | 10B | 53.96 | 32k | ❌ | **[4](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#falcon-3)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   |  [OLMo-2-1124-13B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct) | 13B | 48.80 | 4k  | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |

##### Small models (7B to <10B parameters)

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (v0.5.2) | [Context Window](https://research.ibm.com/blog/larger-context-window) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Multilinguality |
|:------------------:|:---------------------------------------------------------------------------------|:--------------:|:------------:|:------------------:|:----:|:-------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | **[DeepSeek-R1-0528-Qwen3-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B)** | **8B** | **65.03** | **128K** | ✔️ |  **[119](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen3-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | 8B | 64.22 | 131K | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | **[119](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen3-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-3.5-7.8B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct) | 7.8B | 62.49 | 32k  | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/kr.svg" alt="korea" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenBMB.svg" alt="OpenBMB" width="200" height="20" />](https://www.openbmb.cn/) | [MiniCPM4-8B](https://huggingface.co/openbmb/MiniCPM4-8B) | 8B | 58.15 | 32K  | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) | 8B | 52.86 |  128K | ❌ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)  | [GLM-Z1-9B-0414](https://huggingface.co/THUDM/GLM-Z1-9B-0414) | 9B | 53.03 | 132K | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/IBM.svg" alt="ibm" width="200" height="20" />](https://github.com/ibm-granite/) | [Granite-3.3-8b-instruct](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct) | 8B | 52.03 | 128k | ❌ | **[12](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#ibm-granite-models)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM) | [Internlm3-8b-instruct](https://huggingface.co/internlm/internlm3-8b-instruct) | 8B | 52.32 | 300K  | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B) | 7B | 52.53 | 128K | ✔️ | **[29](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen2-family)**|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Xiaomi.svg" alt="Xiaomi" width="200" height="20" />](https://www.mi.com/global/) | [MiMo-7B-RL](https://huggingface.co/XiaomiMiMo/MiMo-7B-RL) | 7B | 52.44 | 32K | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)  | [GLM-4-9B-0414](https://huggingface.co/THUDM/GLM-4-32B-0414) | 9B | 52.20 | 132K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  | [Llama-3.1-Nemotron-Nano-8B-v1](https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1) | 8B | 51.26 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon-H1-7B-Instruct](https://huggingface.co/tiiuae/Falcon-H1-7B-Instruct) | 7B | 51.13 | 256k | ❌ | **[18](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#falcon-h1)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-Deep-7.8B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-7.8B) | 7.8B | 50.27 | 32k | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/kr.svg" alt="korea" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | [Ministral-8B-Instruct](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) | 8B | 49.62 | 128K | ❌ |  **[10](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#ministral)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   | [OLMo-2-1124-7B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct) | 7B | 49.01 | 4k  | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/DeepCogito.svg" alt="DeepCogito" width="200" height="20" />](https://www.deepcogito.com/research/cogito-v1-preview) | [Cogito-v1-preview-llama-8B](https://huggingface.co/deepcogito/cogito-v1-preview-llama-8B) | 8B | 48.90 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) | 8B | 48.90 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Kakao.svg" alt="Kakao" width="220" height="22" />](https://www.kakaocorp.com/page/) | [Kanana-1.5-8b-instruct-2505](https://huggingface.co/kakaocorp/kanana-1.5-8b-instruct-2505) | 8B | 47.30 | 32k  | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/kr.svg" alt="korea" width="20" height="15" />  |
| [Polaris Project](https://huggingface.co/POLARIS-Project) | [Polaris-7B-Preview](https://huggingface.co/POLARIS-Project/Polaris-7B-Preview) | 7B | **Incoming** | 128k  | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

***Tiny models (under 7B parameters)*** : Designed for broad compatibility, these models run effectively on older or less powerful machines, making them accessible to a wider range of users. They typically require only 6–8 GB of RAM and can be deployed across a wide range of standard consumer hardware setups.

##### Tiny models (3B to <7B parameters)

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (v0.5.2) | [Context Window](https://research.ibm.com/blog/larger-context-window) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Multilinguality |
|:------------------:|:---------------------------------------------------------------------------------|:--------------:|:------------:|:------------------:|:----:|:-------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | **[Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)** | **4B** | **54.46** | **131K** | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | **[119](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen3-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenBMB.svg" alt="OpenBMB" width="200" height="20" />](https://www.openbmb.cn/) | [MiniCPM3-4B](https://huggingface.co/openbmb/MiniCPM3-4B) | 4B | 52.62  | 32K  | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it) | 4B | 50.53 | 128k | ❌ | **[140+](https://ai.google.dev/gemma/docs/core#multilingual)** |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  | [Llama-3.1-Nemotron-Nano-4B-v1.1](https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-4B-v1.1) | 4B | 49.29 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon3-3B-Instruct](https://huggingface.co/tiiuae/Falcon3-3B-Instruct) | 3B | 48.71 | 32k | ❌ | **[4](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#falcon-3)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) | 3B | 46.37 | 128K | ❌ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/DeepCogito.svg" alt="DeepCogito" width="200" height="20" />](https://www.deepcogito.com/research/cogito-v1-preview) | [Cogito-v1-preview-llama-3B](https://huggingface.co/deepcogito/cogito-v1-preview-llama-3B) | 3B | 45.95 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon-H1-3B-Instruct](https://huggingface.co/tiiuae/Falcon-H1-3B-Instruct) | 3B | 42.79 | 128k | ❌ | **[18](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#falcon-h1)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/ServiceNow.svg" alt="Service Now" width="200" height="20" />](https://www.servicenow.com/)  | [Apriel-5B-Instruct](https://huggingface.co/ServiceNow-AI/Apriel-5B-Instruct) | 5B | 42.55 | 32K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3n-E4B-it-preview](https://huggingface.co/google/gemma-3n-E4B-it-litert-preview) | [E4B](https://ai.google.dev/gemma/docs/gemma-3n#parameters) | 35.75 | 32k | ❌ | **[140+](https://ai.google.dev/gemma/docs/core#multilingual)** |
| [Polaris Project](https://huggingface.co/POLARIS-Project) | [Polaris-4B-Preview](https://huggingface.co/POLARIS-Project/Polaris-4B-Preview) | 4B | **Incoming** | 131k  | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |

##### Tiny models (under 3B parameters)

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (v0.5.2) | [Context Window](https://research.ibm.com/blog/larger-context-window) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Multilinguality |
|:------------------:|:---------------------------------------------------------------------------------|:--------------:|:------------:|:------------------:|:----:|:-------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | **[EXAONE-3.5-2.4B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct)** | **2.4B** | **54.48** | **32k** | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/kr.svg" alt="korea" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | 1.7B | 49.20 | 131K | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | **[119](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen3-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/LG.svg" alt="LG" width="200" height="20" />](https://www.lgresearch.ai/) | [EXAONE-Deep-2.4B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-2.4B) | 2.4B | 48.63 | 32k | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/kr.svg" alt="korea" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/IBM.svg" alt="ibm" width="200" height="20" />](https://github.com/ibm-granite/) | [Granite-3.3-2b-instruct](https://huggingface.co/ibm-granite/granite-3.3-2b-instruct) | 2B | 47.77 | 128k | ❌ | **[12](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#ibm-granite-models)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenBMB.svg" alt="OpenBMB" width="200" height="20" />](https://www.openbmb.cn/) | [MiniCPM4-0.5B](https://huggingface.co/openbmb/MiniCPM4-0.5B) | 0.5B | 45.93 | 32K  | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon-H1-1.5B-Deep-Instruct](https://huggingface.co/tiiuae/Falcon-H1-1.5B-Deep-Instruct) | 1.5B | 42.93 | 128k | ❌ | **[18](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#falcon-h1)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon3-1B-Instruct](https://huggingface.co/tiiuae/Falcon3-1B-Instruct) | 1B | 42.16 | 8k | ❌ | **[4](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#falcon-3)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Kakao.svg" alt="Kakao" width="220" height="22" />](https://www.kakaocorp.com/page/) | [Kanana-1.5-2.1b-instruct-2505](https://huggingface.co/kakaocorp/kanana-1.5-2.1b-instruct-2505) | 2.1B | 40.92 | 32k  | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/kr.svg" alt="korea" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon-H1-1.5B-Instruct](https://huggingface.co/tiiuae/Falcon-H1-1.5B-Instruct) | 1.5B | 39.52 | 128k | ❌ | **[18](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#falcon-h1)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/) | [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) | 1B | 37.97 |128K | ❌ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) | 1.5B | 36.21 | 128K | ✔️ | **[29](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen2-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)   | [OLMo-2-0425-1B-Instruct](https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct) | 1B | 34.33 | 4k | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it) | 1B | 34.29 | 32k | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3n-E2B-it-preview](https://huggingface.co/google/gemma-3n-E2B-it-litert-preview) | [E2B](https://ai.google.dev/gemma/docs/gemma-3n#parameters) | 32.49 | 32k | ❌ | **[140+](https://ai.google.dev/gemma/docs/core#multilingual)**|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon-H1-0.5B-Instruct](https://huggingface.co/tiiuae/Falcon-H1-0.5B-Instruct) | 0.5B | 33.57 | 16k | ❌ | **[18](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#falcon-h1)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | 0.6B | 32.05 | 131K | [Hybrid](https://qwenlm.github.io/blog/qwen3/) | **[119](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#qwen3-family)** |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Baidu.svg" alt="Baidu" width="200" height="20" />](https://ernie.baidu.com/) | [ERNIE-4.5-0.3B-PT](https://huggingface.co/baidu/ERNIE-4.5-0.3B-PT) | 0.3B | **Incoming** | 131K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |

<br>

<details>
<summary>✳️ <b>Bitnet Models</b></summary>

<br>

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (v0.5.2) | [Context Window](https://research.ibm.com/blog/larger-context-window) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Multilinguality |
|:------------------:|:---------------------------------------------------------------------------------|:--------------:|:------------:|:------------------:|:----:|:-------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon-E-3B-Instruct](https://huggingface.co/tiiuae/Falcon-E-3B-Instruct) | 3B | 30.72 | 32k | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TII.svg" alt="TII" width="200" height="20" />](https://www.tii.ae/) | [Falcon-E-1B-Instruct](https://huggingface.co/tiiuae/Falcon-E-1B-Instruct) | 1B | 26.35 | 8k | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/) | [Bitnet-b1.58-2B-4T](https://huggingface.co/microsoft/bitnet-b1.58-2B-4T) | 2B | **Incoming** | 4k | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |

</details>

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

#### Proprietary Models

**Note that scores reflect an overall assessment and do not guarantee consistently superior performance in every situation.**

| Organization       | Model Name                                                                       | [Score](https://github.com/LSeu-Open/LLMScoreEngine) (v0.5.2) | [Context Window](https://research.ibm.com/blog/larger-context-window) | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Multilinguality | Pricing  |
|:------------------:|:---------------------------------------------------------------------------------|:--------------:|:---------------:|:---:|:-------------:|:-------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)  | **[Gemini 2.5 Pro](https://deepmind.google/technologies/gemini/pro/)** | **79.07** | **1M** | ✔️ | **[38](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#gemini-family)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude 4 Sonnet](https://claude.ai/) | 73.62  | 200k | ✔️ | **[15](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#claude-4-and-claude-3x)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/)  | [Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/flash/) | 71.71 | 1M | ✔️ | **[38](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#gemini-family)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [o3](https://openai.com/index/introducing-o3-and-o4-mini/) | 71.06 | 256k | ✔️ | **[57](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#chatgpt-and-ox-families)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude 4 Opus](https://claude.ai/) | 70.71  | 200k | ✔️ | **[15](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#claude-4-and-claude-3x)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/) | 70.34 | 256k | ✔️ | **[57](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#chatgpt-and-ox-families)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/BigModel.svg" alt="BigModel" width="200" height="20" />](https://bigmodel.cn/) | [GLM-4-Plus](https://bigmodel.cn/dev/howuse/glm-4) | 69.36  | 1M | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen 2.5 Max](https://qwenlm.github.io/blog/qwen2.5-max/) | 68.79 | 32K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4.1](https://openai.com/index/gpt-4-1/) | 68.21 | 1M | ❌ | **[57](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#chatgpt-and-ox-families)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/xAI.svg" alt="xAI" width="220" height="20" />](https://x.ai/) | [Grok-3](https://grok.com/) | 66.88 | 1M | ✔️ | ? | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Doubao.svg" alt="doubao" width="200" height="20" />](https://team.doubao.com/en/) | [Doubao 1.5 Pro](https://team.doubao.com/en/special/doubao_1_5_pro) | 66.57 | 256K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | [Magistral Medium](https://mistral.ai/news/magistral) | 65.67 | 128K | ✔️ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#magistral-small-and-medium)** | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/MoonshotAI.svg" alt="moonshot" width="200" height="20" />](https://www.moonshot.cn/) | [Kimi-k1.5](https://github.com/MoonshotAI/Kimi-k1.5) | 65.20 | Unknown | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude 3.7 Sonnet](https://claude.ai/) | 65.09 | 200k | ✔️ | **[15](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#claude-4-and-claude-3x)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4.1 mini](https://openai.com/index/gpt-4-1/) | 63.47 | 1M | ❌ | **[57](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#chatgpt-and-ox-families)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/StepFun.svg" alt="Stepfun" width="200" height="20" />](https://platform.stepfun.com/) | [Step-2-16k-exp](https://platform.stepfun.com/) | 61.08 | 16K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/xAI.svg" alt="xAI" width="220" height="20" />](https://x.ai/) | [Grok-3-mini](https://grok.com/) | 60.78 | 1M | ✔️ | ? | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/) | [Medium 3](https://mistral.ai/news/mistral-medium-3) | 59.27 | 128K | ❌ | **[13](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#mistral-large)** |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4o](https://openai.com/index/hello-gpt-4o/) | 57.62 | 128K | ❌ | **[57](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#chatgpt-and-ox-families)** | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude 3.5 Sonnet](https://claude.ai/) | 55.33 | 200k | ❌ | **[15](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#claude-4-and-claude-3x)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Perplexity.svg" alt="Perplexity" width="200" height="20" />](https://www.perplexity.ai)  | [Sonar Pro](https://sonar.perplexity.ai/) | 54.25 | 127k | ❌ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/amazon.svg" alt="Amazon" width="200" height="20" />](https://aws.amazon.com/ai/) | [Nova Premier](https://aws.amazon.com/ai/) | 54.17 | 1M | ❌ | **[15](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#nova-family)** |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4.1 nano](https://openai.com/index/gpt-4-1/) | 52.28 | 1M | ❌ | **[57](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#chatgpt-and-ox-families)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Perplexity.svg" alt="Perplexity" width="200" height="20" />](https://www.perplexity.ai)  | [Sonar](https://sonar.perplexity.ai/) | 51.33  | 127k | ❌ | **[8](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#llama-31-and-32-and-33)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude 3.5 Haiku](https://claude.ai/) | 50.96 | 200k | ❌ | **[15](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#claude-4-and-claude-3x)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/amazon.svg" alt="Amazon" width="200" height="20" />](https://aws.amazon.com/ai/) | [Nova Pro](https://aws.amazon.com/ai/) | 48.93 | 300K | ❌ | **[15](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#nova-family)** |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [o3-pro](https://platform.openai.com/docs/models/o3-pro) | **Incoming** | 200K | ✔️ | **[57](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Supplementary/Multilinguality.md#chatgpt-and-ox-families)** | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

### Finetuned LLMs

**Fine-tuned Large Language Models (LLMs)** refer to AI models that have been **specifically adapted for a particular domain, task, or dataset.** This adaptation significantly **enhances their performance and accuracy within that specific context**, compared to using them on more general-purpose datasets.

#### Astrophysics

Models **optimized for Astrophysics and Astronomy research** through specialized training datasets.

| Organization       |Base Model                                       | Finetuned Model | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Geographic Origin |
|:------------------:|:-----------------------------------------|:------------------------------------------------------------------------------------------|:--------------:|:------------:|:----------------:|:----------------:|
|  **AstroMLab**  | [Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) | [AstroSage-8B](https://huggingface.co/AstroMLab/AstroSage-8B) | 8B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  **Tijmen de Haan**  | [Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) | [Cosmosage-v3.1](https://huggingface.co/Tijmen2/cosmosage-v3.1) | 8B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/jp.svg" alt="japan" width="20" height="15" />  |
|  **AstroMLab**  | [Llama-2-70b-hf](https://huggingface.co/meta-llama/Llama-2-70b-hf) | [Astrollama-2-70b-base_aic](https://huggingface.co/AstroMLab/astrollama-2-70b-base_aic) | 8B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |

<br>

#### Function calling

Models **optimized for [Function calling](https://finetunedb.com/blog/what-is-function-calling-simply-explained/) tasks** through specialized training.

Function calling **enables LLMs to interact with external systems and tools through structured interfaces.**

> [!NOTE]
> Models are ranked by **[Berkeley Function Calling Leaderboard V3 Score](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html) (Higher is better)**., designed to evaluate the function calling capabilities of LLMs. it provides a comprehensive evaluation of LLMs' function calling capabilities, offering insights into their performance, cost-effectiveness, and error patterns in real-world scenarios.


| Organization       |Base Model                                       | Finetuned Model                                                                                | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [BCFL Score](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html) | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Geographic Origin |
|:------------------:|:-----------------------------------------|:------------------------------------------------------------------------------------------|:--------------:|:------------:|:----------------:|:----------------:|:-------------:|
|  [Meetkai](https://huggingface.co/meetkai)  | [Llama-3.1-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) | [Functionary-medium-v3.1](https://huggingface.co/meetkai/functionary-medium-v3.1) | 70B | 62.53| 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | 
|  [Katanemo](https://katanemo.com/)  | [Qwen2.5-7B](https://huggingface.co/Qwen/Qwen2.5-7B) | [Arch-Function-7B](https://huggingface.co/katanemo/Arch-Function-7B) | 7B | 59.62 | 131K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [Team-ACE](https://huggingface.co/Team-ACE)  | [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | [ToolACE-8B](https://huggingface.co/Team-ACE/ToolACE-8B) | 8B | 58.31 | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [Salesforce](https://huggingface.co/Salesforce)  | [Mixtral-8x22B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) | [xLAM-8x22b-r](https://huggingface.co/Salesforce/xLAM-8x22b-r) | 141B | 58.03 | 64K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [MadeAgents](https://github.com/MadeAgents)  | [Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) | [Hammer2.0-7b](https://huggingface.co/MadeAgents/Hammer2.0-7b) | 7B | 55.19 | 131K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [Fireworks](https://fireworks.ai/) | [Llama-3.1-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) | [llama-3-firefunction-v2](https://huggingface.co/fireworks-ai/llama-3-firefunction-v2) | 70B | 53.12 | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/IBM.svg" alt="ibm" width="200" height="20" />](https://github.com/ibm-granite/)  | [Granite-20b-code-instruct-8k](https://huggingface.co/ibm-granite/granite-20b-code-instruct-8k) | [Granite-20b-functioncalling](https://huggingface.co/ibm-granite/granite-20b-functioncalling) | 20B | 49.19 | 8k  | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Nexusflow.svg" alt="Nexuflow" width="200" height="20" />](https://nexusflow.ai/) | [CodeLlama-13b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-13b-Instruct-hf) | [NexusRaven-V2-13B](https://huggingface.co/Nexusflow/NexusRaven-V2-13B) | 13B | 36.98 | 8K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

#### Language Specific

Models fine-tuned for **efficiency in a specific language or language family.**

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Language |
|:------------------:|:----------------------------------------|:-----------------------------------------------------------------------------------------:|:--------------:|:------------:|:----------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Shisa.svg" alt="Shisa" width="200" height="23" />](https://shisa.ai/) | [Shisa-v2-llama3.1-405b](https://huggingface.co/shisa-ai/shisa-v2-llama3.1-405b) | 405B | 128k | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/jp.svg" alt="japan" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Shisa.svg" alt="Shisa" width="200" height="23" />](https://shisa.ai/) | [Shisa-v2-llama3.3-70b](https://huggingface.co/shisa-ai/shisa-v2-llama3.3-70b) | 70B | 128k | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/jp.svg" alt="japan" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Shisa.svg" alt="Shisa" width="200" height="23" />](https://shisa.ai/) | [Shisa-v2-qwen2.5-32b](https://huggingface.co/shisa-ai/shisa-v2-qwen2.5-32b) | 32B | 128k | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/jp.svg" alt="japan" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Shisa.svg" alt="Shisa" width="200" height="23" />](https://shisa.ai/) | [Shisa-v2-mistral-small-24b](https://huggingface.co/shisa-ai/shisa-v2-mistral-small-24b) | 24B | 128k | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/jp.svg" alt="japan" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Shisa.svg" alt="Shisa" width="200" height="23" />](https://shisa.ai/) | [Shisa-v2-qwen2.5-32b](https://huggingface.co/shisa-ai/shisa-v2-mistral-nemo-12b) | 12B | 128k | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/jp.svg" alt="japan" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Shisa.svg" alt="Shisa" width="200" height="23" />](https://shisa.ai/) | [Shisa-v2-mistral-llama3.1-8b](https://huggingface.co/shisa-ai/shisa-v2-llama3.1-8b) | 8B | 128k | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/jp.svg" alt="japan" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Shisa.svg" alt="Shisa" width="200" height="23" />](https://shisa.ai/) | [Shisa-v2-mistral-qwen2.5-7b](https://huggingface.co/shisa-ai/shisa-v2-qwen2.5-7b) | 7B | 128k | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/jp.svg" alt="japan" width="20" height="15" />  |

<br>

#### Math

Models **optimized for mathematical reasoning and computation** through specialized training architectures.

> [!NOTE]
> Model rankings utilize combined performance metrics from **GSM8K, MATH, AIME, Olympiad Bench and other maths benchmarks, averaging scores across multiple approach to provide comprehensive evaluation standards (Higher score is better).**
>
> **Generalist models can match or exceed domain-specific Math models in certain tasks.** 

***Large-scale models (70+ billion parameters)*** : These require substantial amounts of RAM and GPU memory, making local installation impractical for most users. As a result, these models are typically deployed on cloud-based platforms that provide the necessary computational resources.

| Organization       | Model Name                                                       | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)   | Score        | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Geographic Origin |
|:------------------:|:-----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------:|:-------------:|:------------:|:----------------:|:----------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-Prover-V2-671B](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-671B) | 671B | 88.9 | 128K |  ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/) | [AceMath-72B-Instruct](https://huggingface.co/nvidia/AceMath-72B-Instruct) | 72B | 71.98 | 132K | ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen2.5-Math-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Math-72B-Instruct) | 72B | 72.03 | 132K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Numina.svg" alt="Numina" width="200" height="20" />](https://huggingface.co/AI-MO) | [NuminaMath-72B-CoT](https://huggingface.co/AI-MO/NuminaMath-72B-CoT) | 72B | 53.78 | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM) | [Internlm2-math-plus-mixtral8x22b](https://huggingface.co/internlm/internlm2-math-plus-mixtral8x22b) | 141B | 49.96 | 65K |   ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |

<br>

***Mid-sized and smaller models (less than 70 billion parameters)*** :  These models are suitable for local deployment on high-end to mid-range consumer setup. However, such deployments require a significant hardware investment, including a GPU (16–32 GB of VRAM) and related components, typically resulting in total costs ranging from $1000 to $3,000 (or equivalent).


| Organization       | Model Name                                                       | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)   | Score        | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Geographic Origin |
|:------------------:|:-----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------:|:-------------:|:------------:|:----------------:|:----------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [DeepSeek-Prover-V2-7B](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-7B) | 7B | 82.0 | 128K |  ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/) | [AceReason-Nemotron-14B](https://huggingface.co/nvidia/AceReason-Nemotron-14B) | 14B | 80.33 | 132K |  ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/) | [AceMath-RL-Nemotron-7B](https://huggingface.co/nvidia/AceMath-RL-Nemotron-7B) | 7B | 75.94 | 32K |  ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/) | [AceReason-Nemotron-7B](https://huggingface.co/nvidia/AceReason-Nemotron-7B) | 7B | 72.23 | 128K |  ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/) | [AceMath-7B-Instruct](https://huggingface.co/nvidia/AceMath-7B-Instruct) | 7B | 67.52| 132K |  ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen2.5-Math-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Math-7B-Instruct) | 7B | 64.38 | 132K |  ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM) | [Internlm2-math-plus-20B](https://huggingface.co/internlm/internlm2-math-plus-20b) | 20B | 60.15 | 4K |  ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/) | [AceMath-1.5B-Instruct](https://huggingface.co/nvidia/AceMath-1.5B-Instruct) | 1.5B | 59.77 | 32K |  ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)     | [Mathstral-7B-v0.1](https://huggingface.co/mistralai/Mathstral-7B-v0.1) | 7B | 58.25 | 4K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen2.5-Math-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Math-1.5B-Instruct) | 1.5B | 57.03 | 132K |  ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [Deepseek-math-7b-instruct](https://huggingface.co/deepseek-ai/deepseek-math-7b-instruct) | 7B | 50.2| 4K |  ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM) | [Internlm2-math-plus-7B](https://huggingface.co/internlm/internlm2-math-plus-7b) | 7B | 49.62 | 4K |  ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Numina.svg" alt="Numina" width="200" height="20" />](https://huggingface.co/AI-MO) | [NuminaMath-7B-CoT](https://huggingface.co/AI-MO/NuminaMath-7B-CoT) | 7B | 42.4 | 4K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM) | [Internlm2-math-plus-1.8B](https://huggingface.co/internlm/internlm2-math-plus-1_8b) | 1.8B | 34.33  | 4K |  ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

#### Role Play

Models **optimized for Role Play tasks** through specialized training datasets.

Role-playing in LLMs is a technique where **the model assumes a specific character, profession, or persona to generate more focused and contextually relevant responses.**

***Large-scale models (70+ billion parameters)*** : These require substantial amounts of RAM and GPU memory, making local installation impractical for most users. As a result, these models are typically deployed on cloud-based platforms that provide the necessary computational resources.

| Organization       | Base Model                               | Finetuned Model | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Geographic Origin |
|:------------------:|:-----------------------------------------|:------------------------------------------------------------------------------------------|:--------------:|:------------:|:----------------:|:----------------:|
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Steelskull.svg" alt="Steelskull" width="200" height="25" />](https://huggingface.co/Steelskull) | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [L3.3-Electra-R1-70b](https://huggingface.co/Steelskull/L3.3-Electra-R1-70b) | 70B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | 
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Steelskull.svg" alt="Steelskull" width="200" height="25" />](https://huggingface.co/Steelskull) | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [L3.3-MS-Nevoria-70b](https://huggingface.co/Steelskull/L3.3-MS-Nevoria-70b) | 70B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Latitude.svg" alt="LatitudeGames" width="200" height="25" />](https://play.aidungeon.com/) | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [Wayfarer-Large-70B-Llama-3.3](https://huggingface.co/LatitudeGames/Wayfarer-Large-70B-Llama-3.3) | 70B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  **BosonAI**  | [Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) | [Higgs-Llama-3-70B](https://huggingface.co/bosonai/Higgs-Llama-3-70B) | 70B | 32K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |

<br>

***Mid-sized and smaller models (less than 70 billion parameters)*** :  These models are suitable for local deployment on high-end to mid-range consumer setup. However, such deployments require a significant hardware investment, including a GPU (16–32 GB of VRAM) and related components, typically resulting in total costs ranging from $1000 to $3,000 (or equivalent).

| Organization       | Base Model                               | Finetuned Model | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Geographic Origin |
|:------------------:|:-----------------------------------------|:------------------------------------------------------------------------------------------|:--------------:|:------------:|:----------------:|:----------------:|
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Gryphe.svg" alt="Gryphe" width="200" height="25" />](https://huggingface.co/Gryphe) | [Qwen3-30B-A3B-Base](https://huggingface.co/Qwen/Qwen3-30B-A3B-Base) | [Pantheon-Proto-RP-1.8-30B-A3B](https://huggingface.co/Gryphe/Pantheon-Proto-RP-1.8-30B-A3B) | 30B | 128K | [Hybrid](https://qwenlm.github.io/blog/qwen3/) |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Latitude.svg" alt="LatitudeGames" width="200" height="25" />](https://play.aidungeon.com/) | [Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) | [Harbinger-24B](https://huggingface.co/LatitudeGames/Harbinger-24B) | 24B | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Gryphe.svg" alt="Gryphe" width="200" height="25" />](https://huggingface.co/Gryphe)   | [Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) | [Pantheon-RP-1.8-24b-Small-3.1](https://huggingface.co/Gryphe/Pantheon-RP-1.8-24b-Small-3.1) | 24B | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Gryphe.svg" alt="Gryphe" width="200" height="25" />](https://huggingface.co/Gryphe)   | [Mistral-Small-Instruct-2409](https://huggingface.co/mistralai/Mistral-Small-Instruct-2409) | [Pantheon-RP-Pure-1.6.2-22b-Small](https://huggingface.co/Gryphe/Pantheon-RP-Pure-1.6.2-22b-Small) | 22B | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Latitude.svg" alt="LatitudeGames" width="200" height="25" />](https://play.aidungeon.com/) | [Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) | [Muse-12B](https://huggingface.co/LatitudeGames/Muse-12B) | 12B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Latitude.svg" alt="LatitudeGames" width="200" height="25" />](https://play.aidungeon.com/) | [Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) | [Wayfarer-12B](https://huggingface.co/LatitudeGames/Wayfarer-12B) | 12B | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Oxygen.svg" alt="Oxygen" width="200" height="25" />](https://huggingface.co/oxyapi) | [Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) | [Oxy-1-small](https://huggingface.co/oxyapi/oxy-1-small) | 14.8B |  131K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Oxygen.svg" alt="Oxygen" width="200" height="25" />](https://huggingface.co/oxyapi) | [Qwen2-1.5B](https://huggingface.co/Qwen/Qwen2-1.5B) | [Oxy-1-micro](https://huggingface.co/oxyapi/oxy-1-micro) | 1.54B |  131K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |

<br>
<br>

#### Uncensored

Models modified to **operate without standard content filtering mechanisms**, enabling **unrestricted response generation beyond typical LLM safeguards.**

> [!NOTE]
> Models are ranked by **[UGI Leaderboard Score](https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard) (Higher score is better)**, designed to evaluate both willingness to answer and accuracy in fact-based contentious questions.
>
> The provided score **does not evaluate the overall performance of the models** but instead focuses on how **effectively they remain uncensored.**

***Large-scale models (70+ billion parameters)*** : These require substantial amounts of RAM and GPU memory, making local installation impractical for most users. As a result, these models are typically deployed on cloud-based platforms that provide the necessary computational resources.

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d) | [Context Window](https://research.ibm.com/blog/larger-context-window) | UGI Score        | Reasoning Model | Geographic Origin |
|:------------------:|:-----------|:-----------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|:---------------:|:-----------------:|:-----------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/NousResearch.svg" alt="NousResearch" width="200" height="25" />](https://nousresearch.com/) | [Hermes-3-Llama-3.1-405B](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-405B) | 405B | 128K | 62.52 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TheDrummer.svg" alt="TheDrummer" width="200" height="25" />](https://huggingface.co/TheDrummer) | [Behemoth-123B-v2](https://huggingface.co/TheDrummer/Behemoth-123B-v2) | 123B | 128K | 57.43 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Steelskull.svg" alt="Steelskull" width="200" height="25" />](https://huggingface.co/Steelskull) | [L3.3-MS-Nevoria-70b](https://huggingface.co/Steelskull/L3.3-MS-Nevoria-70b) | 70B | 128K | 56.75 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/au.svg" alt="au" width="20" height="15" /> |
| **zerofata** | [L3.3-GeneticLemonade-Final-70B](https://huggingface.co/zerofata/L3.3-GeneticLemonade-Final-70B) | 70B | 128K | 55.53 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/mlabonne.svg" alt="mlabonne" width="200" height="25" />](https://mlabonne.github.io/blog/) | [Llama-3.1-70B-Instruct-lorablated](https://huggingface.co/mlabonne/Llama-3.1-70B-Instruct-lorablated) | 70B | 128K | 46.79 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TheDrummer.svg" alt="TheDrummer" width="200" height="25" />](https://huggingface.co/TheDrummer) | [Fallen-Command-A-111B-v1](https://huggingface.co/TheDrummer/Fallen-Command-A-111B-v1) | 111B | 256K | 43.03 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/NousResearch.svg" alt="NousResearch" width="200" height="25" />](https://nousresearch.com/) | [Hermes-3-Llama-3.1-70B](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-70B) | 72B | 128K | 36.7 |  ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |

<br>

***Mid-sized models (14+ billion parameters)*** :  These models are suitable for local deployment on high-end workstations. However, such deployments require a significant hardware investment, including a powerful GPU (24–32 GB of VRAM) and related components, typically resulting in total costs exceeding $3,000 (or equivalent).

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d) | [Context Window](https://research.ibm.com/blog/larger-context-window) | UGI Score       | Reasoning Model | Geographic Origin |
|:------------------:|:-----------|:-----------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|:---------------:|:-----------------:|:-----------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/TheDrummer.svg" alt="TheDrummer" width="200" height="25" />](https://huggingface.co/TheDrummer) | [Cydonia-22B-v1.3](https://huggingface.co/TheDrummer/Cydonia-22B-v1.3) | 22B | 128K | 40.04 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/NousResearch.svg" alt="NousResearch" width="200" height="25" />](https://nousresearch.com/) | [DeepHermes-3-Mistral-24B-Preview](https://huggingface.co/NousResearch/DeepHermes-3-Mistral-24B-Preview) | 24B | 128K | 39.91 | ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/CognitiveComputations.svg" alt="CognitiveComputations" width="200" height="20" />](https://erichartford.com/)  | [Dolphin3.0-Mistral-24B](https://huggingface.co/cognitivecomputations/Dolphin3.0-Mistral-24B) | 24B | 128K | 39.49 |  ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/CognitiveComputations.svg" alt="CognitiveComputations" width="200" height="20" />](https://erichartford.com/)  | [Dolphin3.0-R1-Mistral-24B](https://huggingface.co/cognitivecomputations/Dolphin3.0-R1-Mistral-24B) | 24B  | 128K | 39.49 | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/mlabonne.svg" alt="mlabonne" width="200" height="25" />](https://mlabonne.github.io/blog/) | [Gemma-3-27b-it-abliterated](https://huggingface.co/mlabonne/gemma-3-27b-it-abliterated) | 27B | 128K | 34.96 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  | 

<br>

***Small models (7B+ parameters)*** :  These are lightweight and easy to deploy on standard machines, offering wider accessibility. They typically require a mid-range consumer setup, including a GPU (8–16 GB of VRAM) and related components, with costs generally ranging from $1,000 to $2,000 (or equivalent).

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d) | [Context Window](https://research.ibm.com/blog/larger-context-window) | UGI Score       | Reasoning Model | Geographic Origin |
|:------------------:|:-----------|:-----------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|:---------------:|:-----------------:|:-----------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/NousResearch.svg" alt="NousResearch" width="200" height="25" />](https://nousresearch.com/) | [DeepHermes-3-Llama-3-8B-Preview](https://huggingface.co/NousResearch/DeepHermes-3-Llama-3-8B-Preview) | 8B | 128K | 30.48 | ✔️ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/NousResearch.svg" alt="NousResearch" width="200" height="25" />](https://nousresearch.com/) |[Hermes-3-Llama-3.1-8B](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B) | 8B | 128K | 30.48 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
| **Orenguteng** | [Llama-3.1-8B-Lexi-Uncensored-V2](https://huggingface.co/Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2) | 8B |  128K | 25.94 |  ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/mlabonne.svg" alt="mlabonne" width="200" height="25" />](https://mlabonne.github.io/blog/) | [Gemma-3-12b-it-abliterated](https://huggingface.co/mlabonne/gemma-3-12b-it-abliterated) | 12B | 128K | 23.51 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/CognitiveComputations.svg" alt="CognitiveComputations" width="200" height="20" />](https://erichartford.com/)  | [Dolphin3.0-Llama3.1-8B](https://huggingface.co/cognitivecomputations/Dolphin3.0-Llama3.1-8B) | 8B  | 128K | 20.72 |  ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/NousResearch.svg" alt="NousResearch" width="200" height="25" />](https://nousresearch.com/) | [OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B) | 7B | 32K | 18.4 | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

### LLM Providers

#### Cloud-based LLM Providers

> [!Tip]
> Reference the [Artificial Analysis Leaderboard](https://artificialanalysis.ai/leaderboards/providers) for **comparative analysis of LLM providers across key performance metrics**: pricing, token generation speed, response latency, and context window capabilities.

***Major Cloud AI Providers***

These are typically large tech companies that develop and offer access to their own flagship LLMs. Access is usually via APIs, and they manage all the underlying infrastructure.

| Tool             | Description                                                                                                                 | Models      | Pricing     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [AI21 Labs](https://www.ai21.com/) |  Known for their language models like Jurassic-1 Jumbo focused on quality, safety, and controllability. |  [Jamba Large 1.6](https://huggingface.co/ai21labs/AI21-Jamba-Large-1.6) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Anthropic](https://www.anthropic.com/claude) | Known for their constitutional AI model Claude, focused on being helpful, harmless, and honest. | [Claude 3.7 Sonnet](https://claude.ai/) and more  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [Cohere](https://cohere.com/) | Provides an enterprise AI platform with models like Cohere Generate for custom content creation. | [Command A](https://cohere.com/blog/command-A) | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Databricks](https://www.databricks.com/) | A unified, open analytics platform that provides tools and services for data processing, analytics, and artificial intelligence at scale. | [Dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct) | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Deepseek](https://chat.deepseek.com/) | An AI company that has developed several notable AI models and technologies | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) and more | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Google](https://gemini.google.com/) |  Provides models like LaMBDA, PaLM, and Bard for language understanding, generation, and multimodal AI tasks. | [Gemini 2.5 Pro](https://deepmind.google/technologies/gemini/pro/) and more | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [Mistral AI](https://mistral.ai/) | A French artificial intelligence company that specializes in developing large language models (LLMs) and AI products. | [Mistral Large 2](https://huggingface.co/mistralai/Mistral-Large-Instruct-2411) and more | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [OpenAI](https://chatgpt.com/) | Offers models like GPT-4, DALL-E, and Whisper for natural language processing, image generation, and speech recognition. | [o3](https://openai.com/index/introducing-o3-and-o4-mini/) and more | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Qwen](https://chat.qwen.ai/) | A Chinese AI company that has developed several notable AI models and technologies | [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) and more |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Reka](https://chat.reka.ai/) | An AI company that develops advanced multimodal AI models and technologies. | [Reka Flash 3](https://huggingface.co/RekaAI/reka-flash-3) and more | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

***Aggregator & Specialized Cloud Platforms***

These platforms offer access to a variety of models from different developers, including many popular open-source models and sometimes proprietary ones, often through a single API or interface. Some may offer specialized hardware or value-added services like fine-tuning.

| Tool             | Description                                                                                                                 | Models      | Pricing     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [Amazon Web Services (AWS)](https://aws.amazon.com/bedrock/) | Offers models like Amazon CodeWhisperer for code generation and understanding through their SageMaker platform. | Large Panel of Open source and Proprietary Models | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Cerebras](https://inference.cerebras.ai/) | An AI company that has developed innovative hardware and software solutions for AI computing. | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) and more | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [DeepInfra](https://deepinfra.com/chat) | A platform that provides scalable and cost-effective infrastructure for deploying machine learning models. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Featherless](https://featherless.ai/) | A subscription-based, serverless LLM hosting provider that gives you instant, unlimited access to thousands of Hugging Face models, all via a simple API and with no infrastructure hassles. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Fireworks](https://fireworks.ai/) | A comprehensive solution for companies looking to deploy AI into production, focusing on performance, cost-effectiveness, and developer experience. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Groq](https://groq.com/) | Specializes in high-performance AI inference with custom LPU (Language Processing Unit) hardware, offering models like Meta's Llama 3. | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) and more  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [Hyperbolic](https://app.hyperbolic.xyz/models) | an open-access AI cloud platform designed to democratize AIe by making high-performance compute resources—especially GPUs—affordable and accessible to everyone. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [LeptonAI](https://www.lepton.ai/) | A platform that provides cloud-based infrastructure and tools for deploying and running AI applications efficiently. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Microsoft Azure](https://azure.microsoft.com/) | A comprehensive suite of AI services and tools designed to help developers and organizations build, deploy, and manage AI applications at scale. | Large Panel of Open source and Proprietary Models | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Nebius](https://studio.nebius.com/) | A high-performance, cost-effective Inference-as-a-Service platform designed to make advanced AI generation accessible | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Novita](https://novita.ai/models) | A high-performance, cost-effective Inference-as-a-Service platform designed to make advanced AI generation accessible | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [OctoAI](https://octoai.cloud/) | A full-stack inference platform designed specifically for generative AI applications. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [OpenRouter](https://openrouter.ai/) |  A versatile platform designed to provide access to a wide range of large language models (LLMs) from both proprietary and open-source sources. |  Large Panel of Open source and Proprietary Models | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Parasail](https://www.parasail.io/) | A next-generation AI infrastructure platform that makes deploying, scaling, and managing AI models fast, flexible, and affordable. | Large Panel of Open source Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Poe](https://poe.com) | An AI chatbot aggregator platform developed by Quora that provides users access to multiple advanced language models and chatbots within a single interface. | Large Panel of Open source and Proprietary Models | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [SambaNova](https://sambanova.ai/) | An artificial intelligence company that provides a comprehensive AI platform for enterprises. | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) and more | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Together](https://www.together.ai/) | A cloud platform designed for building and running generative AI applications. | Large Panel of Open source Models | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> | 

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

#### Local LLM Providers

> [!IMPORTANT]
> **Deploy LLMs locally** with our [implementation guide](./Tutorials/how-to-run-llms-on-your-machine.md) for privacy-focused language processing and model experimentation on your hardware.

| Tool             | Description                                                                                                                 | OS     | Models     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [AnythingLLM](https://anythingllm.com/) | An open-source, full-stack application that allows users to chat with their documents in a private and enterprise-friendly environment. | All | All Open source Models |
| [Chatbox](https://chatboxai.app) |  AI-powered conversational interface that enables human-like interactions through text or voice. | All | All Open source Models |
| [ChatWise](https://chatwise.app/) | A high-performance, privacy-focused AI chatbot platform that supports multiple LLMs for versatile, multimodal interactions. | All | Large Panel of Models |
| [Cherry Studio](https://cherry-ai.com/) | A cross-platform desktop application that serves as a unified interface for interacting with multiple large language models (LLMs)—both cloud-based and locally hosted. | All | Large Panel of Models |
| [Enchanted](https://github.com/AugustDev/enchanted) | iOS and macOS app for chatting with private self hosted language models.| MacOS/IOS | Large Panel of Open source Models |
| [FreeChat](https://www.freechat.run/) | An AI-powered chat application designed specifically for macOS. | MacOS | Large Panel of Open source Models |
| [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) | Open-source app designed to showcase and let users interact with on-device machine learning (ML) and generative AI (GenAI) models directly on their smartphones. | Android / iOS(Soon) | All Open source Models |
| [GPT4ALL](https://www.nomic.ai/gpt4all) | An open-source software ecosystem developed by Nomic AI that enables users to run powerful large language models (LLMs) locally on their personal computers. | All | Large Panel of Open source Models |
| [Jan](https://jan.ai/) | Clean UI with useful features like system monitoring and LLM library.| All | Large Panel of Open source Models |
| [LibreChat](https://www.librechat.ai/) | Open-source chat interface that supports multiple AI models, including Anthropic, AWS, OpenAI, and Azure. It offers features like agents with file handling, a code interpreter for various languages. | All | Large Panel of Models |
| [LLMFarm](https://github.com/guinmoon/LLMFarm) | An open-source app for running LLMs locally and offline on iOS and macOS devices. | iOS/ MacOS | All Open source Models |
| [LM Studio](https://superagi.com/) |  Elegant UI with the ability to run every Hugging Face repository. | All | Large Panel of Open source Models |
| [Msty](https://msty.app/) | An AI chat application that offers a user-friendly interface for interacting with both local and online AI language models. | All | Large Panel of Open source Models |
| [Ollama](https://ollama.com/) | Fastest when used on the terminal, and any model can be downloaded with a single command. | All | All Open source Models |
| [Open WebUI](https://openwebui.com/) | Self-hosted, open-source web interface designed for running and managing LLMs locally or offline. | All | All Open source Models |
| [Silly Tavern](https://sillytavern.app/) | Open-source LLM frontend designed for power users. | All | All Open source Models |
| [Witsy](https://witsyai.com/) | Open-source LLM frontend designed for power users. | All | All Open source Models |
| [Pocketpal](https://github.com/a-ghorbani/pocketpal-ai) |  AI assistant powered by small language models (SLMs) that run directly on your phone. | Android / iOS | All Open source Models |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

#### LLM Inference Engines

This table lists notable frameworks and libraries designed for running and serving Large Language Models efficiently, focusing on performance, scalability, and deployment.

> The landscape evolves rapidly. Some tools might integrate techniques or components from others (e.g., many serving frameworks might leverage optimized kernels like FlashAttention or specific backend libraries like `vLLM` or `TensorRT-LLM`). This table focuses on the primary offering or framework level.

| Engine/Server          | Developer/Origin       | Key Features & Focus                                                                 | Primary Use Case(s)         | Notes                                                              |
| :--------------------- | :--------------------- | :----------------------------------------------------------------------------------- | :-------------------------- | :----------------------------------------------------------------- |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | Georgi Gerganov et al. | Highly optimized C++ inference for GGUF models; CPU & GPU (Metal, CUDA, OpenCL) support. | Local inference, experimentation, backend for other tools | Foundational library/CLI, broad hardware support.                    |
| [vLLM](https://github.com/vllm-project/vllm) | vLLM Project (Berkeley) | High-throughput serving library; PagedAttention, continuous batching.                 | Production serving, research | Primarily Python library, integrates with frameworks like Ray, OpenLLM. |
| [Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference) | Hugging Face           | Production-ready server; Optimized for HF models, high throughput, streaming.       | Production serving          | Rust/Python based, commonly used for deploying HF models.         |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | NVIDIA                 | Optimization library & engine for NVIDIA GPUs; Quantization, in-flight batching.   | High-performance serving (NVIDIA HW) | Requires model compilation, integrates with Triton.                  |
| [Triton Inference Server](https://developer.nvidia.com/triton-inference-server) | NVIDIA                 | General-purpose inference server; Supports multiple frameworks (TRT, PyTorch, TF). | Production serving (diverse models) | Can serve LLMs (often via TensorRT-LLM backend) and other models. |
| [OpenLLM](https://github.com/bentoml/OpenLLM) | BentoML                | Production-ready LLM serving framework; Integrates vLLM/BentoML, OpenAI API compat. | Production serving          | Aims to simplify deployment and scaling.                           |
| [Ray Serve](https://docs.ray.io/en/latest/serve/index.html) | Anyscale (Ray Team)    | Scalable model serving library on Ray; Distributed computing support.            | Distributed production serving | General purpose, but powerful for scaling LLM endpoints.           |
| [LMDeploy](https://github.com/InternLM/lmdeploy) | OpenMMLab / MMDeploy   | Efficient inference framework; Quantization, TurboMind engine.                     | Research, production serving | Part of the OpenMMLab ecosystem.                                  |
| [MLC LLM](https://github.com/mlc-ai/mlc-llm) | MLC AI Team            | Universal deployment solution; Compiles models for diverse hardware (CPU, GPU, mobile). | Cross-platform deployment | Focuses on Machine Learning Compilation.                           |
| [SGLang](https://github.com/sgl-project/sglang) | SGL Project            | Efficient structured generation & inference; RadixAttention.                         | Research, production serving | Optimized for complex generation tasks.                            |
| [DeepSpeed Inference](https://www.deepspeed.ai/inference/) | Microsoft              | Optimized inference kernels & engine (part of DeepSpeed library).                  | High-performance serving | Leverages techniques developed for large-scale training.          |
| [Xinference](https://github.com/xorbitsai/inference) | Xorbits                | Platform for deploying LLMs & embedding models; API compatible with popular tools.  | Local & cloud deployment    | Aims to be a unified deployment solution.                        |
| [LocalAI](https://localai.io/) | Go-Skynet              | OpenAI-compatible API layer; Pluggable backends (incl. llama.cpp, but others too). | Local development, API replacement | Acts as a bridge, not the core engine itself.                     |
| [LLM Engine (Scale)](https://github.com/scaleapi/llm-engine) | Scale AI               | Fine-tuning & serving platform; Optimized inference, simplified deployment.        | Production serving (hosted or self-hosted) | Provides both infrastructure and optimization.                    |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

## Multimodal Language Models

<br>

### Vision Language Models

 Vision Language Models (VLMs) are a specialized type of multimodal AI that understands and generates content by integrating **both visual and text-based data.** This allows them to perform tasks like image captioning, visual question answering, and object recognition. For more Technical details, see the  [Huggingface VLM overview](https://huggingface.co/blog/vlms).

**Deploy these open-source models locally** using our Local LLM Deployment Guide : ***[How to run LLMs on your machine](./Tutorials/how-to-run-llms-on-your-machine.md)***.

> [!IMPORTANT]
> Models are ranked using our [VLM scoring framework](https://github.com/LSeu-Open/VLMScoreEngine), which synthesizes performance benchmarks, human preference evaluations, and technical specifications. A higher score indicates better overall performance.
>
> **Note that scores provide a relative ranking within each model's size category. A higher score does not guarantee superior performance on any specific task or in every language.**


#### Open source VLMs

***Large-scale models (70+ billion parameters)*** : These require significant amounts of both RAM and GPU memory, often rendering local installation infeasible for most users. Consequently, such models are predominantly deployed on cloud-based platforms designed to provide the essential computational resources needed.

| Organization     | Model Name                                                                         | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d) | [Score](https://github.com/LSeu-Open/VLMScoreEngine) (v0.1.0) | Geographic Origin |
|:-----------------:|:------------------------------------------------------------------------------|:----------:|:-----------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL3-78B](https://huggingface.co/OpenGVLab/InternVL3-78B) | 78B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL2_5-78B-MPO](https://huggingface.co/OpenGVLab/InternVL2_5-78B-MPO) | 78B | **Incoming**  | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)      | [Qwen2.5-VL-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct) | 72B   | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)      | [Qwen2-VL-72B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-72B-Instruct) | 72B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/) | [NVLM-D-72B](https://huggingface.co/nvidia/NVLM-D-72B) | 72B | **Incoming** |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)         | [Llama-3.2-90B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct) | 90B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Allen.svg" alt="Allen" width="200" height="20" />](https://allenai.org/)      | [Molmo-72B](https://huggingface.co/allenai/Molmo-72B-0924) | 72B | **Incoming** |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |


<br>

***Mid-sized models (14+ billion parameters)*** : These models are well-suited for local deployment on high-end workstations. However, such deployments require a significant hardware investment, including a powerful GPU (24-32 GB of VRAM) and associated components, typically resulting in total costs exceeding $3,000 (or equivalent).

| Organization     | Model Name                                                                         | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d) | [Score](https://github.com/LSeu-Open/VLMScoreEngine) (v0.1.0) | Geographic Origin |
|:-----------------:|:------------------------------------------------------------------------------|:----------:|:-----------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL3-38B](https://huggingface.co/OpenGVLab/InternVL3-38B) | 38B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL2_5-38B-MPO](https://huggingface.co/OpenGVLab/InternVL2_5-38B-MPO) | 38B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)      | [Ovis2-34B](https://huggingface.co/AIDC-AI/Ovis2-34B) | 34B   | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL2_5-26B-MPO](https://huggingface.co/OpenGVLab/InternVL2_5-26B-MPO) | 26B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)      | [Ovis2-16B](https://huggingface.co/AIDC-AI/Ovis2-16B) | 16B   | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  | 
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/MoonshotAI.svg" alt="moonshot" width="200" height="20" />](https://www.moonshot.cn/)     | [Kimi-VL-A3B-Instruct](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct) | 16.4B   | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)     | [InternVL2-26B](https://huggingface.co/OpenGVLab/InternVL2-26B) | 26B | **Incoming**  | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) | 27B | **Incoming** |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Rhymes.svg" alt="Rhymes" width="200" height="20" />](https://rhymes.ai/)  | [Aria](https://huggingface.co/rhymes-ai/Aria) | 25.3B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> | 

<br>

***Small models (7B+ parameters)*** : These are lightweight and easily deployable on medium machines, offering broader accessibility. They typically require a mid-range consumer configuration, including a GPU (8-16 GB of VRAM) and associated components, with costs generally between $1,000 to $2,000 (or equivalent).

| Organization     | Model Name                                                                         | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d) | [Score](https://github.com/LSeu-Open/VLMScoreEngine) (v0.1.0) | Geographic Origin |
|:-----------------:|:------------------------------------------------------------------------------|:----------:|:-----------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL3-14B](https://huggingface.co/OpenGVLab/InternVL3-14B) | 14B | **Incoming**  | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL3-8B](https://huggingface.co/OpenGVLab/InternVL3-8B) | 8B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL2_5-8B-MPO](https://huggingface.co/OpenGVLab/InternVL2_5-8B-MPO) | 8B | **Incoming**  | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)      | [Ovis2-8B](https://huggingface.co/AIDC-AI/Ovis2-8B) | 8B   | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/ByteDance.svg" alt="Bytedance" width="200" height="20" />](https://www.bytedance.com/en/) | [SAIL-VL-1.6-8B](https://huggingface.co/BytedanceDouyinContent/SAIL-VL-1d6-8B) | 8B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)      | [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) | 7B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)      | [Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct) | 7B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)     | [InternVL2-8B](https://huggingface.co/OpenGVLab/InternVL2-8B) | 8B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenBMB.svg" alt="OpenBMB" width="200" height="20" />](https://www.openbmb.cn/) | [MiniCPM-V-2_6](https://huggingface.co/openbmb/MiniCPM-V-2_6) | 8B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it) | 12B | **Incoming** |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Mistral.svg" alt="Mistral" width="200" height="20" />](https://mistral.ai/)   | [Pixtral-12B](https://huggingface.co/mistralai/Pixtral-12B-2409) | 12B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/BigModel.svg" alt="BigModel" width="200" height="20" />](https://bigmodel.cn/) | [GLM-4V-9B](https://huggingface.co/THUDM/glm-4v-9b) | 9B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Meta.svg" alt="Meta" width="200" height="20" />](https://ai.meta.com/)         | [Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) | 11B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/nvidia.svg" alt="Nvidia" width="200" height="20" />](https://build.nvidia.com/)  | [Llama-3.1-Nemotron-Nano-VL-8B-V1](https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1) | 8B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/THUDM.svg" alt="THUDM" width="200" height="20" />](https://github.com/THUDM)  | [GLM-4.1V-9B-Thinking](https://huggingface.co/THUDM/GLM-4.1V-9B-Thinking) | 9B | **Incoming** | 132K | ✔️ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |

<br>

***Tiny models (under 7B parameters)*** : Designed for broad compatibility, these models run effectively on older or less powerful machines, making them accessible to a wider range of users. They typically require only 6-8 GB of RAM and can be deployed across a wide range of standard consumer hardware setups.

| Organization     | Model Name                                                                         | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d) | [Score](https://github.com/LSeu-Open/VLMScoreEngine) (v0.1.0) | Geographic Origin |
|:-----------------:|:------------------------------------------------------------------------------|:----------:|:-----------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL3-2B](https://huggingface.co/OpenGVLab/InternVL3-2B) | 2B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL2_5-4B-MPO](https://huggingface.co/OpenGVLab/InternVL2_5-4B-MPO) | 4B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/ByteDance.svg" alt="Bytedance" width="200" height="20" />](https://www.bytedance.com/en/) | [SAIL-VL-1.5-2B](https://huggingface.co/BytedanceDouyinContent/SAIL-VL-1d5-2B) | 2B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/InternLM.svg" alt="InternLM" width="200" height="20" />](https://github.com/InternLM)    | [InternVL3-1B](https://huggingface.co/OpenGVLab/InternVL3-8B) | 1B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it) | 4B | **Incoming** |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|[<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Microsoft.svg" alt="microsoft" width="200" height="20" />](https://www.microsoft.com/)    | [Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct) | 4.15B | **Incoming** |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/HuggingFace.svg" alt="HuggingFace" width="200" height="20" />](https://huggingface.co/) | [SmolVLM2-2.2B-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM2-2.2B-Instruct) | 2.2B | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" /> |

<br>

#### Proprietary VLMs  

| Organization     | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d) | [Score](https://github.com/LSeu-Open/VLMScoreEngine) (v0.1.0) | Geographic Origin | Pricing |
|:-----------------:|:------------------------------------------------------------------------------|:----------:|:----------:|:------------------------------------------------------------:|:------------------------------------------------------------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/BigModel.svg" alt="BigModel" width="200" height="20" />](https://bigmodel.cn/) | [GLM-4V-Plus](https://bigmodel.cn/dev/howuse/glm-4v) | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
|  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/) | [Qwen VL Max](https://qwenlm.github.io/blog/qwen2.5-max/) | **Incoming**| <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |  [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4o](https://openai.com/index/hello-gpt-4o/) | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Tencent.svg" alt="Tencent" width="200" height="20" />](https://github.com/Tencent/) | [HunYuan-Standard-Vision](https://unitalk.ai/discover/model/hunyuan-vision) | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)   |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.7 Sonnet](https://claude.ai//) | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/xAI.svg" alt="xAI" width="220" height="20" />](https://x.ai/) | [Grok-2-vision](https://x.ai/blog/grok-2) | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="200" height="20" />](https://openai.com/) | [GPT-4V](https://chat.openai.com/) | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | <img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" />|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenAI.svg" alt="OpenAI" width="130" height="20" />](https://openai.com/) | [GPT-4o-mini](https://openai.com/index/hello-gpt-4o/) | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Google.svg" alt="Google" width="200" height="20" />](https://gemini.google.com/) | [Gemini 1.5 Flash](https://gemini.google.com/) | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Anthropic.svg" alt="Anthropic" width="200" height="20" />](https://www.anthropic.com/) | [Claude-3.5 Sonnet](https://claude.ai//) | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |

<br>

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>

### Omni Large Language Models

Omni Large Language Models (OLLMs) extend beyond traditional image and text processing to handle **audio, video, and real-time streaming data**. This advanced capability enables sophisticated applications including video transcription, audiovisual reasoning, and comprehensive multimodal integration. The models support versatile output formats including text, audio, and images, making them powerful tools for complex multimedia applications.

#### Open-Source OLLMs

| Organization     | Model Name                                                                         | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d) | Input | Output | Geographic Origin |
|:-----------------:|:------------------------------------------------------------------------------|:----------:|:-----------:|:-----------:|:-----------:|
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/OpenBMB.svg" alt="OpenBMB" width="200" height="20" />](https://www.openbmb.cn/) | [MiniCPM-o-2_6](https://huggingface.co/openbmb/MiniCPM-o-2_6) | 8.67B | **Incoming** | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/) | [Janus-Pro-7B](https://huggingface.co/deepseek-ai/Janus-Pro-7B) | 7B | **Incoming** | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/FlagOpen.svg" alt="flagopen" width="200" height="23" />](https://flagopen.baai.ac.cn/#/home)    | [Emu3-Gen](https://huggingface.co/BAAI/Emu3-Gen) | 8.49B | **Incoming** | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> | 
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Deepseek.svg" alt="Deepseek" width="200" height="20" />](https://www.deepseek.com/)     | [Janus-1.3B](https://huggingface.co/deepseek-ai/Janus-1.3B) | 1.3B | **Incoming** | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/Alibaba.svg" alt="Alibaba" width="200" height="20" />](https://qwenlm.github.io/)      | [Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) | 10.7B | **Incoming** | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
| [<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Organization/AntGroup.svg" alt="AntGroup" width="200" height="20" />](https://github.com/inclusionAI)| [Ming-Lite-Omni](https://huggingface.co/inclusionAI/Ming-Lite-Omni) | 19.1B | **Incoming** | **Incoming** | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |

<div align="center">

[⬆️ Back to Top](#table-of-contents)

</div>

<br>
