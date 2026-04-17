import re
import os

file_path = r'c:\Users\정세진\Desktop\icb7\teamproject2\olist-business-analysis-marketing\html\part2_lead_conversion_analysis.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# List of image files in order
images = [
    "01_funnel.png",
    "02_origin_cvr.png",
    "03_time_fatigue.png",
    "04_sales_cycle.png",
    "05_landing_page.png",
    "06_segment.png",
    "07_lead_type.png",
    "08_logistic_or.png",
    "09_rf_importance.png",
    "10_roc_curve.png",
    "11_persona.png",
    "12_quarter.png",
    "13_conversion_speed.png",
    "14_lost_segments.png",
    "15_channel_evolution.png",
    "16_ml_enhanced.png"
]

# We will replace <img src="data:..." ...> tags. 
# There are exactly 16 such tags.
# We can find them one by one.

def replace_img(match):
    global counter
    img_name = images[counter]
    # Capture the existing alt and style if possible, or just use defaults
    # For simplicity and consistency with the other report, we'll use a standard style.
    
    # Extract alt text if present
    alt_match = re.search(r'alt="([^"]+)"', match.group(0))
    alt_text = alt_match.group(1) if alt_match else f"Chart {counter + 1}"
    
    new_tag = f'<img src="../images/{img_name}" alt="{alt_text}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">'
    counter += 1
    return new_tag

counter = 0
# Regex to match the img tag with base64 src
# Using non-greedy match for src and ensuring it's an img tag
pattern = re.compile(r'<img[^>]+src="data:image/[^"]+"[^>]*>')

new_content = pattern.sub(replace_img, content)

if counter == 16:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully replaced {counter} images.")
else:
    print(f"Error: Found {counter} images, expected 16.")
