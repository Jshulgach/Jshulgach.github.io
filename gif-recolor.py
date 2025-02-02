from PIL import Image, ImageSequence


gif_path = "robot.gif"
# Reload the original GIF for processing
original_gif = Image.open(gif_path)

# Process frames to make the linkages white
processed_frames = []

for frame in ImageSequence.Iterator(original_gif):
    # Convert frame to RGBA for pixel manipulation
    frame = frame.convert("RGBA")
    pixels = frame.load()

    # Iterate through each pixel and replace yellow linkages with white
    width, height = frame.size
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]

            # Detect yellow shades and replace with blue
            if 100 <= r <= 255 and 100 <= g <= 210 and 0 <= b <= 100:
                pixels[x, y] = (50, 100, 255, a)  # Set to blue

    processed_frames.append(frame)

# Save the modified GIF with white linkages
output_path = "robot_white_linkages.gif"
processed_frames[0].save(output_path, save_all=True, append_images=processed_frames[1:], loop=0, duration=original_gif.info['duration'])

