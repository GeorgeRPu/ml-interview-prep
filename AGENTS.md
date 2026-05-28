# AGENTS.md

@README

- After making code changes, check if `AGENTS.md` or `README.md` needs to be updated to reflect the new project state (e.g. new files, changed tools, updated commands)

## Heading Capitalization

- H1 titles (`#`) use title case, but keep minor words lowercase (e.g. `Law of Large Numbers`, not `Law Of Large Numbers`)
- All lower-level headings (`##` and below) use sentence case (e.g. `State the central limit theorem`, `Weak vs. strong law`)
- Preserve the capitalization of proper nouns and acronyms in any heading (e.g. `Bayes' theorem`, `LLN`)

## Terminology

- Use lowercase for distribution names in prose: "normal distribution", "t-distribution", "binomial distribution" (not "Normal distribution")
- Capitalize only when the name derives from a proper noun: "Gaussian distribution", "Poisson distribution"

## Formal Blocks

Use `sphinx-proof` directives (four backticks) for formal mathematical concepts:

- `` `{prf:definition} `` — definitions of terms and concepts (e.g. conditional probability, p-value, statistical power)
- `` `{prf:theorem} `` — named theorems with formal statements (e.g. CLT, LLN)
- `` `{prf:proof} `` — derivations and proofs of theorems
- `` `{prf:algorithm} `` — step-by-step algorithmic procedures (e.g. gradient boosting)

Keep interpretive commentary, intuition, and caveats **outside** the block. The block itself should contain only the formal statement and its formula.

## Math Conventions

- Always use `\left` and `\right` around parentheses and brackets in LaTeX math expressions
- Use brackets for `\text{Bias}` and `\text{Var}` operators: `\text{Bias}\left[...\right]`, `\text{Var}\left[X\right]`

## Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <short summary>

- Bullet point describing one change
- Bullet point describing another change
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `build`, `chore`, `test`

**Scope:** optional, name of the affected area (e.g. `docs`, `scripts`, `solutions`)

**Rules:**
- Summary line is lowercase, no trailing period, under 72 characters
- Use bullet points for the body when there are multiple changes
- Do not add `Co-Authored-By` attribution
