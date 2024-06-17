<template>
  <div class="bank-page">
    <div class="category-search-container">
      <div class="category-selection">        
        <label for="region-select" class="visually-hidden">지역 선택</label>
        <select v-model="selectedRegion" id="region-select" class="category-select">
          <option value="">지역 선택</option>
          <option v-for="region in regions" :value="region" :key="region">{{ region }}</option>
        </select>
        
        <label for="district-select" class="visually-hidden">지역구 선택</label>
        <select v-model="selectedDistrict" id="district-select" class="category-select">
          <option value="">지역구 선택</option>
          <option v-for="district in selectedDistricts" :value="district" :key="district">{{ district }}</option>
        </select>

        <label for="bank-select" class="visually-hidden">은행 선택</label>
        <select v-model="selectedBank" id="bank-select" class="category-select">
          <option value="">전체</option>
          <option v-for="bank in banks" :value="bank" :key="bank">{{ bank }}</option>
        </select>
      </div>

      <button @click="searchLocations" class="search-button">검색</button>
    </div>
    <div ref="map" class="map-container"></div>
  </div>
</template>

<script>
export default {
  name: 'KakaoMap',
  data() {
    return {
      map: null,
      markers: [],
      selectedBank: '',
      selectedRegion: '',
      selectedDistrict: '',
      selectedDistricts: [],
      regions: ['서울', '경기', '대구', '부산', '인천', '광주', '대전', '울산', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주'],
      districtList: {
        '서울': ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구'],
        '경기': ['수원시', '성남시', '의정부시', '안양시', '부천시', '광명시', '평택시', '동두천시', '안산시', '고양시', '과천시', '구리시', '남양주시', '오산시', '시흥시', '군포시', '의왕시', '하남시', '용인시', '파주시', '이천시', '안성시', '김포시', '화성시', '광주시', '양주시', '포천시', '여주시', '연천군', '가평군', '양평군'],
        '대구': ['중구', '동구', '서구', '남구', '북구', '수성구', '달서구', '달성군'],
        '부산': ['중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구', '사상구', '기장군'],
        '인천': ['중구', '동구', '미추홀구', '연수구', '남동구', '부평구', '계양구', '서구', '강화군', '옹진군'],
        '광주': ['동구', '서구', '남구', '북구', '광산구'],
        '대전': ['동구', '중구', '서구', '유성구', '대덕구'],
        '울산': ['중구', '남구', '동구', '북구', '울주군'],
        '강원': ['춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군', '고성군', '양양군'],
        '충북': ['청주시', '충주시', '제천시', '보은군', '옥천군', '영동군', '증평군', '진천군', '괴산군', '음성군', '단양군'],
        '충남': ['천안시', '공주시', '보령시', '아산시', '서산시', '논산시', '계룡시', '당진시', '금산군', '부여군', '서천군', '청양군', '홍성군', '예산군', '태안군'],
        '전북': ['전주시', '군산시', '익산시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군', '장수군', '임실군', '순창군', '고창군', '부안군'],
        '전남': ['목포시', '여수시', '순천시', '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군', '장흥군', '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군', '진도군', '신안군'],
        '경북': ['포항시', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시', '상주시', '문경시', '경산시', '군위군', '의성군', '청송군', '영양군', '영덕군', '청도군', '고령군', '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군'],
        '경남': ['창원시', '진주시', '통영시', '사천시', '김해시', '밀양시', '거제시', '양산시', '의령군', '함안군', '창녕군', '고성군', '남해군', '하동군', '산청군', '함양군', '거창군', '합천군'],
        '제주': ['제주시', '서귀포시']
      },
      banks: [
        '경남은행',
        '광주은행',
        '국민은행',
        '농협은행주식회사',
        '대구은행',
        '부산은행',
        '수협은행',
        '신한은행',
        '우리은행',
        '전북은행',
        '제주은행',
        '주식회사 카카오뱅크',
        '주식회사 케이뱅크',
        '중소기업은행',
        '토스뱅크 주식회사',
        '하나은행',
        '한국산업은행',
        '한국스탠다드차타드은행'
      ],
      selectedMarker: null
    };
  },
  mounted() {
    this.initMap();
    this.zoomToUserLocation();
  },
  methods: {
    initMap() {
      const container = this.$refs.map;
      const options = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567),
        level: 9
      };
      this.map = new kakao.maps.Map(container, options);
      kakao.maps.load(() => {
        this.places = new kakao.maps.services.Places(this.map);
      });
    },
    addMarkers(locations) {
      locations.forEach(location => {
        const marker = new kakao.maps.Marker({
          position: new kakao.maps.LatLng(location.lat, location.lng),
          map: this.map
        });
        this.markers.push(marker);
        kakao.maps.event.addListener(marker, 'click', () => {
          this.selectedMarker = location;
          this.showInfoWindow(location);
        });
      });
    },
    showInfoWindow(location) {
      const content = `<div class="marker-info-window">
                        <div class="marker-info-title">${location.name}</div>
                        <div class="marker-info-address">${location.address}</div>
                      </div>`;

      if (!this.infowindow) {
        this.infowindow = new kakao.maps.InfoWindow({
          content: content,
          disableAutoPan: true,
          removable: true
        });
      }

      this.infowindow.setContent(content);
      const markerPosition = new kakao.maps.LatLng(location.lat, location.lng);
      const offsetX = 40; // 마커 옆으로 이동할 거리
      const offsetY = -30; // 마커 위로 이동할 거리
      const infoWindowPosition = new kakao.maps.LatLng(markerPosition.getLat() + offsetY / 100000, markerPosition.getLng() + offsetX / 100000);
      this.infowindow.setPosition(infoWindowPosition);
      this.infowindow.open(this.map);
    },
    searchLocations() {
      this.clearMarkers();
      if (this.selectedBank && this.selectedRegion && this.selectedDistrict) {
        const keyword = `${this.selectedBank} ${this.selectedRegion} ${this.selectedDistrict}`;
        this.places.keywordSearch(keyword, (result, status) => {
          if (status === kakao.maps.services.Status.OK) {
            this.clearMarkers();
            result.forEach(place => {
              const marker = new kakao.maps.Marker({
                position: new kakao.maps.LatLng(place.y, place.x),
                map: this.map
              });
              this.markers.push(marker);
              kakao.maps.event.addListener(marker, 'click', () => {
                this.selectedMarker = {
                  lat: place.y,
                  lng: place.x,
                  name: place.place_name,
                  address: place.address_name
                };
                this.showInfoWindow(this.selectedMarker);
              });
            });
            if (result.length > 0) {
              this.map.setCenter(new kakao.maps.LatLng(result[0].y, result[0].x));
              this.map.setLevel(5);
            }
          } else {
            alert('검색 결과가 없습니다.')
            console.error('검색 결과가 없습니다:', status);
          }
        });
      } else {
        alert('은행, 지역 및 지역구를 선택해야 합니다.')
        console.error('은행, 지역 및 지역구를 선택해야 합니다.');
      }
    },
    clearMarkers() {
      this.markers.forEach(marker => {
        marker.setMap(null);
      });
      this.markers = [];
    },
    zoomToUserLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
          const coords = new kakao.maps.LatLng(position.coords.latitude, position.coords.longitude);
          this.map.panTo(coords);
          this.map.setLevel(12);
        });
      }
    }
  },
  watch: {
    selectedRegion(newRegion) {
      this.selectedDistricts = newRegion ? this.districtList[newRegion] : [];
      this.selectedDistrict = '';
    }
  }
};
</script>

<style scoped>
@import url('@/assets/fonts.css');

.bank-page {
  font-family: 'Pretendard', sans-serif;
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.category-search-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  margin-bottom: 20px;
}

.category-selection {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-grow: 1;
}

.category-select {
  width: calc(33.33% - 10px);
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  box-sizing: border-box;
}

.search-button {
  flex-shrink: 0;
  padding: 12px 20px;
  background-color: #4E5CBF;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.search-button:hover {
  background-color: #0056b3;
}

.map-container {
  width: 100%;
  height: 400px;
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

.marker-info-window {
  background-color: #fff;
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 4px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.marker-info-title {
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 5px;
}

.marker-info-address {
  font-size: 12px;
  color: #666;
}
</style>
