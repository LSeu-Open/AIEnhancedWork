<!-- last-reviewed: 2026-06 -->
<div align="center">

<img src="../Images/AIEnhancedWork.png">

<br>
<br>

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg?style=flat)](../LICENSE.md)

<br>

[Back to the main index](../README.md)

</div>

<br>

# LLM Operations and Observability

Tools for building, evaluating, and operating applications built on top of large
language models — often grouped under the term **LLMOps**. These sit one layer
above the models themselves: they help you assemble LLM and RAG pipelines, route
and cache requests, trace what your application does in production, and measure
output quality over time.

For the models and providers these tools run on, see
[Foundation Models](Foundation_Models.md); for autonomous-agent frameworks
(CrewAI, LangGraph, AutoGen), see [Automation](Automation.md#autonomous-agents).

<br>

## Table of contents

- [Application Frameworks](#application-frameworks)
- [Observability and Tracing](#observability-and-tracing)
- [Evaluation and Testing](#evaluation-and-testing)
- [AI Gateways and Routing](#ai-gateways-and-routing)

<br>
<br>

## Application Frameworks

Libraries for composing LLM calls, retrieval (RAG), and tools into applications.
For agent-runtime frameworks, see the [Automation](Automation.md#autonomous-agents) section.

| Tool | Description | License | Pricing |
|:---|:---|:---:|:---:|
| [LangChain](https://www.langchain.com/) | A widely used framework for building LLM applications by chaining models, prompts, retrieval, and tools. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [LlamaIndex](https://www.llamaindex.ai/) | A data framework for connecting LLMs to your own data, focused on retrieval and RAG pipelines. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Haystack](https://haystack.deepset.ai/) | An open-source framework from deepset for building production RAG and search pipelines. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | <img src="../Images/Pricing/free.svg" alt="free" width="80" height="20" /> |
| [DSPy](https://github.com/stanfordnlp/dspy) | A framework from Stanford for programming (rather than prompting) and automatically optimizing LLM pipelines. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | <img src="../Images/Pricing/free.svg" alt="free" width="80" height="20" /> |
| [Pydantic AI](https://ai.pydantic.dev/) | A type-safe Python agent framework from the Pydantic team, with structured, validated outputs. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | <img src="../Images/Pricing/free.svg" alt="free" width="80" height="20" /> |

<br>

## Observability and Tracing

Tools to log, trace, and monitor LLM and agent applications in production —
inspecting prompts, responses, latency, cost, and errors.

| Tool | Description | License | Pricing |
|:---|:---|:---:|:---:|
| [Langfuse](https://langfuse.com/) | An open-source LLM engineering platform for tracing, prompt management, and evaluation. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [LangSmith](https://www.langchain.com/langsmith) | LangChain's platform for tracing, testing, and monitoring LLM applications (works with or without LangChain). | [<img src="../Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Helicone](https://www.helicone.ai/) | An open-source observability platform that proxies LLM requests to log, monitor, and cache them. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Arize Phoenix](https://phoenix.arize.com/) | An open-source tool for tracing, evaluating, and debugging LLM applications, with strong RAG support. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | <img src="../Images/Pricing/free.svg" alt="free" width="80" height="20" /> |
| [Lunary](https://lunary.ai/) | An open-source platform for monitoring, prompt management, and analytics of LLM apps. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Langtrace](https://www.langtrace.ai/) | An open-source, OpenTelemetry-based tracing tool for LLM applications and frameworks. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |

<br>

## Evaluation and Testing

Tools to measure output quality, regression-test prompts, and catch issues such
as hallucinations before and after deployment.

| Tool | Description | License | Pricing |
|:---|:---|:---:|:---:|
| [Promptfoo](https://www.promptfoo.dev/) | An open-source tool for testing, evaluating, and red-teaming prompts and LLM applications. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [DeepEval](https://github.com/confident-ai/deepeval) | An open-source evaluation framework for LLM outputs, with a wide set of metrics and unit-test-style assertions. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | <img src="../Images/Pricing/free.svg" alt="free" width="80" height="20" /> |
| [Ragas](https://github.com/explodinggradients/ragas) | An open-source framework for evaluating retrieval-augmented generation (RAG) pipelines. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | <img src="../Images/Pricing/free.svg" alt="free" width="80" height="20" /> |
| [Braintrust](https://www.braintrust.dev/) | A platform for evaluating, testing, and iterating on LLM applications with datasets and scoring. | [<img src="../Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Confident AI](https://www.confident-ai.com/) | The cloud platform behind DeepEval, for running, tracking, and sharing LLM evaluations. | [<img src="../Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Galileo](https://galileo.ai/) | An enterprise platform for evaluating and monitoring LLM and agent applications. | [<img src="../Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |

<br>

## AI Gateways and Routing

Tools that sit between your application and the model providers to give you a
single API, with routing, fallbacks, caching, rate limiting, and cost controls.

| Tool | Description | License | Pricing |
|:---|:---|:---:|:---:|
| [LiteLLM](https://www.litellm.ai/) | An open-source gateway exposing 100+ providers behind a single OpenAI-compatible API, with routing and cost tracking. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Portkey](https://portkey.ai/) | An open-source AI gateway with routing, caching, guardrails, and built-in observability. | [<img src="../Images/Licence/opensource.svg" alt="opensource" width="90" height="25" />](https://opensource.com/resources/what-open-source) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) | A gateway that adds caching, rate limiting, logging, and analytics in front of model providers. | [<img src="../Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |
| [OpenRouter](https://openrouter.ai/) | A unified API that routes requests across many proprietary and open models from a single account. | [<img src="../Images/Licence/proprietary.svg" alt="proprietary" width="90" height="15" />](https://www.heavybit.com/library/article/open-source-vs-proprietary) | [<img src="../Images/Pricing/Freemium.svg" alt="Freemium" width="80" height="20" />](https://builtin.com/articles/freemium) |

<br>
<br>

<div align="center">

[Back to the main index](../README.md)

</div>

<br>
