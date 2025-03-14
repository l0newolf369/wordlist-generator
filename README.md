ifREADME.md

Wordlists_generator

A powerful tool for generating wordlists for penetration testing and password cracking.

Description

Wordlists_generator takes a name, alphabet, or special characters as input and generates a list of probable passwords by combining the input string with numbers (1-4 digits) at the starting, ending, or middle of the string.

Features

- Generates a list of probable passwords based on the input string
- Allows users to choose from 24 different options for combining numbers with the input string
- Saves the generated wordlist to a file named by the user

Usage

1. Run the tool and enter the input string (name, alphabet, or special characters)
2. Choose the desired options for combining numbers with the input string
3. Enter the name of the output file
4. The tool will generate the wordlist and save it to the specified file


INSTALLATION : 

1. First update the terminal:

    $.  sudo apt update

  [if you don't have python then install it ]
 
    $.  sudo apt install python3    

2. install the necessary package colorama

    $.   pip3 install colorama
 
if it doesn't work then use the followings-

    $.  puthon3 -m venv venv
    $.  source venv/bin/activate
    $.  pip3 install colorama

3. Clone the repository:    
  
    $.  git clone https://github.com/l0newolf369/wordlist-generator.git

if it the link doesn't work then just simply download the gif file from code (light green colour block) section at the top of the page

4.Navigate to the repository directory:

     $.  cd Wordlists_generator

5.Run the tool: 

    $.   python3 Wordlist.py



