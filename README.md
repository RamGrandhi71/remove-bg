Remove-Bg

This Python script uses the rembg library to remove the background from an image. It utilizes the easygui library for file dialogs and the Pillow library for image processing.
Requirements

Ensure you have the required dependencies installed by running:

pip install -r requirements.txt

    rembg==1.0.0
    easygui==0.98.2
    Pillow==8.3.2

Usage

    Run the script.
    A file dialog will prompt you to select an image for background removal.
    After selecting the input image, another dialog will appear for saving the output image.
    The script will process the image, remove the background, and save the result.

Example


Notes

    Make sure the input image has a clear contrast between the subject and the background for optimal results.
    Experiment with different images and adjust parameters if necessary.
