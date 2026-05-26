import { useEffect, useState } from "react";
import axios from "axios";
import "./index.css";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend
} from "recharts";

function App() {

  const API_BASE =
    "https://breathe-esg-platform-hmrs.onrender.com";

  const [records, setRecords] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);

  const [searchTerm, setSearchTerm] = useState("");

  const [showSuspiciousOnly, setShowSuspiciousOnly] =
    useState(false);

  const totalRecords = records.length;

  const suspiciousRecords = records.filter(
    (record) => record.is_suspicious
  ).length;

  const approvedRecords = records.filter(
    (record) => record.status === "APPROVED"
  ).length;

  const pendingRecords = records.filter(
    (record) => record.status === "PENDING"
  ).length;

  const chartData = [
    {
      name: "Approved",
      value: approvedRecords
    },
    {
      name: "Pending",
      value: pendingRecords
    },
    {
      name: "Suspicious",
      value: suspiciousRecords
    }
  ];

  const COLORS = [
    "#22c55e",
    "#f59e0b",
    "#ef4444"
  ];

  const filteredRecords = records.filter((record) => {

    const matchesSearch =
      record.activity_type
        .toLowerCase()
        .includes(searchTerm.toLowerCase());

    const matchesSuspicious =
      showSuspiciousOnly
        ? record.is_suspicious
        : true;

    return matchesSearch && matchesSuspicious;
  });

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {

    try {

      const response = await axios.get(
        `${API_BASE}/api/emissions/`
      );

      setRecords(response.data);

    } catch (error) {

      console.error(error);

      alert("Failed to fetch records");
    }
  };

  const approveRecord = async (id) => {

    try {

      await axios.post(
        `${API_BASE}/api/emissions/${id}/approve/`
      );

      fetchRecords();

    } catch (error) {

      console.error(error);

      alert("Approval failed");
    }
  };

  const rejectRecord = async (id) => {

    try {

      await axios.post(
        `${API_BASE}/api/emissions/${id}/reject/`
      );

      fetchRecords();

    } catch (error) {

      console.error(error);

      alert("Reject failed");
    }
  };

  const uploadCsv = async () => {

    if (!selectedFile) {

      alert("Please select CSV file");

      return;
    }

    const formData = new FormData();

    formData.append("file", selectedFile);

    try {

      await axios.post(
        `${API_BASE}/api/upload-csv/`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );

      alert("CSV uploaded successfully");

      fetchRecords();

    } catch (error) {

      console.error(error);

      alert("CSV upload failed");
    }
  };

  return (

    <div className="app-container">

      <h1 className="dashboard-title">
        Breathe ESG Dashboard
      </h1>

      <div className="upload-section">

        <input
          type="file"
          accept=".csv"
          onChange={(e) =>
            setSelectedFile(e.target.files[0])
          }
        />

        <button
          onClick={uploadCsv}
          className="upload-button"
        >
          Upload CSV
        </button>

      </div>

      <div className="search-section">

        <input
          type="text"
          placeholder="Search activity..."
          value={searchTerm}
          onChange={(e) =>
            setSearchTerm(e.target.value)
          }
          className="search-input"
        />

        <label>

          <input
            type="checkbox"
            checked={showSuspiciousOnly}
            onChange={(e) =>
              setShowSuspiciousOnly(
                e.target.checked
              )
            }
          />

          Show Suspicious Only

        </label>

      </div>

      <div className="cards-container">

        <div className="card total-card">
          <h3>Total Records</h3>
          <h2>{totalRecords}</h2>
        </div>

        <div className="card suspicious-card">
          <h3>Suspicious Records</h3>
          <h2>{suspiciousRecords}</h2>
        </div>

        <div className="card approved-card">
          <h3>Approved Records</h3>
          <h2>{approvedRecords}</h2>
        </div>

        <div className="card pending-card">
          <h3>Pending Reviews</h3>
          <h2>{pendingRecords}</h2>
        </div>

      </div>

      <div
        style={{
          display: "flex",
          justifyContent: "center",
          marginBottom: "40px"
        }}
      >

        <PieChart width={400} height={300}>

          <Pie
            data={chartData}
            cx="50%"
            cy="50%"
            outerRadius={100}
            dataKey="value"
            label
          >

            {chartData.map((entry, index) => (

              <Cell
                key={`cell-${index}`}
                fill={COLORS[index % COLORS.length]}
              />

            ))}

          </Pie>

          <Tooltip />

          <Legend />

        </PieChart>

      </div>

      <table className="records-table">

        <thead>

          <tr>

            <th>ID</th>

            <th>Activity</th>

            <th>Quantity</th>

            <th>Scope</th>

            <th>Status</th>

            <th>Suspicious</th>

            <th>Analyst Notes</th>

            <th>Actions</th>

          </tr>

        </thead>

        <tbody>

          {filteredRecords.map((record) => (

            <tr
              key={record.id}
              className={
                record.is_suspicious
                  ? "suspicious-row"
                  : ""
              }
            >

              <td>{record.id}</td>

              <td>{record.activity_type}</td>

              <td>{record.quantity}</td>

              <td>{record.scope}</td>

              <td>

                <span
                  className={
                    `status-pill ${
                      record.status === "APPROVED"
                        ? "status-approved"
                        : record.status === "REJECTED"
                        ? "status-rejected"
                        : "status-pending"
                    }`
                  }
                >
                  {record.status}
                </span>

              </td>

              <td>
                {record.is_suspicious
                  ? "⚠️ Yes"
                  : "No"}
              </td>

              <td>

                <textarea
                  placeholder="Add analyst notes..."
                  defaultValue={
                    record.analyst_notes || ""
                  }
                  rows="2"
                  style={{
                    width: "180px",
                    padding: "6px",
                    borderRadius: "6px"
                  }}
                />

              </td>

              <td>

                <button
                  onClick={() =>
                    approveRecord(record.id)
                  }
                  className="action-button approve-button"
                >
                  Approve
                </button>

                <button
                  onClick={() =>
                    rejectRecord(record.id)
                  }
                  className="action-button reject-button"
                >
                  Reject
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default App;