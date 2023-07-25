import React from 'react';
import './Records.css'; 
import { useState } from 'react';

const Records = () => {
    const [selectedYear, setSelectedYear] = useState('2021');
  // Dummy data for the table rows
//   const dummyData = [
//     { srNo: 1, courseName: 'Course 1', faculty: 'Faculty 1', attendanceTheory: 80, attendancePractical: 90, ise: 85, ia1: 78, ia2: 88,others: 90, labTW: 10, ese: 100, grade: 'A', status: 'Pass' },
//     { srNo: 2, courseName: 'Course 2', faculty: 'Faculty 2', attendanceTheory: 75, attendancePractical:40, ise: 2, ia1: 4, ia2: 1, others: 2, labTW: 20, ese:40, grade: 'A+', status: 'Pass' },
//     {srNo: 3,courseName: 'Course 3',faculty: 'Faculty 3',attendanceTheory: 90,attendancePractical: 95,ise: 92,ia1: 88,ia2: 95,others: 90,labTW: 92,ese: 90,grade: 'A+', status: 'Pass'},
//       {srNo: 4,courseName: 'Course 4',faculty: 'Faculty 4',attendanceTheory: 75,attendancePractical: 80,ise: 78,ia1: 70,ia2: 75,others: 80,labTW: 75,ese: 78,grade: 'A+', status: 'Pass'}
//     // Add more dummy data rows here as needed
//   ];


const dummyData = [
    {
      srNo: 1,
      courseName: 'Course 1',
      faculty: 'Faculty 1',
      year: '2021',
      attendanceTheory: 80,
      attendancePractical: 90,
      ise: 85,
      ia1: 78,
      ia2: 88,
      others: 90,
      labTW: 85,
      ese: 78,
      grade: 'A+', status: 'Pass'
    },
    {
        srNo: 4,
        courseName: 'Course 4',
        faculty: 'Faculty 4',
        year: '2021',
        attendanceTheory: 80,
        attendancePractical: 10,
        ise: 1,
        ia1: 1,
        ia2: 1,
        others: 2,
        labTW: 1,
        ese: 10,
        grade: 'A+', status: 'Pass'
      },
    {
      srNo: 2,
      courseName: 'Course 2',
      faculty: 'Faculty 2',
      year: '2022',
      attendanceTheory: 70,
      attendancePractical: 85,
      ise: 75,
      ia1: 80,
      ia2: 70,
      others: 85,
      labTW: 80,
      ese: 72,
      grade: 'A+', status: 'Pass'
    },
    {
      srNo: 3,
      courseName: 'Course 3',
      faculty: 'Faculty 3',
      year: '2023',
      attendanceTheory: 90,
      attendancePractical: 95,
      ise: 92,
      ia1: 88,
      ia2: 95,
      others: 90,
      labTW: 92,
      ese: 90,
      grade: 'A+', status: 'Pass'
    },
]

// Filter data based on selected year
const filteredData = dummyData.filter((data) => data.year === selectedYear);

// Function to handle year selection
const handleYearChange = (event) => {
  setSelectedYear(event.target.value);
};
  return (
    <div className="records-container">
      <h2>Records Table</h2>
      <div className="year-selector">
        <label htmlFor="year">Select Year: </label>
        <select id="year" value={selectedYear} onChange={handleYearChange}>
          <option value="2021">2021</option>
          <option value="2022">2022</option>
          <option value="2023">2023</option>
        </select>
      </div>
      <table className="records-table">
        <thead>
          <tr>
            <th>Sr No</th>
            <th>Course name</th>
            <th>Faculty</th>
            <th>Attendance-Theory</th>
            <th>Attendance-Practical</th>
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
          {filteredData.map((data) => (
            <tr key={data.srNo}>
              <td>{data.srNo}</td>
              <td>{data.courseName}</td>
              <td>{data.faculty}</td>
              <td>{data.attendanceTheory}</td>
              <td>{data.attendancePractical}</td>
              <td>{data.ise}</td>
              <td>{data.ia1}</td>
              <td>{data.ia2}</td>
              <td>{data.others}</td>
              <td>{data.ise + (data.ia1 + data.ia2) / 2 + data.others}</td>
              <td>{data.labTW}</td>
              <td>{data.ese}</td>
              <td>{data.ise + data.others + (data.ia1 + data.ia2) / 2 + data.ese}</td>
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
