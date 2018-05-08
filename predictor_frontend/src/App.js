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

class App extends Component {
  render() {
    return (
      <div>
        <MuiThemeProvider>
          <NavBar />
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
                <Link to="/worldcup">Premier League Matches</Link>
              </button>
              <Route path="/premier" component={PremierLeagueTeams} />
              <Route path="/liga" component={LaLigaTeams} />
              <Route path="/bundesliga" component={BundesligaTeams} />
              <Route path="/premier-matches" component={PremierLeagueMatches} />
              <Route path="/worldcup" component={WorldCupMatches} />

            </div>
          </Router>
        </MuiThemeProvider>
      </div>
    );
  }
}

export default App;
