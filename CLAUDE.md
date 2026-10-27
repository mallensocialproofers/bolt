# Bolt: company context for every agent

Read this before doing any work. Everything here applies to every agent in this project.

## The business

Bolt sells oral caffeine pouches in the United States, online (Shopify store) and through wholesale. There is one strength: 25 mg of caffeine per pouch, set low so customers can use several pouches a day. Customers are adults only. The owner will set the minimum age (18+ or 21+); until it is recorded in `work/decisions.md`, treat it as 21+ and say so.

The owner is the only decision-maker. Agents research, draft, compare and calculate. The owner approves.

## Rules for all agents

1. Never send an email or message, sign anything, pay for anything, publish anything, or accept terms. Produce drafts for the owner to review.
2. Every factual claim gets a source URL and the date you checked it. Mark anything you could not confirm from a primary source as UNVERIFIED.
3. Never state that something is legal, compliant or safe as a conclusion. Present findings and open questions for a lawyer.
4. No health, performance, disease, weight-loss or sleep-replacement claims. No nicotine-replacement or quit-smoking implications. No content, slang, imagery or channels that appeal to minors.
5. Never invent numbers, quotes, suppliers, regulations or sources. If a number is missing, ask the owner.
6. Save every deliverable to `work/<agent-name>/` with a dated file name (for example `work/sourcing/2026-10-27-supplier-comparison.md`). End your reply with a short summary and the path to the file.
7. When a finding changes a decision (a rule, a cost, a risk), also add one line to `work/decisions.md`: date, agent, finding, and what the owner needs to decide.
8. Flag anything that needs a lawyer, an accountant or an insurance broker under the heading "For a professional".

## Known facts and open items (research leads, checked October 27, 2026)

Treat these as starting points to verify, not conclusions.

- A 2025 trade explainer says caffeine pouches are sold in the US as dietary supplements with no federal minimum age, citing FDA's 2018 guidance on highly concentrated caffeine and a 400 mg per day reference for healthy adults (https://tobaccoinsider.com/caffeine-pouches-questions-and-answers/). This is a trade site, not FDA.
- FDA is considering guidance on labeling caffeine content in foods and beverages, on its 2026 priority list with no date (https://www.fooddive.com/news/caffeine-labeling-fda-guidance-celsius-alani-nu/824355/). Bolt prints caffeine per pouch regardless.
- State-level laws for caffeine pouches, ad-platform rules and payment-processor rules have NOT been researched yet.
- Name risk for "Bolt": research found a Gatorade product line called Bolt24 (including a caffeinated version), PROBAR "Bolt" energy chews, a live site at boltpouches.com selling "BOLT Energy Pouches" (owner not identified), caffeine products named Jolt and Volt, and a registered BOLT mark for e-cigarettes. USPTO's own search could not be accessed, so none of this is a clearance search. A trademark attorney must clear the name before major branding spend.
- Because 25 mg pouches invite several uses a day, 12 pouches is 300 mg. Labeling must make daily totals clear, and the wording is for counsel to approve.

## Marketing content

Marketing content for Bolt (images, video, captions, copy) is drafted through the content studio (`mallensocialproofers/my-content-studio`). That repo is a production tool only. Bolt's brief, rules and files live here.

1. The studio drafts and generates. Nothing is posted, scheduled, sent or published automatically. The studio can post to social accounts and send through Blotato, so every post or send needs the owner's explicit approval at that moment. Studio rules such as "log to Airtable" or "schedule the next slot" never override this.
2. Every piece goes to `label-claims-reviewer` before the owner sees it, and the review is saved in `work/label-claims-reviewer/`.
3. Content is for adults only. Use the age policy in `work/decisions.md`; until it is recorded, treat it as 21+ and say so.
4. No health, performance or nicotine-related claims, and no content, slang, imagery or channels that appeal to minors.
5. Do not carry over other brands' characters, hosts, voices, accounts or standing defaults from the studio.
6. Do not publish much under the Bolt name until the trademark question in `work/decisions.md` is settled.

## Project phases

0. Compliance gate (weeks 1-3): regulatory-research, label-claims-reviewer, finance.
1. Product and supply (weeks 3-10): sourcing, product-development, finance.
2. Brand and storefront (weeks 6-12): brand-strategy, label-claims-reviewer.
3. Launch and sell (weeks 12-20) and 4. Scale (month 6 on): more agents are added later.

Do not recommend spending on inventory, branding or advertising until the compliance gate is cleared by the owner, recorded in `work/decisions.md`.
