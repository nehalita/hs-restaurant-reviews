// console.log( queryLink );

var res;
$(document).ready(function(){
    $('button#address').click( function() {
      //get restaurantName from input 
      var restaurantName = $('#restaurant_name').val();

      console.log(restaurantName)

      //for the endpoint URL to use with foursquare's API
      var url = "https://api.foursquare.com/v2/venues/search?"
      , version = "v=" + getDateString() // ex: 20130318 for march 18
      , API_KEY= "&client_id=JSM3WVVM1OTXSHTUALUK1VADIKD5TGS3IQT2H5CX40TC4M1V&client_secret=KZ1Q4UGUJZD21TLPMK3SJY1YBUCBHGQN2X5MLRKVXYV5YVVA"
      , intent = "&intent=browse"
      , llHackerSchool = "&ll=40.726576,-74.000645"
      , radius = "&radius=800" //meters
      , query = "&query=" + restaurantName;

      var queryLink = "";
      queryLink += url;
      queryLink += version;
      queryLink += API_KEY;
      queryLink += intent;
      queryLink += llHackerSchool;
      queryLink += radius;
      queryLink += query;

      //send ajax request
      $.get( queryLink, function ( body ) {
          console.log(body)
          var search_html =  Handlebars.templates['handlebars_files.hbs'](body.response)
          $('#restaurant-js').html(search_html)
        });

        $('input.radio-button').change( function(event) {
            //event.target is dom element
            //pass $ for jquery element

            var query = $(event.target)
            
            var address = query.attr('address'); 
            console.log (address);

            var restaurantName = query.attr('restaurant-name');
            console.log(restaurantName);
            console.log(arguments);
        });
      });
      

    //forms a date string for the API request in the proper format
    function getDateString(){
        var date = new Date();
        var year = date.getFullYear()
            , month = date.getMonth() + 1
            , day = date.getDate();

        month = month < 10 ? "0" + month : month;
        day = day < 10 ? "0" + day : day;
        
        return "" + year + month + day;
    }
});
