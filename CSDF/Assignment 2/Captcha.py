from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string

# Generate random captcha text
def random_captcha_text(length=5):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Generate captcha image
def generate_captcha_image(text):
    width, height = 200, 70
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Draw text
    for i, ch in enumerate(text):
        x = 20 + i*30
        y = random.randint(10, 30)
        draw.text((x, y), ch, font=font, fill=(0,0,0))

    # Add some noise lines
    for _ in range(5):
        start = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([start, end], fill=(0,0,0), width=1)

    # Blur slightly
    image = image.filter(ImageFilter.GaussianBlur(1))
    return image

# Main
captcha_text = random_captcha_text()
img = generate_captcha_image(captcha_text)
img.show()  # opens the captcha image

# Ask user to enter captcha
user_input = input("Enter the CAPTCHA you see: ")

if user_input.upper() == captcha_text.upper():
    print("CAPTCHA verified successfully!")
else:
    print("CAPTCHA incorrect. Try again.")
