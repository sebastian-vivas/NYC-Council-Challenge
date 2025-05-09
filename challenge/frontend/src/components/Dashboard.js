import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = ({ token, onLogout }) => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  
  const [allComplaints, setAllComplaints] = useState([]);
  const [openCases, setOpenCases] = useState([]);
  const [closedCases, setClosedCases] = useState([]);
  const [topComplaints, setTopComplaints] = useState([]);
  
  const [currentView, setCurrentView] = useState('all');
  
  useEffect(() => {
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Token ${token}`;
    }
  }, [token]);
  
  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const [allComplaintsRes, openCasesRes, closedCasesRes, topComplaintsRes] = await Promise.all([
          axios.get('http://localhost:8000/api/complaints/allComplaints/'),
          axios.get('http://localhost:8000/api/complaints/openCases/'),
          axios.get('http://localhost:8000/api/complaints/closedCases/'),
          axios.get('http://localhost:8000/api/complaints/topComplaints/')
        ]);
        
        setAllComplaints(allComplaintsRes.data);
        setOpenCases(openCasesRes.data);
        setClosedCases(closedCasesRes.data);
        setTopComplaints(topComplaintsRes.data);
        setError('');
      } catch (err) {
        console.error('Error fetching data:', err);
        setError('Failed to fetch data. Please try logging in again.');
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);
  
  const handleConstituentView = async () => {
    setLoading(true);
    try {
      const response = await axios.get('http://localhost:8000/api/complaints/constituentComplaints/');
      setAllComplaints(response.data);
      setCurrentView('constituent');
    } catch (err) {
      console.error('Error fetching constituent complaints:', err);
      setError('Failed to fetch constituent complaints.');
    } finally {
      setLoading(false);
    }
  };
  
  const handleAllComplaintsView = () => {
    setCurrentView('all');
  };
  
  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleDateString();
  };
  
  const handleLogout = () => {
    localStorage.removeItem('token');
    onLogout();
  };
  
  if (loading) {
    return <div className="loading">Loading dashboard data...</div>;
  }
  
  if (error) {
    return (
      <div className="error-container">
        <p className="error-message">{error}</p>
        <button onClick={handleLogout}>Logout</button>
      </div>
    );
  }
  
  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>NYC Council Member Dashboard</h1>
        <button onClick={handleLogout} className="logout-button">Logout</button>
      </header>
      
      <div className="stats-container">
        <div className="stat-card">
          <h3>Open Cases</h3>
          <p className="stat-number">{openCases.length}</p>
        </div>
        
        <div className="stat-card">
          <h3>Closed Cases</h3>
          <p className="stat-number">{closedCases.length}</p>
        </div>
        
        <div className="stat-card top-complaints">
          <h3>Top Complaint Types</h3>
          <ol>
            {topComplaints.length > 0 ? (
              topComplaints.map((complaint, index) => (
                <li key={index}>
                  {complaint.complaint_type} ({complaint.count})
                </li>
              ))
            ) : (
              <li>No data available</li>
            )}
          </ol>
        </div>
      </div>
      
      <div className="view-controls">
        <button 
          onClick={handleAllComplaintsView} 
          className={currentView === 'all' ? 'active' : ''}
          disabled={currentView === 'all'}
        >
          All Complaints in My District
        </button>
        <button 
          onClick={handleConstituentView} 
          className={currentView === 'constituent' ? 'active' : ''}
          disabled={currentView === 'constituent'}
        >
          Complaints by My Constituents
        </button>
      </div>
      
      <div className="complaints-table-container">
        <h2>
          {currentView === 'all' 
            ? 'All Complaints in Your District' 
            : 'Complaints by Your Constituents'}
        </h2>
        
        <div className="table-wrapper">
          <table className="complaints-table">
            <thead>
              <tr>
                <th>Complaint Type</th>
                <th>Descriptor</th>
                <th>Borough</th>
                <th>Open Date</th>
                <th>Close Date</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {allComplaints.length > 0 ? (
                allComplaints.map((complaint) => (
                  <tr key={complaint.unique_key}>
                    <td>{complaint.complaint_type || 'N/A'}</td>
                    <td>{complaint.descriptor || 'N/A'}</td>
                    <td>{complaint.borough || 'N/A'}</td>
                    <td>{formatDate(complaint.opendate)}</td>
                    <td>{formatDate(complaint.closedate)}</td>
                    <td>
                      <span className={complaint.closedate ? 'status-closed' : 'status-open'}>
                        {complaint.closedate ? 'Closed' : 'Open'}
                      </span>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="6" className="no-data">No complaints data available</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;