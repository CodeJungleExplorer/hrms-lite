import { useState } from "react";
import api from "../api/axios";

export default function Attendance() {
  const [employeeId, setEmployeeId] = useState("");
  const [date, setDate] = useState("");
  const [status, setStatus] = useState("Present");
  const [records, setRecords] = useState([]);
  const [error, setError] = useState("");

  const markAttendance = (e) => {
    e.preventDefault();
    setError("");
    api.post("/attendance", { employee_id: employeeId, date, status })
      .then(() => fetchAttendance())
      .catch(err => setError(err?.response?.data?.detail || "Error marking attendance"));
  };

  const fetchAttendance = () => {
    api.get(`/attendance/${employeeId}`)
      .then(res => setRecords(res.data))
      .catch(err => setError(err?.response?.data?.detail || "No attendance records"));
  };

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Attendance</h1>

      <form onSubmit={markAttendance} className="flex flex-wrap gap-3 mb-4">
        <input className="p-2 bg-gray-800 rounded"
          placeholder="Employee ID"
          value={employeeId}
          onChange={e => setEmployeeId(e.target.value)}
          required
        />
        <input type="date" className="p-2 bg-gray-800 rounded"
          value={date}
          onChange={e => setDate(e.target.value)}
          required
        />
        <select className="p-2 bg-gray-800 rounded"
          value={status}
          onChange={e => setStatus(e.target.value)}>
          <option>Present</option>
          <option>Absent</option>
        </select>
        <button className="bg-red-600 px-4 rounded">Mark</button>
      </form>

      <button onClick={fetchAttendance}
              className="mb-4 bg-gray-700 px-3 py-1 rounded">
        View Attendance
      </button>

      {error && <p className="text-red-400 mb-3">{error}</p>}

      <div className="grid gap-2">
        {records.map((r, i) => (
          <div key={i} className="p-3 bg-gray-800 rounded">
            <p>{r.date} — {r.status}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
