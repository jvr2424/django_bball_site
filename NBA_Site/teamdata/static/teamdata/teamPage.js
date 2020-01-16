

window.addEventListener('load', function () {

    //var request = new XMLHttpRequest()
    var team_id = document.getElementById('team-id').textContent;
    var tableBody = document.getElementsByTagName('tbody')[0];
    var tableHead = document.getElementsByTagName('thead')[0];
    console.log(team_id);

    //request.open('GET', 'https://api.pbpstats.com/get-totals/nba?Season=2019-20&SeasonType=Regular%2BSeason&TeamId=' + team_id + '&Type=Player', true)
    fetch('https://api.pbpstats.com/get-totals/nba?Season=2019-20&SeasonType=Regular%2BSeason&TeamId=' + team_id + '&Type=Player')
        .then(response => {
            return response.json()
        })
        .then(data => {
            // Work with JSON data here
            data.multi_row_table_data.forEach((player) => {
                //create the elements we need
                const t_row = document.createElement('tr');
                // these are the columns
                const data_name = document.createElement('td');
                const data_rim_freq = document.createElement('td');
                const data_arc_three_freq = document.createElement('td');

                //this is where we add data from api
                data_name.innerHTML = player.Name;
                data_rim_freq.innerHTML  = (player.AtRimFrequency * 100).toFixed(2);
                data_arc_three_freq.innerHTML  = (player.Arc3Frequency * 100).toFixed(2);

                console.log(player.Name)
                //append the data we got to the appropriate table elements
                tableBody.appendChild(t_row);
                t_row.appendChild(data_name);
                t_row.appendChild(data_rim_freq);
                t_row.appendChild(data_arc_three_freq);
            })
            //set the correct headders
            const t_head_name = document.createElement('th');
            const t_head_rim_freq = document.createElement('th');
            const t_head_arc_three_freq = document.createElement('th');
            // set table header text
            t_head_name.innerHTML = "Name";
            t_head_rim_freq.innerHTML = "Rim Freq";
            t_head_arc_three_freq.innerHTML = "Arc 3 Freq"
            //append to header tag
            tableHead.appendChild(t_head_name);
            tableHead.appendChild(t_head_rim_freq);
            tableHead.appendChild(t_head_arc_three_freq);
        })
        .catch(err => {
            // Do something for an error here
        })
 })
