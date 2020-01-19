window.addEventListener('load', function () {

    //set a dictionary of key = key from API, value = header text
    var offShootingKeys = {Name: "Name",OffPoss: "Poss",AtRimFG3AFrequency: "Morey Rt",AtRimFrequency: "Rim Freq", Arc3Frequency: "Arc 3 Freq", 
                        Corner3Frequency: "C3 Freq", LongMidRangeFrequency: "Long Mid Freq", LongMidRangeFGA: "Long Mid FGA", ShortMidRangeFrequency: "Short Mid Freq",
                        blank: "", AtRimAccuracy: "Rim FG%", Arc3Accuracy: "Arc 3 FG%", Corner3Accuracy: "C3 FG%", LongMidRangeAccuracy: "Long Mid FG%",
                        ShortMidRangeAccuracy: "Short Mid FG%"};
    var team_id = document.getElementById('team-id').textContent;
    var tableBody = document.getElementsByTagName('tbody')[0];
    var tableHead = document.getElementsByTagName('thead')[0];
    var tableFoot = document.getElementsByTagName('tfoot')[0];

    

    //request.open('GET', 'https://api.pbpstats.com/get-totals/nba?Season=2019-20&SeasonType=Regular%2BSeason&TeamId=' + team_id + '&Type=Player', true)
    fetch('https://api.pbpstats.com/get-totals/nba?Season=2019-20&SeasonType=Regular%2BSeason&TeamId=' + team_id + '&Type=Player')
        .then(response => {
            return response.json()
        })
        .then(data => {
            // get the player level data
            data.multi_row_table_data.forEach((player) => {
                returnSpecificData(player, offShootingKeys, tableBody, false);
            })
            //set the correct headders
            createHeaders(offShootingKeys, tableHead);
        })
        .catch(err => {
            // Do something for an error here
        })
     //https://api.pbpstats.com/get-totals/nba?Season=2019-20&SeasonType=Regular%2BSeason&StartType=All&Type=Team
     fetch('https://api.pbpstats.com/get-totals/nba?Season=2019-20&SeasonType=Regular%2BSeason&StartType=All&Type=Team')
            .then(response => {
                return response.json()
        })
        .then(data => {
           
             //get team average info
            data.multi_row_table_data.forEach((team) => {
                if (team.TeamId == team_id) {    
                    returnSpecificData(team, offShootingKeys,tableFoot, true, 'Team Average');
                }
            })
            //league averages
            returnSpecificData(data.single_row_table_data, offShootingKeys,tableFoot, true, 'League Average');
       })
        .catch(err => {
            // Do something for an error here
        })
 })


//returns data into table using the api repsonse and keys we pass, adds to the table element we pass
 function returnSpecificData(data, keysToReturn, parentElement, isFooter, footerLabel){
    let keysArray = Object.keys(keysToReturn);
    
    let row = parentElement.insertRow();
    let cell = '';
    //set the cell type to a header if its a footer and a regular td if not
    if (isFooter == true) {
        cell = 'th';
        let tableLabel = document.createElement(cell);
        tableLabel.innerHTML = footerLabel;
        row.appendChild(tableLabel);
        
        //remove name from the list of keys if were in the footer ie addng to averages
        if (keysArray.indexOf('Name')>= 0){
            keysArray.splice(keysArray.indexOf('Name'), 1 );
        }
        
    } else {
        cell = 'td';
    }    
    
    //loop through the keys to get data in the order we set, set the table cell and add it to the row
    for (j= 0; j< keysArray.length;j++) {
        let apiData = data[keysArray[j]];
        //turn percentages into whole numbers
        if (typeof apiData === "number" && apiData <= 1 && keysArray[j].indexOf("FGA")<0 && keysArray[j].indexOf("FGM")<0) {
            apiData = (apiData*100).toFixed(2);
        }
        if (apiData == null) { apiData = "";}
        let tableCell = document.createElement(cell);
        tableCell.innerHTML =  apiData;
        row.appendChild(tableCell);
    }
 }

 //returns the column headers for the element passed in
 function createHeaders(keysToReturn,parentElement){
    let row = parentElement.insertRow();
    //loop through the values of the dictionary to get the header names and add them to the table
    for (j= 0; j< Object.values(keysToReturn).length;j++) {
        let tableCell = document.createElement('th');
        tableCell.innerHTML = Object.values(keysToReturn)[j];
        row.appendChild(tableCell);
    }
 }