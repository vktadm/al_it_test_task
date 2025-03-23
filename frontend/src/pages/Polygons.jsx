import { useState, useEffect } from "react";
import api from "../api";
import Polygon from "../components/Polygon";
import "../styles/Home.css";

function Polygons() {
  const [polygons, setPolygons] = useState([]);
  const [poly, setPoly] = useState("");
  const [name, setName] = useState("");
  const [antemeridian, setAntemeridian] = useState(false);

  useEffect(() => {
    getPolygons();
  }, []);

  const getPolygons = () => {
    api
      .get("/api/polygons/")
      .then((res) => res.data)
      .then((data) => {
        setPolygons(data);
        console.log(data);
      })
      .catch((err) => alert(err));
  };

  const deletePolygon = (id) => {
    api
      .delete(`/api/polygons/delete/${id}/`)
      .then((res) => {
        if (res.status === 204) alert("Полигон удален!");
        else alert("Ошибка при удалении полигона!");
        getPolygons();
      })
      .catch((error) => alert(error));
  };

  return (
    <div>
      <div>
        <h2>Полигоны</h2>
        {polygons.map((polygon) => (
          <Polygon
            polygon={polygon}
            onDelete={deletePolygon}
            key={polygon.id}
          />
        ))}
      </div>
    </div>
  );
}

export default Polygons;
