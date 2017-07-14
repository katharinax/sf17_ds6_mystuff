----------- README for the Egyptian hieroglyph dataset ----------------
This dataset is compiled by Morris Franken, complementary to the paper titeled "Automatic Egyptian Hieroglyph Recognition by Retrieving Images as Texts" (ACM Conference on Multimedia, 2013).
We kindly request that you cite our paper if you find this dataset helpful in any way.

NOTE: The labelling may not be 100% correct. I am not an Egyptologist, and the hieroglyphs that I was unable to identify are labelled as "UNKNOWN".

totalImages = 4210 (of which 179 are labelled as UNKNOWN)
totalClasses = 171 (excluding the UNKNOWN class)

This dataset is build from the hieroglyphs found in 10 different pictures from the book "The Pyramid of Unas" (Alexandre Piankoff, 1955). We therefore urge you to have access to this book before using the dataset.
The ten different pictures used throughout this dataset are: 3,5,7,9,20,21,22,23,39,41 (numbers represent the numbers used in the book "The pyramid of Unas")
Each hieroglyph is manually annotated and labelled according the Gardiner Sign List. The images are stored with their label and number in their name.

Example: 030001_D58.png
The first two digits of the name represent the picture number from which the hieroglyph is extracted. The remaining 4 digits represent the hieroglyph number with respect to its picture, which is related to the reading order. However, since these pictures only depict a part of a pyramid wall, each column is separate from the next. Further more, the Gardiner label of this image is 'D58'.

Aside from the manual annotation, we used a text-detection method to extract the hieroglyphs automatically. The results are shown in Dataset/Automated/
The labels on automatic detected images are based on a comparison with the manual detection, and are labelled according the the Pascal VOC overlap criteria (50% overlap).

The x/y position of each hieroglyph is stored in the Location-folder. Each file in this folder contains the exact position of all (raw) annotated hieroglyphs in their corresponding picture. 
Example: "030000_S29.png,71,27,105,104," from Dataset/Manual/Locations/3.txt:
  - image = Dataset/Manual/Raw/3/030000_D35.png
  - Picture number = 3 	(Dataset/Pictures/egyptianTexts3.jpg)
  - index number = 0
  - Gardiner label = D35
  - top-left position = 71,27
  - bottom-right position = 105,104		(such that width = (105-71) = 34, and the height is (104-27) = 77)

After the hieroglyphs are cut out, the images are pre-processed to fit in a 50x75 frame, while maintaining their with/height ratio. The remaining unfilled pixels are filled with background texture to mimic the actual background.

Included in this dataset are some tools to create the language model.
in Dataset/LanguageModel/JSESH_EgyptianTexts/ are the Egyptian texts from the JSesh database. Jsesh is an open source program, used to write hieroglyphs (http://jsesh.qenherkhopeshef.org/). The texts are written in a mixture of Gardiner labels and transliteration. Each text can be opened by Jsesh to view the hieroglyphs.
Furthermore, a lexicon is included in Dataset/LanguageModel/Lexicon.txt. Originally from OpenGlyp (http://sourceforge.net/projects/openglyph/), but with added word-occurrence based on the EgyptianTexts. Each time a word is encoutered in the text, the word-occurrence is increased by 1 divided by the amount of other possible words that can be made with the surrounding hieroglyphs.
The lexicon is organised as follows: each line contains a word, that is made up by a number of hieroglyphs. Other information such as the translation, transliteration and word-occurrence is also stored. Each element is separated by a ';'
Example: D36,N35,D7,;an;beautiful;0.333333;
  - The 3 hieroglyphs used to write this word: D36,N35,D7,
  - transliteration: an
  - English translation: beautiful
  - word-occurrence: 0.333333

nGrams are included in this dataset as well, under Dataset/LanguageModel/nGrams.txt
Each line in this file contains an nGram (either uni-gram, bi-gram or tri-gram) accompanied by their occurrence. 
Example: G17,N29,G1,;9;
  - Hieroglyphs used to write this tri-gram: G17,N29,G1
  - number of occurrences in the EgyptianTexts database: 9

The dataset is organised as follows:
Dataset/
  Pictures/			Contains 10 pictures from the book "The Pyramid of Unas", which are used throughout this dataset

  Manual/			Contains the manually annotated images of hieroglyphs
    Locations/			Contains the location-files that hold the x/y position of each hieroglyph.
    Preprocessed/		Contains the pre-processed images
    Raw/			Contains the raw, un-pre-processed, images of hieroglyphs
	
  Automated/			Contains the result of the automatic hieroglpyh detection
    Locations/			Contains the location-files that hold the x/y position of each hieroglyph.
    Preprocessed/		Contains the pre-processed images
    Raw/			Contains the raw, un-pre-processed, images of hieroglyphs

  ExampleSet7/			An example of how the test and train set can be separated. In this case the hieroglyphs found on picture #7 are used for testing, while the others are used for training.
    test/			Simply contains all pre-processed images from picture #7
    train/			Contains all the hieroglyphs images from other pictures, organised in such a way that each class has its own separate folder. The train set is build from the pre-processed and manually annotated images, minus the "UNKNOWN" images.

  Language Model/
    JSESH_EgyptianTexts/	Contains the EgyptianTexts database of JSesh, which is a program used to write hieroglyphs (http://jsesh.qenherkhopeshef.org/).
    Lexicon.txt
    nGrams.txt

