$(document).ready(function () {
    $('#mapLocationSetModalHandler').click(function () {
        $('#locationModal').modal('show');
        mapboxgl.accessToken = 'pk.eyJ1Ijoid3dmYmNvbSIsImEiOiJja3h5ZzY4dzE2emw1Mm9zdDlpbXRld3kwIn0.FpPT0OUONvotj4grUbSmog';

        // Initialize the map
        var map = new mapboxgl.Map({
            container: 'location_picker_map',
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [0, 0],
            zoom: 1
        });

        // Add a marker on click
        var marker = new mapboxgl.Marker({
            draggable: true
        })
            .setLngLat([0, 0])
            .addTo(map);


        map.on('click', (e) => {
            marker.setLngLat(e.lngLat);
            marker.addTo(map);

            $('#latitude').val(e.lngLat.lat)
            $('#longitude').val(e.lngLat.lng)
        });

         map.addControl(
            new mapboxgl.GeolocateControl({
                positionOptions: {
                    enableHighAccuracy: true
                },
                trackUserLocation: true,
                showUserHeading: true
            })
        );
    });

});




