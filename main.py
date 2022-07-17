from fastapi import FastAPI
from Bio.Blast import NCBIWWW as bb
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
import xmltodict

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:80",
    "http://localhost:9000",
    "http://localhost:*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Data(BaseModel):
    formInput: Union[str, None] = None


@app.put('/', response_model=Data)
async def root(form_value: Data):
    data_dict = dict(form_value)
    print(data_dict, data_dict['formInput'])
    return {'message': 'hello world'}

def get_blast_data(user_input: str) -> dict:
    result = bb.qblast("blastx", "pdbaa", test_sequence, format_type='XML')
    
    # write blast result to xml file
    with open('query_result.xml', 'w') as output_file:
        blast_result = result.read()
        output_file.write(blast_result)
    
    # read XML file and return dictionary
    with open('query_result.xml', 'r') as file:
        xml_file = file.read()
    query_dict = xmltodict.parse(xml_file)

    return query_dict

def main():
    test_sequence = """
    >lcl|LISX01000001.1_cds_OKJ16671.1_31 [locus_tag=AMK19_00175] [protein=penicillin-binding protein] [protein_id=OKJ16671.1] [location=39730..41184]
    GTGAACAAGCCGATCCGCCGGGTGTCGATCTTCTGCCTGGTCCTGATCCTGGCCCTGATG
    CTCCGGGTGAACTGGGTGCAGGGCGTTCAGGCGTCGACGTGGGCCAACAACCCGCACAAC
    GACCGCACCAAGTACGACAAGTACGCCTACCCGCGCGGCAACATCATCGTCGGCGGCCAG
    GCCGTCACCAAGTCCGACTTCGTCAACGGGCTGCGCTACAAGTACAAGCGCTCCTGGGTG
    GACGGGCCGATGTACGCGCCGGTCACCGGCTACTCCTCGCAGACGTACGACGCCAGCCAG
    CTGGAGAAGCTGGAGGACGGCATCCTCTCCGGCACCGACTCGCGGCTGTTCTTCCGCAAC
    ACCCTGGACATGCTGACCGGCAAGCCCAAGCAGGGCGGCGACGTGGTCACCACCATCGAC
    CCCAAGGTGCAGAAGGCCGGCTTCGAGGGGCTCGGCAACAAGAAGGGCGCCGCGGTCGCC
    ATCGACCCGAAGACCGGGGCGATCCTCGGGCTGGTCTCCACCCCGTCCTACGACCCGGGC
    ACCTTCGCGGGCGGCACCAAGGACGACGAGAAGGCCTGGACGGCACTCGACAGCGACCCG
    AACAAGCCGATGCTGAACCGGGCGCTGCGCGAGACCTACCCGCCCGGCTCGACCTTCAAG
    CTGGTCACCGCGGCGACCGCGTTCGAGACCGGCAAGTACCAGAGCCCGTCGGACGTCACC
    GACACCCCGGACCAGTACATCCTGCCCGGCACCAGCACCCCGCTGATCAACGCCAGCCCC
    ACCGAGGACTGCGGGAACGCCACCGTGCAACACGCGATGGACCTGTCCTGCAACACGGTG
    TTCGGCAAGATGGGCGCCGAGCTGGGCGGCGACAAGCTGCGGGCGCAGGCCGAGAAGTTC
    GGCTTCAACAAGGAAGTGACCATCCCGATCCGGGCCGACGCCAGCCACTTCCCGTCCGGC
    TCCAAGCCCGACGGCACCGCGATGGACGCGATCGGCCAGCACGACACCCGGGCCACCCCG
    CTGCAGATGGCCATGGTGGCCGCCGCGATCGCCAACAACGGCTCGCTGATGGAGCCCTAC
    CTGGTCGCCCAGGAGGGCTCGGCCGGGAACGTGATCTCCACCCACACCGAGCACCAGCTG
    TCGCAGGCGGTCTCGCCGGCCACCGCGCAGAAGCTCCAGCAGCTGATGGAGTCGGTGGTG
    CAGCACGGCACCGGCACGAACGCGAAGATCCCGGGCGTGACGGTCGGCGGCAAGACCGGC
    ACCGCCCAGCACGGCCAGGACAACTCGGGTCTGCCGTTCGCCTGGTTCGTCTCCTACGCC
    AAGGGCCAGGACGGCAAGCAGGTCGCCGTCGCGGTGGTGGTCGAGGACGGCTCCAGCGAG
    GCGCAGCAGATCTCCGGCGGCTCGCTGGCCGCGCCGATCGCCAAGGCGATGATGCAGGCG
    GCGCTCGGGAAGTAG
    """
    # result = bb.qblast('blastn', 'nt', test_sequence)
    result = bb.qblast("blastx", "pdbaa", test_sequence, format_type='XML')
    # print(xmltodict.parse(result.read()))
    a = 13
    with open('query_result.xml', 'w') as output_file:
        blast_result = result.read()
        output_file.write(blast_result)
    
    with open('query_result.xml', 'r') as file:
        xml_file = file.read()
    query_dict = xmltodict.parse(xml_file)
    print(query_dict)


if __name__ == '__main__':
    main()
