# AGENTS.md

@README

- After making code changes, check if `AGENTS.md` or `README.md` needs to be updated to reflect the new project state (e.g. new files, changed tools, updated commands)

## Heading Capitalization

- H1 titles (`#`) use title case, but keep minor words lowercase (e.g. `Law of Large Numbers`, not `Law Of Large Numbers`)
- All lower-level headings (`##` and below) use sentence case (e.g. `State the central limit theorem`, `Weak vs. strong law`)
- Preserve the capitalization of proper nouns and acronyms in any heading (e.g. `Bayes' theorem`, `LLN`)

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
