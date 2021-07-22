# Unit Diagram Reader (connection macro)

### Welcome! If you're on this page, you probably want to help out with, upgrade, or just get familiar with the source code of the Unit Diagram Reader.

## Getting started

1. You'll need to install Anaconda https://www.anaconda.com/products/individual
     - You also need to download the Unit Diagram Reader source code. Click on the green 'Code' button that's near the top of this page and 'Download ZIP'. Extract it to wherever you like.
     
2. Once you've installed Anaconda, open Anaconda Prompt from your start menu. Use the 'cd' command to navigate to the folder where you extracted the Unit Diagram Reader ZIP file to. Here, there should be a file called ```environment.yml.```
3. Type the following command into your Anaconda Prompt and hit enter: ```conda env create -f environment.yml```
4. Once it's done, do ```conda activate unitdiagramreader```
5. Finally, do ```python main.py```. If you followed all the steps above correctly, the Unit Diagram Reader should open!

Feel free to open any of the .py files to see what they do. After you make any changes, always run ```python main.py``` to test your code.

#### Notes
 - We recommend using the Spyder editor to edit Python files. It should already be in your Start menu if you installed Anaconda.
     - To run the Unit Diagram Reader in Spyder, open ```main.py``` in Spyder, and click the green 'Run' button at the top.
 - Instructions on how to compile to an .EXE (so that you can send the program to non-coders) are found at the top of main.py.

## Wishlist (as of 20/05/2021)

| Task                                                                                                        | Progress             |
|:-------------------------------------------------------------------------------------------------------------|:----------------------|
| ability to add multiple stations at once including generated set of location names + manual entry of TIPLOC | Not done             |
| TODO tags in source code.                                                                                   | Some done            |
| 24:xx:xx times                                                                                              | Not done             |
| Ability to select day codes e.g. SX                                                                         | Not done             |
| Read start/end times in dialog box. Currently the from time/to time boxes do nothing.                       | Not done             |
| Flag illegal if connecting between different train classes.                                                 | Not done             |
| Import/Export list of connections.                                                                          | Not done             |
| Colour code based on legality.                                                                              | Highlights in Excel. |
