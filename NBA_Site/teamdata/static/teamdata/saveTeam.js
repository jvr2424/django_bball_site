window.addEventListener('load', function ()
{
  console.log("It's loaded!")
    var tbl = document.getElementsByClassName("sortable");
    for (j = 0; j<tbl.length; j++)
    {

        var rows = tbl[j].getElementsByTagName("tr");


        for (i=1; i< rows.length;i++)
        {
            var team_name = rows[i].getElementsByTagName("td")[0];
            team_name.addEventListener("click", addToDeeperLook);
            //console.log(team_name);
        }
    }
})

var deeper_look_teams = []
var counter = 0

function addToDeeperLook()
 {
  var list = document.getElementById("add_team");
  var current_team =  "<tr class=\"remove_team\"><td style=\"width: 95%;\">" + this.textContent  + "</td><td style=\"width: 5%;\"><button type=\"button\" class=\"btn btn-outline-danger btn-sm\">x</button></td></tr>";
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
     list.innerHTML = list.innerHTML + deeper_look_teams[deeper_look_teams.length-1];

     var added_teams = document.getElementsByClassName("remove_team");
      for (i=0; i<added_teams.length;i++)
     {
        added_teams[i].getElementsByTagName("td")[1].addEventListener("click", removeFromDeeperLook);

     }
     counter = counter + 1;

 }
}

function removeFromDeeperLook()
{
    var this_entire_row = this.parentElement.parentElement.innerHTML;
    console.log(this_entire_row);
    console.log(deeper_look_teams);
    var pos = deeper_look_teams.indexOf(this_entire_row);
    console.log(pos);
    var list = document.getElementById("add_team");
    deeper_look_teams.splice(pos, 1);
   // deeper_look_teams.filter(team => team != this);
    //console.log(deeper_look_teams)
    //clear the list and reprint
    list.innerHTML = "";

    for (i =0; i<deeper_look_teams.length;i++)
    {
        list.innerHTML = list.innerHTML + deeper_look_teams[i];
    }

    var added_teams = document.getElementsByClassName("remove_team")
     for (i=0; i< added_teams.length;i++)
     {
        added_teams[i].getElementsByTagName("td")[1].addEventListener("click", removeFromDeeperLook);
     }


}