import React, { Component } from 'react';
import './App.css';

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import NavBar from './components/NavBar.js';

import PremierLeagueTeams from './components/PremierLeagueTeams.js';
import LaLigaTeams from './components/LaLigaTeams.js';
import BundesligaTeams from './components/BundesligaTeams.js';
import PremierLeagueMatches from './components/PremierLeagueMatches.js';
import WorldCupMatches from './components/WorldCupMatches.js';
import WorldCupMatches2 from './components/WorldCupMatches2.js';

class App extends Component {
  render() {
    return (
      <div>
        <MuiThemeProvider>
          <Router>
            <div>
              <button>
                <Link to="/premier">Premier League Teams</Link>
              </button>
              <button>
                <Link to="/liga">La Liga Teams</Link>
              </button>
              <button>
                <Link to="/bundesliga">Bundesliga Teams</Link>
              </button>
              <button>
                <Link to="/premier-matches">Premier League Matches</Link>
              </button>
              <button>
                <Link to="/worldcup">World Cup</Link>
              </button>
              <button>
                <Link to="/worldcup2">World Cup Matchday 2</Link>
              </button>
              <Route path="/premier" component={PremierLeagueTeams} />
              <Route path="/liga" component={LaLigaTeams} />
              <Route path="/bundesliga" component={BundesligaTeams} />
              <Route path="/premier-matches" component={PremierLeagueMatches} />
              <Route path="/worldcup" component={WorldCupMatches} />
              <Route path="/worldcup2" component={WorldCupMatches2} />

            </div>
          </Router>
        </MuiThemeProvider>
      </div>
    );
  }
}

export default App;
