import React, { Component } from 'react';

class WorldCupMatches extends Component {
  state = {
   worldcupmatches: [],
 };

 async componentDidMount() {
   try {
     const res = await fetch('http://127.0.0.1:8000/api/worldcupmatch/');
     const worldcupmatches = await res.json();
     this.setState({
       worldcupmatches,
     });
   } catch (e) {
     console.log(e);
   }
 }

  render() {
    return (
      <div>
          <h2> World Cup Matches </h2>
          {this.state.worldcupmatches.map(item => (
            <div>
              <h3>{item.match_date}</h3>
              <p>{item.group}</p>
              <p>{item.away_team}</p>
              <p>{item.home_team}</p>
              <p>{item.away_score}</p>
              <p>{item.home_score}</p>
              <p></p>
            </div>
          ))}
      </div>
    );
  }
}

export default WorldCupMatches;
