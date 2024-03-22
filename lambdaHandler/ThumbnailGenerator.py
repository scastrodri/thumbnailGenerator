from PIL import Image
import io

class ThumbnailGenerator:
    """
    Class for generating thumbnails from images.
    """
    def __init__(self):
        pass

    def generate_thumbnail(self, image_file):
        """
        Generates a thumbnail from an image file.

        Args:
            image_file: The image file from the lambda handler function
        """
        thumbnail_size = (128, 128) # The default one
        
        try:
            # This should be a function
            image_extension = image_file.split(b".")[-1].lower()
            if image_extension in [b"jpg", b"jpeg"]:
                image = Image.open(io.BytesIO(image_file), mode="r")
            elif image_extension == b"png":
                image = Image.open(io.BytesIO(image_file), mode="rb")
            else:
                print(f"Error: Unsupported image format: {image_extension}") # This should be LOG.info
                return None

            # Create the thumbnail and save the file
            image.thumbnail(thumbnail_size)
            # Save the processed image in-memory
            thumbnail_buffer = io.BytesIO()
            image.save(thumbnail_buffer, format="JPEG")
            print("Thumbnail created successfully") # This should be LOG.info
            return thumbnail_buffer.getvalue()
        except (OSError, IOError) as e:
            print(f"Error opening image: {e}") # This should be LOG.info
            return None
        except Exception as e: 
            print(f"Unexpected error generating thumbnail: {e}") # This should be LOG.info
            return None