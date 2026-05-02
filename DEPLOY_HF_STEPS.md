# Deploy to Hugging Face Spaces - Step by Step

## 📋 Prerequisites
- Hugging Face account (free): https://huggingface.co/join
- Git installed on your computer

## 🚀 Deployment Steps

### Step 1: Create Hugging Face Space

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Fill in details:
   - **Space name**: `smart-classroom-detector`
   - **License**: MIT
   - **SDK**: Gradio
   - **Hardware**: CPU basic (free) or upgrade to GPU
   - **Visibility**: Public or Private

4. Click **"Create Space"**

### Step 2: Prepare Files

Rename/copy these files:
```bash
# Rename Gradio app
copy app_gradio.py app.py

# Rename requirements
copy requirements_hf.txt requirements.txt

# Rename README
copy README_HF.md README.md
```

### Step 3: Upload Files to Hugging Face

**Option A: Web Upload (Easiest)**

1. In your Space, click **"Files"** tab
2. Click **"Add file"** → **"Upload files"**
3. Upload these files:
   - `app.py` (renamed from app_gradio.py)
   - `requirements.txt` (renamed from requirements_hf.txt)
   - `README.md` (renamed from README_HF.md)
   - `yolo26_detector.py`
   - `attendance_logger.py`
   - `yolo26n.pt`
   - `yolo26n-seg.pt`
   - `yolo26n-pose.pt`
   - `runs/detect/runs/detect/train_continued/weights/best.pt`

4. Click **"Commit changes to main"**

**Option B: Git Push (Advanced)**

```bash
# Clone your space
git clone https://huggingface.co/spaces/YOUR_USERNAME/smart-classroom-detector
cd smart-classroom-detector

# Copy files
copy app_gradio.py app.py
copy requirements_hf.txt requirements.txt
copy README_HF.md README.md
copy yolo26_detector.py .
copy attendance_logger.py .
copy yolo26n.pt .
copy yolo26n-seg.pt .
copy yolo26n-pose.pt .

# Create runs directory structure
mkdir -p runs/detect/runs/detect/train_continued/weights
copy runs\detect\runs\detect\train_continued\weights\best.pt runs/detect/runs/detect/train_continued/weights/

# Commit and push
git add .
git commit -m "Initial deployment"
git push
```

### Step 4: Wait for Build

1. Hugging Face will automatically:
   - Install dependencies from `requirements.txt`
   - Load your models
   - Start the Gradio app

2. Build time: 5-10 minutes

3. Watch the **"Logs"** tab for progress

### Step 5: Test Your App

1. Once build completes, your app will be live at:
   ```
   https://huggingface.co/spaces/YOUR_USERNAME/smart-classroom-detector
   ```

2. Test by uploading a classroom image

3. Share the link with others!

## 📁 Required Files Structure

```
smart-classroom-detector/
├── app.py (Gradio interface)
├── requirements.txt
├── README.md
├── yolo26_detector.py
├── attendance_logger.py
├── yolo26n.pt
├── yolo26n-seg.pt
├── yolo26n-pose.pt
└── runs/detect/runs/detect/train_continued/weights/best.pt
```

## ⚙️ Hardware Options

**Free Tier (CPU Basic)**
- ✅ FREE forever
- ⚠️ Slower inference (~5-10 seconds per image)
- ✅ Good for demos

**Upgraded (GPU)**
- 💰 ~$0.60/hour
- ✅ Fast inference (~1-2 seconds)
- ✅ Better for production

To upgrade: Space Settings → Hardware → Select GPU

## 🐛 Troubleshooting

**Build fails?**
- Check **Logs** tab for errors
- Ensure all model files are uploaded
- Verify `requirements.txt` is correct

**App crashes?**
- Model files might be too large (>5GB limit on free tier)
- Try using Git LFS for large files:
  ```bash
  git lfs install
  git lfs track "*.pt"
  git add .gitattributes
  git add *.pt
  git commit -m "Add models with LFS"
  git push
  ```

**Slow inference?**
- Normal on free CPU tier
- Upgrade to GPU for faster performance

## 🎨 Customization

Edit `app.py` to customize:
- Interface colors/theme
- Add more examples
- Change descriptions
- Add analytics

## 📊 Monitor Usage

- Go to Space Settings → Analytics
- View visitor count, usage stats
- Monitor performance

## 🔒 Privacy

**Public Space:**
- Anyone can use your app
- Good for portfolio/demos

**Private Space:**
- Only you can access
- Good for testing

Change in: Space Settings → Visibility

## ✅ Success Checklist

- [ ] Space created on Hugging Face
- [ ] All files uploaded
- [ ] Build completed successfully
- [ ] App loads without errors
- [ ] Test image detection works
- [ ] Share link with others

## 🎉 Your App is Live!

Share your space:
```
https://huggingface.co/spaces/YOUR_USERNAME/smart-classroom-detector
```

Add to your portfolio, resume, or GitHub README!

---

**Need Help?**
- Hugging Face Docs: https://huggingface.co/docs/hub/spaces
- Community Forum: https://discuss.huggingface.co
