# JPG to PDF Converter and Merger Script

This Python script provides a simple way to:
1. Convert all `.jpg` or `.jpeg` images in a folder to individual PDF files.
2. Merge all PDF files in a folder into a single output PDF file named `OUTPUT.PDF`.
3. Process multiple folders recursively within a given root directory.

## Requirements

Before using this script, make sure you have the following Python libraries installed:

- `Pillow` for image processing
- `PyPDF2` for PDF manipulation

You can install these libraries using pip:

```bash
pip install Pillow PyPDF2
```

## How to Use

1. Place the script in a directory of your choice.
2. Set the `root_folder` variable to the root directory you want to process. By default, it is set to the current directory (`.`).
3. Run the script using Python:

```bash
python script_name.py
```

The script will:
- Traverse through all subdirectories of the specified root folder.
- Convert `.jpg` and `.jpeg` files to `.pdf` in each folder.
- Merge all resulting PDF files in each folder into a single `OUTPUT.PDF` file.

### Example

Suppose you have the following folder structure:

```
root_folder/
  folder1/
    image1.jpg
    image2.jpg
  folder2/
    file1.jpg
    file2.pdf
```

After running the script:

- `folder1/` will contain:
  - `image1.pdf`
  - `image2.pdf`
  - `OUTPUT.PDF` (merged PDF of `image1.pdf` and `image2.pdf`)

- `folder2/` will contain:
  - `file1.pdf`
  - `file2.pdf` (unchanged)
  - `OUTPUT.PDF` (merged PDF of `file1.pdf` and `file2.pdf`)

## Notes

- The script processes only folders containing files (it skips empty folders).
- If there are no PDF files in a folder, the merging step is skipped for that folder.
- The final merged PDF for the last processed folder is explicitly printed for convenience.

## Output

- Converted PDF files are saved in the same folder as the original images.
- The merged PDF file is named `OUTPUT.PDF` and is saved in each respective folder.

Enjoy your streamlined JPG-to-PDF conversion and merging workflow!

