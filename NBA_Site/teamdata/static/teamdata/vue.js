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
              {Team:'NYK', Wins:3, Losses:50},
              {Team:'HOU', Wins:43, Losses:7},
              {Team:'LAL', Wins:33, Losses:17},
              {Team:'LAC', Wins:35, Losses:15},
            ]
          },
          1:{
            headers:['Team','ORTG','DRTG'], 
            data:[
              {Team:'NYK', ORTG:95, DRTG:150},
              {Team:'HOU', ORTG:115, DRTG:109},
              {Team:'LAL', ORTG:106, DRTG:100},
              {Team:'LAC', ORTG:108, DRTG:99},
            ]
          },
          2:{
            headers:['Team','TS','EFG'], 
            data:[
              {Team:'NYK', TS:0.5, EFG:0.55},
              {Team:'HOU', TS:0.65, EFG:0.64},
              {Team:'LAL', TS:0.54, EFG:0.53},
              {Team:'LAC', TS:0.56, EFG:0.53},
            ]
          },
          3:{
            headers:['Team','ORB','DRB'], 
            data:[
              {Team:'NYK', ORB:5, DRB:35},
              {Team:'HOU', ORB:7, DRB:30},
              {Team:'LAL', ORB:8, DRB:40},
              {Team:'LAC', ORB:8, DRB:45},
            ]
          }
        },


        //option selector
        table: 0,
        currentTable: null,
        tableOptions: [
          {value:0, selected:true, text:'Quick Look' },
          {value:1, selected:false, text:'Standings' },
          {value:2, selected:false, text:'Shooting' },
          {value:3, selected:false, text:'Opponent Shooting' }
        ],

      }
    });

  });