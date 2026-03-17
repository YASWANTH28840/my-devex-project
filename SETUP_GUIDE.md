# DevEx Sample - Setup & Deployment Guide

This guide walks you through deploying the devex-sample project to GitHub.

## 📋 Pre-Deployment Checklist

- [ ] GitHub account created and logged in
- [ ] Git installed locally (`git --version`)
- [ ] Docker installed (for testing locally, optional)
- [ ] Project files downloaded/copied to your machine

## 🚀 Step 1: Create GitHub Repository

### Option A: Using GitHub Web UI (Recommended)

1. Go to https://github.com/new
2. **Repository name**: `devex-sample`
3. **Description**: "Flask REST service with DevEx best practices - automated workflows, CI/CD, and AI documentation"
4. **Visibility**: Public (so we can share it)
5. **Add .gitignore**: Skip (we have it)
6. **Add license**: Skip (we have it)
7. Click **Create repository**

### Option B: Using GitHub CLI

```bash
# Install: https://cli.github.com/
gh repo create devex-sample --public --source=. --remote=origin --push
```

## 📤 Step 2: Initialize & Push to GitHub

```bash
# Navigate to project directory
cd "path/to/devex-sample"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "feat: initial devex-sample project setup

- Flask REST service with /health and /products endpoints
- Docker containerization with multi-stage build
- Comprehensive test suite with pytest
- CI/CD pipeline with GitHub Actions
- Automated dependency checking and security scanning
- AI-based documentation generation
- Developer-friendly Makefile for all common tasks

Supports full DevEx workflow: setup → test → lint → CI → deploy"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/devex-sample.git
git branch -M main

# Push to GitHub
git push -u origin main
```

## 🔧 Step 3: Configure GitHub Settings

### Enable Branch Protection (optional but recommended)

1. Go to your repository settings
2. Navigate to **Branches**
3. Click **Add rule**
4. **Branch name pattern**: `main`
5. ✅ Enable:
   - Require pull request reviews
   - Require status checks to pass
   - Require branches to be up to date
6. Click **Create**

### Add Secrets for CI/CD

For the AI documentation generation to work:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. **Name**: `ANTHROPIC_API_KEY`
4. **Value**: Your actual Anthropic API key
5. Click **Add secret**

> Note: If you don't have an Anthropic API key, the CI/CD will gracefully skip AI doc generation. Get one at: https://console.anthropic.com/

## ✅ Step 4: Verify Setup

### Test Locally (Optional)

```bash
# If you have Docker installed
make dev          # Start service
curl http://localhost:5000/   # Should return {"service": "devex-sample", "status": "ok"}
make test         # Run tests
make lint         # Check code quality
make clean        # Stop services
```

### Test CI/CD Pipeline

1. Go to your GitHub repo
2. Click **Actions** tab
3. You should see **CI Pipeline** workflow

To test it:
```bash
# Create a test branch
git checkout -b test/verify-ci
echo "# Test" >> README.md
git add README.md
git commit -m "test: verify CI pipeline"
git push origin test/verify-ci
```

4. Go to your repo and create a Pull Request
5. GitHub Actions will automatically run
6. You should see ✅ checks pass

## 📊 Step 5: Generate Initial Documentation

If you have ANTHROPIC_API_KEY set:

```bash
export ANTHROPIC_API_KEY="your-key-here"
cd devex-sample
make docs
git add docs/SDD.md
git commit -m "docs: initial AI-generated system design document"
git push origin main
```

## 🎯 Step 6: Ready to Share!

Your repository is now ready. Share the link:

```
https://github.com/YOUR_USERNAME/devex-sample
```

## 📚 Project Structure Verification

Verify these files exist in your repo:

```
✅ app.py
✅ requirements.txt
✅ requirements-dev.txt
✅ Dockerfile
✅ docker-compose.yml
✅ Makefile
✅ pyproject.toml
✅ .flake8
✅ .gitignore
✅ .dockerignore
✅ tests/
   ✅ __init__.py
   ✅ test_app.py
✅ scripts/
   ✅ check-deps.py
   ✅ generate-docs.py
✅ docs/
   ✅ SDD.md
✅ .github/
   ✅ workflows/
      ✅ ci.yml
✅ README.md
✅ CONTRIBUTING.md
✅ LICENSE
```

## 🆘 Troubleshooting

### "Permission denied" when pushing

```bash
# Switch to SSH (recommended) or use personal access token
git remote set-url origin git@github.com:YOUR_USERNAME/devex-sample.git

# Or use HTTPS with token
git remote set-url origin https://YOUR_USERNAME:YOUR_TOKEN@github.com/YOUR_USERNAME/devex-sample.git
```

### "Changes not showing" after push

```bash
# Verify remote is set
git remote -v

# Force push (only if needed!)
git push -u origin main --force
```

### CI/CD not running

1. Check `.github/workflows/ci.yml` exists
2. Go to **Actions** tab → see if workflow appears
3. Try creating a new branch and PR to trigger

### Tests failing locally

```bash
# Clean and reinstall
make clean
pip install -r requirements.txt -r requirements-dev.txt
make test
```

## 📈 Next Steps

1. **Share Repository**: Send link to evaluators
2. **Document**: Keep README updated
3. **Iterate**: Make improvements based on feedback
4. **Monitor CI**: Check that CI passes on all PRs

## 🎓 Learning Resources

- **Makefile**: `cat Makefile` to see all commands
- **Tests**: Read `tests/test_app.py` for testing patterns
- **CI/CD**: Read `.github/workflows/ci.yml` for pipeline
- **Documentation**: See `README.md` for full setup guide

## 📞 Support

If something isn't working:

1. Check **Actions** tab for error logs
2. Run locally: `make ci-check`
3. Check GitHub documentation
4. Review error messages carefully

---

**Ready?** Run these commands to get started:

```bash
cd path/to/devex-sample
git init
git add .
git commit -m "feat: initial setup"
git remote add origin https://github.com/YOUR_USERNAME/devex-sample.git
git branch -M main
git push -u origin main
```

Enjoy! 🚀

*Generated for devex-sample project - DevEx Best Practices Demo*
