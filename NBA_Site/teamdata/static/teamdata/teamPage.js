 //set a dictionary of key = key from API, value = header text
 var percentOfPlayerColumns = {Name: "Name",OffPoss: "Poss",AtRimFG3AFrequency: "Morey Rt",AtRimFrequency: "Rim Freq", Arc3Frequency: "Arc 3 Freq", 
 Corner3Frequency: "C3 Freq", LongMidRangeFrequency: "Long Mid Freq", ShortMidRangeFrequency: "Short Mid Freq",
 blank: "", AtRimAccuracy: "Rim FG%", Arc3Accuracy: "Arc 3 FG%", Corner3Accuracy: "C3 FG%", LongMidRangeAccuracy: "Long Mid FG%",
 ShortMidRangeAccuracy: "Short Mid FG%"};

 
var rawColumns = {Name: "Name", AtRimFGM: "Rim FGM", AtRimFGA: "Rim FGA", ShortMidRangeFGM: "SMid FGM", ShortMidRangeFGA: "SMid FGA", LongMidRangeFGM: "Long Mid FGM",
LongMidRangeFGA: "Long Mid FGA", Arc3FGM: "Arc3 FGM", Arc3FGA: "Arc3 FGA",Corner3FGM: "C3 FGM",Corner3FGA: "C3 FGA" }


//var percentOfTeamColumns = {LongMidRangeFGA: "Long Mid FGA", }


window.addEventListener('load', function () {

    var tbl_options = document.getElementById("table-options");
    tbl_options.addEventListener("change", changeTableView); 
      
    changeTableView();

})

function changeTableView() {
    
    var selection_value = this.value;
    if (selection_value == "PCT_Player" || selection_value == null){
            buildTable(percentOfPlayerColumns);
    } else if (selection_value == "Raw"){
            buildTable(rawColumns);
    } else if (selection_value == "PCT_Team"){
        buildTable(rawColumns, true);
        
        //user the build table function (maybe split it into more functions) to get the team average data and player data and do the division before its in the HTML
        
    }
}

function makePercentOfTeam(tableBody, tableFoot) {
    //var tableBody = document.getElementsByTagName('tbody')[0];
    //var tableFoot = document.getElementsByTagName('tfoot')[0];
    setTimeout(function(){
        var rows = tableBody.getElementsByTagName('tr');
        var teamFooterRow = tableFoot.getElementsByTagName('tr')[0];
        var footerCols = teamFooterRow.getElementsByTagName('th');
     
        for (j= 0; j< rows.length;j++) {
            var cols = rows[j].getElementsByTagName('td')
            for (i= 1; i< cols.length;i++) {
                cols[i].innerHTML =  (((Number(cols[i].innerHTML) / Number(footerCols[i].innerHTML)))*100).toFixed(2);
            }
        }
    }, 1000);
}

    
function buildTable(columnKeys, isPercentOfTeam) {
    var team_id = document.getElementById('team-id').textContent;
    var tableBody = document.getElementsByTagName('tbody')[0];
    var tableHead = document.getElementsByTagName('thead')[0];
    var tableFoot = document.getElementsByTagName('tfoot')[0];
    tableBody.innerHTML = "";
    tableHead.innerHTML = "";
    tableFoot.innerHTML = "";

    //request.open('GET', 'https://api.pbpstats.com/get-totals/nba?Season=2019-20&SeasonType=Regular%2BSeason&TeamId=' + team_id + '&Type=Player', true)
    fetch('https://api.pbpstats.com/get-totals/nba?Season=2019-20&SeasonType=Regular%2BSeason&TeamId=' + team_id + '&Type=Player')
        .then(response => {
            return response.json()
        })
        .then(data => {
            // get the player level data
            data.multi_row_table_data.forEach((player) => {
                returnSpecificData(player, columnKeys, tableBody, false);
            })
            //set the correct headders
            createHeaders(columnKeys, tableHead);
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
                    returnSpecificData(team, columnKeys,tableFoot, true, 'Team Average');
                }
            })
            //league averages
            returnSpecificData(data.single_row_table_data, columnKeys,tableFoot, true, 'League Average');
       })
        .catch(err => {
            // Do something for an error here
        })
    
    if (isPercentOfTeam ==true) {
        console.log("done");
        setTimeout(makePercentOfTeam(tableBody, tableFoot), 3000);
    }

} 


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