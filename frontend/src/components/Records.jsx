import React from 'react';
import './Records.css'; // Create a CSS file named "Records.css" for styling

const Records = () => {
  // Dummy data for the table rows
  const dummyData = [
    { srNo: 1, courseName: 'Course 1', faculty: 'Faculty 1', attendance: 80, ise: 'Jan', ia1: 'Feb', ia2: 'Mar', others: 'Apr', ca: 85, labTW: 'May', ese: 'Jun', total: 400, grade: 'A', status: 'Pass' },
    { srNo: 2, courseName: 'Course 2', faculty: 'Faculty 2', attendance: 75, ise: 'Jul', ia1: 'Aug', ia2: 'Sep', others: 'Oct', ca: 90, labTW: 'Nov', ese: 'Dec', total: 420, grade: 'A+', status: 'Pass' },
    // Add more dummy data rows here as needed
  ];

  return (
    <div className="records-container">
      <h2>Records Table</h2>
      <table className="records-table">
        <thead>
          <tr>
            <th>Sr No</th>
            <th>Course name</th>
            <th>Faculty</th>
            <th>Attendance</th>
            <th>ISE</th>
            <th>IA1</th>
            <th>IA2</th>
            <th>Others</th>
            <th>CA</th>
            <th>Lab TW</th>
            <th>ESE</th>
            <th>Total</th>
            <th>Grade</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {dummyData.map((data) => (
            <tr key={data.srNo}>
              <td>{data.srNo}</td>
              <td>{data.courseName}</td>
              <td>{data.faculty}</td>
              <td>{data.attendance}</td>
              <td>{data.ise}</td>
              <td>{data.ia1}</td>
              <td>{data.ia2}</td>
              <td>{data.others}</td>
              <td>{data.ca}</td>
              <td>{data.labTW}</td>
              <td>{data.ese}</td>
              <td>{data.total}</td>
              <td>{data.grade}</td>
              <td>{data.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Records;
