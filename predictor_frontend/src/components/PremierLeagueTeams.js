import React, { Component } from 'react';

class PremierLeagueTeams extends Component {
  state = {
   premierleagueteams: [],
 };

 async componentDidMount() {
   try {
     const res = await fetch('http://localhost:8000/api/premierleague/');
     const premierleagueteams = await res.json();
     this.setState({
       premierleagueteams,
     });
   } catch (e) {
     console.log(e);
   }
 }

  render() {
    return (
      <div>
          <h2> Premier League Teams </h2>
          {this.state.premierleagueteams.map(item => (
            <div>
              <h3>{item.name}</h3>
              <p>{item.location}</p>
              <p>{item.league}</p>
            </div>
          ))}
      </div>
    );
  }
}

export default PremierLeagueTeams;
