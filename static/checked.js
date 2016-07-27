/*

google.charts.load("current", {packages:["timeline"]});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var container = document.getElementById('example5.3');
  var chart = new google.visualization.Timeline(container);
  var dataTable = new google.visualization.DataTable();
  dataTable.addColumn({ type: 'string', id: 'Room' });
  dataTable.addColumn({ type: 'string', id: 'Name' });
  dataTable.addColumn({ type: 'date', id: 'Start' });
  dataTable.addColumn({ type: 'date', id: 'End' });
  dataTable.addRows([
    [ 'Center', 'CSS Fundamentals',    new Date(0,0,0,12,0,0),  new Date(0,0,0,14,0,0) ],
    [ 'Center', 'Intro JavaScript',    new Date(0,0,0,14,30,0), new Date(0,0,0,16,0,0) ],
    [ 'Center', 'Advanced JavaScript', new Date(0,0,0,16,30,0), new Date(0,0,0,19,0,0) ],
    [ 'Google', 'Basic Python',   new Date(0,0,0,12,30,0), new Date(0,0,0,14,0,0) ],
    [ 'Google', 'Intermediate Python',       new Date(0,0,0,14,30,0), new Date(0,0,0,16,0,0) ],
    [ 'Google', 'Python Review',        new Date(0,0,0,16,30,0), new Date(0,0,0,18,0,0) ],
    [ 'Conference Room', 'Google Charts',  new Date(0,0,0,12,30,0), new Date(0,0,0,14,0,0) ],
    [ 'Conference Room', 'Closure',        new Date(0,0,0,14,30,0), new Date(0,0,0,16,0,0) ],
    [ 'Conference Room', 'App Engine',     new Date(0,0,0,16,30,0), new Date(0,0,0,18,30,0) ]]);

  var options = {
    timeline: { colorByRowLabel: true },
    backgroundColor: '#ffd'
  };

  chart.draw(dataTable, options);
}
*/
