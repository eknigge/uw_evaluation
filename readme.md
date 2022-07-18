# Installation
You will need to have Python 3 installed and the following libraries
- fastapi
- Bio
- pydantic
- typing
- xmltodict

You can install them using the python package manager
```
pip install [package]
```
The apps has a fastpi back-end and a bootstrap front-end. 

## Hosting the API
To host the back-end API run the following command in the project directory
```
unicorn main:app
```

## Running the web server
To run the web server run the following command
```
python -m http.server 9000
```

## Running a BLAST query
Enter sample data into the form box, e.g. 
```
>NC_009085_A1S_r15 NC_009085.1 Acinetobacter baumannii ATCC 17978 chromosome, complete genome.
ATTGAACGCTGGCGGCAGGCTTAACACATGCAAGTCGAGCGGGGGAAGGTAGCTTGCTAC
TGGACCTAGCGGCGGACGGGTGAGTAATGCTTAGGAATCTGCCTATTAGTGGGGGACAAC
ATCTCGAAAGGGATGCTAATACCGCATACGTCCTACGGGAGAAAGCAGGGGATCTTCGGA
CCTTGCGCTAATAGATGAGCCTAAGTCGGATTAGCTAGTTGGTGGGGTAAAGGCCTACCA
AGGCGACGATCTGTAGCGGGTCTGAGAGGATGATCCGCCACACTGGGACTGAGACACGGC
CCAGA
```

Then click **Submit**. Note that it **will take a long time** to query the data and display it to the page. 


# Future Features 
- [ ] Disable submit query button when query is active
- [ ] Change text of query button to "Running..." when active
- [ ] Limit table to 10 results and provide templating for additional results
- [ ] Add some sort of loading screen or show progression