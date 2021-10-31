var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = {
        center: new kakao.maps.LatLng(35.152389, 128.105114), // 지도의 중심좌표
        level: 5 // 지도의 확대 레벨 
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
var shop_list = "{{shop_list}}";
var shopss = "{{ shopJson }}";
var shops = JSON.parse("{{ shopJson|escapejs }}");
console.log(shops)

var positions = [];
for (var i = 0; i < Object.keys(shops).length; i++) {
    var content = {
        name: shops[i].name,
        latlng: new kakao.maps.LatLng(shops[i].latitude, shops[i].longitude),
        type: shops[i].type,
    }
    positions.push(content);
};
console.log(positions);

var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
for (var i = 0; i < positions.length; i++) {
    // 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(24, 35);
    // 마커 이미지를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: positions[i].latlng, // 마커를 표시할 위치
        title: positions[i].name, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
        image: markerImage // 마커 이미지
    });
}

// HTML5의 geolocation으로 사용할 수 있는지 확인합니다 
if (navigator.geolocation) {

    // GeoLocation을 이용해서 접속 위치를 얻어옵니다
    navigator.geolocation.getCurrentPosition(function (position) {

        var lat = position.coords.latitude, // 위도
            lon = position.coords.longitude; // 경도

        var locPosition = new kakao.maps.LatLng(lat, lon)

        // 마커와 인포윈도우를 표시합니다
        displayMarker(locPosition);

    });

} else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다
    var locPosition = new kakao.maps.LatLng(35.152389, 128.105114)
    displayMarker(locPosition);
}
