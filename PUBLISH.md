# 发布清单

## GitHub Release v1.0

```bash
cd /Users/zhaoguoqiang/soul-system

# 1. Verify
find . -type f | wc -l          # should be ~50+
python3 -m pytest libs/python/tests/ -q

# 2. Commit
git add -A
git commit -m "v1.0: AContext spec + Python lib + LangChain adapter"
git tag v1.0
git push origin main --tags

# 3. Create GitHub Release (manual)
# - Tag: v1.0
# - Title: "AContext v1.0 — Open Standard for Agent Context"
# - Body: paste CHANGELOG v2.6 and below
# - Attach: nothing (pure source)
```

## PyPI Publish

```bash
cd libs/python
pip install build twine
python3 -m build
twine upload dist/*
```

## Install for Users

```bash
# Skill only (no code)
ln -sfn ~/soul-system ~/.agents/skills/soul-system

# Python library
pip install acontext
# or: pip install git+https://github.com/zhaoguoqiang-hub/soul-system.git#subdirectory=libs/python

# LangChain
pip install acontext[langchain]
```
