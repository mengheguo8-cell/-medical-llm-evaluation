# 📚 Reference Answers & Evidence

## Overview

This document provides reference answers for the Medical LLM Evaluation benchmark.

Reference answers are designed as gold-standard evaluation targets rather than exhaustive textbook responses. They define the key biomedical concepts that an LLM response should contain.

---

## Q001 — Basic Mechanism of CAR-T Cell Therapy

**Domain:** CAR-T  
**Difficulty:** Easy

### Reference Answer

CAR-T cell therapy genetically modifies T cells to express a chimeric antigen receptor (CAR) that recognizes a specific antigen on target cells.

After antigen recognition, CAR signaling activates the engineered T cells, promoting cytokine production, proliferation, and cytotoxic activity against antigen-expressing cells.

### Key Evaluation Points

- Genetically engineered T cells
- Chimeric antigen receptor
- Antigen-specific recognition
- T-cell activation
- Cytotoxic killing

---

## Q002 — CAR-T Limitations in Solid Tumors

**Domain:** CAR-T  
**Difficulty:** Medium

### Reference Answer

CAR-T therapy faces several barriers in solid tumors, including heterogeneous antigen expression, limited trafficking and infiltration into tumor tissue, an immunosuppressive tumor microenvironment, T-cell exhaustion, and the difficulty of identifying tumor-specific antigens without significant on-target/off-tumor toxicity.

### Key Evaluation Points

- Antigen heterogeneity
- Poor tumor trafficking
- Limited infiltration
- Immunosuppressive tumor microenvironment
- T-cell dysfunction or exhaustion
- On-target/off-tumor toxicity

---

## Q003 — Antigen Heterogeneity and CAR-T Failure

**Domain:** CAR-T  
**Difficulty:** Hard

### Reference Answer

When tumor cells express different levels or types of target antigens, CAR-T cells preferentially eliminate antigen-positive cells while antigen-negative or low-antigen tumor populations may survive.

This selective pressure can promote antigen escape and contribute to disease persistence or relapse.

### Key Evaluation Points

- Heterogeneous antigen expression
- Selective pressure
- Antigen-negative tumor cells
- Antigen escape
- Relapse or treatment failure

---

## Q004 — Tumor Microenvironment

**Domain:** Tumor Immunology  
**Difficulty:** Easy

### Reference Answer

The tumor microenvironment consists of tumor cells, immune cells, stromal cells, extracellular matrix, signaling molecules, and metabolic factors surrounding a tumor.

It can regulate antitumor immunity by influencing immune-cell recruitment, activation, proliferation, metabolism, and effector function.

### Key Evaluation Points

- Multiple cellular components
- Extracellular environment
- Immune regulation
- Immune-cell function

---

## Q005 — Immunosuppressive TME and T-cell Function

**Domain:** Tumor Immunology  
**Difficulty:** Medium

### Reference Answer

An immunosuppressive tumor microenvironment can impair T-cell activity through inhibitory checkpoint signaling, suppressive immune cells, immunoregulatory cytokines, metabolic competition, hypoxia, and nutrient deprivation.

These factors may reduce T-cell proliferation, cytokine production, cytotoxicity, and persistence.

### Key Evaluation Points

- Immune checkpoints
- Suppressive immune cells
- Immunosuppressive cytokines
- Metabolic restriction
- Hypoxia
- Reduced T-cell effector function

---

## Q006 — Mechanisms of Oncolytic Viruses

**Domain:** Oncolytic Virus  
**Difficulty:** Easy

### Reference Answer

Oncolytic viruses can preferentially infect and replicate in tumor cells, resulting in direct tumor-cell lysis.

Tumor destruction can also release tumor-associated antigens and inflammatory signals that stimulate innate and adaptive antitumor immune responses.

### Key Evaluation Points

- Tumor-selective infection
- Viral replication
- Direct oncolysis
- Tumor-antigen release
- Immune activation

---

## Q007 — Potential Synergy Between Oncolytic Viruses and CAR-T

**Domain:** Oncolytic Virus  
**Difficulty:** Hard

### Reference Answer

Oncolytic viruses may complement CAR-T therapy by inducing tumor-cell lysis and local inflammation, increasing tumor-antigen release, modifying the tumor microenvironment, and potentially improving immune-cell recruitment.

Engineered oncolytic viruses may additionally deliver immunomodulatory molecules locally.

The magnitude and mechanism of synergy depend on the viral platform, CAR design, tumor model, and treatment context.

### Key Evaluation Points

- Direct oncolysis
- Local inflammation
- Antigen release
- TME remodeling
- Improved immune recruitment
- Potential transgene delivery
- Appropriate scientific qualification

---

## Q008 — IL-23 and Immune Regulation

**Domain:** Cytokine Biology  
**Difficulty:** Medium

### Reference Answer

IL-23 is a heterodimeric cytokine composed of p19 and p40 subunits and belongs to the IL-12 cytokine family.

It contributes to immune regulation particularly through the maintenance and expansion of Th17-associated responses and can influence other immune-cell populations depending on biological context.

### Key Evaluation Points

- Heterodimeric cytokine
- p19 and p40
- IL-12 cytokine family
- Th17-associated immunity
- Context-dependent immune effects

---

## Q009 — Context-dependent Effects of IL-23

**Domain:** Cytokine Biology  
**Difficulty:** Hard

### Reference Answer

The biological effects of IL-23 can vary according to tumor type, immune-cell composition, cytokine environment, receptor expression, and disease stage.

Because IL-23 participates in inflammatory and immune-regulatory pathways, its effects should not automatically be classified as universally antitumor or protumor.

Interpretation therefore requires context-specific experimental evidence.

### Key Evaluation Points

- Context dependence
- Tumor type
- Immune-cell composition
- Cytokine environment
- Avoidance of oversimplified causal conclusions

---

## Q010 — Interpreting Increased IFN-γ

**Domain:** Biomedical Reasoning  
**Difficulty:** Hard

### Reference Answer

An increase in IFN-γ alone is not sufficient to demonstrate improved antitumor efficacy.

IFN-γ may indicate immune activation, but treatment efficacy should be evaluated using additional endpoints such as tumor growth, survival, functional immune-cell activity, appropriate controls, and statistical evidence.

Mechanistic and safety data may also be necessary depending on the study objective.

### Key Evaluation Points

- IFN-γ alone is insufficient
- Distinction between biomarker and efficacy endpoint
- Tumor-growth evidence
- Survival or relevant efficacy endpoints
- Functional immune evidence
- Appropriate controls
- Statistical analysis
- Avoidance of causal overinterpretation
