import React, {useEffect, useState} from "react";
import axios from "axios";

function App(){
  const [inspections, setInspections] = useState([]);

  useEffect(() => {
    fetchInspections();
    const id = setInterval(fetchInspections, 5000); // poll every 5s
    return () => clearInterval(id);
  },[]);

  async function fetchInspections(){
    try {
      const res = await axios.get("/api/inspections"); // set proxy in package.json dev
      setInspections(res.data);
    } catch (err) {
      console.error(err);
    }
  }

  return (
    <div style={{padding:20}}>
      <h1>Warehouse Dashboard</h1>
      <table border="1" cellPadding="8" style={{width:"100%",borderCollapse:"collapse"}}>
        <thead>
          <tr><th>ID</th><th>Batch</th><th>Label</th><th>Confidence</th><th>Image</th><th>Created</th></tr>
        </thead>
        <tbody>
          {inspections.map(i => (
            <tr key={i.id}>
              <td>{i.id}</td>
              <td>{i.batch_id || "-"}</td>
              <td>{i.label}</td>
              <td>{(i.confidence*100).toFixed(1)}%</td>
              <td>{i.image_path ? <a href={i.image_path} target="_blank" rel="noreferrer">view</a> : "-"}</td>
              <td>{new Date(i.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
