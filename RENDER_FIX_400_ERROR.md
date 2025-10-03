# 🚨 Fix "Bad Request (400)" Error on Render

## ✅ **Quick Fix Applied**
I've updated your code to include your Render domain in `ALLOWED_HOSTS`. The app should redeploy automatically.

## 🔧 **To Properly Configure Render Environment Variables:**

### Step 1: Go to Your Render Dashboard
1. Visit [render.com](https://render.com) and login
2. Find your **`crud-mytodo-django`** service
3. Click on it to open the service details

### Step 2: Update Environment Variables
1. Click on **"Environment"** in the left sidebar
2. Add/Update these environment variables:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | `(Aj&5i=8LUq+AeMKqLbIM49GN5Q0&B0v*SJe!6Y$1oxyL@YFBp` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `crud-mytodo-django.onrender.com` |

### Step 3: Save and Redeploy
1. Click **"Save Changes"**
2. Render will automatically redeploy your app
3. Wait 2-3 minutes for the deployment to complete

## 🎯 **Alternative Quick Test**
Your app should work now because I added `crud-mytodo-django.onrender.com` to the default allowed hosts in the code.

## 🔍 **Check if it's Working:**
1. Visit: **https://crud-mytodo-django.onrender.com/**
2. You should see your Django todo app instead of the 400 error

## 🚨 **If Still Getting 400 Error:**

### Check Render Logs:
1. In your Render dashboard, go to **"Logs"**
2. Look for any error messages about ALLOWED_HOSTS
3. The logs might show exactly which hostname is being rejected

### Common Issues:
- Make sure `ALLOWED_HOSTS` environment variable matches your exact Render URL
- Ensure there are no extra spaces in the environment variable
- Check that `DEBUG=False` (not `DEBUG=false` or `DEBUG=0`)

## ✅ **Expected Result:**
Once fixed, you should see your Django todo application with:
- Working homepage
- Admin interface at `/admin/`
- All your todo functionality

---

**The fix has been pushed to GitHub and should auto-deploy to Render in 2-3 minutes!** 🚀