import React, { Component } from 'react';

class PremierLeagueMatches extends Component {
  state = {
   premierleaguematches: [],
 };

 async componentDidMount() {
   try {
     const res = await fetch('http://127.0.0.1:8000/premierleaguematch/');
     const premierleaguematches = await res.json();
     this.setState({
       premierleaguematches,
     });
   } catch (e) {
     console.log(e);
   }
 }

  render() {
    return (
      <div>
          <h2> Premier League Matches </h2>
          {this.state.premierleaguematches.map(item => (
            <div>
              <h3>{item.match_date}</h3>
              <p>{item.away_team}</p>
              <p>{item.home_team}</p>
              <p>{item.away_score}</p>
              <p>{item.home_score}</p>
            </div>
          ))}
      </div>
    );
  }
}

export default PremierLeagueMatches;
