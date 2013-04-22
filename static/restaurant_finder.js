// console.log( queryLink );

var res;
$(document).ready(function(){
    $('button#address').click( function() {
      //get restaurantName from input 
        var restaurantName = $('#restaurant_name').val();
    
      //for the endpoint URL to use with foursquare's API
        var url = "https://api.foursquare.com/v2/venues/search?";
        var fsq_params = {
          v: "" + getDateString() // ex: 20130318 for march 18
          , client_id: "JSM3WVVM1OTXSHTUALUK1VADIKD5TGS3IQT2H5CX40TC4M1V"
          , client_secret: "KZ1Q4UGUJZD21TLPMK3SJY1YBUCBHGQN2X5MLRKVXYV5YVVA"
          , intent: "browse"
          , ll: "40.726576,-74.000645"
          , radius: "800" //meters
          , query: "" + restaurantName
        };
          // creates foursquare's query link based on parameters above

        var queryLink = url + $.param(fsq_params) 
            
        //ajax request that happens in the background
        $.get( queryLink, function ( body ) {
          
          console.log(body);
          var search_html =  Handlebars.templates['handlebars_files.hbs'](body.response)
          $('#restaurant-js').html(search_html)
        });
    });
            
    $('#restaurant-js').on('change', 'input.radio-button', function(event){ 
        console.log("something is being called");
        var nameAddress = getRestaurantNameAddress(event);
        var name = nameAddress['restaurantName']
            , address = nameAddress['address']; 
        
        $('#res').val(name);
        $('#add').val(address);
    });
    
    function getRestaurantNameAddress(event){
        //event.target is dom element
        var query = $(event.target)
        
        var address = query.data('address'); 
        console.log (address);

        var restaurantName = query.data('name');
        console.log(restaurantName);
        console.log(arguments);
        return {'address': address, 'restaurantName': restaurantName};
    }


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
