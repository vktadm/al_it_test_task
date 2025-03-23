import React from "react";
import { useState } from "react";
import Map from "../components/Map";
import "../styles/Polygon.css";

function Polygon({ polygon, onDelete }) {
  const [isVisible, setIsVisible] = useState(false);
  const ant_merid = polygon.antemeridian.toString();

  return (
    <div className="polygon-container">
      <p className="polygon-name">{polygon.name}</p>
      <p className="polygon-poly">{polygon.poly.coordinates}</p>
      <p className="polygon-antemeridian">
        Пересечения антимеридиана: {ant_merid}
      </p>
      {isVisible && <Map id={polygon.id} geojson={polygon.poly} />}
      <button
        className="details-button"
        onClick={() => setIsVisible(!isVisible)}
      >
        Показать/скрыть полигон на карте
      </button>
      <button className="delete-button" onClick={() => onDelete(polygon.id)}>
        Удалить
      </button>
    </div>
  );
}

export default Polygon;
