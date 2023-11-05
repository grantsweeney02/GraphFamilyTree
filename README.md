# Fraternity Family Tree Visualizer

Visualize your fraternity's lineage with this Family Tree Visualizer. Using data from an Excel file, this script creates a graphical representation of the 'big' and 'little' brother relationships in your fraternity using the `graphviz` library.

## Table of Contents

- [Getting Started](##getting-started)
  - [Prerequisites](###prerequisites)
  - [Installation](###installation)
- [Usage](##usage)
- [File Structure](##file-structure)
- [Contributing](##contributing)
- [Authors](##authors)
- [License](##license)
- [Acknowledgments](##acknowledgments)

## Getting Started

These instructions will guide you on how to deploy the script on your local machine.

### Prerequisites

What things you need to install the software and how to install them:

```bash
pip install pandas
pip install graphviz
```
### Installation
'''
git clone https://github.com/your-username/fraternity-family-tree.git
cd fraternity-family-tree
'''

## Usage
Place your tree_data.xlsx file in the root directory of the project and run the script:
```
python family_tree_visualizer.py
```
The script will generate a PNG image named Theta_Tau_family_tree.png, visualizing the fraternity's family tree.

## File Structure
-'family_tree_visualizer.py': The main Python script for generating the family tree.
-'tree_data.xlsx': The Excel spreadsheet that contains the data of fraternity members.

## Contributing
If you have suggestions for improving the script, please fork the repo and create a pull request, or open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!
*Fork the Project
*Create your Feature Branch (git checkout -b feature/AmazingFeature)
*Commit your Changes (git commit -m 'Add some AmazingFeature')
*Push to the Branch (git push origin feature/AmazingFeature)
*Open a Pull Request

## Authors
- Grant Sweeney

## License
N/A

## Acknowledgments
- Hat tip to anyone whose code was used as inspiration.
- Gratitude to the fraternity members for their support and participation.
- Special thanks to the `graphviz` and `pandas` communities for maintaining such useful open-source tools.

