import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

import NavBar from './components/NavBar.js';

class App extends Component {
  state = {

   premierleagueteams: [],
   laligateams: [],
   bundesligateams: []

 };

 async componentDidMount() {
   try {
     const res = await fetch('http://127.0.0.1:8000/premierleague/');
     const res2 = await fetch('http://127.0.0.1:8000/laliga/');
     const res3 = await fetch('http://127.0.0.1:8000/bundesliga/');
     const premierleagueteams = await res.json();
     const laligateams = await res2.json();
     const bundesligateams = await res3.json();
     this.setState({
       premierleagueteams,
       laligateams,
       bundesligateams
     });
   } catch (e) {
     console.log(e);
   }
 }

  render() {
    return (
      <div>
        <MuiThemeProvider>
          <NavBar />
          <h2> Premier League Teams </h2>
          {this.state.premierleagueteams.map(item => (
            <div>
              <h3>{item.name}</h3>
              <p>{item.location}</p>
              <p>{item.league}</p>
            </div>
          ))}
          <h2> La Liga Teams </h2>
          {this.state.laligateams.map(item => (
            <div>
              <h3>{item.name}</h3>
              <p>{item.location}</p>
              <p>{item.league}</p>
            </div>
          ))}
          <h2> Bundesliga Teams </h2>
          {this.state.bundesligateams.map(item => (
            <div>
              <h3>{item.name}</h3>
              <p>{item.location}</p>
              <p>{item.league}</p>
            </div>
          ))}
        </MuiThemeProvider>
      </div>
    );
  }
}

export default App;
