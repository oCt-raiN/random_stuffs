// Initialize the map
const map = L.map('map').setView([0, 0], 2);

// Add the tile layer from a provider like OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Add the GeoJSON data for continents and countries
const continentsLayer = new L.GeoJSON.AJAX('continents.geojson').addTo(map);
const countriesLayer = new L.GeoJSON.AJAX('countries.geojson');

// Add the country flags as markers (using font icons)
countriesLayer.on('data:loaded', function () {
  countriesLayer.eachLayer(function (layer) {
    const countryFlagIcon = L.divIcon({
      className: 'flag-icon flag-icon-' + layer.feature.properties.iso_a2.toLowerCase(),
      iconSize: [20, 15],
    });
    layer.setIcon(countryFlagIcon);
  });
});

// Add the hover interaction
let tooltip = L.DomUtil.create('div', 'tooltip', document.body);

countriesLayer.on('mouseover', function (e) {
  const layer = e.layer;
  const props = layer.feature.properties;
  const tooltipContent = `
    <strong>${props.name}</strong><br>
    Value: ${props.value}
  `;
  tooltip.innerHTML = tooltipContent;
  tooltip.style.display = 'block';
  tooltip.style.left = (e.originalEvent.pageX + 10) + 'px';
  tooltip.style.top = (e.originalEvent.pageY - 30) + 'px';
});

countriesLayer.on('mouseout', function () {
  tooltip.style.display = 'none';
});

countriesLayer.addTo(map);

// Fit the map to show all countries
map.fitBounds(countriesLayer.getBounds());
