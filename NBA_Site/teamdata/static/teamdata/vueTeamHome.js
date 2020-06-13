document.addEventListener('DOMContentLoaded', function () {
    
    var selectVue = new Vue({
      delimiters: ['[[', ']]'],
      el: '#app',
      
      data: {
        //table data
        tableData: {
          0:{
            headers:['Team','Wins','Losses'], 
            data:[
              {Team:'NYK', Conference: "East", Wins:3, Losses:50},
              {Team:'HOU', Conference: "West", Wins:43, Losses:7},
              {Team:'LAL', Conference: "West", Wins:33, Losses:17},
              {Team:'LAC', Conference: "West", Wins:35, Losses:15},
            ]
          },
          1:{
            headers:['Team','ORTG','DRTG'], 
            data:[
              {Team:'NYK', Conference: "East", ORTG:95, DRTG:150},
              {Team:'HOU', Conference: "West", ORTG:115, DRTG:109},
              {Team:'LAL', Conference: "West", ORTG:106, DRTG:100},
              {Team:'LAC', Conference: "West", ORTG:108, DRTG:99},
            ]
          },
          2:{
            headers:['Team','TS','EFG'], 
            data:[
              {Team:'NYK', Conference: "East", TS:0.5, EFG:0.55},
              {Team:'HOU', Conference: "West", TS:0.65, EFG:0.64},
              {Team:'LAL', Conference: "West", TS:0.54, EFG:0.53},
              {Team:'LAC', Conference: "West", TS:0.56, EFG:0.53},
            ]
          },
          3:{
            headers:['Team','ORB','DRB'], 
            data:[
              {Team:'NYK', Conference: "East", ORB:5, DRB:35},
              {Team:'HOU', Conference: "West", ORB:7, DRB:30},
              {Team:'LAL', Conference: "West", ORB:8, DRB:40},
              {Team:'LAC', Conference: "West", ORB:8, DRB:45},
            ]
          }
        },
        allTableData: null,

        //table option selector
        table: 0,
        currentTable: null,
        tableOptions: [
          {value:0, text:'Quick Look' },
          {value:1, text:'Standings' },
          {value:2, text:'Shooting' },
          {value:3, text:'Opponent Shooting' }
        ],

        //conference
        conference:0,
        conferenceOptions: [
          {value:0, text:'All' },
          {value:1, text:'East' },
          {value:2, text:'West' },
        ],

      },

      methods: {
        filterConference: function(e) {
          var index = e.target.value;
          var query = this.conferenceOptions.filter(function(c){return c.value == index });
          query = query[0].text;
          
          if (this.allTableData == null){
            this.allTableData = JSON.parse(JSON.stringify(this.tableData));
          }
          if (query != 'All'){
            this.tableData[this.table].data = this.allTableData[this.table].data.filter(function(d) {
              return d.Conference == query;
            }
          );
          } else{
            this.tableData[this.table].data = this.allTableData[this.table].data
          }
          
          
        }
      }
    });

  });