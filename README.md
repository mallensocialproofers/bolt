# Delphine agent team for Claude Code

This folder holds six Claude Code agents and a shared company brief.

## What is inside

- `CLAUDE.md`: company context and rules that every agent reads. Edit it as facts change.
- `.claude/agents/`: one Markdown file per agent.
  - `regulatory-research`: FDA, state, labeling, ad-platform and payment rules.
  - `label-claims-reviewer`: checks labels, pages, ads and emails before you approve them.
  - `sourcing`: manufacturers and suppliers, comparisons, request-for-quote drafts.
  - `product-development`: lineup, formulation briefs, dose math at 25 mg per pouch.
  - `brand-strategy`: positioning, voice, tagline and name-modifier options.
  - `finance`: unit economics, usage-based reorder model, cash flow.
- `work/decisions.md`: a running log of decisions you need to make. Agents add to it.

## Set up

1. Install Claude Code if you have not (see https://code.claude.com/docs for current steps).
2. Put this whole folder somewhere permanent on your computer, keeping the hidden `.claude` folder inside it.
3. Open Claude Code in this folder (the folder that contains `CLAUDE.md`).
4. Run `/agents` and confirm all six agents appear. If one is missing, check that its file is in `.claude/agents/` and that the first line is `---`.
5. Fill in the blanks: your name and age policy in `CLAUDE.md` and `work/decisions.md`, and the tin size and order size once you know them.

## How to use it

Ask in plain language and name the agent. Each agent starts with a fresh context and reads `CLAUDE.md`, so keep the brief current. Agents report back to your main session rather than to each other, so you pass outputs along (the `work/` folder makes that easy).

Starter prompts, in order:

1. "Use regulatory-research to build the state-by-state sales matrix for my top five states: [list]. Then summarize what could block a launch."
2. "Use regulatory-research to document ad-platform and payment-processor policies for caffeine pouches: Google, Meta, TikTok, Shopify Payments, and three high-risk processors."
3. "Use finance to build a first cost model once I paste in supplier quotes."
4. "Use sourcing to find 8-10 contract manufacturers for 25 mg caffeine pouches and draft the request for quote."
5. "Use product-development to propose the launch lineup and formulation briefs."
6. "Use brand-strategy to draft positioning, voice and three tagline options, then use label-claims-reviewer to review the draft."

## Rules to keep

- Agents draft; you decide and send. Nothing goes out under your name unreviewed.
- Anything under "For a professional" in an output goes to a lawyer, accountant or insurance broker.
- Get the name Delphine cleared by a trademark attorney before major branding spend.
- Do not spend on inventory, branding or ads until you have cleared the compliance gate and recorded it in `work/decisions.md`.
