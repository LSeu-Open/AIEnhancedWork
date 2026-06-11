<div align="center">

<img src="../Images/AIEnhancedWork.png">

<br>
<br>

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg?style=flat)](../LICENSE.md)

<br>

[Back to the main index](../README.md)

</div>

<br>

# Foundation Models

Large language models and multimodal models. This file is organized into
language-only LLMs (general-purpose models, domain fine-tuned variants, and the
providers and engines used to run them) and multimodal models (vision-language
and omni models).

Fast-moving general rankings are delegated to external leaderboards that stay
current. The curated tables here cover the niche, fine-tuned, and
infrastructure tools that those leaderboards do not track.

<br>

## Table of contents

- [Foundation Models](#foundation-models)
  - [Table of contents](#table-of-contents)
  - [Language Only Large Language Models](#language-only-large-language-models)
    - [Advanced Language and Reasoning LLMs](#advanced-language-and-reasoning-llms)
    - [Finetuned LLMs](#finetuned-llms)
      - [Language Specific](#language-specific)
      - [Role Play](#role-play)
      - [Uncensored](#uncensored)
    - [LLM Providers](#llm-providers)
      - [Cloud-based LLM Providers](#cloud-based-llm-providers)
      - [Local LLM Providers](#local-llm-providers)
      - [LLM Inference Engines](#llm-inference-engines)
  - [Multimodal Language Models](#multimodal-language-models)
    - [Vision Language Models](#vision-language-models)
    - [Omni Large Language Models](#omni-large-language-models)
      - [Open-Source OLLMs](#open-source-ollms)

<br>

## Language Only Large Language Models

Large language models (LLMs) are systems trained on large text corpora to
recognize patterns and generate natural language. This section covers
instruction-tuned general-purpose models, domain fine-tuned variants, and the
providers and engines used to run them.

> [!NOTE]
> Effective use of any model depends on understanding its capabilities, its
> limitations, and the strategies needed to mitigate bias.

### Advanced Language and Reasoning LLMs

General-purpose model quality changes from week to week, so a hand-maintained
ranking goes stale quickly. For current comparisons across quality, context
window, speed, and price, use the leaderboards below. Each links to a filtered
view; on Artificial Analysis you can add or remove models to build your own
comparison.

> [!NOTE]
> **Open-source models**
> - [Artificial Analysis](https://artificialanalysis.ai/models?model-filters=open-source&models=gpt-oss-20b%2Cgpt-oss-120b%2Cgemma-4-31b%2Cmistral-medium-3-5%2Cdeepseek-v4-flash%2Cdeepseek-v4-pro%2Cminimax-m2-7%2Cnvidia-nemotron-3-ultra-550b-a55b%2Ckimi-k2-6%2Cmimo-v2-5-pro%2Ck2-think-v2%2Cglm-5-1%2Cqwen3-5-397b-a17b)
> - [LM Arena](https://arena.ai/leaderboard/text?license=open-source)
>
> **Proprietary models**
> - [Artificial Analysis](https://artificialanalysis.ai/models?model-filters=proprietary&models=gpt-5-4-mini%2Cgpt-5-5-high%2Cgpt-5-5%2Cgpt-5-5-pro%2Cmuse-spark%2Cgemini-3-5-flash%2Cgemini-3-1-pro-preview%2Cclaude-4-5-haiku-reasoning%2Cclaude-fable-5%2Cclaude-opus-4-8%2Cclaude-sonnet-4-6-adaptive%2Cgrok-4-3%2Cnova-2-0-pro-reasoning-medium%2Csolar-pro-3%2Cminimax-m3%2Cqwen3-7-max)
> - [LM Arena](https://arena.ai/leaderboard/text?license=proprietary)

> [!TIP]
> To run open-source models on your own hardware, see
> [How to run LLMs on your machine](../Tutorials/how-to-run-llms-on-your-machine.md).

<br>

<div align="center">

[Back to top](#table-of-contents)

</div>

<br>

### Finetuned LLMs

Fine-tuned LLMs are models adapted to a particular domain, task, or dataset. This adaptation typically improves performance and accuracy within that context, compared to general-purpose use. The categories below focus on axes that general-purpose leaderboards do not rank: language-specific performance, role-play, and uncensored behavior.

#### Language Specific

Models fine-tuned for a specific language or language family.

<img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/in.svg" alt="Indian" width="20" height="15" />   ***Indian languages*** 

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) |
|:------------------:|:----------------------------------------|:-----------------------------------------------------------------------------------------:|:--------------:|:------------:|
| [Sarvam AI](https://www.sarvam.ai/) | [Sarvam-m](https://huggingface.co/sarvamai/sarvam-m) | 24B | 131k | ✔️ |

<img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/jp.svg" alt="japan" width="20" height="15" />  ***Japanese*** 

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) |
|:------------------:|:----------------------------------------|:-----------------------------------------------------------------------------------------:|:--------------:|:------------:|
| [<img src="../Images/Organization/Shisa.svg" alt="Shisa" width="100" height="23" />](https://shisa.ai/) | [Shisa-v2-llama3.1-405b](https://huggingface.co/shisa-ai/shisa-v2-llama3.1-405b) | 405B | 128k | ❌ |
| [<img src="../Images/Organization/Shisa.svg" alt="Shisa" width="100" height="23" />](https://shisa.ai/) | [Shisa-v2-llama3.3-70b](https://huggingface.co/shisa-ai/shisa-v2-llama3.3-70b) | 70B | 128k | ❌ |
| [<img src="../Images/Organization/Shisa.svg" alt="Shisa" width="100" height="23" />](https://shisa.ai/) | [Shisa-v2-qwen2.5-32b](https://huggingface.co/shisa-ai/shisa-v2-qwen2.5-32b) | 32B | 128k | ❌ |
| [<img src="../Images/Organization/Shisa.svg" alt="Shisa" width="100" height="23" />](https://shisa.ai/) | [Shisa-v2-mistral-small-24b](https://huggingface.co/shisa-ai/shisa-v2-mistral-small-24b) | 24B | 128k | ❌ |
| [<img src="../Images/Organization/Shisa.svg" alt="Shisa" width="100" height="23" />](https://shisa.ai/) | [Shisa-v2-mistral-nemo-12b](https://huggingface.co/shisa-ai/shisa-v2-mistral-nemo-12b) | 12B | 128k | ❌ |
| [<img src="../Images/Organization/Shisa.svg" alt="Shisa" width="100" height="23" />](https://shisa.ai/) | [Shisa-v2-mistral-llama3.1-8b](https://huggingface.co/shisa-ai/shisa-v2-llama3.1-8b) | 8B | 128k | ❌ | 
| [<img src="../Images/Organization/Shisa.svg" alt="Shisa" width="100" height="23" />](https://shisa.ai/) | [Shisa-v2-mistral-qwen2.5-7b](https://huggingface.co/shisa-ai/shisa-v2-qwen2.5-7b) | 7B | 128k | ❌ |
| [ELYZA](https://huggingface.co/elyza) | [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) | 8B | 8k | ❌ |
| [Swallow](https://huggingface.co/tokyotech-llm) | [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) | 8B | 128k | ❌ | 

<img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/kr.svg" alt="korea" width="20" height="15" />  ***Korean*** 

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) |
|:------------------:|:----------------------------------------|:-----------------------------------------------------------------------------------------:|:--------------:|:------------:|
| [sktelecom](https://www.sktelecom.com/)  | [A.X-4.0](https://huggingface.co/skt/A.X-4.0) | 72B | 128k | ❌ |
| [sktelecom](https://www.sktelecom.com/)  | [A.X-4.0-Light](https://huggingface.co/skt/A.X-4.0-Light) | 7B | 131k | ❌ |
| [kt](https://ai.kt.com/main)  | [Midm-2.0-Base-Instruct](https://huggingface.co/K-intelligence/Midm-2.0-Base-Instruct) | 12B | 32k | ❌ |
| [kt](https://ai.kt.com/main)  | [Midm-2.0-Mini-Instruct](https://huggingface.co/K-intelligence/Midm-2.0-Mini-Instruct) | 2B | 32k | ❌ |
| [Naver](https://huggingface.co/naver-hyperclovax) | [HyperCLOVAX-SEED-Think-14B](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B) | 14B | ? | ✔️ |
| [Trillion Labs](https://huggingface.co/trillionlabs) | [Trillion-7B-preview](https://huggingface.co/trillionlabs/Trillion-7B-preview) | 7B | ? | ❌ |

<img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/sa.svg" alt="Arabic" width="20" height="15" />  ***Arabic***

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) |
|:------------------:|:----------------------------------------|:-----------------------------------------------------------------------------------------:|:--------------:|:------------:|
| [Inception](https://huggingface.co/inceptionai) | [Jais-family-30B-16K-chat](https://huggingface.co/inceptionai/jais-family-30b-16k-chat) | 30B | 16k | ❌ |
| [ALLaM](https://huggingface.co/ALLaM-AI/ALLaM-7B-Instruct-preview) | [ALLaM-7B-Instruct](https://huggingface.co/ALLaM-AI/ALLaM-7B-Instruct-preview) | 7B | ? | ❌ |

<img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/sg.svg" alt="Southeast Asian" width="20" height="15" />  ***Southeast Asian***

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) |
|:------------------:|:----------------------------------------|:-----------------------------------------------------------------------------------------:|:--------------:|:------------:|
| [Sea AI Lab](https://huggingface.co/sail) | [Sailor2-20B-Chat](https://huggingface.co/sail/Sailor2-20B-Chat) | 20B | 32k | ❌ |
| [AI Singapore](https://huggingface.co/aisingapore) | [Llama-SEA-LION-v3-8B-IT](https://huggingface.co/aisingapore/Llama-SEA-LION-v3-8B-IT) | 8B | 128k | ❌ |

<img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="European" width="20" height="15" />  ***European***

| Organization       | Model Name | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) |
|:------------------:|:----------------------------------------|:-----------------------------------------------------------------------------------------:|:--------------:|:------------:|
| [UTTER](https://huggingface.co/utter-project) | [EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct) | 9B | 4k | ❌ |
| [BSC](https://huggingface.co/BSC-LT) | [Salamandra-7B-Instruct](https://huggingface.co/BSC-LT/salamandra-7b-instruct) | 7B | 8k | ❌ |

<br>

#### Role Play

Models optimized for role-play tasks through specialized training data.

Role-playing is a technique where the model assumes a specific character, profession, or persona to generate more focused, contextually relevant responses.

***Large-scale models (70+ billion parameters)*** : These require substantial amounts of RAM and GPU memory, making local installation impractical for most users. As a result, these models are typically deployed on cloud-based platforms that provide the necessary computational resources.

| Organization       | Base Model                               | Finetuned Model | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Geographic Origin |
|:------------------:|:-----------------------------------------|:------------------------------------------------------------------------------------------|:--------------:|:------------:|:----------------:|:----------------:|
|  [<img src="../Images/Organization/Steelskull.svg" alt="Steelskull" width="100" height="25" />](https://huggingface.co/Steelskull) | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [L3.3-Electra-R1-70b](https://huggingface.co/Steelskull/L3.3-Electra-R1-70b) | 70B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  | 
|  [<img src="../Images/Organization/Steelskull.svg" alt="Steelskull" width="100" height="25" />](https://huggingface.co/Steelskull) | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [L3.3-MS-Nevoria-70b](https://huggingface.co/Steelskull/L3.3-MS-Nevoria-70b) | 70B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [<img src="../Images/Organization/Latitude.svg" alt="LatitudeGames" width="100" height="25" />](https://play.aidungeon.com/) | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [Wayfarer-Large-70B-Llama-3.3](https://huggingface.co/LatitudeGames/Wayfarer-Large-70B-Llama-3.3) | 70B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  **BosonAI**  | [Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) | [Higgs-Llama-3-70B](https://huggingface.co/bosonai/Higgs-Llama-3-70B) | 70B | 32K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [<img src="../Images/Organization/TheDrummer.svg" alt="TheDrummer" width="100" height="25" />](https://huggingface.co/TheDrummer) | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [Anubis-70B-v1.1](https://huggingface.co/TheDrummer/Anubis-70B-v1.1) | 70B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [Sao10K](https://huggingface.co/Sao10K) | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [L3.3-70B-Euryale-v2.3](https://huggingface.co/Sao10K/L3.3-70B-Euryale-v2.3) | 70B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/us.svg" alt="usa" width="20" height="15" />  |
|  [Anthracite](https://huggingface.co/anthracite-org) | [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) | [magnum-v4-72b](https://huggingface.co/anthracite-org/magnum-v4-72b) | 72B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |

<br>

***Mid-sized and smaller models (less than 70 billion parameters)*** :  These models are suitable for local deployment on high-end to mid-range consumer setup. However, such deployments require a significant hardware investment, including a GPU (16–32 GB of VRAM) and related components, typically resulting in total costs ranging from $1000 to $3,000 (or equivalent).

| Organization       | Base Model                               | Finetuned Model | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d)    | [Context Window](https://research.ibm.com/blog/larger-context-window)  | [Reasoning Model](https://www.ibm.com/think/topics/ai-reasoning) | Geographic Origin |
|:------------------:|:-----------------------------------------|:------------------------------------------------------------------------------------------|:--------------:|:------------:|:----------------:|:----------------:|
|  [<img src="../Images/Organization/Gryphe.svg" alt="Gryphe" width="100" height="25" />](https://huggingface.co/Gryphe) | [Qwen3-30B-A3B-Base](https://huggingface.co/Qwen/Qwen3-30B-A3B-Base) | [Pantheon-Proto-RP-1.8-30B-A3B](https://huggingface.co/Gryphe/Pantheon-Proto-RP-1.8-30B-A3B) | 30B | 128K | [Hybrid](https://qwenlm.github.io/blog/qwen3/) |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
|  [<img src="../Images/Organization/Latitude.svg" alt="LatitudeGames" width="100" height="25" />](https://play.aidungeon.com/) | [Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) | [Harbinger-24B](https://huggingface.co/LatitudeGames/Harbinger-24B) | 24B | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  [<img src="../Images/Organization/Gryphe.svg" alt="Gryphe" width="100" height="25" />](https://huggingface.co/Gryphe)   | [Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) | [Pantheon-RP-1.8-24b-Small-3.1](https://huggingface.co/Gryphe/Pantheon-RP-1.8-24b-Small-3.1) | 24B | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  [<img src="../Images/Organization/Gryphe.svg" alt="Gryphe" width="100" height="25" />](https://huggingface.co/Gryphe)   | [Mistral-Small-Instruct-2409](https://huggingface.co/mistralai/Mistral-Small-Instruct-2409) | [Pantheon-RP-Pure-1.6.2-22b-Small](https://huggingface.co/Gryphe/Pantheon-RP-Pure-1.6.2-22b-Small) | 22B | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  [<img src="../Images/Organization/Latitude.svg" alt="LatitudeGames" width="100" height="25" />](https://play.aidungeon.com/) | [Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) | [Muse-12B](https://huggingface.co/LatitudeGames/Muse-12B) | 12B | 128K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  [<img src="../Images/Organization/Latitude.svg" alt="LatitudeGames" width="100" height="25" />](https://play.aidungeon.com/) | [Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) | [Wayfarer-12B](https://huggingface.co/LatitudeGames/Wayfarer-12B) | 12B | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  Wave | [Mistral-Nemo-Base-2407](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407) | [silly-v0.2](https://huggingface.co/wave-on-discord/silly-v0.2) | 12.2B |  128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />   |
|  [<img src="../Images/Organization/Oxygen.svg" alt="Oxygen" width="100" height="25" />](https://huggingface.co/oxyapi) | [Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) | [Oxy-1-small](https://huggingface.co/oxyapi/oxy-1-small) | 14.8B |  131K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
|  [<img src="../Images/Organization/Oxygen.svg" alt="Oxygen" width="100" height="25" />](https://huggingface.co/oxyapi) | [Qwen2-1.5B](https://huggingface.co/Qwen/Qwen2-1.5B) | [Oxy-1-micro](https://huggingface.co/oxyapi/oxy-1-micro) | 1.54B |  131K | ❌ |  <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" />  |
|  [<img src="../Images/Organization/TheDrummer.svg" alt="TheDrummer" width="100" height="25" />](https://huggingface.co/TheDrummer) | [Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) | [Cydonia-24B-v2](https://huggingface.co/TheDrummer/Cydonia-24B-v2) | 24B | 32K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |
|  [<img src="../Images/Organization/TheDrummer.svg" alt="TheDrummer" width="100" height="25" />](https://huggingface.co/TheDrummer) | [Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) | [Rocinante-12B-v1.1](https://huggingface.co/TheDrummer/Rocinante-12B-v1.1) | 12B | 128K | ❌ | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/eu.svg" alt="eu" width="20" height="15" />  |


<br>
<br>

#### Uncensored

Mainstream leaderboards do not measure how readily a model answers contentious
or restricted prompts, so this ranking is delegated to a leaderboard built for
that axis.

> [!NOTE]
> - [UGI Leaderboard (Uncensored General Intelligence)](https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard)

<br>

<div align="center">

[Back to top](#table-of-contents)

</div>

<br>

### LLM Providers

#### Cloud-based LLM Providers

> [!Tip]
> Reference the [Artificial Analysis Leaderboard](https://artificialanalysis.ai/leaderboards/providers) for comparisons of LLM providers across key metrics: pricing, token generation speed, response latency, and context window.

***Major Cloud AI Providers***

These are typically large tech companies that develop and offer access to their own flagship LLMs. Access is usually via APIs, and they manage all the underlying infrastructure.

| Tool             | Description                                                                                                                 | Models      | Pricing     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [AI21 Labs](https://www.ai21.com/) | Develops the Jamba family of hybrid SSM-Transformer models, focused on long context and efficiency. |  [Jamba Large 1.6](https://huggingface.co/ai21labs/AI21-Jamba-Large-1.6) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Anthropic](https://www.anthropic.com/claude) | Develops the Claude family of models, trained with Constitutional AI to be helpful, harmless, and honest. | [Claude Fable5](https://www.anthropic.com/news/claude-fable-5-mythos-5), [Claude Opus 4.8](https://www.anthropic.com/claude/opus) and more  | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [Cohere](https://cohere.com/) | Develops the Command family of enterprise-focused models for retrieval, generation, and tool use. | [Command A](https://cohere.com/blog/command-A) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Databricks](https://www.databricks.com/) | A unified, open analytics platform that provides tools and services for data processing, analytics, and artificial intelligence at scale. | [Dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct) | <img src="../Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Deepseek](https://chat.deepseek.com/) | A Chinese AI lab known for its open-weight DeepSeek models, with strong reasoning at low cost. | [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) and more | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Google](https://gemini.google.com/) | Develops the Gemini family of multimodal models for language, vision, and reasoning. | [Gemini 3.5](https://deepmind.google/models/gemini/pro/), [Gemini 3.5 Flash](https://deepmind.google/models/gemini/flash/) and more | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [Mistral AI](https://mistral.ai/) | A French AI company developing open-weight and commercial language models, agents, and developer tools. | [Mistral Medium 3.5](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5/) and more | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [OpenAI](https://chatgpt.com/) | Develops the GPT family of language models, along with DALL-E for images and Whisper for speech. | [GPT-5.5](https://openai.com/index/introducing-gpt-5/) and more | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Qwen](https://chat.qwen.ai/) | Alibaba's Qwen model family, spanning open-weight and hosted models. | [Qwen3.7-Max](https://qwen.ai/) and more |  [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Reka](https://chat.reka.ai/) | Develops multimodal Reka models with strong vision, audio, and video understanding. | [Reka Flash 3.1](https://huggingface.co/RekaAI/reka-flash-3.1) and more | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [xAI](https://x.ai/) | Develops the Grok family of models, integrated with the X platform and available via API. | [Grok 4.3](https://grok.com/) and more | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |

<br>

<div align="center">

[Back to top](#table-of-contents)

</div>

<br>

***Aggregator & Specialized Cloud Platforms***

These platforms offer access to a variety of models from different developers, including many popular open-source models and sometimes proprietary ones, often through a single API or interface. Some may offer specialized hardware or value-added services like fine-tuning.

| Tool             | Description                                                                                                                 | Models      | Pricing     |
|:-----------------|-----------------------------------------------------------------------------------------------------------------------------|:-----------:|:-----------:|
| [Amazon Web Services (AWS)](https://aws.amazon.com/bedrock/) | Provides hosted access to many open-source and proprietary models through Amazon Bedrock and SageMaker. | Large Panel of Open source and Proprietary Models | <img src="../Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Baseten](https://www.baseten.co/) | An inference platform for deploying and serving open-source and custom models in production, with autoscaling and low-latency serving. | Large Panel of Open source Models | <img src="../Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Cerebras](https://inference.cerebras.ai/) | An AI company that has developed innovative hardware and software solutions for AI computing. | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) and more | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [DeepInfra](https://deepinfra.com/chat) | A platform that provides scalable and cost-effective infrastructure for deploying machine learning models. | Large Panel of Open source Models | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Featherless](https://featherless.ai/) | A subscription-based, serverless LLM hosting provider that gives you instant, unlimited access to thousands of Hugging Face models, all via a simple API and with no infrastructure hassles. | Large Panel of Open source Models | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Fireworks](https://fireworks.ai/) | An inference platform for deploying and fine-tuning open-source models in production. | Large Panel of Open source Models | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Groq](https://groq.com/) | Specializes in high-performance AI inference with custom LPU (Language Processing Unit) hardware, offering models like Meta's Llama 3. | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) and more  | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  | 
| [Hyperbolic](https://app.hyperbolic.xyz/models) | An open-access AI cloud platform offering affordable GPU compute and open-source model inference. | Large Panel of Open source Models | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [LeptonAI](https://www.lepton.ai/) | A platform that provides cloud-based infrastructure and tools for deploying and running AI applications efficiently. | Large Panel of Open source Models | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Lumo by Proton](https://lumo.proton.me/guest) | A privacy-first AI assistant developed by Proton, the company known for Proton Mail, Proton VPN, and Proton Pass. | Panel of Open source Models | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Microsoft Azure](https://azure.microsoft.com/) | A comprehensive suite of AI services and tools designed to help developers and organizations build, deploy, and manage AI applications at scale. | Large Panel of Open source and Proprietary Models | <img src="../Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Nebius](https://studio.nebius.com/) | An inference-as-a-service platform for running open-source models | Large Panel of Open source Models | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Novita](https://novita.ai/models) | An inference-as-a-service platform for running open-source models | Large Panel of Open source Models | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [OpenRouter](https://openrouter.ai/) |  A versatile platform designed to provide access to a wide range of large language models (LLMs) from both proprietary and open-source sources. |  Large Panel of Open source and Proprietary Models | <img src="../Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Parasail](https://www.parasail.io/) | An AI infrastructure platform for deploying and scaling open-source models. | Large Panel of Open source Models | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Poe](https://poe.com) | An AI chatbot aggregator platform developed by Quora that provides users access to multiple advanced language models and chatbots within a single interface. | Large Panel of Open source and Proprietary Models | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium)  |
| [Replicate](https://replicate.com/) | A platform for running and deploying open-source models through a simple API; now part of Cloudflare. | Large Panel of Open source Models | <img src="../Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [SambaNova](https://sambanova.ai/) | An artificial intelligence company that provides a comprehensive AI platform for enterprises. | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) and more | <img src="../Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> |
| [Together](https://www.together.ai/) | A cloud platform designed for building and running generative AI applications. | Large Panel of Open source Models | <img src="../Images/Pricing/Paid.svg" alt="Paid" width="80" height="20" /> | 

<br> 

<div align="center">

[Back to top](#table-of-contents)

</div>

<br>

#### Local LLM Providers

> [!IMPORTANT]
> To run LLMs locally, see the [setup guide](../Tutorials/how-to-run-llms-on-your-machine.md) for private, on-device model use.

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
| [LM Studio](https://lmstudio.ai/) |  Elegant UI with the ability to run every Hugging Face repository. | All | Large Panel of Open source Models |
| [Msty](https://msty.app/) | An AI chat application that offers a user-friendly interface for interacting with both local and online AI language models. | All | Large Panel of Open source Models |
| [Ollama](https://ollama.com/) | Fastest when used on the terminal, and any model can be downloaded with a single command. | All | All Open source Models |
| [Open WebUI](https://openwebui.com/) | Self-hosted, open-source web interface designed for running and managing LLMs locally or offline. | All | All Open source Models |
| [Silly Tavern](https://sillytavern.app/) | Open-source LLM frontend designed for power users. | All | All Open source Models |
| [Witsy](https://witsyai.com/) | Open-source LLM frontend designed for power users. | All | All Open source Models |
| [Pocketpal](https://github.com/a-ghorbani/pocketpal-ai) |  AI assistant powered by small language models (SLMs) that run directly on your phone. | Android / iOS | All Open source Models |

<br>

<div align="center">

[Back to top](#table-of-contents)

</div>

<br>

#### LLM Inference Engines

This table lists notable frameworks and libraries designed for running and serving Large Language Models efficiently, focusing on performance, scalability, and deployment.

> The landscape evolves rapidly. Some tools might integrate techniques or components from others (e.g., many serving frameworks might leverage optimized kernels like FlashAttention or specific backend libraries like `vLLM` or `TensorRT-LLM`). This table focuses on the primary offering or framework level.

| Engine/Server          | Developer/Origin       | Key Features & Focus                                                                 | Primary Use Case(s)         | Notes                                                              |
| :--------------------- | :--------------------- | :----------------------------------------------------------------------------------- | :-------------------------- | :----------------------------------------------------------------- |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | Georgi Gerganov et al. | Highly optimized C++ inference for GGUF models; CPU & GPU (Metal, CUDA, OpenCL) support. | Local inference, experimentation, backend for other tools | Foundational library/CLI, broad hardware support.                    |
| [MLX LM](https://github.com/ml-explore/mlx-lm) | Apple | Inference and fine-tuning on Apple Silicon; built on the MLX unified-memory framework. | Local inference on Mac | Powers Ollama's Apple Silicon backend as of 2026. |
| [ExLlamaV2](https://github.com/turboderp-org/exllamav2) | turboderp | Fast inference for NVIDIA consumer GPUs; EXL2 quantization format and custom CUDA kernels. | Local inference (consumer NVIDIA GPUs) | Among the fastest single-user engines on RTX hardware. |
| [vLLM](https://github.com/vllm-project/vllm) | vLLM Project (Berkeley) | High-throughput serving library; PagedAttention, continuous batching.                 | Production serving, research | Primarily Python library, integrates with frameworks like Ray, OpenLLM. |
| [Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference) | Hugging Face           | Production-ready server; Optimized for HF models, high throughput, streaming.       | Production serving          | Rust/Python based; in maintenance mode since 2026, with Hugging Face pointing users to vLLM and SGLang. |
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

[Back to top](#table-of-contents)

</div>

<br>

## Multimodal Language Models

<br>

### Vision Language Models

Vision Language Models (VLMs) are multimodal models that understand and generate
content by combining visual and text input, supporting tasks such as image
captioning, visual question answering, and object recognition. For technical
background, see the [Hugging Face VLM overview](https://huggingface.co/blog/vlms).

The VLM landscape moves as quickly as the text-only one, so the size-tiered
ranking that previously lived here is delegated to external leaderboards that
are kept current.

> [!NOTE]
> - [Open VLM Leaderboard (OpenCompass)](https://huggingface.co/spaces/opencompass/open_vlm_leaderboard)
> - [LM Arena - vision](https://arena.ai/leaderboard/vision)

> [!TIP]
> To run open-source VLMs on your own hardware, see
> [How to run LLMs on your machine](../Tutorials/how-to-run-llms-on-your-machine.md).

<br>

<div align="center">

[Back to top](#table-of-contents)

</div>

<br>

### Omni Large Language Models

Omni Large Language Models (OLLMs) extend beyond image and text to handle audio, video, and real-time streaming data, supporting tasks such as video transcription, audiovisual reasoning, and multimodal integration. They can produce text, audio, and image output.

This is a fast-moving, mostly open-weight niche with no established leaderboard, so the table below is a curated snapshot of current open models rather than a ranking.

#### Open-Source OLLMs

| Organization     | Model Name                                                                         | [Model Sizes](https://catherinebreslin.medium.com/what-is-a-parameter-3d4b7736c81d) | Input | Output | Geographic Origin |
|:-----------------:|:------------------------------------------------------------------------------|:----------:|:-----------:|:-----------:|:-----------:|
| [<img src="../Images/Organization/Alibaba.svg" alt="Alibaba" width="100" height="20" />](https://qwenlm.github.io/) | [Qwen3-Omni-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct) | 30B (A3B) | Text, Image, Audio, Video | Text, Speech | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [<img src="../Images/Organization/OpenBMB.svg" alt="OpenBMB" width="80" height="20" />](https://www.openbmb.cn/) | [MiniCPM-o 4.5](https://huggingface.co/openbmb/MiniCPM-o-4_5) | 9B | Text, Image, Audio, Video | Text, Speech | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [<img src="../Images/Organization/AntGroup.svg" alt="AntGroup" width="80" height="20" />](https://github.com/inclusionAI) | [Ming-Lite-Omni-1.5](https://huggingface.co/inclusionAI/Ming-Lite-Omni-1.5) | 19.1B | Text, Image, Audio, Video | Text, Image, Speech | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [Baichuan](https://huggingface.co/baichuan-inc) | [Baichuan-Omni-1.5](https://huggingface.co/baichuan-inc/Baichuan-Omni-1d5) | 7B | Text, Image, Audio, Video | Text, Speech | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [VITA](https://huggingface.co/VITA-MLLM) | [VITA-1.5](https://huggingface.co/VITA-MLLM/VITA-1.5) | 7B | Text, Image, Audio, Video | Text, Speech | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [Infinigence](https://huggingface.co/Infinigence) | [Megrez-3B-Omni](https://huggingface.co/Infinigence/Megrez-3B-Omni) | 3B | Text, Image, Audio | Text | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [<img src="../Images/Organization/Deepseek.svg" alt="Deepseek" width="100" height="20" />](https://www.deepseek.com/) | [Janus-Pro-7B](https://huggingface.co/deepseek-ai/Janus-Pro-7B) | 7B | Text, Image | Text, Image | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [<img src="../Images/Organization/FlagOpen.svg" alt="flagopen" width="100" height="23" />](https://flagopen.baai.ac.cn/#/home) | [Emu3](https://huggingface.co/BAAI/Emu3-Gen) | 8B | Text, Image, Video | Text, Image, Video | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |
| [<img src="../Images/Organization/ByteDance.svg" alt="ByteDance" width="100" height="20" />](https://www.bytedance.com/en/) | [BAGEL-7B-MoT](https://huggingface.co/ByteDance-Seed/BAGEL-7B-MoT) | 7B (14B MoE) | Text, Image | Text, Image | <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/cn.svg" alt="China" width="20" height="15" /> |

<div align="center">

[Back to top](#table-of-contents)

</div>

<br>
