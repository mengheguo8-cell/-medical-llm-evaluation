# 🤖 Medical LLM Prompt Strategy

## Overview

This project compares different prompting strategies for biomedical question answering and evaluates their impact on factual accuracy, scientific reasoning, evidence consistency, and hallucination risk.

The same benchmark questions are tested under standardized prompting conditions.

---

## Strategy 1 — Zero-shot Prompt

### Purpose

Evaluate the model's baseline biomedical knowledge without additional guidance.

### Prompt

You are answering a biomedical research question.

Answer the following question accurately and concisely based on established biomedical knowledge.

Question:
{question}

---

## Strategy 2 — Structured Reasoning Prompt

### Purpose

Encourage structured biomedical reasoning and reduce unsupported conclusions.

### Prompt

You are a biomedical research assistant.

Answer the following biomedical question using scientifically grounded reasoning.

Please structure your response as:

1. Core Answer
2. Biological Mechanism
3. Key Evidence or Scientific Rationale
4. Limitations or Uncertainty

Do not invent references or unsupported facts.

Question:
{question}

---

## Strategy 3 — Evidence-aware Prompt

### Purpose

Evaluate whether explicit evidence constraints improve reliability and reduce hallucination.

### Prompt

You are evaluating a biomedical research question using evidence-based reasoning.

Provide an answer based only on well-established biomedical knowledge.

For each major conclusion:

- distinguish established evidence from interpretation;
- explicitly state uncertainty when evidence is insufficient;
- avoid fabricated citations or unverifiable claims;
- avoid inferring causality from a single biomarker or experimental observation.

Question:
{question}

---

## Experimental Design

Each benchmark question will be evaluated under the three prompting strategies:

| Strategy | Description |
|---|---|
| Zero-shot | Baseline model response |
| Structured | Structured scientific reasoning |
| Evidence-aware | Evidence-constrained reasoning |

Model outputs will be evaluated using the predefined Medical LLM Evaluation Rubric.

---

## Evaluation Hypotheses

### H1

Structured prompting may improve completeness and scientific reasoning compared with zero-shot prompting.

### H2

Evidence-aware prompting may reduce unsupported claims and hallucination risk.

### H3

The effect of prompting strategy may vary according to question difficulty and task type.

---

## Controlled Variables

To improve reproducibility:

- The same benchmark questions should be used across prompt strategies.
- The same model version should be used within each comparison.
- Model settings should remain consistent where configurable.
- Responses should be stored without manual modification before evaluation.
- Evaluation should follow the same scoring rubric.

---

## Output Schema

Each model response should be recorded with:

- Question ID
- Prompt Strategy
- Model
- Model Version
- Response
- Accuracy Score
- Completeness Score
- Reasoning Score
- Evidence Score
- Hallucination Score
- Safety Score
- Overall Score
- Error Category
