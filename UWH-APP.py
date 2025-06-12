import streamlit as st
from PIL import Image
import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity
from io import BytesIO
from streamlit_image_comparison import image_comparison  # correct import

# Page config
st.set_page_config(page_title="UWH Enhancer Quality Analyzer", layout="wide")
st.title("🌊 Underwater Image Enhancement Quality Analyzer")

uploaded = st.sidebar.file_uploader("Upload underwater image", type=["jpg", "png", "jpeg"])
if uploaded:
    original = Image.open(uploaded).convert("RGB")
    
    # Enhancement placeholder (swap with your enhancement logic)
    enhanced = original  # <-- replace with: enhance(original)

    # Visual comparison
    st.subheader("Original vs Enhanced")
    image_comparison(
        img1=original,
        img2=enhanced,
        label1="Original",
        label2="Enhanced",
        width=700,
    )

    # Compute metrics
    orig_arr = np.array(original)
    enh_arr = np.array(enhanced)
    psnr_val = peak_signal_noise_ratio(orig_arr, enh_arr, data_range=255)
    ssim_val = structural_similarity(orig_arr, enh_arr, multichannel=True, data_range=255)

    st.markdown("### 📊 Quality Metrics")
    st.write(f"- **PSNR**: {psnr_val:.2f} dB")
    st.write(f"- **SSIM**: {ssim_val:.3f}")

    st.info("🔎 PSNR & SSIM compare how close the enhanced image is to the original.")
else:
    st.sidebar.info("Upload an image to start analysis.")
