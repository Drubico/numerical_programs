let formula_loading=()=>{
    txt_formula.innerHTML = "Formula :";
    txt_formula.innerHTML =formula_string;
}

btn_comenzar.addEventListener("click", ()=>
{
    console.log(index);
    if(index!=0){
        for (let i=0; i < index; i++) {
            var row = table.deleteRow(-1);    
    }

    }
    index=0
    for (index; index < input_1.value; index++) {
        var row = table.insertRow(-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        
        cell1.innerHTML = index;
        cell2.innerHTML =input_2.value;
        cell3.innerHTML =input_3.value;
        cell4.innerHTML = input_1.value;
    }
    
    resultados.style.display = 'block'
    var resultados_row = resultados_table.insertRow(-1);
    var resultados_cell1 = resultados_row.insertCell(0);
    var resultados_cell2 = resultados_row.insertCell(1);
    var resultados_cell3 = resultados_row.insertCell(2);
    var resultados_cell4 = resultados_row.insertCell(3);
    
    resultados_cell1.innerHTML = index;
    resultados_cell2.innerHTML =input_2.value;
    resultados_cell3.innerHTML =input_3.value;
    resultados_cell4.innerHTML = input_1.value;

});

