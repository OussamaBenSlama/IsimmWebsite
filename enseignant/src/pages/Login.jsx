// Login.js
import React, { useState } from "react";
import './styles/Login.css'
import { useNavigate } from "react-router-dom";
import {useAuth} from '../components/AuthContext'



const Login = () => {
  const {isAuthenticated, login } = useAuth();
  const navigate = useNavigate()

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  
  const handleLogin = async (e) => {
    e.preventDefault(); 
    try {
      const response = await fetch('http://127.0.0.1:8000/profs/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          password: password,
        }),
      });

      const data = await response.json();
      // console.log('====================================');
      // console.log(data);
      // console.log('====================================');
      if (response.ok) {
         login(); // Update authentication state
         navigate('/home', {state:{'student' : data}})
      } else {
         setError(data.error || 'Invalid email or password');
        console.log(data.error);
         window.alert(error);
      }
    } catch (error) {
      console.error('Error during login:', error);
      setError('An error occurred during login');
    }

   
  };
  
  return (
    <div className="Login">
        <div className="login-form">
          <h2>Login</h2>
          <form>
            <input
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              type="email"
              id="email"
              placeholder="Email"
            />
            <input
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              type="password"
              id="password"
              placeholder="Password"
            />
            <input 
                type="submit" 
                value="Sign In"
                onClick={handleLogin}
                id="signinbtn"
            />
          </form>
        </div>
      </div>
    
  );
};

export default Login;