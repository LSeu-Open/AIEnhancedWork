<!-- last-reviewed: 2026-06 -->
<div align="center">

<img src="../Images/Tutorials/CodingAI.png">

<br>
<br>

This guide covers the tools and models for coding with AI: editors, extensions,
terminal agents, providers, and how to pick a model for the job.

Reading time: ~16 min

<br>

[Back to the main index](../README.md)

</div>

<br>

# How to Use LLMs in Coding

## Table of Contents

* [Introduction](#introduction)
* [AI Coding Tools](#ai-coding-tools)
  * [AI-Powered IDEs](#ai-powered-ides)
    * [Cursor](#cursor)
    * [Windsurf](#windsurf)
    * [Zed](#zed)
    * [Void](#void)
  * [VS Code Extensions](#vs-code-extensions)
    * [Cline](#cline)
    * [Continue](#continue)
    * [GitHub Copilot](#github-copilot)
    * [Kilo Code](#kilo-code)
  * [Agentic CLI Coding Tools](#agentic-cli-coding-tools)
    * [Claude Code](#claude-code)
    * [OpenAI Codex CLI](#openai-codex-cli)
    * [Gemini CLI](#gemini-cli)
    * [Aider](#aider)
* [Choosing a Provider](#choosing-a-provider)
* [Find the Model that is Right for You](#find-the-model-that-is-right-for-you)
  * [Estimating Hardware Needs](#estimating-hardware-needs)
  * [Coding Leaderboards](#coding-leaderboards)

<br>

## Introduction

Modern development environments integrate language models to assist with code
completion, refactoring, testing, and multi-file changes through natural
language. Used well, they speed up routine work and lower the barrier to
unfamiliar code; used carelessly, they introduce subtle bugs and erode the
habit of understanding your own codebase.

**Benefits**

* **Productivity**: automate repetitive tasks, generate boilerplate, and get contextual suggestions, freeing you to focus on harder problems.
* **Code quality**: AI-assisted analysis can surface bugs, security issues, and code smells earlier.
* **Learning**: explanations and examples in context help when working with a new language, framework, or codebase.

**Trade-offs**

* **Errors and bias**: models can produce confident but wrong code, or inherit biases from their training data.
* **Skill atrophy**: over-reliance can weaken your ability to reason about code without assistance.
* **Security and privacy**: code sent to a hosted model leaves your machine; review each tool's data-handling policy.
* **Cost**: the strongest models are paid, and local models need capable hardware.

> [!CAUTION]
> Treat AI-generated code as a suggestion, not an authority. Validate it against
> official documentation, run your tests, and review every change before
> committing it.

<br>
<br>

## AI Coding Tools

The tools below fall into three groups: full **IDEs** (usually VS Code forks
with AI built in), **extensions** that add AI to an editor you already use, and
**terminal agents** that work from the command line.

Where a tool connects to external models, the exact list changes constantly, so
this guide describes the *kind* of models each supports rather than pinning
specific versions. For the current model landscape, see
[Foundation Models](../Docs/Foundation_Models.md).

### AI-Powered IDEs

#### Cursor

[Cursor](https://cursor.com/) is a VS Code-based editor with language models
integrated throughout: contextual completion, codebase-aware chat, and
natural-language multi-file edits. As a fork of VS Code, it imports your
existing extensions, themes, and keybindings.

* **Models**: Cursor's own models plus frontier models from Anthropic, OpenAI, and Google.
* **Notable**: whole-codebase context, an agent mode for multi-step tasks, and a privacy mode that keeps your code off Cursor's servers.
* **License/Pricing**: proprietary; free tier with paid plans.

#### Windsurf

[Windsurf](https://windsurf.com/editor) is an agentic VS Code fork built around
**Cascade**, its engine for codebase understanding, command execution, and
multi-file editing. It is now developed by **Cognition** (the team behind Devin),
which has integrated Devin's autonomous agents into the editor.

* **Models**: Windsurf's in-house **SWE** models, plus frontier models from the major providers.
* **Notable**: background/autonomous agents dispatched from the IDE, live previews, and predictive navigation.
* **License/Pricing**: proprietary; free tier with paid plans.

#### Zed

[Zed](https://zed.dev/) is a high-performance editor written in Rust, with native
AI features: agentic editing and **Edit Prediction** (powered by its open-source
**Zeta** model). It runs on macOS, Linux, and Windows.

* **Models**: its own Zeta model for edit prediction, plus external LLMs (Anthropic, OpenAI, Google, and others) for chat and agentic editing.
* **Notable**: very fast, with native Git, remote development, multibuffer editing, collaboration, and Vim-style modal editing.
* **License/Pricing**: open-source editor; AI features can use your own API keys or Zed's hosted option.

#### Void

[Void](https://voideditor.com/) is an open-source VS Code fork focused on privacy:
it connects directly to any LLM (cloud or local via Ollama) with no proprietary
backend in between.

* **Models**: any provider you configure, including local models.
* **Notable**: tab autocomplete, inline edits, and an agent that can read and modify your codebase; your VS Code extensions and settings transfer over.
* **License/Pricing**: open-source and free.

> [!NOTE]
> Void's active development is paused — the released builds still work, but the
> core team is not currently shipping fixes or features. Consider this if you
> rely on ongoing maintenance.

<br>

### VS Code Extensions

If you'd rather keep your editor, these add AI to VS Code (and, for some, to
JetBrains IDEs). They also work in [VSCodium](https://vscodium.com/), the
fully open-source build of VS Code without Microsoft's telemetry and branding.

#### Cline

[Cline](https://cline.bot/) is an open-source VS Code extension that plans before
it acts: it proposes a step-by-step plan, explains its reasoning, and applies
changes behind a checkpoint system so you can review and roll back.

* **Models**: bring your own API key (Anthropic, OpenAI, Google, and others), a Cline account, or enterprise endpoints (AWS Bedrock, GCP Vertex, Azure). Local models are supported.
* **Notable**: monitors terminals, files, and error logs; connects to external tools and data via MCP servers.
* **License/Pricing**: open-source; pay for whatever model/provider you use.

#### Continue

[Continue](https://www.continue.dev/) provides open-source extensions for VS Code
and JetBrains, plus a hub of models, rules, prompts, and docs for building custom
AI assistants tailored to your codebase and workflow.

* **Models**: works with many providers and with local models via Ollama and LM Studio.
* **Notable**: tab autocomplete, context from files/docs/issues, highlight-and-edit, and shareable assistant configurations.
* **License/Pricing**: open-source; pay for whatever model/provider you use.

#### GitHub Copilot

[GitHub Copilot](https://github.com/features/copilot) is an AI pair programmer
built into GitHub and available across major IDEs (VS Code, Visual Studio,
JetBrains, Neovim, Xcode, and more). It offers completions, chat, code review,
and an agent mode that can plan, edit, test, and open pull requests.

* **Models**: a selectable mix of models from OpenAI, Anthropic, and Google, depending on your plan.
* **Notable**: agent mode and a coding agent that can take an issue to a pull request; MCP support; next-edit suggestions.
* **License/Pricing**: proprietary; free tier, paid Pro/Pro+ plans, and free access for verified students, teachers, and popular open-source maintainers.

#### Kilo Code

[Kilo Code](https://github.com/Kilo-Org/kilocode) is an open-source VS Code
extension that builds on ideas from Cline and Roo Code, offering a team of
specialized agent modes for different kinds of tasks. It became a leading
successor after Roo Code was discontinued in 2026.

* **Models**: model-agnostic — bring your own provider or use local models.
* **Notable**: multiple agent modes, MCP support, and adjustable autonomy from supervised to mostly hands-off.
* **License/Pricing**: open-source; pay for whatever model/provider you use.

<br>

### Agentic CLI Coding Tools

Terminal agents are the fastest-growing category of AI coding tools. They run in
your shell, read and edit files across a project, run commands and tests, and
iterate toward a goal — without an editor. They pair naturally with any editor
(including VSCodium), and most also offer editor extensions.

#### Claude Code

[Claude Code](https://www.claude.com/product/claude-code) is Anthropic's
terminal-based coding agent. It works in your existing project, reads and edits
files, runs commands and tests, and uses tools and MCP servers. It also ships
**editor extensions for VS Code/VSCodium and JetBrains** that surface the agent
alongside your code, and a cloud/web version for delegating longer tasks.

* **Models**: Anthropic's Claude family (Opus / Sonnet / Haiku).
* **Notable**: strong multi-step agentic editing, subagents, hooks, MCP, and a permissions model for controlling what it can do.
* **License/Pricing**: proprietary; included with Claude Pro/Max subscriptions or billed via the API.

#### OpenAI Codex CLI

[OpenAI Codex CLI](https://github.com/openai/codex) is OpenAI's open-source
terminal coding agent. It runs locally, edits your project, and executes
commands, with a sandbox/approval model for safety. OpenAI also offers a matching
IDE extension and a cloud agent.

* **Models**: OpenAI's models (including its coding-focused models).
* **Notable**: open-source, configurable autonomy and sandboxing, and MCP support.
* **License/Pricing**: open-source CLI; usage billed via your OpenAI account (a subscription tier is also available).

#### Gemini CLI

[Gemini CLI](https://github.com/google-gemini/gemini-cli) is Google's
open-source terminal agent for Gemini. It brings Gemini into the shell for
codebase questions, edits, and command execution, and supports tools and MCP.

* **Models**: Google's Gemini models.
* **Notable**: open-source (Apache-2.0), a large free usage tier, and a large context window suited to big codebases.
* **License/Pricing**: open-source; generous free tier, with paid options via an API key.

#### Aider

[Aider](https://aider.chat/) is an open-source command-line pair programmer with
first-class **Git integration** — it makes focused commits as it edits, so every
change is easy to review or undo. It is model-agnostic and works with hosted or
local models. The Aider team also maintains the widely cited polyglot coding
benchmark.

* **Models**: most providers (Anthropic, OpenAI, Google, DeepSeek, and others), plus local models.
* **Notable**: repository mapping for context, automatic commits, and a lightweight, scriptable workflow.
* **License/Pricing**: open-source (Apache-2.0) and free; pay only for the model you use.

> [!TIP]
> Other strong terminal agents include [OpenCode](https://opencode.ai/) and
> [Goose](https://block.github.io/goose/) (both open-source and model-agnostic),
> and [Warp](https://www.warp.dev/) (an agentic terminal). See the
> [Agentic Coding Tools](../Docs/Coding_and_Software_Development.md#agentic-coding-tools)
> section for the full list.

<br>
<br>

## Choosing a Provider

A "provider" is whatever gives you access to a model: the lab that builds it, a
cloud platform that hosts many models, or software that runs models on your own
machine. Your choice affects which models you can use, the cost and licensing,
the integration experience, and how your code is handled.

Providers fall into three broad types:

* **Major cloud labs** (Anthropic, OpenAI, Google, Mistral, DeepSeek, and others): their own flagship models via API. Best when you want the most capable proprietary models.
* **Aggregators and inference platforms** (OpenRouter, Together, Fireworks, Groq, Cerebras, and others): many models — often open-source — behind one API, sometimes with specialized hardware for high-speed inference.
* **Local self-hosting**: run models on your own hardware, so your code never leaves your machine. Covered in [How to Run LLMs on Your Machine](how-to-run-llms-on-your-machine.md).

The full, maintained list of providers and the models they serve lives in the
[LLM Providers](../Docs/Foundation_Models.md#llm-providers) section of the
Foundation Models page ([cloud-based](../Docs/Foundation_Models.md#cloud-based-llm-providers)
and [local](../Docs/Foundation_Models.md#local-llm-providers)).

To choose between the types, weigh your priorities: maximum capability points to
the cloud labs; absolute privacy and offline use point to local; broad model
choice and high-speed or low-cost inference point to aggregators. Budget,
hardware, and how much setup you're willing to do narrow it down from there.

<br>
<br>

## Find the Model that is Right for You

Once you've picked a provider, choose a model. Two things matter most: whether
your hardware can run it (for local models), and how well it performs on coding
tasks.

### Estimating Hardware Needs

The estimates below assume a model **quantized to 4-bit** (a common balance of
size and quality — see [How to Select the Right Quantized Model](how-to-select-the-right-quantized-model.md)).
Actual usage varies with the runtime, context length, and architecture.

> [!IMPORTANT]
> You can **run models without a GPU**: the model loads into system RAM and runs
> on the CPU. This works but is much slower than running on a GPU or on a machine
> with fast unified memory.

| Model size (parameters, approx. Q4) | Estimated VRAM / memory | Typical hardware |
|-------------------------------------|-------------------------|------------------|
| > 100B (very large)                 | 64GB - 400GB+           | Multiple data-center GPUs (NVIDIA H100/H200/B200) or a high-capacity unified-memory machine; often run in the cloud |
| ~50B - 100B (large)                 | 32GB - 64GB+            | 1-2 high-end GPUs (RTX 5090, A100) or 64GB+ of unified memory (Apple Silicon, AMD Ryzen AI Max) |
| ~15B - 50B (medium)                 | 16GB - 40GB             | Single high-end consumer GPU (RTX 4090 / 5080 / 5090) or 32GB+ of unified memory |
| ~7B - 15B (small-medium)            | 8GB - 16GB              | Mid-to-high range consumer GPU (RTX 4070 / 5070) or 16GB+ of unified memory |
| < 7B (small)                        | 4GB - 8GB+ VRAM, or 8GB+ system RAM (CPU) | Entry-level GPU, a recent laptop, or any Apple Silicon Mac |

For local coding, strong open-source options at the time of writing include the
**Qwen3 Coder** family, **DeepSeek** models, and **GLM** and **Codestral**
variants — but this moves quickly, so use the leaderboards below for the current
ranking.

### Coding Leaderboards

Coding ability changes with every model release, so rather than a fixed table,
use a live leaderboard:

> [!NOTE]
> - **[Artificial Analysis — Coding Agents](https://artificialanalysis.ai/agents/coding-agents)**: ranks models on agentic coding tasks (terminal use, multi-step edits), reflecting how these models are actually used in the tools above.
> - **[LM Arena — WebDev](https://arena.ai/leaderboard/code/webdev)**: human-preference rankings for web-development tasks.
>
> Filter by open-source or proprietary on each site to match your provider
> choice, and cross-reference both — they measure different things.

<br>
<br>

<div align="center">

[Back to top](#table-of-contents)

</div>

<br>
