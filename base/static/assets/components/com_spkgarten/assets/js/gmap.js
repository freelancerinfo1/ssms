jQuery(function($){
  google.maps.event.addDomListener(window, 'load', function(){

    var latlng = new google.maps.LatLng($('#spkgarten-event-map').data('lat'), $('#spkgarten-event-map').data('lng'));
    var styles = [{"featureType": "all", "elementType": "all", "stylers": [{"saturation": -100}, {"gamma": 1}]}];

    var mapOptions = {
      center: latlng,
      scrollwheel: false,
      styles: styles,
      zoom: 16,
      zoomControl: false,
      panControl: false,
      streetViewControl: false,
      mapTypeControl: false,
      overviewMapControl: false,
      clickable: false
    };

    var map = new google.maps.Map(document.getElementById('spkgarten-event-map'), mapOptions);
    var marker = new google.maps.Marker({position: latlng, map: map});
    map.setMapTypeId(google.maps.MapTypeId.ROADMAP);

    map.setStyle("map_style");
    

  });

});