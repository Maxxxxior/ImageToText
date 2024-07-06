# ImageToText

This Python software converts text found in images into text files.

## How to Use

1. Place your desired image containing visible text into the **Images** folder.
2. Run the program. It will scan the **Images** folder, extract text from the images, and save the text into the **Text** folder.
3. Each text file in the **Text** folder will be named after its corresponding image file with a `.txt` extension.

## Supported Image Formats

Images in the following formats are supported: `.png`, `.jpg`, `.jpeg`, `.bmp`, and `.gif`. Note that support for `.gif` images may vary.

## Example Files

In the repository, you'll find sample files for testing:

- Images: `text.png`, `text2.png`
- Text: `text.txt`, `text2.txt`

Feel free to use these for testing purposes, but they are not required.

## Note on Text Extraction

- The program may encounter difficulties with fancy or elaborate fonts.
- Text extraction from images may not always be accurate or complete.