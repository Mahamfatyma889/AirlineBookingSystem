import React, { useState, useEffect } from "react";
import "./../scss/Auth.scss";
import { useNavigate } from "react-router-dom";
import { checkLoginFromNonLogin } from "./../CONSTANT";

function Profile() {
  let navigate = useNavigate();
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    if (checkLoginFromNonLogin()) {
      navigate("/login");
    } else {
        const storedData = localStorage.getItem("loggedin");
        if (storedData) {
            setUserData(JSON.parse(storedData).data);
        }
    }
  }, []);

  if (!userData) {
      return <div className="p-5 text-center">Loading...</div>;
  }

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8">
          <div className="card shadow-sm">
            <div className="card-header bg-primary text-white">
              <h3 className="mb-0">My Profile</h3>
            </div>
            <div className="card-body">
              <div className="row mb-3">
                <div className="col-sm-4 fw-bold">Username:</div>
                <div className="col-sm-8">{userData.username}</div>
              </div>
              <div className="row mb-3">
                  <div className="col-sm-4 fw-bold">Email:</div>
                  <div className="col-sm-8">{userData.email}</div>
              </div>
              <div className="row mb-3">
                  <div className="col-sm-4 fw-bold">First Name:</div>
                  <div className="col-sm-8">{userData.first_name || "N/A"}</div>
              </div>
              <div className="row mb-3">
                  <div className="col-sm-4 fw-bold">Last Name:</div>
                  <div className="col-sm-8">{userData.last_name || "N/A"}</div>
              </div>
              <hr />
              <div className="row mb-3">
                  <div className="col-sm-4 fw-bold">Phone Number:</div>
                  <div className="col-sm-8">{userData.phone_no || "N/A"}</div>
              </div>
              <div className="row mb-3">
                  <div className="col-sm-4 fw-bold">Address:</div>
                  <div className="col-sm-8">{userData.address || "N/A"}</div>
              </div>
              <div className="row mb-3">
                  <div className="col-sm-4 fw-bold">Role:</div>
                  <div className="col-sm-8">{userData.role || "N/A"}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Profile;
