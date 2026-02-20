import os

def create_svg(filename, text, color):
    width = 600
    height = 400
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="{color}"/>
    <text x="50%" y="50%" font-family="Arial" font-size="24" fill="white" text-anchor="middle" dominant-baseline="middle">{text}</text>
</svg>'''
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Change extension to .svg if it was .jpg
    base = os.path.splitext(filename)[0]
    with open(f"{base}.svg", "w") as f:
        f.write(svg_content)
    
    # Also create a dummy jpg file if needed, but browser can't display svg as jpg.
    # So we will update the HTML to use .svg or just rely on the browser not finding jpg and showing alt text?
    # Better: Update the HTML to reflect .svg or assume the user will replace them later.
    # Wait, the HTML expects .jpg.
    # If I cannot generate real JPGs without PIL, I should stick to SVGs and update HTML.
    # Or I can try to use a simple BMP generator in pure python if I really need binary images.
    # Let's just stick to SVG and update the HTML.

    print(f"Created {base}.svg")

images = [
    ("static/images/hero-banana-cake.jpg", "Hero Banana Cake", "#D4A373"),
    ("static/images/cake-banana.jpg", "Banana Walnut Loaf", "#FAEDCD"),
    ("static/images/cake-chocolate.jpg", "Chocolate Fudge", "#5D4037"),
    ("static/images/cake-strawberry.jpg", "Strawberry Delight", "#FFCDD2"),
    ("static/images/cake-cheesecake.jpg", "New York Cheesecake", "#FFF9C4"),
    ("static/images/cake-vanilla.jpg", "Vanilla Bean Dream", "#F5F5F5")
]

for path, text, color in images:
    create_svg(path, text, color)
