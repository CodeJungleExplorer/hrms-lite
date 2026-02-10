import { useEffect, useState } from "react";
import api from "../api/axios";
import Loader from "../components/common/Loader";
import EmptyState from "../components/common/EmptyState";

export default function Employees() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [form, setForm] = useState({
    employee_id: "",
    full_name: "",
    email: "",
    department: "",
  });
  const [error, setError] = useState("");

  const fetchEmployees = () => {
    setLoading(true);
    api.get("/employees")
      .then(res => setEmployees(res.data))
      .catch(() => setError("Failed to load employees"))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  const addEmployee = (e) => {
    e.preventDefault();
    setError("");
    api.post("/employees", form)
      .then(() => {
        setForm({ employee_id: "", full_name: "", email: "", department: "" });
        fetchEmployees();
      })
      .catch(err => {
        setError(err?.response?.data?.detail || "Error adding employee");
      });
  };

  const deleteEmployee = (employee_id) => {
    api.delete(`/employees/${employee_id}`)
      .then(fetchEmployees)
      .catch(() => setError("Failed to delete employee"));
  };

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Employees</h1>

      {/* Add Employee */}
      <form onSubmit={addEmployee} className="grid grid-cols-1 md:grid-cols-4 gap-3 mb-6">
        <input className="p-2 rounded bg-gray-800" placeholder="Employee ID"
          value={form.employee_id}
          onChange={e => setForm({ ...form, employee_id: e.target.value })}
          required
        />
        <input className="p-2 rounded bg-gray-800" placeholder="Full Name"
          value={form.full_name}
          onChange={e => setForm({ ...form, full_name: e.target.value })}
          required
        />
        <input className="p-2 rounded bg-gray-800" placeholder="Email"
          value={form.email}
          onChange={e => setForm({ ...form, email: e.target.value })}
          required
        />
        <input className="p-2 rounded bg-gray-800" placeholder="Department"
          value={form.department}
          onChange={e => setForm({ ...form, department: e.target.value })}
          required
        />
        <button className="md:col-span-4 bg-red-600 py-2 rounded">
          Add Employee
        </button>
      </form>

      {error && <p className="text-red-400 mb-3">{error}</p>}

      {/* List */}
      {loading && <Loader />}
      {!loading && employees.length === 0 && (
        <EmptyState message="No employees yet" />
      )}

      <div className="grid gap-3">
        {employees.map(emp => (
          <div key={emp.employee_id}
               className="p-4 bg-gray-800 rounded flex justify-between items-center">
            <div>
              <p className="font-medium">{emp.full_name}</p>
              <p className="text-sm text-gray-400">{emp.email}</p>
              <p className="text-sm">{emp.department}</p>
            </div>
            <button
              onClick={() => deleteEmployee(emp.employee_id)}
              className="text-sm bg-gray-700 px-3 py-1 rounded hover:bg-red-600">
              Delete
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
