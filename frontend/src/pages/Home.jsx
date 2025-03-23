import { useState } from "react";
import { MapContainer, TileLayer, GeoJSON } from "react-leaflet";
import api from "../api";

import "leaflet/dist/leaflet.css";
import "../styles/Home.css";
import "../styles/Map.css";

function Home() {
  const [showGeoJSON, setShowGeoJSON] = useState(false);
  const [geo, setGeo] = useState({
    type: "Point",
    coordinates: [59.9386, 30.3141],
  });
  const [center, setCenter] = useState([59.9386, 30.3141]);
  const [zoom, setZoom] = useState(10);

  const [name, setName] = useState("");
  const [antemeridian, setAntemeridian] = useState(false);
  const [coordinates, setCoordinates] = useState("");

  const [latitude, setLatitudeValue] = useState("");
  const [longitude, setLongitudeValue] = useState("");

  const LatitudeInput = (e) => {
    setLatitudeValue(e.target.value);
  };
  const LongitudeInput = (e) => {
    setLongitudeValue(e.target.value);
  };

  const handleTransfer = () => {
    if (latitude != "" && longitude != "") {
      if (!isNaN(parseFloat(latitude)) && isFinite(latitude)) {
        if (!isNaN(parseFloat(longitude)) && isFinite(longitude)) {
          setCoordinates(
            (prevValue) => prevValue + latitude + " " + longitude + "\n"
          );
          setLongitudeValue("");
          setLatitudeValue("");
        } else {
          setLongitudeValue("");
          alert("Неверный формат ДОЛГОТЫ! Введите числовое значение!");
        }
      } else {
        setLatitudeValue("");
        alert("Неверный формат ШИРОТЫ! Введите числовое значение!");
      }
    } else {
      alert("Заполните поля ШИРОТА и ДОЛГОТА!");
    }
  };

  const createPolygon = (e) => {
    e.preventDefault();

    const poly = {
      type: "Polygon",
      coordinates: [
        coordinates
          .split("\n")
          .map((coord) => coord.trim().split(",").map(Number)),
      ],
    };

    console.log(poly);
    api
      .post("/api/polygons/", { name, poly, antemeridian })
      .then((res) => {
        if (res.status === 201) {
          alert("Полигон создан!");
        } else {
          alert("Что-то пошло не так! Полигон не создан!");
        }
      })
      .catch((err) => {
        if (err) alert("Полигон не создан! Ошибка: \n" + err);
      });

    setShowGeoJSON(true);
    setGeo(poly);
  };

  return (
    <div>
      <form onSubmit={createPolygon}>
        <h2>Создать полигон</h2>
        <label htmlFor="name">Название</label>
        <br />
        <input
          type="text"
          id="name"
          name="name"
          required
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <br />
        <label htmlFor="latitude">Широта</label>
        <input type="text" value={latitude} onChange={LatitudeInput} />
        <br />
        <label htmlFor="longitude">Долгота</label>
        <input type="text" value={longitude} onChange={LongitudeInput} />
        <br />
        <button type="button" onClick={handleTransfer}>
          Добавить
        </button>
        <br />
        <br />
        <label htmlFor="coordinates">Координаты полигона:</label>
        <textarea
          id="coordinates"
          name="coordinates"
          required
          readOnly
          value={coordinates}
          rows="6"
          // onChange={(e) => setCoordinates(e.target.value)}
        ></textarea>
        <br />
        <div>
          <MapContainer center={center} zoom={zoom}>
            <TileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              attribution="© OpenStreetMap contributors"
            />
            {showGeoJSON && <GeoJSON data={geo} />}
          </MapContainer>
        </div>
        <input type="submit" value="Создать"></input>
      </form>
    </div>
  );
}

export default Home;
