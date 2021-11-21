function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}

function readData() {
    // readTextFile("./janeTrigrams.json", function(text){
    //     var data = JSON.parse(text);
    //     console.log(data);
    // });
    console.log(trigrams.length);

}

function findFirstEntry(word){
    var wordList = [];
    for (let i=0; i<trigrams.length; i++){
        if(trigrams[i][0][0] == word){
            var nextTwo = [trigrams[i][0][1], trigrams[i][1]];
            wordList.push(nextTwo)
        }
    }
    return wordList;
}

function findBigram(word, bigramList){
    var wordList = []
    for(let i=0; i<bigramList.length; i++){
        if(bigramList[i][0] == word){
            wordList.push(bigramList[i][1]);
        }
    }
    return wordList;
}

function generateLineFromTrigram(given){
    
    for (let i = 0; i < 16; i++) {
        var wordList = findBigram(given[1], findFirstEntry(given[0]))  
        var nextWord;
        if(wordList.length != 0){
            nextWord = wordList[Math.floor(Math.random() * wordList.length)];
        }else{
            nextWord = trigrams[Math.floor(Math.random() * trigrams.length)][1];
        }

        console.log(nextWord);

        given[0] = given[1];
        given[1] = nextWord;
    }

    //console.log(findBigram("away",findFirstEntry("passed")));

}
