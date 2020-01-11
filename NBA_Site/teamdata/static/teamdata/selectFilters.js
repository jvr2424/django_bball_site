window.addEventListener('load', function ()
{
    var tbl_selector = document.getElementById("table-select");
    var conference_selector = document.getElementById("conference");


    tbl_selector.addEventListener("click", showHideTable);
    conference_selector.addEventListener("click", selectConference);
    showHideTable();
    selectConference();
})

//shows the table the user selects, hides all others
function showHideTable(){
    var tbl_num = this.value;
    if (tbl_num ==  null){
        tbl_num = 0;
    }
    //console.log(tbl_num);
    var tables = document.getElementsByClassName("sortable");

    for (i=0;i< tables.length; i++)
    {
        if (i != tbl_num){
            tables[i].style.display = "none";
        } else {
            tables[i].style.display = "";
        }
    }
}


function selectConference() {
   var selection_value = this.value;
   if (selection_value ==  null){
        selection_value = "All";
    }

    var teams =  document.getElementsByClassName("conference");

    for (i=0;i<teams.length; i++)
    {
        if (selection_value == "All") {
            teams[i].parentElement.style.display = "";
        } else if (selection_value == "East"){
            if(teams[i].innerHTML == "East") {
                teams[i].parentElement.style.display = "";
            } else {
                teams[i].parentElement.style.display = "none";
            }
        } else if (selection_value == "West"){
            if(teams[i].innerHTML == "West") {
                teams[i].parentElement.style.display = "";
            } else {
                teams[i].parentElement.style.display = "none";
            }
        }
    }





}


