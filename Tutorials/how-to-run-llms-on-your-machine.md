<div align="center"> 
 
<img src="https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Images/Tutorials/TextGeneration.png">

<br>
<br>

 ***This guide explains how to set up and run language models on your computer, enabling you to maintain full control over your AI tools.***
 
 <br>

***<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20with%20Monocle.png" alt="Face with Monocle" width="25" height="25" /> Reading Time : +15min***

</div> 

## Table of Contents

* [Introduction](#introduction)
* [Find the Model that is right for you](#find-the-model-that-is-right-for-you)
* [LM Studio (Beginner)](#lm-studio)
* [Ollama (Intermediate)](#ollama)
* [Llama.cpp (Expert)](#llama-cpp)

<br>

## Introduction

This tutorial guides **individuals seeking greater control and transparency in their data processing by setting up a local Large Language Model (LLM) environment.*** We'll use Ollama as the backend and the Page Assist extension in your browser for this purpose.

#### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20in%20Clouds.png" alt="Face in Clouds" width="25" height="25" /> Challenges with Cloud-Based AI Services

* **Privacy Concerns** : Your data traverses remote servers, raising questions about who might access it and how it will be handled.
* **Lack of Transparency**: Complex algorithms make it difficult to understand or verify how your data is processed, potentially leading to biased results.
* **Security Risks** : Major AI providers handle vast amounts of user data, making them attractive targets for breaches.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Love-You%20Gesture.png" alt="Love-You Gesture" width="25" height="25" /> Benefits of Running LLMs Locally

* **Data Control** : Keep your information entirely on your machine, ensuring it's not shared with external parties.
* **Instant Performance** : Eliminate internet latency for real-time tasks and continuous interaction.
* **Simplified Compliance** : Maintain complete control over data storage and processing, easing adherence to privacy regulations.

<br>

## Find the Model that is right for you

Now that you've chosen your provider, let's find the right model for your coding needs, particularly if you are considering self-hosting open-source models.

Understanding hardware requirements is crucial. The estimates below generally assume models are quantized (specifically using a common 4-bit quantization), a process that reduces size and memory footprint, offering a balance between performance and quality. Actual performance can vary based on software and system configuration.

Learn more about quantization [here](https://huggingface.co/blog/merve/quantization).

> [!IMPORTANT]
> Please note that while it is possible to **run models without a GPU**, doing so will load the model into RAM and perform inference using the CPU.
>
> ***This approach will significantly slow down inference speeds.***

For evaluating specific model performance on coding tasks, the **[Aider polyglot coding leaderboard](https://aider.chat/docs/leaderboards/)** is an excellent resource. It benchmarks LLMs on complex coding challenges across multiple languages.

### Open Source Models: Estimating Hardware Needs

Instead of listing every model here (as that detailed list is maintained in our **[Open Source Models Tables](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/Docs/Foundation_Models.md#open-source-models)**), here's a general guide to help you estimate VRAM/RAM requirements based on model size when using 4-bit quantization:

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

## LM Studio 

***(Beginner)*** LM Studio is a powerful yet user-friendly tool for running large language models (LLMs) on your local machine. It's especially well-suited for beginners who want to experiment with AI without needing advanced technical skills or an internet connection.

### Why Use LM Studio?

LM Studio offers several advantages that make it ideal for **newcomers**:

**Ease of Use**: It provides a graphical user interface (GUI), so you don't need to know command-line tools or coding.

**Privacy**: Since models run locally, your data stays on your machine — no uploading required.

**Model Access**: You can easily download and use many popular open-source LLMs.

### System Requirements

Before installing LM Studio, make sure your system meets the following minimum requirements:

**RAM**: At least 8GB (16GB or more is recommended for larger models).

**Storage**: Enough space to store model files (typically between 2GB and 20GB+).

**CPU/GPU**: A modern CPU is sufficient. An NVIDIA or AMD GPU can improve performance, but it's not required. Mac users with M1/M2/M3/M4 chips don't need a separate GPU.

**Operating System**:: Windows (x86/ARM), macOS (M1–M4 recommended), or Linux (x86 with AVX2 support)

### Installation

To get started, follow these simple steps:

1. Go to the official [LM Studio website](https://lmstudio.ai/).
2. Download the installer for your operating system.
3. Run the installer and follow the on-screen instructions.
4. Launch LM Studio after installation is complete.

### Finding and Downloading Models

Once installed, you can use LM Studio to find, download, and run a wide variety of open-source LLMs.

1. Open LM Studio and click the Discover tab (magnifying glass icon) or use Ctrl + 2 (Windows/Linux) / Cmd + 2 (macOS).
2. Browse featured models or search for specific ones like "Llama", "Phi-3", "Mistral", or "Gemma" based on the info you gathered in the [Find the Model that is right for you section](#find-the-model-that-is-right-for-you).
3. Choose a model version: many are available in quantized forms (e.g., Q4_K_M), which are optimized for performance and size. LM Studio will automatically select the most suitable version based on your machine specifications.
4. Click Download to get the model.

### Loading a Model

After downloading, you can load the model into LM Studio.

1. Go to the AI Chat tab (chat bubble icon) or use Ctrl + 3 (Windows/Linux) / Cmd + 3 (macOS).
2. Open the Model Loader by clicking the dropdown at the top center or using Ctrl + L (Windows/Linux) / Cmd + L (macOS).
3. Select the model you downloaded.
4. Click Load — LM Studio will allocate memory to run the model. Default loading settings usually work well for beginners.

### Chatting with the Model

Once a model is loaded, you can start interacting with it:

1. Type your question or prompt in the message box at the bottom of the screen.
2. Press Enter to send.
3. The AI will process and respond locally — no internet connection required.

You'll see the response appear immediately in the chat window.

For more detailed information, please refer to the [official LM Studio documentation](https://lmstudio.ai/docs/app). Read more on [Downloading Models](https://lmstudio.ai/docs/app/basics/download-model) or [Manage chats](https://lmstudio.ai/docs/app/basics/chat).

<br>
<br>

## Ollama 

***(Intermediate)*** Ollama is our top recommendation for running LLMs locally for non beginners users due to its robust integration capabilities and adaptability. 

As an example, you will find below a step-by-step guide on setting up Ollama as a local model provider through an accessible and user-friendly interface. 

Please follow  official documentations if you wish to use other providers, or open an issue on this repository if you want a dedicated section for your preferred provider in this file.

### Installation

| Platform          | Installation Method |
|:-----------------:|:--------------------:|
| **macOS**         | [Download](https://ollama.com/download/Ollama-darwin.zip) |
| **Windows**       | [Download](https://ollama.com/download/OllamaSetup.exe)  |
| **Linux**         | [Manual install instructions](https://github.com/ollama/ollama/blob/main/docs/linux.md) |
| **Docker**        | [Ollama Docker image](https://hub.docker.com/r/ollama/ollama) is available on Docker Hub.  |

### Quickstart

<br>

To run and chat with [Llama 3.1](https://ollama.com/library/llama3.1) write the following input in a terminal:

```
ollama run llama3.1
```
This will allow you to chat with the **llama3.1:8B model** within the command-line interface (CLI). See the list of models available on [ollama.com/library](https://ollama.com/library 'ollama model library'). 

To download a model without launching it, simply enter the following command:

```
ollama pull llama3.1
```
To view the list of models you've downloaded, simply use the following command:

```
ollama list
```

<br>

### User Friendly Ollama Models Interaction

For those who prefer a more user-friendly experience, we'll demonstrate how to interact with your Ollama model through our browser-based interface, which provides a graphical and intuitive way of working with your LLM. We will be using the [Page assist extension](https://github.com/n4ze3m/page-assist).

Page Assist is an open-source Chrome Extension that provides a Sidebar and Web UI for your Local AI model. It allows you to interact with your model from any webpage.

Want to explore other possibilities? Take a look at the alternative solutions available in our [Local Providers section](https://github.com/LSeu-Open/AIEnhancedWork/blob/main/README.md#local-providers-1).

#### Installation and setup 

You can install the extension from the [Chrome Web Store](https://chromewebstore.google.com/detail/page-assist-a-web-ui-for/jfgfiigpkhlkbnfnbobbkinehhfdhndo)

#### Browser Support

| Browser  | Sidebar | Chat With Webpage | Web UI |
| -------- | ------- | ----------------- | ------ |
| Chrome   | ✅      | ✅                | ✅     |
| Brave    | ✅      | ✅                | ✅     |
| Firefox  | ✅      | ✅                | ✅     |
| Vivaldi  | ✅      | ✅                | ✅     |
| Edge     | ✅      | ❌                | ✅     |
| Opera    | ❌      | ❌                | ✅     |
| Arc      | ❌      | ❌                | ✅     |


If needed, see the [Manual Installation](https://github.com/n4ze3m/page-assist) instructions on their github repository.

Once the extension is installed Just click on the extension icon and it'll take you straight to the chatGPT-like UI.

After installation, I suggest the following steps :

- A center message **must letting you know that Ollama is running in the background**, ready to handle your requests.
- To the top left corner, a **dropdown menu** awaits, listing all models you've installed and are currently available for interaction. Simply **select the model with which you wish to engage.**
- In the **top left icon**, click to open a sidebar that enables Conversation Management. This feature allows you to **manage and organize your conversations**.

> [!Note]
> When you first interact with your model, there might be a brief delay as it loads into memory. But once you're chatting away, responses should come quickly !
> Just remember that processing time can vary depending on your computer's specs.

#### Usage

##### Sidebar

Once the extension is installed, you can **open the sidebar via context menu or keyboard shortcut**.  By exploiting this sidebar functionality, you can engage in seamless conversations with your model while **leveraging the current web page as contextual reference (website, documentation, PDF...).**

▶️ in order to use `chat with the current page` option you need to set a Embedding Model in the `RAG Settings`.

> Default Keyboard Shortcut: `Ctrl+Shift+P`

##### Web UI

You can open the Web UI by clicking on the extension icon which will open a new tab with the Web UI.

> Default Keyboard Shortcut: `Ctrl+Shift+L`

> [!Note]
> You can change the keyboard shortcuts from the extension settings on the Chrome Extension Management page.

<br>
<br>

## Llama cpp 

***(Expert)*** Llama.cpp is a high-performance C++ library designed to run large language models (LLMs) efficiently on various hardware platforms. It supports both standard CPUs and systems with limited resources, making it ideal for deploying quantized models in the **GGUF** format.

### Prerequisites

Before you begin, make sure the following tools are installed:

1. Git
Git is used to clone the Llama.cpp repository from GitHub.

2. Build Tools (Based on Your OS)

- Linux:
Install essential build tools using `apt`:

```bash
sudo apt update && sudo apt install build-essential cmake git
```

- macOS:
Install Xcode command line tools:

```bash
xcode-select --install
```

- Windows:
Use **MSYS2** or a similar environment that provides C++ compilation tools such as `make`, `g++`, and `clang++`. Git for Windows often includes these tools by default.

---

3. Python (Optional)

Python is optional but required if you plan to use the Python bindings (`llama-cpp-python`). You can install it using:

```bash
sudo apt install python3   # Linux
brew install python     # macOS
```

### Installation and Setup

You have two main options for using Llama.cpp: either via its **C++ executable** or through **Python bindings**.

#### Option 1: Using the Core C++ Executable

This is the most straightforward way to run Llama.cpp on your system.

**Step 1: Clone the Repository**

Open a terminal and run:

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
```

**Step 2: Build the Project**

Compile the source code using `make`:

```bash
make
```

This builds the main executable, `./main`, which is optimized for **CPU inference**. For significantly improved performance on compatible hardware, you can build with GPU acceleration (e.g., using `make LLAMA_CUDA=1` for NVIDIA GPUs). Refer to the official documentation for specific commands for CUDA, Metal (macOS), and other backends.

> 🔧 **Note**: For GPU acceleration (CUDA, Metal), you'll need to use specific build commands. See the [Llama.cpp Build Documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) for more details.


**Step 3: Verify the Build (Optional)**

You can check the available command-line options by running:

```bash
./main -h
```

This will display all the supported flags and usage examples.


#### Option 2: Using Python Bindings (`llama-cpp-python`)

If you want to use Llama.cpp within Python, follow these steps:

**Step 1: Create a Virtual Environment**

It's recommended to create an isolated environment to avoid package conflicts.

Using **Conda**:

```bash
conda create --name llama-cpp-env
conda activate llama-cpp-env
```

Using **Python's built-in `venv`** (Linux/macOS):

```bash
python -m venv llama-cpp-env
source llama-cpp-env/bin/activate  # On Linux/macOS
```

On Windows:

```bash
llama-cpp-env\Scripts\activate
```

**Step 2: Install the Python Bindings**

Install `llama-cpp-python` using pip:

```bash
pip install llama-cpp-python
```

**Step 3: Verify Installation (Optional)**

Run a simple test to confirm it's working:

```bash
python -c "from llama_cpp import Llama; print('llama-cpp-python installed successfully!')"
```

### Getting a Model

Llama.cpp primarily uses models in the **GGUF** format, which are quantized versions of popular large language models. These allow running large models with reduced memory usage.

### Steps to Get a GGUF Model:

1. Visit [Hugging Face Hub](https://huggingface.co/) and search for models compatible with Llama.cpp (e.g., "Llama-3-8B-Instruct-GGUF").
2. Choose the desired **quantization level**:
   - `Q4_K_M`: Low memory usage, good for most users.
   - `Q5_K_M`, `Q8_0`: Higher quality but uses more memory.
3. Download the `.gguf` file and save it in a known location (e.g., `models/`).


### Running Inference

#### Option 1 : Using the Core Executable (`./main`)

Run inference from the command line:

```bash
./main -m <path_to_model.gguf> -p "<your_prompt>" [options]
```

**Example:**

```bash
./main -m ./models/llama-3-8b-instruct.Q4_K_M.gguf \
      -p "Explain the theory of relativity in simple terms." \
      -n 256 \          # Max tokens to generate
      -c 2048 \         # Context size (must be >= prompt length + max tokens)
      --temp 0.7        # Temperature setting for randomness
```

**Flags explained:**

- `-m`: Path to your GGUF model file.
- `-p`: The prompt or input text you want the model to respond to.
- `-n`: Maximum number of tokens (words/subwords) to generate.
- `-c`: Context size — how much text the model considers at once. Should be >= prompt length + max tokens.
- `--temp`: Temperature value for controlling randomness.


#### Option 2 : Using Python Bindings

Here's a simple example script (`inference.py`) that loads and runs a model:

```python
from llama_cpp import Llama

# Load the model (adjust path as needed)
llm = Llama(
    model_path="./models/llama-3-8b-instruct.Q4_K_M.gguf",
    n_ctx=2048,      # Context window size
    n_gpu_layers=-1,   # Use GPU if available
    verbose=True     # Show detailed output
)

# Define the prompt
user_prompt = "What are the main benefits of using Python?"

# Generate text
output = llm(
    user_prompt,
    max_tokens=256,
    temperature=0.7,
    top_p=0.9,
    echo=True,        # Include the prompt in output
    stop=["\n", "User:"]
)

# Process and print the result
if output and 'choices' in output and len(output['choices']) > 0:
    generated_text = output['choices'][0]['text']
    response_only = generated_text.replace(user_prompt, "", 1).strip()
    print("Model Response:\n", response_only)
else:
    print("No output generated.")
```

**To run the script:**

```bash
python inference.py
```

## Next Steps

This tutorial covers the basics of setting up and using Llama.cpp. For more advanced features such as:

- **Multi-GPU support**
- **Grammar-based output control**
- **Quantization tuning**
- **Custom sampling methods**

You can refer to the [official Llama.cpp documentation](https://github.com/ggml-org/llama.cpp).

<br>
<br>
