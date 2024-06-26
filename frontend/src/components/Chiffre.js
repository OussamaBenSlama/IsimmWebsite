import React from 'react';
import CountUp from 'react-countup';
import { FaUsers, FaChalkboardTeacher, FaFlask, FaHandshake, FaBook } from 'react-icons/fa'; // Import icons from react-icons library
import '../styles/chiffre.css';  



export default function Chiffre() {
    const chiffreData = [
        { title: "Nombre d'Étudiants (2023/2024)", count: 2000, icon: <FaUsers style={{color:'#061e6e'}}/> },
        { title: "Nombre d'Enseignants (2023/2024)", count: 150, icon: <FaChalkboardTeacher style={{color:'#061e6e'}}/> },
        { title: "Structures de Recherche", count: 10, icon: <FaFlask style={{color:'#061e6e'}}/> },
        { title: "Partenaires", count: 80, icon: <FaHandshake style={{color:'#061e6e'}}/> },
        { title: "Livres Publiés", count: 1720, icon: <FaBook style={{color:'#061e6e'}}/> },
       ];
      return (
        <div className="chiffre-page">
          <div className="cont">
            <h2>ISIMM en chiffres</h2>
            <div className="card-container">
              {chiffreData.map((item, index) => (
                <div key={index} className="chiffre-card">
                 <b>+<CountUp start={0} end={item.count} duration={6} separator=" "  /></b>
                 <div className="icon-container">{item.icon}</div>

                  <p>{item.title}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      );
    }
    
