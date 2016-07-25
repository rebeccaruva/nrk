$.ajax({
  url: 'http://quotes.rest/qod.json',
  dataType: 'json',
  success: function(data) {
    console.log(data);
  }
});
