# Overview of LLm Models, Grouped by License and Purpose

## Table of Contents

  + [Proprietary Models](#proprietary-models)
    - [01.ai](#01)
    - [Anthropic](#anthropic)
    - [Databricks](#databricks)
    - [Google](#google)
    - [Mistral](#mistral)
    - [MosaicML](#mosaicml)
    - [OpenAI](#openai)
    - [Perplexity.ai](#perplexity)
      
  + [Open source Models](#open-source-models)
    - [01.ai](#01)
    - [Alibaba](#alibaba)
    - [Cognitive Computations](#cognitive-computations)
    - [Cohere](#cohere)
    - [Deepseek](#deepseek)
    - [Google](#google)
    - [Hugging Face](#hugging-face)
    - [LMSYS](#lmsys)
    - [Meta](#meta)
    - [Microsoft](#microsoft)
    - [Mistral](#mistral)

<br>

# Introduction

 ➡️ To provide a clearer picture of model performance within an organization, I'll include Elo Rankings : 
 
 🔴 Bottom Tier → 🟢 Top Tier

**Smaller LLM models are not necessarily older or inferior versions of larger models**. They can be designed to run efficiently on lower-end machine specs or for specific tasks, such as text classification or sentiment analysis. These models may use different architectures or techniques to achieve better performance on certain hardware or applications.

 ➡️ You can find an overall leaderboard at [chat.lmsys.org](https://chat.lmsys.org/?leaderboard).

 > [!IMPORTANT]
> If you're concerned about **privacy issues related to cloud based LLM providers** or you want to experiment with chatbots check out this ***[practical guide](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Tutorials/run-local-llm-ollama-and-page-assist.md)*** on how to set up and run your own model on your local machine.

## Proprietary Models

### **01**

- [Yi-Large](https://www.01.ai/) (Proprietary) 🟢

### **Anthropic**
- [Claude 3 Opus](https://docs.anthropic.com/claude/docs/models-overview#model-comparison) (Proprietary) 🟢
- [Claude 3 Sonnet](https://docs.anthropic.com/claude/docs/models-overview#model-comparison) (Proprietary)
- [Claude 3 Haiku](https://docs.anthropic.com/claude/docs/models-overview#model-comparison) (Proprietary)
- [Claude 2.1](https://docs.anthropic.com/claude/docs/models-overview#model-comparison) (Proprietary)
- [Claude 2](https://docs.anthropic.com/claude/docs/models-overview#model-comparison) (Proprietary)
- [Claude Instant 1.2](https://docs.anthropic.com/claude/docs/models-overview#model-comparison) (Proprietary) 🔴

### **Databricks**
- [DBRX](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm) (Proprietary) 🟢

### **Google**
- [Gemini Advanced](https://gemini.google.com/advanced?hl=en) (Proprietary) 
- [Gemini Flash](https://deepmind.google/technologies/gemini/flash/) (Proprietary) 
- [Gemini 1.5 Pro](https://gemini.google.com/?hl=en) (Proprietary) 🟢
- [Gemini Pro (API)](https://ai.google.dev/docs/gemini_api_overview) (Proprietary)
- [Gemini Pro](https://blog.google/technology/ai/gemini-api-developers-cloud/) (Proprietary)
- [PaLM-chat-Bison-001](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#foundation_models) (Proprietary)

### **Mistral**
- [Mistral Large](https://mistral.ai/news/mistral-large/) (Proprietary) 🟢
- [Mistral Medium](https://mistral.ai/) (Proprietary)
- [Mistral-Next](https://mistral.ai/) (Proprietary) 🔴
  
### **MosaicML**
- [MPT-30B-chat](https://huggingface.co/mosaicml/mpt-30b-chat) (Proprietary) 🟢
- [MPT-7B-chat](https://huggingface.co/mosaicml/mpt-7b-chat) (Proprietary) 🔴

### **OpenAI**
- [GPT-4o](https://openai.com/index/hello-gpt-4o/) (Proprietary) 🟢
- [GPT-4 Turbo](https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4) (Proprietary) 
- [GPT-4](https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4) (Proprietary)
- [GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5-turbo) (Proprietary) 🔴

### **Perplexity**
- [pplx-70b-online](https://www.perplexity.ai/hub/blog/introducing-pplx-online-llms) (Proprietary) 🟢
- [pplx-7b-online](https://www.perplexity.ai/hub/blog/introducing-pplx-online-llms) (Proprietary) 🔴

## Open source Models

### **01**

> Yi-1.5 (upgraded version of Yi)
- [Yi-1.5-34B-Chat](https://huggingface.co/01-ai/Yi-1.5-34B-Chat) (Open) 🟢
- [Yi-1.5-9B-Chat](https://huggingface.co/01-ai/Yi-1.5-9B-Chat) (Open)
- [Yi-1.5-6B-Chat](https://huggingface.co/01-ai/Yi-1.5-6B-Chat) (Open)
  
> Yi
- [Yi-34B-Chat](https://huggingface.co/01-ai/Yi-34B-Chat) (Open)
- [Yi-6B-Chat](https://huggingface.co/01-ai/Yi-6B-Chat) (Open) 🔴
  
> Yi VL (Vision)
- [Yi-VL-34B](https://huggingface.co/01-ai/Yi-VL-34B) (Open)
- [Yi-VL-6B](https://huggingface.co/01-ai/Yi-VL-6B) (Open)
  
### **Alibaba**

- [Qwen-Max](https://qwenlm.github.io/blog/qwen-max-0428/) (Open) ❓

> Qwen2
- [Qwen2-72B-instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct) (Open) 🟢
- [Qwen2-7B-instruct](https://huggingface.co/Qwen/Qwen2-7B-Instruct) (Open)
- [Qwen2-1.5B-instruct](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct) (Open)
- [Qwen2-0.5B-instruct](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct) (Open) 
  
> Qwen1.5 (the improved version of Qwen)
- [Qwen1.5-110B-Chat](https://qwenlm.github.io/blog/qwen1.5-110b/) (Open) 
- [Qwen1.5-72B-Chat](https://huggingface.co/Qwen/Qwen1.5-72B-Chat) (Open) 
- [Qwen1.5-32B-Chat](https://huggingface.co/Qwen/Qwen1.5-32B-Chat) (Open)
- [Qwen1.5-14B-Chat](https://huggingface.co/Qwen/Qwen1.5-14B-Chat) (Open)
- [Qwen1.5-7B-Chat](https://huggingface.co/Qwen/Qwen1.5-7B-Chat) (Open)
- [Qwen1.5-4B-Chat](https://huggingface.co/Qwen/Qwen1.5-4B-Chat) (Open)
- [Qwen1.5-0.5B-Chat](https://huggingface.co/Qwen/Qwen1.5-0.5B-Chat) (Open) 
  
> Qwen
- [Qwen-72B-Chat](https://huggingface.co/Qwen/Qwen-72B-Chat) (Open) 
- [Qwen-14B-Chat](https://huggingface.co/Qwen/Qwen-14B-Chat) (Open) 
- [Qwen-7B-Chat](https://huggingface.co/Qwen/Qwen-7B-Chat) (Open) 
- [Qwen-1.8B-Chat](https://huggingface.co/Qwen/Qwen-1_8B-Chat) (Open) 🔴

> CodeQwen
- [CodeQwen1.5-7B-Chat](https://huggingface.co/Qwen/CodeQwen1.5-7B-Chat) (Open) 🟢
  
### **Cognitive Computations**

> Qwen
- [dolphin-2.9.2-qwen2-7b](https://huggingface.co/cognitivecomputations/dolphin-2.9.2-qwen2-7b) (Open)
- [dolphin-2.9.2-qwen2-72b](https://huggingface.co/cognitivecomputations/dolphin-2.9.2-qwen2-72b) (Open)
  
> Mixtral
- [dolphin-2.2.1-mistral-7b](https://huggingface.co/cognitivecomputations/dolphin-2.2.1-mistral-7b) (Open) 🔴
- [dolphin-2.5-mixtral-8x7b](https://huggingface.co/cognitivecomputations/dolphin-2.5-mixtral-8x7b) (Open)
- [dolphin-2.9.1-mixtral-1x22b](https://huggingface.co/cognitivecomputations/dolphin-2.9.1-mixtral-1x22b) (Open)
  
> Llama
- [dolphin-2.9-llama3-8b](https://huggingface.co/cognitivecomputations/dolphin-2.9-llama3-8b) (Open)
- [dolphin-2.9.1-llama-3-70b](https://huggingface.co/cognitivecomputations/dolphin-2.9.1-llama-3-70b) (Open) 🟢
  
> Phi
- [dolphin-2.9.2-Phi-3-Medium-abliterated](https://huggingface.co/cognitivecomputations/dolphin-2.9.2-Phi-3-Medium-abliterated) (Open)

### **Cohere**

> Aya 23
- [aya-23-35B](https://huggingface.co/CohereForAI/aya-23-35B) (Open) 
- [aya-23-8B](https://huggingface.co/CohereForAI/aya-23-8B) (Open) 🔴
  
> Command R Plus
- [Command R+](https://huggingface.co/CohereForAI/c4ai-command-r-plus) (Open) 🟢
  
> Command R
- [Command R](https://huggingface.co/CohereForAI/c4ai-command-r-v01) (Open) 

### **DeepSeek**

> LLM
- [DeepSeek-LLM-67b-Chat](https://huggingface.co/deepseek-ai/deepseek-llm-67b-chat) (Open) 🟢
- [DeepSeek-LLM-7b-Chat](https://huggingface.co/deepseek-ai/deepseek-llm-7b-chat) (Open) 🔴
  
> Coder
- [DeepSeek-Coder-33B-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-33b-instruct) (Open) 🟢
- [DeepSeek-Coder-6.7B-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) (Open)
- [DeepSeek-Coder-7B-instruct-v1.5](https://huggingface.co/deepseek-ai/deepseek-coder-7b-instruct-v1.5) (Open)
- [DeepSeek-Coder-1.3B-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-instruct) (Open) 🔴

> VL (Vision)
- [DeepSeek-vl-7b-Chat](https://huggingface.co/deepseek-ai/deepseek-vl-7b-chat) (Open) 
- [DeepSeek-vl-1.3b-Chat](https://huggingface.co/deepseek-ai/deepseek-vl-1.3b-chat) (Open) 
  
> Math
- [DeepSeek-math-7b-instruct](https://huggingface.co/deepseek-ai/deepseek-math-7b-instruct) 
  
> MoE
- [DeepSeek-moe-16b-Chat](https://huggingface.co/deepseek-ai/deepseek-moe-16b-chat) 

### **Google**

> Gemma
- [Gemma-1.1-7b-it](https://huggingface.co/google/gemma-1.1-7b-it) 🟢
- [Gemma-1.1-2b-it](https://huggingface.co/google/gemma-1.1-2b-it)
- [Gemma-7b-it](https://huggingface.co/google/gemma-7b-it)
- [Gemma-2b-it](https://huggingface.co/google/gemma-2b-it) 🔴
   
> PaliGemma (Vision)
- [Paligemma-3b-pt-224](https://huggingface.co/google/paligemma-3b-pt-224)
  
> CodeGemma (Coding)
- [Codegemma-1.1-7b-it](https://huggingface.co/google/codegemma-1.1-7b-it) 🟢
- [Codegemma-1.1-2b](https://huggingface.co/google/codegemma-1.1-2b)
- [Codegemma-7b-it](https://huggingface.co/google/codegemma-7b-it-GGUF)
- [Codegemma-2b](https://huggingface.co/google/codegemma-2b-GGUF) 🔴

  
### **Hugging Face**

> Zephyr ORPO
- [Zephyr-orpo-141b-A35b-v0.1](https://huggingface.co/HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1) (Open) 🟢
  
> Zephyr 7B
- [zephyr-7b-alpha](https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha) (Open) 🔴
- [zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) (Open)
- [zephyr-7b-gemma-v0.1](https://huggingface.co/HuggingFaceH4/zephyr-7b-gemma-v0.1) (Open) 
  
> Starchat (Coding)
- [Starchat2-15b-v0.1](https://huggingface.co/HuggingFaceH4/starchat2-15b-v0.1) (Open)
  
### **LMSYS**
- [Vicuna-33B](https://huggingface.co/lmsys/vicuna-33b-v1.3) (open) 🟢
- [Vicuna-13B](https://huggingface.co/lmsys/vicuna-13b-v1.5) (open)
- [Vicuna-7B](https://huggingface.co/lmsys/vicuna-7b-v1.5) (open)
- [FastChat-T5-3B](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0) (open) 🔴
  
### **Meta**
- [Llama-3-70b-Instruct](https://llama.meta.com/llama3/) (Open) 🟢
- [Llama-3-8b-Instruct](https://llama.meta.com/llama3/) (Open)
- [Llama-2-70b-chat](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) (Open)
- [Llama-2-13b-chat](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) (Open)
- [Llama-2-7b-chat](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) (Open) 🔴

### **Microsoft**

> Phi-3
- [Phi-3-vision-128k-instruct](https://huggingface.co/microsoft/Phi-3-vision-128k-instruct) (Open) 
- [Phi-3-medium-128k-instruct](https://huggingface.co/microsoft/Phi-3-medium-128k-instruct) (Open) 🟢
- [Phi-3-small-128k-instruct](https://huggingface.co/microsoft/Phi-3-small-128k-instruct) (Open)  
- [Phi-3-mini-128k-instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct) (Open) 

> Phi-1
- [Phi-1.5](https://huggingface.co/microsoft/phi-1_5) (Open) 
- [Phi-1](https://huggingface.co/microsoft/phi-1) (Open) 🔴
  
### **Mistral**

> Mixtral (MoE)
- [Mixtral-8x7b-Instruct-v0.1](https://mistral.ai/news/mixtral-of-experts/) (Open)
- [Mixtral-8x22b-Instruct-v0.1](https://mistral.ai/news/mixtral-8x22b/) (Open) 🟢
  
> Mistral
- [Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) (Open) 🔴
- [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) (Open)
- [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) (Open)

> Codestral (Coding)
- [Codestral-22B-v0.1](https://huggingface.co/mistralai/Codestral-22B-v0.1) (Open)




  


