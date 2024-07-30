from PIL import Image, ImageDraw, ImageFont
import os

def add_text(image_path, output_path, text, font_path, position = (10,10)):
    """adds text with custom font on image and saves

    Args:
        image_path (_type_): innput imagee path
        output_path (_type_): saved output image
        text (_type_): text added to picture
        font_path (_type_): path to font file
        position (tuple): x, y position on image.
    """
    try:
        with Image.open(image_path) as img:
            draw = ImageDraw.Draw(img)
            try:
                font = ImageFont.truetype(font_path, size = 20)
            except IOError:
                font = ImageFont.load_default()
            left, top, right, bottom = draw.textbbox(position, text, font = font)
            text_width, text_height = right - left , bottom - top
            
            x,y = position
            if x + text_width > img.width:
                x = img.width - text_width - 10
            if y + text_height > img.height:
                y = img.height - text_height - 10

            rect_x1, rect_y1 = x - 5, y- 5
            rect_x2 , rect_y2 = x + text_width + 5, y + text_height + 5
            draw.rectangle([rect_x1, rect_y1, rect_x2, rect_y2], fill = 'black', outline = 'white')


            draw.text((x,y), text, font = font, fill = 'white')
            os.makedirs(os.path.dirname(output_path), exist_ok = True)
            img.save(output_path)

    except Exception as e:
        print(f"error: {e}")

