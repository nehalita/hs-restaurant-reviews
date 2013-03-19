// console.log( query_link );

var res;

$('button#address').click( function() {
    //var date = new Date();
    //var dateString = "" + date.getFullYear() + (date.getMonth()+1) + date.getDate();
  
  var restaurant_name = $('input#restaurant_name').val();

  var url = "https://api.foursquare.com/v2/venues/search?"
  , version = "v=20130318" // time.strftime("%Y%m%d")
  , API_KEY= "&client_id=JSM3WVVM1OTXSHTUALUK1VADIKD5TGS3IQT2H5CX40TC4M1V&client_secret=KZ1Q4UGUJZD21TLPMK3SJY1YBUCBHGQN2X5MLRKVXYV5YVVA"
  , intent = "&intent=browse"
  , ll_hacker_school = "&ll=40.726576,-74.000645"
  , radius = "&radius=800"
  , query = "&query=" + restaurant_name;

  var query_link = "";
  query_link += url;
  query_link += version;
  query_link += API_KEY;
  query_link += intent;
  query_link += ll_hacker_school;
  query_link += radius;
  query_link += query;

  $.get( query_link, function ( response ) {
  
    res = response;

    $('div.restaurant-list').remove();

    $('button#address').after('<div class="restaurant-list"><h3>Addresses</h3><dl class="addresses"></dl></div>');

    res.response.venues.forEach( function ( venue ) {
      var address = venue.location.address + " " + venue.location.crossStreet
        , name    = venue.name;
      
      if ( address ) {
        $('dl.addresses').append("<input type='radio' name='address' value='" + address + "'><b>" + name + "</b>: " + address + "</input><br />");
      }
    });

  })
});
