# Password Security Analysis & Hash Demo

### Project Description
A beginner-friendly cybersecurity project that evaluates password strength, hashes passwords with SHA-256, and visualizes the distribution of weak, medium, and strong passwords. Includes CSV export for analysis. Demonstrates Python scripting, basic security concepts, and data visualization.

## Features

Analyze password strength based on length, character types, and patterns.

Generate SHA-256 hashes of passwords to demonstrate secure storage.

Visualize the distribution of weak, medium, and strong passwords with a bar chart.

Export results to CSV for documentation or further analysis.

Supports importing password lists from external files for scalability.

## Installation

Clone the repository:

git clone https://github.com/rotnik/password-safety.git

Navigate to the project directory:

cd password-safety

Install required packages:

pip install matplotlib

## Usage

Prepare a password list file `passwords.txt` (one password per line) in the project directory.

Run the script:

python `password_security.py`

Outputs:

- Console summary of password strengths.

- `password_analysis.csv` containing Password, Strength, and SHA-256 Hash.

- Bar chart showing distribution of Weak, Medium, and Strong passwords.

## Skills Demonstrated

- Python scripting and file handling

- Basic cybersecurity concepts: password strength, hashing

- Data analysis and visualization

- CSV export and report generation

## Notes

- Safe dataset only: Do not include real user passwords.

- Designed for learning and portfolio demonstration purposes.

- Can be extended to check against known leak databases or integrate with interactive visualization tools
