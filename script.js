/*
    Function used courtesy of Oxford Protein Informatics Group
    https://www.blopig.com/blog/2013/03/a-javascript-function-to-validate-fasta-sequences/
 */
function validateFasta(fasta) {

	if (!fasta) { // check there is something first of all
		return false;
	}

	// immediately remove trailing spaces
	fasta = fasta.trim();

	// split on newlines... 
	var lines = fasta.split('\n');

	// check for header
	if (fasta[0] == '>') {
		// remove one line, starting at the first position
		lines.splice(0, 1);
	}

	// join the array back into a single string without newlines and 
	// trailing or leading spaces
	fasta = lines.join('').trim();

	if (!fasta) { // is it empty whatever we collected ? re-check not efficient 
		return false;
	}

	// note that the empty string is caught above
	// allow for Selenocysteine (U)
	return /^[ACDEFGHIKLMNPQRSTUVWY\s]+$/i.test(fasta);
}

async function blast_request(){
    let form_data = document.getElementById("sequence_input").value
    let fasta_valid = validateFasta(form_data);
    if (fasta_valid){
        console.log('FASTA data validates')
        try{
            let response = await fetch(
                'http://localhost:8000/', {
                method: 'PUT',
                headers: {"Content-type": "application/json"},
                body: JSON.stringify({"formInput":form_data})
            });
            
            // get blast data
            let blastData = await response.json();
            console.log("data received", blastData);

            // extract relevant fields
            let rowData = getRowData(blastData)
            console.log("row data ready", rowData);

            // load data to table
            $('#table').bootstrapTable({data: rowData})
            console.log("data loaded to table")
        } catch (error){
            console.log(error)
        }
    } else {
        console.log("Input does not validate");
        $('#exampleModal').modal('show')
    }
}

function getRowData(input){
    n = input['data'].length
    data = input['data']
    console.log(input)
    rows = []

    for (var i = 0; i<n; i++){
        rows.push({
            id: data[i]['Hit_id'],
            def: data[i]['Hit_def'],
            acc: data[i]['Hit_accession']
        })
    }

    return rows
}