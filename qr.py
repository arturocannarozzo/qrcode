Python
from qrcode import QRCode, make
import os


# Function to generate and save QR code
def generate_qr(link, filename):
  """Generates a QR code from a website link and saves it as an image.

  Args:
      link: The website link to encode in the QR code.
      filename (str): The filename to save the QR code image.
  """
  qr = QRCode(
      version=1,  # Adjust version for complexity (higher = smaller modules)
      box_size=10,  # Size of each module in pixels
      border=4,  # White border around the QR code
  )
  qr.add_data(link)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save(filename)


def bulk_generate_qr(file_path, output_folder):
  """Reads website links from a text file and generates QR codes for each, saving them in a folder.

  Args:
      file_path (str): Path to the text file containing website links (one per line).
      output_folder (str): Path to the folder where QR codes will be saved.
  """
  # Check if output folder exists, create it if not
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  # Open the text file in read mode
  with open(file_path, "r") as file:
    lines = file.readlines()

  # Generate QR code for each link in the file
  for i, line in enumerate(lines):
    link = line.strip()  # Remove trailing newline character
    filename = f"{output_folder}/qr_{i+1}.png"  # Generate unique filenames
    generate_qr(link, filename)
    print(f"QR code generated for {link} and saved as {filename}")


# Get user input for file path and output folder
file_path = input("Enter path to text file (one link per line): ")
output_folder = input("Enter path to output folder for QR codes: ")

# Generate QR codes in bulk
bulk_generate_qr(file_path, output_folder)

print("All QR codes generated successfully!")
