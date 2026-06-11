<!-- last-reviewed: 2026-06 -->
<div align="center">

<img src="../../Images/AIEnhancedWork.png">

<br>
<br>

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg?style=flat)](../../LICENSE.md)

<br>

[Back to the main index](../../README.md)

</div>

<br>

# Multilinguality

This supplementary page lists the languages officially supported by each LLM
family, with the source for each list. Counts and lists reflect what the vendor
or model card states; most models also handle additional languages that are not
formally listed.

<br>

## Table of contents

- [ChatGPT and o-Series Families](#chatgpt-and-o-series-families)
- [Claude Families](#claude-families)
- [Command Family](#command-family)
- [DeepSeek Family](#deepseek-family)
- [Falcon Families](#falcon-families)
- [Gemini Family](#gemini-family)
- [Gemma Family](#gemma-family)
- [Granite Family](#granite-family)
- [Llama Families](#llama-families)
- [Mistral Families](#mistral-families)
- [Nova Family](#nova-family)
- [SmolLM Family](#smollm-family)
- [Qwen Families](#qwen-families)

<br>
<br>

## ChatGPT and o-Series Families

Source: [OpenAI documentation](https://platform.openai.com/docs/)

**57** officially supported languages: Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

<br>

## Claude Families

### Claude 4 family

Source: [Anthropic multilingual support](https://platform.claude.com/docs/en/docs/build-with-claude/multilingual-support)

**15** benchmarked languages: English, Spanish, Portuguese, Italian, French, Indonesian, German, Arabic, Chinese (Simplified), Korean, Japanese, Hindi, Bengali, Swahili, and Yoruba.

> [!NOTE]
> Anthropic does not publish a fixed list of supported languages. The set above is the languages benchmarked in the multilingual support documentation; Claude processes input and output in most world languages that use standard Unicode characters.

<br>

## Command Family

Source: [Command A](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025), [Command R](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) and [Command R+](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024)

**23** officially supported languages: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, Chinese, Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.

<br>

## DeepSeek Family

Source: [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

DeepSeek does not publish an enumerated list of supported languages. The V4 models (V4-Pro and V4-Flash) are trained primarily on English and Chinese, with broad additional multilingual coverage; benchmarks are reported in English and Chinese by default.

<br>

## Falcon Families

### Falcon H1

Source: [Falcon-H1](https://falcon-lm.github.io/blog/falcon-h1/)

**18** officially supported languages: Arabic, Czech, German, English, Spanish, French, Hindi, Italian, Japanese, Korean, Dutch, Polish, Portuguese, Romanian, Russian, Swedish, Urdu, and Chinese.

### Falcon 3

Source: [Falcon3-10B-Instruct](https://huggingface.co/tiiuae/Falcon3-10B-Instruct)

**4** officially supported languages: English, French, Spanish, and Portuguese.

<br>

## Gemini Family

Source: [Gemini supported languages](https://cloud.google.com/gemini/docs/codeassist/supported-languages)

**38** officially supported languages: Arabic, Bengali, Bulgarian, Chinese (Simplified and Traditional), Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Latvian, Lithuanian, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Thai, Turkish, Ukrainian, and Vietnamese.

<br>

## Gemma Family

Source: [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)

Gemma 4 provides out-of-the-box support for **35+** languages and was pre-trained on over **140** languages. Google does not publish an exhaustive list.

<br>

## Granite Family

Source: [granite-3.3-8b-instruct](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct)

**12** officially supported languages: English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese.

<br>

## Llama Families

### Llama 4

Source: [Llama 4](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct)

**12** officially supported languages: Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese.

> [!NOTE]
> Llama 4 was pre-trained on a broader collection of languages than the 12 supported languages (pre-training includes 200 total languages). Developers may fine-tune Llama 4 models for languages beyond the 12 supported languages provided they comply with the Llama 4 Community License and the Acceptable Use Policy.

### Llama 3.1, 3.2 and 3.3

Source: [Llama 3.1](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct), [Llama 3.2](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) and [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)

**8** officially supported languages: English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai.

This list also applies to fine-tuned models built on Llama 3.1, such as Sonar (Perplexity).

> [!NOTE]
> Llama 3.1, 3.2 and 3.3 were trained on a broader collection of languages than the 8 supported languages. Developers may fine-tune these models for languages beyond the 8 supported languages provided they comply with the Llama Community License and the Acceptable Use Policy, and in such cases are responsible for ensuring that any use in additional languages is done in a safe and responsible manner.

<br>

## Mistral Families

### Mixtral 8x22B

Source: [Mixtral 8x22B](https://mistral.ai/news/mixtral-8x22b)

**5** officially supported languages: English, French, Italian, German, and Spanish.

### Mistral Large

Source: [Mistral Large 2](https://mistral.ai/news/mistral-large-2407)

**13** officially supported languages: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, and Hindi.

> [!NOTE]
> No separate list is published for Mistral Medium 3; it appears to match the Mistral Large list.

### Magistral Small and Medium

Source: [Magistral](https://mistral.ai/news/magistral)

**8** officially supported languages: English, French, Spanish, German, Italian, Arabic, Russian, and Simplified Chinese.

### Mistral Small

Source: [Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)

**11** officially supported languages: English, French, German, Spanish, Italian, Chinese, Japanese, Korean, Portuguese, Dutch, and Polish.

### Ministral

Source: [Ministral-8B-Instruct-2410](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410)

**10** officially supported languages: English, French, German, Spanish, Italian, Chinese, Japanese, Korean, Portuguese, and Russian.

<br>

## Nova Family

Source: [Amazon Nova user guide](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html)

**15** officially supported languages: English, German, Spanish, French, Italian, Japanese, Korean, Arabic, Simplified Chinese, Russian, Hindi, Portuguese, Dutch, Turkish, and Hebrew.

<br>

## SmolLM Family

Source: [SmolLM3](https://huggingface.co/blog/smollm3)

**6** officially supported languages: English, French, Spanish, German, Italian, and Portuguese.

<br>

## Qwen Families

### Qwen3.5 Family (open source)

Source: [Qwen3.5](https://qwen.ai/blog?id=qwen3.5)

**201** languages and dialects, expanding on the 119 covered by Qwen3. Alibaba does not publish a full enumerated list for the 201; the table below is the per-family breakdown published with the Qwen3 release, which Qwen3.5 builds on and extends.

| Language Family | Languages & Dialects |
|:------------------:|:---------------------------------------------------------------------------------|
| Indo-European | English, French, Portuguese, German, Romanian, Swedish, Danish, Bulgarian, Russian, Czech, Greek, Ukrainian, Spanish, Dutch, Slovak, Croatian, Polish, Lithuanian, Norwegian Bokmål, Norwegian Nynorsk, Persian, Slovenian, Gujarati, Latvian, Italian, Occitan, Nepali, Marathi, Belarusian, Serbian, Luxembourgish, Venetian, Assamese, Welsh, Silesian, Asturian, Chhattisgarhi, Awadhi, Maithili, Bhojpuri, Sindhi, Irish, Faroese, Hindi, Punjabi, Bengali, Oriya, Tajik, Eastern Yiddish, Lombard, Ligurian, Sicilian, Friulian, Sardinian, Galician, Catalan, Icelandic, Tosk Albanian, Limburgish, Dari, Afrikaans, Macedonian, Sinhala, Urdu, Magahi, Bosnian, Armenian |
| Sino-Tibetan | Chinese (Simplified Chinese, Traditional Chinese, Cantonese), Burmese |
| Afro-Asiatic | Arabic (Standard, Najdi, Levantine, Egyptian, Moroccan, Mesopotamian, Ta'izzi-Adeni, Tunisian), Hebrew, Maltese |
| Austronesian | Indonesian, Malay, Tagalog, Cebuano, Javanese, Sundanese, Minangkabau, Balinese, Banjar, Pangasinan, Iloko, Waray (Philippines) |
| Dravidian | Tamil, Telugu, Kannada, Malayalam |
| Turkic | Turkish, North Azerbaijani, Northern Uzbek, Kazakh, Bashkir, Tatar |
| Tai-Kadai | Thai, Lao |
| Uralic | Finnish, Estonian, Hungarian |
| Austroasiatic | Vietnamese, Khmer |
| Other | Japanese, Korean, Georgian, Basque, Haitian, Papiamento, Kabuverdianu, Tok Pisin, Swahili |

<br>

### Qwen3.7 (proprietary)

Source: [Qwen](https://qwen.ai/)

Qwen3.7 (Max and Plus) is the proprietary tier of the Qwen3.x lineup and shares its broad multilingual coverage. Alibaba does not publish a separate language list for it.

<br>

### Qwen2 Family

Source: [Qwen2.5](https://qwenlm.github.io/blog/qwen2.5/#takeaways)

**29** officially supported languages, including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, and Arabic.

<br>
