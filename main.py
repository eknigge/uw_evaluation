from fastapi import FastAPI
from Bio.Blast import NCBIWWW as bb
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
from fastapi.encoders import jsonable_encoder
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


@app.put('/')
async def root(form_value: Data):
    data_dict = dict(form_value)
    blast_data = get_blast_data(data_dict['formInput'])
    return blast_data


def get_blast_data(user_input: str) -> dict:
    result = bb.qblast("blastn", "nt", user_input, format_type='XML')
    
    # write blast result to xml file
    with open('query_result.xml', 'w') as output_file:
        blast_result = result.read()
        output_file.write(blast_result)
    
    # read XML file and return dictionary
    with open('query_result.xml', 'r') as file:
        xml_file = file.read()
    query_dict = xmltodict.parse(xml_file)
    output = {'data': query_dict['BlastOutput']['BlastOutput_iterations']['Iteration']['Iteration_hits']['Hit']}
    return output


def main():
    with open('query_result.xml', 'r') as file:
        xml_file = file.read()
    query_dict = xmltodict.parse(xml_file)
    temp = query_dict['BlastOutput']['BlastOutput_iterations']['Iteration']['Iteration_hits']['Hit']


if __name__ == '__main__':
    main()
