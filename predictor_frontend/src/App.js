import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

const list = [
    {
        "id": 1,
        "name": "Tottenham Hotspur",
        "location": "London, UK",
        "league": "Premier League"
    },
    {
        "id": 2,
        "name": "Barcelona",
        "location": "Barcelona, ES",
        "league": "La Liga"
    },
    {
        "id": 3,
        "name": "Liverpool",
        "location": "Liverpool, UK",
        "league": "Premier League"
    },
    {
        "id": 4,
        "name": "Manchester United",
        "location": "Manchester, UK",
        "league": "Premier League"
    },
    {
        "id": 5,
        "name": "Manchester City",
        "location": "Manchester, UK",
        "league": "Premier League"
    }
]

class App extends Component {
  state = {
   teams: []
 };

 async componentDidMount() {
   try {
     const res = await fetch('http://127.0.0.1:8000/api/');
     const teams = await res.json();
     this.setState({
       teams
     });
   } catch (e) {
     console.log(e);
   }
 }
  render() {
    return (
      <div>
        {this.state.teams.map(item => (
          <div>
            <h1>{item.name}</h1>
            <p>{item.location}</p>
            <p>{item.league}</p>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
