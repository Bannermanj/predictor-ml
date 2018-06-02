import React, { Component } from 'react';



class BundesligaTeams extends Component {
  state = {
   bundesligateams: [],
 };

 async componentDidMount() {
   try {
     const res = await fetch('http://127.0.0.1:8000/api/bundesliga/');
     const bundesligateams = await res.json();
     this.setState({
       bundesligateams,
     });
   } catch (e) {
     console.log(e);
   }
 }

  render() {
    return (
      <div>
          <h2> Bundesliga Teams </h2>
          {this.state.bundesligateams.map(item => (
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

export default BundesligaTeams;
