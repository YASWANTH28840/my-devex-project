# 🖼️ How to Add Your Screenshots to the Repository

The README is now ready to display your screenshots! Here's exactly what to do:

## 📋 What Screenshots You Need

The README expects **5 screenshot images** in the `docs/screenshots/` directory:

1. **`01-service-running.png`** - Your browser showing the Flask service responding with the health check JSON
2. **`02-tests-passing.png`** - Your terminal/IDE showing all 11 tests passing with 100% coverage
3. **`03-debug-output.png`** - Your terminal showing the pytest debug output and environment details
4. **`04-before-failure.png`** - Your terminal showing the test failure (before the fix)
5. **`05-after-success.png`** - Your terminal showing all tests passing (after the fix)

## 🚀 Method 1: Upload via GitHub (Easiest)

### Step 1: Open GitHub Repository
1. Go to: https://github.com/YASWANTH28840/Homeassignment
2. Click on the `docs` folder
3. Click on the `screenshots` folder (or create it if it doesn't exist)

### Step 2: Upload Files
1. Click **"Add file"** → **"Upload files"**
2. Drag & drop your 5 screenshot images OR click to select them
3. Make sure names match exactly:
   - `01-service-running.png`
   - `02-tests-passing.png`
   - `03-debug-output.png`
   - `04-before-failure.png`
   - `05-after-success.png`
4. Click **"Commit changes"**
5. Done! The README will automatically display your images

## 🛠️ Method 2: Upload via Command Line

### Step 1: Copy Screenshots to Local Directory
```bash
# Navigate to the repository
cd devex-sample

# Copy your screenshot images to the docs/screenshots folder
# Example (adjust paths to your actual screenshot locations):
cp ~/Desktop/screenshot1.png docs/screenshots/01-service-running.png
cp ~/Desktop/screenshot2.png docs/screenshots/02-tests-passing.png
cp ~/Desktop/screenshot3.png docs/screenshots/03-debug-output.png
cp ~/Desktop/screenshot4.png docs/screenshots/04-before-failure.png
cp ~/Desktop/screenshot5.png docs/screenshots/05-after-success.png
```

### Step 2: Add to Git
```bash
cd devex-sample
git add docs/screenshots/
git commit -m "docs: add proof of completion screenshots"
git push origin main
```

### Step 3: Verify
Go to GitHub and check that:
- All 5 images are in `docs/screenshots/`
- README displays the images
- File names match exactly

## 🖥️ Method 3: Using Windows Explorer

### Step 1: Navigate to Screenshots Folder
```
C:\Users\yaswanth.subramanya\OneDrive - o9 Solutions\Desktop\random\devex-sample\docs\screenshots\
```

### Step 2: Copy Images
1. Find your 5 screenshot files on your computer
2. Copy them to the `docs/screenshots/` folder
3. Rename them to match the expected names:
   - `01-service-running.png`
   - `02-tests-passing.png`
   - `03-debug-output.png`
   - `04-before-failure.png`
   - `05-after-success.png`

### Step 3: Commit to Git
```bash
git add docs/screenshots/
git commit -m "docs: add proof of completion screenshots"
git push origin main
```

## ✅ Verification

After uploading, verify everything works:

### View on GitHub
1. Go to: https://github.com/YASWANTH28840/Homeassignment
2. Open **README.md**
3. Scroll to the **"📸 Proof of Completion"** section
4. All 5 images should display

### View Locally
```bash
# List the files
ls -la docs/screenshots/

# Output should show:
# 01-service-running.png
# 02-tests-passing.png
# 03-debug-output.png
# 04-before-failure.png
# 05-after-success.png
```

## 📝 Image Requirements

**Format:** PNG, JPG, or GIF
**Size:** Under 5MB per image (recommended: 500KB - 2MB)
**Resolution:** 1024x768 or larger (readability on GitHub)

## 🆘 Troubleshooting

### Images Not Showing on GitHub?
1. **Check filenames:** Must match exactly (case-sensitive on GitHub)
   - ✅ `01-service-running.png`
   - ❌ `01-Service-Running.png`
   - ❌ `01-servicerunning.png`

2. **Check file format:** Must be `.png`, `.jpg`, or `.gif`
   - ✅ `01-service-running.png`
   - ❌ `01-service-running.bmp`

3. **Check location:** Must be in `docs/screenshots/` directory
   - ✅ `docs/screenshots/01-service-running.png`
   - ❌ `screenshots/01-service-running.png`
   - ❌ `01-service-running.png`

4. **Commit properly:** Make sure to `git add`, `git commit`, and `git push`
   ```bash
   git add docs/screenshots/
   git commit -m "add screenshots"
   git push origin main
   ```

5. **Clear cache:** Sometimes GitHub caches old versions. Wait 1-2 minutes or:
   - Hard refresh: Press `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
   - Or try in an Incognito/Private window

## 📦 What Happens Next?

Once you upload the 5 screenshots:

1. ✅ README will display all proof of completion images
2. ✅ GitHub viewers can see your work visually
3. ✅ Evaluation will have clear visual evidence
4. ✅ Project is complete and submission-ready

## 🎯 Summary

| Step | Action | Time |
|------|--------|------|
| 1 | Navigate to `docs/screenshots/` on GitHub or locally | 1 min |
| 2 | Upload/copy your 5 screenshot images | 2 min |
| 3 | Rename to match expected filenames | 1 min |
| 4 | Commit and push to GitHub | 2 min |
| 5 | Verify images display in README | 1 min |
| **Total** | | **7 minutes** |

---

**Questions?** Check the README.md for more context, or refer to the image references in the proof sections.

**Ready to add your screenshots?** Start with Method 1 (GitHub upload) - it's the easiest! 🚀
