function allLongestStrings(inputArray) {
    let novoArray = [];
    let tamanho = 0

    inputArray.forEach(e => {
        if(e.length > tamanho){
        tamanho = e.length;
        }
    });

    inputArray.forEach(function(e){

        if(e.length >= tamanho){
            novoArray.push(e)
        }

    });



    return novoArray;
}


console.log(allLongestStrings(["aba","aa","ad","vcd","aba"]));