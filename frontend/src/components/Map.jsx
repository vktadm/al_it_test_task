import React from "react";
import { MapContainer, TileLayer, GeoJSON, useMap } from "react-leaflet";

import "leaflet/dist/leaflet.css";
import "../styles/Map.css";

const CenterGeoJSON = ({ data }) => {
  const map = useMap();
  const coordinates = data.coordinates[0];
  const correctedCoordinates = coordinates.map(([lng, lat]) => [lat, lng]);

  map.fitBounds(correctedCoordinates);

  return null;
};

function Map({ id, geojson }) {
  return (
    <MapContainer id={id} center={[59.9386, 30.3141]} zoom={10}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="© OpenStreetMap contributors"
      />
      <GeoJSON data={geojson} />
      <CenterGeoJSON data={geojson} />
    </MapContainer>
  );
}

export default Map;
