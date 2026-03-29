# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Single-file interactive study tool (`study-tool.html`) for **Leiden University - Statistics for Computer Scientists (2526, 2025-2026)**. Built as a self-contained HTML/CSS/JS application with no build step or dependencies.

## Source Materials

- **10 lecture PDFs** in `All Lectures/` — covering descriptive stats, data collection, sampling distributions, estimation, statistical testing, comparing two groups, bivariate relationships, categorical variables (chi-squared), regression, and multiple regression.
- **3 practice exams with solutions** in `Past Papers/`.
- **EXAM_STUDY_SYSTEM.md** — comprehensive markdown exam reference (non-interactive).

## Architecture

`study-tool.html` is a single-file app with 6 sections:

1. **Dashboard** — hero + progress overview
2. **Story Mode** — 9 comprehensive chapters (the primary study content)
3. **Test Selection Trainer** — 15 questions on choosing the right statistical test
4. **Formula Flashcards** — 16 flip cards for key formulas
5. **True/False Quiz** — 20 questions on common misconceptions
6. **Exam Simulator** — 5 multi-part exam questions with auto-grading

### Design System
- Dark theme with glassmorphism (backdrop-filter blur, rgba surfaces)
- Blue-purple gradient accents (`--grad: linear-gradient(135deg, #60a5fa, #a78bfa)`)
- Sidebar navigation (collapsible on mobile)
- Google Fonts: Inter (UI), JetBrains Mono (formulas)
- CSS custom properties throughout (see `:root` block)

### JS Patterns
- `localStorage` for progress persistence (chapter completion, quiz scores)
- Fisher-Yates shuffle for randomized question order
- Section-based navigation via `showSection(id)` function
- No framework — vanilla JS with direct DOM manipulation

## Development

Open directly in browser — no server needed:
```bash
open study-tool.html
```

## Key Constraints

- **Must remain a single file** — no external CSS/JS files, no build tools
- **User's ONLY study source** — chapters must be comprehensive with worked examples, all formulas, and exam traps
- **Premium UI/UX** — glassmorphism, gradients, polished typography; not a "student project" look
- Content accuracy is critical — all statistical methods must match the Leiden 2526 course material
