This script will transfrom an image with text from each page of a list of pdf files in a given folder to a jpeg file, then read the image file in order to extract its text.
Upon executing the script you will be asked to provide the absolute path to your folder containing pdf files.

On macOS, install tesseract through brew:
brew install tesseract


In some cases you may need to intall companents manually:
brew install --build-from-source mpdecimal
brew install --build-from-source tcl-tk
brew install --build-from-source bison
brew install --build-from-source python@3.9
brew install --build-from-source sphinx-doc
brew install --build-from-source cmake

For Windows and macOS you will need to specify the path to your tesseract install.

Create a .env file where you will store the path to your tesseract installation (use the command 'which tesseract'):
TESSERACT_PATH = '/path/to/tesseract'

So that the path will be set in the script as such:
pytesseract.pytesseract.tesseract_cmd = config('TESSERACT_PATH')
