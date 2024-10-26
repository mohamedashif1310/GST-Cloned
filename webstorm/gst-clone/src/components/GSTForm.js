import React from 'react';
import './GSTForm.css';

const GSTForm = () => {
    return (
        <div className="gst-form">
            <h2>3.1 Details of Outward Supplies and inward supplies liable to reverse charge</h2>
            <table>
                <thead>
                <tr>
                    <th>Nature of Supplies</th>
                    <th>Total Taxable Value (₹)</th>
                    <th>Integrated Tax (₹)</th>
                    <th>Central Tax (₹)</th>
                    <th>State/UT Tax (₹)</th>
                    <th>Cess (₹)</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>(a) Outward taxable supplies (other than zero rated, nil rated, and exempted)</td>
                    <td><input type="text" value="110000.00" /></td>
                    <td><input type="text" value="0.00" /></td>
                    <td><input type="text" value="9900.00" /></td>
                    <td><input type="text" value="9900.00" /></td>
                    <td><input type="text" value="0.00" /></td>
                </tr>

                </tbody>
            </table>
        </div>
    );
};

export default GSTForm;
