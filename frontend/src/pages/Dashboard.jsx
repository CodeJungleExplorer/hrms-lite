import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

export default function Dashboard() {
  const navigate = useNavigate();
  const [status, setStatus] = useState("Checking");
  const [employeeCount, setEmployeeCount] = useState(0);

  useEffect(() => {
    api.get("/health")
      .then(() => setStatus("Online"))
      .catch(() => setStatus("Offline"));

    api.get("/employees")
      .then(res => setEmployeeCount(res.data.length))
      .catch(() => setEmployeeCount(0));
  }, []);

  return (
    <div className="min-h-screen bg-neutral-950 text-white p-10 space-y-10">

      {/* ===== HERO HEADER (3 SHADES) ===== */}
      <div className="rounded-2xl p-10 text-center bg-gradient-to-r from-neutral-900 via-neutral-800 to-neutral-900 border border-neutral-700">
        <h1 className="text-5xl font-extrabold tracking-wide">
          HRMS <span className="text-red-500">Lite</span>
        </h1>
        <p className="mt-3 text-neutral-400 text-lg">
          Internal Human Resource Management Dashboard
        </p>
      </div>

      {/* ===== MAIN WIDGETS ===== */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">

        <div
          onClick={() => navigate("/employees")}
          className="cursor-pointer bg-neutral-900 hover:bg-neutral-800 transition rounded-xl p-6 border border-neutral-700"
        >
          <h2 className="text-xl font-semibold">Employees</h2>
          <p className="text-neutral-400 mt-2">Manage employee records</p>
          <p className="mt-4 text-4xl font-bold">{employeeCount}</p>
        </div>

        <div
          onClick={() => navigate("/attendance")}
          className="cursor-pointer bg-neutral-900 hover:bg-neutral-800 transition rounded-xl p-6 border border-neutral-700"
        >
          <h2 className="text-xl font-semibold">Attendance</h2>
          <p className="text-neutral-400 mt-2">Track daily attendance</p>
          <p className="mt-4 text-xl font-bold text-blue-400">Active</p>
        </div>

        <div className="bg-neutral-900 rounded-xl p-6 border border-neutral-700">
          <h2 className="text-xl font-semibold">System Status</h2>
          <p
            className={`mt-4 text-2xl font-bold ${
              status === "Online" ? "text-green-400" : "text-red-400"
            }`}
          >
            {status}
          </p>
        </div>

      </div>

      {/* ===== INFO SECTION ===== */}
      <div className="bg-neutral-900 rounded-xl p-6 border border-neutral-700">
        <h3 className="text-xl font-semibold mb-2">About</h3>
        <p className="text-neutral-400 leading-relaxed">
          HRMS Lite is a production-ready internal HR tool designed to manage
          employees and track attendance with a clean, professional interface.
        </p>
      </div>

    </div>
  );
}
