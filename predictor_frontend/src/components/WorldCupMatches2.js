import React, { Component } from 'react';

class WorldCupMatches2 extends Component {
  state = {
   worldcupmatches2: [],
 };

 async componentDidMount() {
   try {
     const res = await fetch('http://127.0.0.1:8000/worldcupmatch2/');
     const worldcupmatches2 = await res.json();
     this.setState({
       worldcupmatches2,
     });
   } catch (e) {
     console.log(e);
   }
 }

  render() {
    return (
      <div>
          <h2> World Cup Matchday 2 </h2>
          {this.state.worldcupmatches2.map(item => (
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

export default WorldCupMatches2;
