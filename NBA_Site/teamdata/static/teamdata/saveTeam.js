window.addEventListener('load', function ()
{
  console.log("It's loaded!")
    var tbl = document.getElementById("misc_data");
    var rows = tbl.getElementsByTagName("tr");

    var i;
    for (i=1; i< rows.length;i++)
    {
        var team_name = rows[i].getElementsByTagName("td")[0];
        team_name.addEventListener("click", addToDeeperLook);
        console.log(team_name);
    }
})

var deeper_look_teams = []
var counter = 0

function addToDeeperLook()
 {
  var list = document.getElementById("add_team");
  var current_team =  "<tr><td>" + this.textContent  + "</td><td id=\"remove_team_" + counter + "\">x</td></tr>";
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

     setTimeout(function()
     {
         document.getElementById("remove_team"+counter.toString()).addEventListener("click", removeFromDeeperLook);
         counter = counter + 1;
    }, 2000);

 }
}

function removeFromDeeperLook()
{
    var pos = deeper_look_teams.indexOf(this);
    var list = document.getElementById("add_team");
    deeper_look_teams.splice(pos, 1);
    //clear the list and reprint
    list.innerHTML = "";

    for (i =0; i<deeper_look_teams.length;i++)
    {
        list.innerHTML = list.innerHTML + deeper_look_teams[i];
    }

}