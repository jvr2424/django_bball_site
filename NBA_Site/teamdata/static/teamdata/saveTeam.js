var list = "";
var added_teams ="";
var deeper_look_teams = []
window.addEventListener('load', function () {

    console.log("It's loaded!")
    //get the loacl storage and set the list global var
    list = document.getElementById("add_team");
    if (localStorage.getItem('deeperLook')===null) {
        localStorage.setItem('deeperLook', JSON.stringify([]));
    } else {
        deeper_look_teams = JSON.parse(localStorage.getItem('deeperLook'));
        addTeams()
    }



    //add event listeners to all table rows so teams can be added
    var tbl = document.getElementsByClassName("sortable");
    for (j = 0; j<tbl.length; j++)
    {

        var rows = tbl[j].getElementsByTagName("tr");


        for (i=1; i< rows.length;i++)
        {
            var team_name_button = rows[i].getElementsByTagName("td")[1];
            team_name_button.addEventListener("click", addToDeeperLook);
            //console.log(team_name);
        }
    }

})

function addTeams() {
    localStorage.setItem('deeperLook', JSON.stringify(deeper_look_teams));
    //add teams in localStorage to the deeper look box
    list.innerHTML = "";
    for (i =0; i<deeper_look_teams.length;i++)
    {
        list.innerHTML = list.innerHTML + deeper_look_teams[i];
    }
    //add the event listeners so they can be deleted
     added_teams = document.getElementsByClassName("remove_team");
      for (i=0; i<added_teams.length;i++)
     {
        added_teams[i].getElementsByTagName("td")[1].addEventListener("click", removeFromDeeperLook);

     }
     console.log("im running");
     console.log(JSON.stringify(deeper_look_teams));
}


function addToDeeperLook()
 {
  var team_name = this.parentElement.getElementsByTagName('td')[0].innerHTML
  var current_team =  "<tr class=\"remove_team\"><td style=\"width: 95%;\">" + team_name  + "</td><td style=\"width: 5%;\"><button type=\"button\" class=\"btn btn-outline-danger btn-sm\">x</button></td></tr>";
  var isAdded = false;

  for (i=0; i< deeper_look_teams.length;i++)
    {
        if (current_team==deeper_look_teams[i])
        {
            isAdded = true;
        }
    }

   if (isAdded==false)
   {
     deeper_look_teams.push(current_team);
     addTeams()

 }
}





function removeFromDeeperLook()
{
    var this_entire_row = this.parentElement.parentElement.innerHTML;
    console.log(this_entire_row);
    console.log(deeper_look_teams);
    var pos = deeper_look_teams.indexOf(this_entire_row);
    console.log(pos);
    // remove the item that was clicked
    deeper_look_teams.splice(pos, 1);
    addTeams();

}