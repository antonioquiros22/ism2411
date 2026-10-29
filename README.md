# ISM2411 — Python for Business

**Name:** Antonio Quiros

**Semester:** Fall 2026

**Instructor:** Markum Reed

## About This Repo

This repository contains my weekly lab submissions for ISM2411.
Each folder corresponds to one module.

## Modules

- `week05/` — Conditionals: tiered discount calculator
- `week06/` — Loops: sales report with sum, average, max
- `week07/` — Functions: calculate_tax, apply_discount
- `week08/` — Git: first GitHub submission

## How to Run

Each script is standalone. Open a terminal and run:
```
python week07/functions.py
```

## Reflection

**1. Commit history**

```
aa3e95d add README with module listing and run instructions
4054887 add module 7 functions: calculate_tax, apply_discount, final_price
39fd65e add .gitignore for Python and OS files
4866cba Initial commit
```

If I were hiring someone and saw this history, it would tell me they work in small, organized steps. Each commit covers one distinct change, and the messages say specifically what was done (for example, naming the exact functions added), so I could understand the project without opening any files. It also shows they set up the project properly, with a .gitignore first, before adding any code.

**2. How Git changes my approach to editing**

Before this module, I would edit a working script directly and hope I could undo any mistake by remembering what I changed. Now I know that committing a working version first gives me a save point I can return to. I will make smaller changes and commit each one that works, so a mistake only costs me one small step instead of the whole script.

**3. Something to add to my .gitignore**

I would add `.ipynb_checkpoints/`. Jupyter creates these folders automatically on my machine, and I found one in my earlier work. They are auto-generated backup copies of notebooks, not real work, and they would clutter the repo and differ on every computer. Since Jupyter can recreate them at any time, there is no reason to track them.
